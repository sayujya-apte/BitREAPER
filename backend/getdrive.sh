#!/usr/bin/bash

FILE="drives.csv"
if [ -f "$FILE" ]; then
	rm -rf drives.csv	
fi

lsblk -dn -o NAME,SIZE,TYPE,TRAN | awk 'BEGIN {OFS = ", " }{ print $1, $2, $3, $4}' >> drives.csv

