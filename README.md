# Opencell backend and analysis tools
[![Build Status](https://github.com/czbiohub/opencell/workflows/build/badge.svg)](https://github.com/czbiohub/opencell/actions)

## About
__Opencell__ is a collaborative project led by the [Leonetti group](https://www.czbiohub.org/manuel-leonetti-intracellular-architecture/) to generate and characterize a proteome-wide library of endogeneously tagged human cell lines. This repo contains a python package, itself called `opencell`, that provides methods to ingest, process, and access the datasets generated by this effort.


## Datasets
 Each OpenCell cell line is characterized by live-cell confocal microscopy and immunoprecipitation-mass spectrometry. These two assays elucidate, respectively, the subcellular localization patterns of each tagged protein and its biochemical interaction partners.


## Development workflow
Our current development workflow is simple: to make changes, simply clone the opencell repo locally, create and push new branches to this remote repo, and, at appropriate intervals, create PRs to merge your changes to the master branch. Currently, we do not use forks, so all development branches appear in this repo and are visible to everyone. Also, the management of feature branches is left to the developer. For example, you might choose to maintain a single 'development' branch, or you might choose to create and delete branches on a per-feature basis. However you manage them, please be sure to keep your development branches up to date by periodically merging master into them.


### Requirements
It is recommended to install the dependencies listed in `requirements.txt` in a virtual environment. Note that some packages, including `pynrrd` and `FlowCytometryTools`, may only be installable via `pip` and not via `conda`.


### pre-commit hooks
We use `pre-commit` to run `flake8` linting automatically before each commit. This is a python package that can be installed using `pip`. The hooks must then be installed in your local repo by running

```
pre-commit install
```

Once installed, pre-commit will block commits that do not pass its checks. It will also modify the staged files to remove any trailing whitespace and missing end-of-file line returns; note that these modifications are not automatically staged. For a commit to 'pass' the pre-commit checks, it is necessary to manually stage these automatic changes, then make and stage any changes necessary to address the issues flagged by `flake8`, then try to make the commit again.

Note that we currently exempt certain flake8 rules; please refer to `setup.cfg` for details and remarks about these exemptions.


### CI
Currently, our CI workflow consists of linting (using `flake8` and `pylint`) and a limited number of unit tests and integration tests. To maximize the likelihood of your PR passing CI, it is advisable to run an approximation of the CI workflow locally before creating or updating a PR. To make doing so convenient, rules are defined in the `Makefile` that mimic the 'real' CI workflow: linting can be run using `make lint` and tests can be run using `make test`. The CI workflow itself is run using Github Actions. The configuration itself is defined in `.github/workflows/ci-workflow.yaml`.

As an aside, note that the linting performed in the CI workflow is __not__ redundant with the pre-commit linting because it runs `pylint` in addition to `flake8`. Running `pylint` is a bit slow too for a pre-commit hook, but it is nevertheless useful (at least until our test coverage improves) because it catches more complex syntax errors than `flake8`.


### Writing and running tests
We use `pytest` for testing. Tests appear in the top-level `tests/` directory; the structure of this directory should mirror the structure of the `opencell` package itself. Tests can be run via either `make test` or by calling pytest itself from the command line. Tests are automatically discovered by `pytest` according to its [test-discovery conventions](https://docs.pytest.org/en/latest/goodpractices.html#conventions-for-python-test-discovery). In short, any method of the form `^test_*` in any file of the form `^test_*.py` in the `tests/` directory is considered a test method.


### Setting up the test database
Running the tests requires the existence of a local postgres database that can be connected to using the credentials defined in `db-credentials-test.json`. This database is run using a Docker container. First, pull the postgres image:
```
docker pull postgres
make start-test-db
```


## Deployment workflow
Coming soon!

## License
Chan Zuckerberg Biohub Software License

This software license is the 2-clause BSD license plus a third clause
that prohibits redistribution and use for commercial purposes without further
permission.

Copyright © 2020. Chan Zuckerberg Biohub.
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1.	Redistributions of source code must retain the above copyright notice,
this list of conditions and the following disclaimer.

2.	Redistributions in binary form must reproduce the above copyright notice,
this list of conditions and the following disclaimer in the documentation
and/or other materials provided with the distribution.

3.	Redistributions and use for commercial purposes are not permitted without
the Chan Zuckerberg Biohub's written permission. For purposes of this license,
commercial purposes are the incorporation of the Chan Zuckerberg Biohub's
software into anything for which you will charge fees or other compensation or
use of the software to perform a commercial service for a third party.
Contact ip@czbiohub.org for commercial licensing opportunities.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.