# ideal-train
Flask repo for basic devops training.

# Building docker image:
Now that we have our Dockerfile ready, is time to build the docker image. 

` 
  docker build -t flaskapp:2.3.3 .
`

# Run the Docker image:

`docker run -p 80:5000 flaskapp:2.3.3 `