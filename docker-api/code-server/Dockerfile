FROM codercom/code-server:latest
COPY ./project /home/coder/project

RUN sudo chmod 777 /home/coder/project
WORKDIR /home/coder/project 
ENTRYPOINT ["/usr/bin/entrypoint.sh", "--bind-addr", "0.0.0.0:8080", "."]


