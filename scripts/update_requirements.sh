#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.." || exit 1

ls
pip-compile \
    --upgrade \
    --build-isolation \
    --generate-hashes \
    --cache-dir ./.cache \
    --output-file requirements/test.lock requirements/test.txt
