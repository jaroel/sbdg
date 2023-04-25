from setuptools import setup, find_packages
import os

version = '0.2.dev0'

setup(name='jaroel.policy',
      version=version,
      description="",
      long_description=open("README.rst").read() + "\n" +
                       open("CHANGES.rst").read(),
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Four Digits',
      author_email='info@fourdigits.nl',
      url='http://www.fourdigits.nl',
      license='GPL version 2',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['jaroel'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [distutils.setup_keywords]
      paster_plugins = setuptools.dist:assert_string_list

      [egg_info.writers]
      paster_plugins.txt = setuptools.command.egg_info:write_arg
      """,
      paster_plugins = ["ZopeSkel"],
      )
