#!/usr/bin/env bash

set -e

docker run -d --name tbtl-postgres -v postgres-data:/var/lib/postgresql/data -p 5432:5432 --env-file ./.env --rm postgres:12-alpine
docker run -d --name tbtl-redis -v redis-data:/data -p 6379:6379 --env-file ./.env --rm redis:5-alpine