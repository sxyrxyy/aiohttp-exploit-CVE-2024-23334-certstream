#!/bin/bash

clear

while true; do
    source ./venv/bin/activate
    python CVE-2024-23334.py
    echo 'Sleeping'
    sleep 1
done
