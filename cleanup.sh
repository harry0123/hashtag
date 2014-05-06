#!/bin/bash

FILE=$1
NEW='clean_sample.csv'

sed 's/^(//g' $FILE | sed 's/),$//g' | sed 's/\(.*\), /\1,/' > $NEW
