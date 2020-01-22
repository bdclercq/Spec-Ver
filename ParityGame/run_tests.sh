#!/usr/bin/env bash
#
#for filename in /tests/*.txt; do
#    python PG.py $filename
#done
for filename in tests/*.txt; do
    [ -e "$filename" ] || continue
    python PG.py $filename
    # ... rest of the loop body
done

for filename in tests/*.dot; do
    [ -e "$filename" ] || continue
    dot -Tpng $filename -o $filename.png
    # ... rest of the loop body
done