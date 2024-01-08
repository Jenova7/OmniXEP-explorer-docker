FROM ubuntu:18.04

#Install deps
RUN apt-get update
RUN apt-get install -y git-core \
                      pkg-config build-essential \
                      pyqt4-dev-tools python-qt4 python-dev python-twisted python-pip python-psutil \
                      swig \
                      libqtcore4 libqt4-dev libtool libpq-dev libffi-dev libssl-dev \
                      autotools-dev autoconf lsb-core supervisor wget \
                      build-essential libevent-dev libtool autotools-dev automake pkg-config \
                      bsdmainutils curl git libboost-all-dev libssl-dev libboost-tools-dev libdb++-dev \
                      libevent-dev libqt5gui5 libqt5core5a libqt5dbus5 qttools5-dev qttools5-dev-tools \
                      libprotobuf-dev protobuf-compiler libevent-dev libboost-all-dev libdb++-dev libssl-dev \
                      libboost-system-dev libboost-filesystem-dev libboost-chrono-dev libboost-program-options-dev \
                      libboost-test-dev libboost-thread-dev g++-arm-linux-gnueabihf gcc-aarch64-linux-gnu nsis libgmp3-dev \
                      libdb-dev                       

# Install nginx
RUN cd /tmp/ && wget http://nginx.org/keys/nginx_signing.key
RUN apt-key add /tmp/nginx_signing.key
RUN sh -c "echo 'deb http://nginx.org/packages/mainline/ubuntu/ '$(lsb_release -cs)' nginx' > /etc/apt/sources.list.d/nginx.list"
RUN apt-get update -y && apt-get -y install nginx

# Move the daemon and cli to a new folder outside of the source to better keep files clean
WORKDIR /root/

# Create the config file for omnixep
RUN mkdir /root/.omnixep/
WORKDIR /root/.omnixep/
COPY omnixep.conf /root/.omnixep/

# Now make a new folder for the daemon and cli
WORKDIR /home/ubuntu/
RUN mkdir /home/ubuntu/core/
WORKDIR /home/ubuntu/core/

RUN wget https://github.com/MotoAcidic/omnilayer-explorer-docker/releases/download/1.0.1/omnixepd
RUN wget https://github.com/MotoAcidic/omnilayer-explorer-docker/releases/download/1.0.1/omnixep-cli
RUN chmod -R 755 omnixepd omnixep-cli
RUN ./omnixepd -daemon

# Install omniapi
WORKDIR /home/ubuntu/

RUN git clone -b dev https://github.com/ElectraProtocol/OmniXEP-API.git
WORKDIR /home/ubuntu/OmniXEP-API

RUN pip install -r requirements.txt
RUN mkdir /home/ubuntu/OmniXEP-API/logs/

#Setup nginx main config
RUN cp  /home/ubuntu/OmniXEP-API/etc/nginx/sites-available/default /etc/nginx/conf.d/default.conf

#Setup OmniXEP-API configs
COPY sql.conf /root/.omni/
COPY config.py /home/ubuntu/OmniXEP-API/api/config.py

# Patch rate limit to be able to disable them
#COPY flask_rate_limit.py /home/ubuntu/OmniXEP-API/api/flask_rate_limit.py

# Patch cacher to be able to use only remote redis
#COPY cacher.py /home/ubuntu/OmniXEP-API/api/cacher.py

# Patch start script to write logs to stdout
#COPY startApi.sh /home/ubuntu/OmniXEP-API/startApi.sh

# Patch nginx configuration to be able to use CORS
#COPY omni-redirects /home/ubuntu/OmniXEP-API/etc/nginx/sites-available/omni-redirects

# Add supervisor conf to launch nginx and api
COPY supervisord.conf /etc/supervisor/conf.d/

EXPOSE 8080
EXPOSE 8332-8333/tcp 18332-18333/tcp
CMD ["/usr/bin/supervisord"]
