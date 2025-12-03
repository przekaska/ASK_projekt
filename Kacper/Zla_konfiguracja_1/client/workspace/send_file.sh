FILE_NAME="$1"
curl -X POST -d @$FILE_NAME "http://server:8080/file/$FILE_NAME"
