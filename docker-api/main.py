import os
import json
import docker


# os.system("docker info  --format '{{json .}}' > temp.json")
# file = open("temp.json")
# docker_info =  json.loads(file.read())

# print(type(docker_info))
# print(docker_info)

client = docker.from_env()
# print(client.containers.list("--all"))

# for i in client.containers.list("--all"):
#     # print(i.)
#     print(i.id)
    
# j = json.loads()

print(json.dumps(client.info(),indent = 8))
    # print(client.containers.list(i.id))
    # i.id()

# client.containers.list("name")