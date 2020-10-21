import os
import json
import docker
import  flask
import data


app = flask.Flask(__name__)
app.config["DEBUG"] = True

DOCKER_IMAGE="codercom/code-server:latest"

client = docker.from_env()

@app.route('/get-container',methods=['GET'])
def get_container():
    container=client.containers.run(DOCKER_IMAGE,detach=True, ports={'8080': None})
    # container.
    # print(type(container))
    return container.name

@app.route('/delete-containers-all',methods=['DELETE'])
def del_all_containers():
    con=client.containers.list(filters={'ancestor':DOCKER_IMAGE})
    for i in con:
        print(i)
        i.kill()
        i.remove(force=True)
    return "ok"






if __name__ == '__main__':
    app.run(host="0.0.0.0",port=80)
    # os.system("docker info  --format '{{json .}}' > temp.json")
    # file = open("temp.json")
    # docker_info =  json.loads(file.read())

    # print(type(docker_info))
    # print(docker_info)





    # client = docker.from_env()
    # print(client.containers.list("--all"))

    # for i in client.containers.list("--all"):
    #     # print(i.)
    #     print(i.id)
        
    # j = json.loads()

    # print(json.dumps(client.info(),indent = 8))
        # print(client.containers.list(i.id))
        # i.id()

    # client.containers.list("name")