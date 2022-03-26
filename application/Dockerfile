# base image
FROM ubuntu:18.04

# define workdir
WORKDIR /app

# define user
USER root

# Copy files
COPY . .

# python3 & pip3 installation
RUN apt update -y
RUN apt install -y software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt install -y python3.7 \
                    chromium-chromedriver
RUN apt-get install -y python3-pip

# install the req file
RUN pip3 install -r requirements.txt

# run the command
CMD [ "python3", "/app/main.py", "--url=" ]