#!/usr/bin/bash

FILE="drives.csv"
if [ -f "$FILE" ]; then
	rm -rf drives.csv	
fi

lsblk -o NAME,TYPE,SIZE,TRAN,MOUNTPOINT --noheadings | awk '$2=="disk"{print "/dev/" $1 "," $2 "," $3 "," $4}' > drives.csv
