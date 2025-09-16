#!/usr/bin/bash

while IFS=',' read -r NAME _ _ TYPE ROTA _; do
	TYPE_TRIM=$(echo "$TYPE" | tr -d '\r\n' | xargs)
	ROTA_TRIM=$(echo "$ROTA" | tr -d '\r\n' | xargs)
	echo "NAME: $NAME, TYPE: $TYPE, ROTA: $ROTA"
done < response.csv

if [ "$TYPE_TRIM" = "sata" ]; then
	echo "test3"
	if [ "$ROTA_TRIM" = "1" ]; then
		echo "HDD detected!"
		# dhdhdh
	elif [ "$ROTA_TRIM" = "0" ]; then
		echo "SSD detected!"
	fi
elif [ "$TYPE_TRIM" = "nvme" ]; then
	echo "test"
elif [ "$TYPE_TRIM" = "usb" ]; then
	echo "test1"
fi



