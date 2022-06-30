source /venv/bin/activate
docker build --tag flask-library .
docker run -p 5000:5000 flask-library
deactivate
# to add a sqlite file - -v /host/path/to/file.sqlite:/container/path/to/file.sqlitea