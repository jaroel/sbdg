from setuptools import setup, find_packages
import os

version = '1.1.dev0'

tests_require=['zope.testing']

setup(name='deliverance.contenttypes',
      version=version,
      description="",
      long_description=open("README.rst").read() + "\n" +
                       open("CHANGES.rst").read(),
      classifiers=[
        'Framework :: Plone',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        ],
      keywords='',
      author='Four Digits',
      author_email='info@fourdigits.nl',
      url='http://www.fourdigits.nl',
      license='GPL version 2',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['deliverance', ],
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        # -*- Extra requirements: -*-
                        ],
      tests_require=tests_require,
      extras_require=dict(tests=tests_require),
      test_suite = 'deliverance.contenttypes.tests.test_docs.test_suite',
      entry_points="""
      # -*- entry_points -*- 
      [distutils.setup_keywords]
      paster_plugins = setuptools.dist:assert_string_list

      [egg_info.writers]
      paster_plugins.txt = setuptools.command.egg_info:write_arg
      """,
      paster_plugins = ["ZopeSkel"],
      )
