#!/usr/bin/env bash

set -euo pipefail

cd "$(dirname "$0")/.." || exit 1

export PYTHONPATH=./src

pytest --workers auto --cov=src
