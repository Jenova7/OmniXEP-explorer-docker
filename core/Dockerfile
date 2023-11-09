FROM ubuntu:16.04
LABEL maintainer="TFinch <nexusnow@protonmail.com>"

ENV OMNICORE_VER          1.0.0
ENV OMNICORE_ARCH         x86_64
ENV OMNICOR_CHECKSUM      

ENV DATA_DIR             /home/ubuntu/.bitcoin
ENV RPCALLOWIP          "::/0"
ENV RPCUSER              omnicore
ENV RPCPASSWORD          omnicore

RUN apt-get update && apt-get install -qq \
  curl
RUN wget https://github.com/MotoAcidic/omnilayer-explorer-docker/releases/download/1.0.0/omnixep-cli
RUN echo  "Downloaded omnixep-cli"
RUN wget https://github.com/MotoAcidic/omnilayer-explorer-docker/releases/download/1.0.0/omnixepd
RUN echo  "Downloaded omnixepd"

EXPOSE 8332-8333/tcp 18332-18333/tcp
VOLUME ["${DATA_DIR}"]

ADD entrypoint.sh /entrypoint.sh

RUN chmod u+x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
CMD ["omnixepd"]
