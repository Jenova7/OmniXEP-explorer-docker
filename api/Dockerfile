FROM ubuntu:18.04

#Install deps
RUN apt-get update
RUN apt-get install -y git-core \
                      pkg-config \
                      build-essential \
                      pyqt4-dev-tools \
                      swig \
                      libqtcore4 \
                      libqt4-dev \
                      python-qt4 \
                      python-dev \
                      python-twisted \
                      python-psutil \
                      autotools-dev \
                      autoconf \
                      libtool \
                      python-pip \
                      wget \
                      lsb-core \
                      supervisor \
                      libpq-dev \
                      libffi-dev \
                      libssl-dev

# Install nginx
RUN cd /tmp/ && wget http://nginx.org/keys/nginx_signing.key
RUN apt-key add /tmp/nginx_signing.key
RUN sh -c "echo 'deb http://nginx.org/packages/mainline/ubuntu/ '$(lsb_release -cs)' nginx' > /etc/apt/sources.list.d/nginx.list"
RUN apt-get update -y && apt-get -y install nginx

# Install omniapi
WORKDIR /home/ubuntu

RUN git clone -b test https://github.com/Jenova7/OmniXEP-API.git
WORKDIR /home/ubuntu/OmniXEP-API

RUN pip install -r requirements.txt
RUN mkdir /home/ubuntu/OmniXEP-API/logs/

#Setup nginx main config
RUN cp  /home/ubuntu/OmniXEP-API/etc/nginx/sites-available/default /etc/nginx/conf.d/default.conf

#Setup omniapi configs
COPY omnixep.conf /root/.omnixep/
COPY sql.conf /root/.omni/
COPY config.py /home/ubuntu/OmniXEP-API/api/config.py

# Patch rate limit to be able to disable them
COPY flask_rate_limit.py /home/ubuntu/OmniXEP-API/api/flask_rate_limit.py

# Patch cacher to be able to use only remote redis
COPY cacher.py /home/ubuntu/OmniXEP-API/api/cacher.py

# Patch start script to write logs to stdout
COPY startApi.sh /home/ubuntu/OmniXEP-API/startApi.sh

# Patch nginx configuration to be able to use CORS
COPY omni-redirects /home/ubuntu/OmniXEP-API/etc/nginx/sites-available/omni-redirects

# Add supervisor conf to launch nginx and api
COPY supervisord.conf /etc/supervisor/conf.d/

EXPOSE 8080
CMD ["/usr/bin/supervisord"]
