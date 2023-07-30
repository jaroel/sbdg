FROM ubuntu:xenial as os
RUN useradd -ms /bin/false plone
RUN apt-get update -y
RUN apt-get install -y mime-support libssl1.0.0
COPY ./dpkgs /dpkgs
# For use on ARM64:
RUN dpkg -i /dpkgs/arm64/python2.4-minimal_2.4.6-8+xenial1_arm64.deb /dpkgs/arm64/python2.4_2.4.6-8+xenial1_arm64.deb
RUN apt-get install -y build-essential libxml2-dev libxslt1-dev libbz2-dev libjpeg62-dev libz-dev libssl-dev
RUN dpkg -i /dpkgs/arm64/libpython2.4_2.4.6-8+xenial1_arm64.deb /dpkgs/arm64/python2.4-dev_2.4.6-8+xenial1_arm64.deb
# # For use on AMD64:
# RUN dpkg -i /dpkgs/amd64/python2.4-minimal_2.4.6-8+xenial1_amd64.deb /dpkgs/amd64/python2.4_2.4.6-8+xenial1_amd64.deb
# RUN apt-get install -y build-essential libxml2-dev libxslt1-dev libbz2-dev libjpeg62-dev libz-dev libssl-dev
# RUN dpkg -i /dpkgs/amd64/libpython2.4_2.4.6-8+xenial1_amd64.deb /dpkgs/amd64/python2.4-dev_2.4.6-8+xenial1_amd64.deb

FROM os as builder
WORKDIR /app
COPY dlcache /app/dlcache/
COPY buildout.cfg /app/
COPY versions.cfg /app/
COPY dlcache/setuptools-0.6c11-py2.4.egg /app/
COPY ez_setup.py /app/
COPY bootstrap.py /app/
COPY src /app/src
RUN python2.4 ez_setup.py
RUN easy_install-2.4 /app/dlcache/zc.buildout-1.4.3.tar.gz
RUN python2.4 bootstrap.py
RUN ./bin/buildout
RUN chown -R plone var/

FROM builder as runner
EXPOSE 19565
VOLUME ["/app/var/filestorage"]
CMD [ "/app/bin/instance0", "console" ]
