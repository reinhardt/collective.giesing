from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='collective.giesing',
      version=version,
      description="Content types, views and utilities for collaborative fiction writing",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='',
      author_email='',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'Plone',
          'plone.app.dexterity [grok]',
          'collective.autopermission',
          'collective.geo.contentlocations',
          'collective.geo.behaviour',
          'plone.app.versioningbehavior',
          'z3c.relationfield',
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=[""],
      )
