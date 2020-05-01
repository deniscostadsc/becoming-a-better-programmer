#!/usr/bin/env bash

export PYTHONPATH=./src

pytest --cov-report term-missing --cov=src
