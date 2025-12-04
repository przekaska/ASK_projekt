#!/bin/sh

FILE_NAME="example.txt"

while true; do
    echo "Pobieram plik"
    curl "http://server:8080/file/$FILE_NAME" -o "$FILE_NAME"
    sleep 1
done