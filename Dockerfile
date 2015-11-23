FROM fedora:23
MAINTAINER rubin.diego@gmail.com

# System dependences 
# install cyclone system dependences
RUN dnf install -y libffi-devel
RUN dnf install -y gcc
RUN dnf install -y rpm-build

# install python2
RUN dnf install -y python-pip
RUN dnf install -y python-devel
RUN dnf install -y openssl-devel 

# Python dependences
RUN pip install cyclone
RUN pip install redis

# Copy application
RUN mkdir /app
ADD bin /app/bin
ADD spellchecker /app/spellchecker
RUN ln -s /app/bin/spellchecker-server /usr/bin/spellchecker-server

WORKDIR /app/spellchecker

EXPOSE 8084

