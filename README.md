# Becoming a better programmer

![CI](https://github.com/deniscostadsc/becoming-a-better-programmer/workflows/CI/badge.svg?branch=master)
[![codecov](https://codecov.io/gh/deniscostadsc/becoming-a-better-programmer/branch/master/graph/badge.svg)](https://codecov.io/gh/deniscostadsc/becoming-a-better-programmer)

The ideia for this repository is to refresh, study and practice algorithms and
data-structures.

I'm doing so far is to implement some [data structures](src/datastructures/)
and solve some [problems](src/problems/) that are heavily based on algorithms
and data structures.

## Running test

All development environment is based on [Docker](https://www.docker.com/),
although is possible to run it locally. With
[Docker installed](https://docs.docker.com/get-docker/), you alread have the
following make tasks available:

```bash
make lint  # run static code analysis, code formating check and etc.
make test  # execute tests
```
