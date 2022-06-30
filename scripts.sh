docker build --tag flask-library .
docker run -p 5000:5000 flask-library

# docker images
# docker rmi $(docker images -q)  


# to add a sqlite file - -v /host/path/to/file.sqlite:/container/path/to/file.sqlitea
