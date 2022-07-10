#!/bin/bash -e

poetry env use python
venv=`poetry env info -p`
source ${venv}/bin/activate

make install
make collectstatic
make migrate
make lint
make check-no-dead-fixtures
make test
