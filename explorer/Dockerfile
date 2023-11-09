FROM ubuntu:18.04

#Install deps
RUN apt-get update
RUN apt-get install -y git-core \
                       wget \
                       dumb-init \
                       software-properties-common \
                       libpng-dev \
                       autoconf \
                       gcc \
                       nodejs \
                       g++ \
                       libtool \
                       pkg-config \
                       make \
                       python2.7

RUN ln -s /usr/bin/python2.7 /usr/bin/python
RUN ln -s /usr/bin/python2.7 /usr/bin/python2

#RUN add-apt-repository -y ppa:linuxuprising/libpng12
#RUN apt-get update -y
#RUN apt-get install -y libpng12-0

#RUN wget -q -O /tmp/libpng12.deb http://mirrors.kernel.org/ubuntu/pool/main/libp/libpng/libpng12-0_1.2.54-1ubuntu1_amd64.deb \
#      && dpkg -i /tmp/libpng12.deb \
#      && rm /tmp/libpng12.deb

#RUN wget https://github.com/Yelp/dumb-init/releases/download/v1.2.1/dumb-init_1.2.1_amd64.deb
#RUN dpkg -i dumb-init_*.deb

# Install omni explorer
WORKDIR /home/ubuntu

#ARG OMNILAYER_VERSION=c706fda96f361b452e4196dcb34d2da44f9d39b0
RUN git clone -b xep-testing https://github.com/MotoAcidic/omniexplorer.git
#COPY omniexplorer /home/ubuntu/omniexplorer
#RUN git clone git@github.com:VXXL-Project/omniexplorer.git
WORKDIR /home/ubuntu/omniexplorer

#RUN git checkout ${OMNILAYER_VERSION}

# Patch several files

COPY package.json /home/ubuntu/omniexplorer/package.json
COPY constants.js /home/ubuntu/omniexplorer/app/containers/App/constants.js
COPY addDevMiddlewares.js /home/ubuntu/omniexplorer/server/middlewares/addDevMiddlewares.js

RUN npm install
RUN npm run build

EXPOSE 3000

ENTRYPOINT ["/usr/bin/dumb-init", "--"]

CMD ["npm", "run", "start:prod"]
