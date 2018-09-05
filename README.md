
### ML Tool Using Flask+Mongo+Docker

The application runs Machine Learning models on your dataset of choice. We can create ML experiments on the tool to record each experiment we run on the dataset. The current implementation uses an ANN model built on Keras and more models will be added in the coming iterations.

### Instructions to Install Docker.
Link - https://docs.docker.com/toolbox/overview/

#### On Windows
Make the following changes after installation. 

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
The default settings seem to suffice or kindly follow the instructions specified on the page. 

### Run the application 

1. Clone the repository.
2. Open Docker terminal and cd to the cloned repo.
3. Build the application by saying "docker-compose up --build"
4. After the build is complete, the application will be up and running on the localhost http://0.0.0.0:4000/
5. Open another docker terminal and cd to the cloned repo.
6. On Windows -> Run the bash file by saying "docker exec "container-name" sh calls.sh" Eg: docker exec fullstackmltool_web_dev_1 cat calls.sh
7. On OSX/Linux -> run "container-name" cat calls_x.sh


#### Steps to Add/Update Experiments

The following curl calls can be executed from a terminal while the application is up and running. 

Note - The name of the experiments are assumed to be "unique".

CREATE ==> curl localhost:4000/experiments -d "{\"exp_name\": \"name of the experiment\", \"train_split\":\"percentage of data used for train\", \"type\":\"type of the experiment\"}" -H "Content-Type: application/json"

READ ==> curl localhost:4000/experiments

DELETE ==> curl -X DELETE localhost:4000/experiments -d "{\"exp_name\":\"name of the experiment\"}" -H "Content-Type: application/json"

UPDATE ==> curl -X PATCH localhost:4000/experiments -d "{\"query\": {\"exp_name\":\"name of the experiment\"}, \"payload\" : {\"field to be updated/added\":\"new value to be updated/added\"}}" -H "Content-Type: application/json"

