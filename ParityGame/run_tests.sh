#!/usr/bin/env bash

FILES=/tests/*
for FILE in $FILES:
do
    echo $FILE
    python PG.py $FILE
done