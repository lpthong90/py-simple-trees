#!/usr/bin/env bash

set -e
set -x

mypy simple_trees
ruff simple_trees tests scripts
ruff format simple_trees tests scripts --check