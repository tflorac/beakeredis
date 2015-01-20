# beakeredis
[![Build Status](https://travis-ci.org/aspyatkin/beakeredis.svg?branch=dev)](https://travis-ci.org/aspyatkin/beakeredis)
## Installation
`pip install beakeredis`
## Configuration
```
beaker.session.type = redis
beaker.session.url = 127.0.0.1:6379
```
## Disclaimer
This is a fork from [didip beaker_extensions package](https://github.com/didip/beaker_extensions).  
The purpose of the fork was to:  
1. eliminate support of all database providers except Redis (which is the one I actually need)  
2. provide a stable package on PyPI (because the original one was not updated and installation from GitHub is not suitable for packages which are dependable on the original package)
