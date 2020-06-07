#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.." || exit 1

pip-compile \
    --upgrade \
    --build-isolation \
    --generate-hashes \
    --cache-dir ./.cache \
    --output-file requirements/ci.lock requirements/ci.txt
