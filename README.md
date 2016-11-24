# beakeredis
[![Build Status](https://travis-ci.org/aspyatkin/beakeredis.svg?branch=master)](https://travis-ci.org/aspyatkin/beakeredis)
## Installation
`pip install beakeredis`
## Configuration
```
beaker.session.type = redis
beaker.session.url = 127.0.0.1:6379
```
## Disclaimer
This is a fork of [didip beaker_extensions package](https://github.com/didip/beaker_extensions).  
The purpose of the fork is to:  
1. eliminate support of all database providers except Redis (which is the only one I actually need)  
2. provide a stable package on PyPI (because the original one has not been updated and installation from GitHub is not suitable for packages which are dependent on the original package)
