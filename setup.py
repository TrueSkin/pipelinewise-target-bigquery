#!/usr/bin/env python

from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(name="pipelinewise-target-bigquery",
      version="1.5.0",
      description="Singer.io target for loading data to BigQuery - PipelineWise compatible",
      long_description=long_description,
      long_description_content_type='text/markdown',
      author="jmriego",
      url='https://github.com/transferwise/pipelinewise-target-bigquery',
      classifiers=[
          'License :: OSI Approved :: Apache Software License',
          'Programming Language :: Python :: 3 :: Only',
          'Programming Language :: Python :: 3.13'
      ],
      py_modules=["target_bigquery"],
      install_requires=[
          'pipelinewise-singer-python>=1,<3',
          'google-cloud-bigquery>=3.0.0',
          'fastavro>=1.4.11'
      ],
      extras_require={
          "test": [
              'pytest>=8.0.0',
              'pylint>=3.0.0',
              'pytest-cov>=4.0.0',
          ]
      },
      entry_points="""
          [console_scripts]
          target-bigquery=target_bigquery:main
      """,
      packages=["target_bigquery"],
      package_data={},
      include_package_data=True,
)
