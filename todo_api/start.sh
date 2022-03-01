#! /usr/bin/env sh
set -e

if [ -f /app/app/main.py ]; then
    DEFAULT_MODULE_NAME=app.main
elif [ -f /app/main.py ]; then
    DEFAULT_MODULE_NAME=main
elif [ -f app/main.py ]; then
    DEFAULT_MODULE_NAME=app.main
fi
MODULE_NAME=${MODULE_NAME:-$DEFAULT_MODULE_NAME}
VARIABLE_NAME=${VARIABLE_NAME:-app}
export APP_MODULE=${APP_MODULE:-"$MODULE_NAME:$VARIABLE_NAME"}

HOST=${HOST:-0.0.0.0}
PORT=${PORT:-8000}
LOG_LEVEL=${LOG_LEVEL:-info}
EXTRA_ARGS=$@

echo "Waiting for postgres connection"
while ! nc -z postgres 5432; do
    sleep 0.1
done
echo "PostgreSQL started"

exec uvicorn --loop asyncio --host $HOST --port $PORT --log-level $LOG_LEVEL $EXTRA_ARGS "$APP_MODULE"
