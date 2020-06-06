#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.." || exit 1

export PYTHONPATH=./src

pytest --cov-report term-missing --cov=src
