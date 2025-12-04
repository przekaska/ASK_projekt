FILE_NAME="$1"
curl "http://server:8080/file/$FILE_NAME" -o $FILE_NAME