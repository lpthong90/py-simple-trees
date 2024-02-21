#!/usr/bin/env bash

set -e
set -x

mypy py_simple_trees
ruff py_simple_trees tests scripts
ruff format py_simple_trees tests scripts --check