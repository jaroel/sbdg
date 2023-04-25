from setuptools import setup, find_packages
import os

version = '0.3.dev0'

setup(name='fourdigits.madeby',
      version=version,
      description="Adds a madeby viewlet",
      long_description=open("README.rst").read() + "\n" +
                       open("CHANGES.rst").read(),
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Four Digits',
      author_email='info@fourdigits.nl',
      url='http://www.fourdigits.nl',
      license='GPL version 2',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['fourdigits'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
