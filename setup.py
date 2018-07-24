#!/usr/bin/env python

import sys
from os.path import join, dirname
from setuptools import setup

sys.path.append(join(dirname(__file__), 'src'))

execfile(join(dirname(__file__), 'src', 'iPerf3RestApi', 'version.py'))

DESCRIPTION = """
iPerf3RestApi is a Rest API Client for Iperf3.
Iperf is a widely used tool for network performance measurement and tuning. It is significant as a cross-platform tool 
that can produce standardized performance measurements for any network.
"""

setup(name         = 'restapi-iperf3',
      version      = VERSION,
      description  = 'iPerf3RestApi is a Rest API Client for Iperf3',
      long_description = DESCRIPTION,
      author       = 'Abhimanyu Pandian',
      author_email = '<pandian.abhimanyu@gmail.com>',
      url          = 'https://github.com/C-Squad/restapi-iperf3',
      license      = 'Apache License 2.0',
      keywords     = 'testing iperf networking restapi',
      platforms    = 'any',
      classifiers  = [
          "Development Status :: 1 - Development",
          "License :: OSI Approved :: Apache Software License",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Topic :: Software Development :: Testing"
      ],
      install_requires = [
          'robotframework >= 2.6.0',
          'iperf3 >= 0.1.10',
          'flask >= 1.0.2'
      ],
      package_dir = {'': 'src'},
      packages    = ['iPerf3RestApi'],
      )
