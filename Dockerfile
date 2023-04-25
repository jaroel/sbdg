FROM ubuntu:bionic as os
RUN apt update
RUN apt install software-properties-common -y
RUN add-apt-repository ppa:deadsnakes
RUN apt update
RUN apt install python2.4-dev build-essential libxml2-dev libxslt1-dev libbz2-dev libjpeg62-dev libz-dev -y
RUN useradd -ms /bin/false plone

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
