
### ML Tool Using Flask+Mongo+Docker

The application runs Machine Learning models on your dataset of choice. The current implementation uses an ANN model built on Keras 

### Instructions to Install Docker.
#### On Windows

Make the following changes. 

Step 1:
Go to C:\Program Files\Docker Toolbox\start.sh
Replace the following line -
"${DOCKER_MACHINE}" create -d virtualbox $PROXY_ENV "${VM}"
with - 
"${DOCKER_MACHINE}" create -d virtualbox --virtualbox-no-vtx-check $PROXY_ENV "${VM}"

Step 2:
If necessary, some Windows firewall settings need to be changed - > Please follow the tutorial on YouTube by Raghav Pal
https://youtu.be/ymlWt1MqURY

#### On Mac/Linux
The default settings seem to suffice. 


### Run the application 

1. Clone the repository.
2. Open Docker terminal and cd to the cloned repo.
3. Build the application by saying "docker-compose up --build"
4. After the build is complete, the application will be up and running on the localhost http://0.0.0.0:4000/
5. Open another docker terminal and cd to the cloned repo.
6. Run the bash file by saying "docker exec "container-name" sh calls.sh" Eg: docker exec fullstackmltool_web_dev_1 cat calls.sh
7. On OSX/Linux run "container-name" cat calls_x.sh

