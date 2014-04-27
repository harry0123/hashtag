#!/bin/bash
# Author: David Wu
# Use Case: ./combine_csv.sh file1 file2 new_file
#
# Use to combine csv files. copies file1 to new_file then appends file2
# to new file, skipping headers.
#
# ASSUMES SAME CSV HEADERS

if [[ -z $1 ]]; then
    echo "FILE1 (\$1) unset"
    exit 1
fi

if [[ -z $2 ]]; then
    echo "FILE2 (\$2) unset"
    exit 1
fi

if [[ -z $3 ]]; then
    echo "NEW_FILE name (\$3) unset"
    exit 1
fi

FILE1=$1
FILE2=$2
NEW_FILE=$3
NUM_LINES=$(expr $(wc -l $FILE2 | cut -d ' ' -f 1) - 1)

echo "Creating $NEW_FILE"
cp $FILE1 $NEW_FILE
echo "Appending to $NEW_FILE"
tail -n $NUM_LINES $FILE2 >> $NEW_FILE
echo "Files combined"
exit 0
