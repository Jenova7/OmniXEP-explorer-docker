FROM ubuntu:20.04
LABEL maintainer="TFinch <nexusnow@protonmail.com>"

ENV OMNICORE_VER=1.0.0
ENV OMNICORE_ARCH=x86_64

ENV DATA_DIR=/root/.omnixep
ENV RPCALLOWIP="::/0"
ENV RPCUSER=omnicore
ENV RPCPASSWORD=omnicore

RUN apt-get update && apt-get install -qq \
  wget

#WORKDIR /root
# Need to change this to the offical release page when going live
# This is only for testing right now.
RUN wget https://github.com/MotoAcidic/omnilayer-explorer-docker/releases/download/1.0.0/omnixep-cli
RUN echo  "Downloaded omnixep-cli"
RUN wget https://github.com/MotoAcidic/omnilayer-explorer-docker/releases/download/1.0.0/omnixepd
RUN echo  "Downloaded omnixepd"

RUN chmod -R 755 omnixepd omnixep-cli

#RUN mkdir /root/.omnixep

EXPOSE 8332-8333/tcp 18332-18333/tcp
VOLUME ["${DATA_DIR}"]

ADD entrypoint.sh /entrypoint.sh

RUN chmod u+x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
CMD ["omnixepd"]