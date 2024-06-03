#!/usr/bin/env bash
docker run --name postgres -e POSTGRES_PASSWORD=mysecretpassword -p 127.0.0.1:5432:5432 -d postgres
