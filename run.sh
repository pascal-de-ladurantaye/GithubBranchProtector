#!/usr/bin/env bash

PORT=$(printf "import configs\nprint(configs.PORT)" | python3)
echo "Starting on port ${PORT}"
gunicorn main:APP --bind 0.0.0.0:${PORT} --worker-class aiohttp.worker.GunicornWebWorker --reload
