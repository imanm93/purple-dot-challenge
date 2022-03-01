#!/usr/bin/env bash

set -e

echo "Waiting for database to be ready"
until pg_isready -h ${POSTGRES_HOST:-postgres};
do
    echo -n "."
    sleep 0.5
done

pytest "${@}"
