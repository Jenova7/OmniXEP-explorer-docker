FROM --platform=linux/amd64 node:8-slim

#Install deps
RUN apt-get update
RUN apt-get install -y git-core \
                       wget \
                       dumb-init \
                       software-properties-common \
                       libpng-dev \
                       autoconf \
                       gcc \
                       g++ \
                       libtool \
                       pkg-config \
                       make \
                       python2.7

RUN ln -s /usr/bin/python2.7 /usr/bin/python
RUN ln -s /usr/bin/python2.7 /usr/bin/python2

# Install omni explorer
WORKDIR /home/ubuntu

ARG OMNILAYER_VERSION=c706fda96f361b452e4196dcb34d2da44f9d39b0
RUN git clone https://github.com/VXXL-Project/omniexplorer.git
WORKDIR /home/ubuntu/omniexplorer

RUN git checkout ${OMNILAYER_VERSION}

# Patch several files

COPY package.json /home/ubuntu/omniexplorer/package.json
COPY constants.js /home/ubuntu/omniexplorer/app/containers/App/constants.js
COPY addDevMiddlewares.js /home/ubuntu/omniexplorer/server/middlewares/addDevMiddlewares.js

RUN npm install
RUN npm run build

EXPOSE 3000

ENTRYPOINT ["/usr/bin/dumb-init", "--"]

CMD ["npm", "run", "start:prod"]
