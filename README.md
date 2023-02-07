# web-app-ip-returner

To build the Docker image, run the following command in the same directory as the Dockerfile:

docker build -t <image_name> .

e.g. 

docker build -t ip-returner .

To start a container from the image, run the following command:

docker run -p 5000:5000 <image_name>

e.g. 

docker run -p 5000:5000 ip-returner