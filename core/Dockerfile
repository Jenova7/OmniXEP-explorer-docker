FROM ubuntu:16.04
LABEL maintainer="Joey Fang <josudoey@gmail.com>"

ENV OMNICORE_VER          1.0.0
ENV OMNICORE_ARCH         x86_64

ENV DATA_DIR             /root/.omnixep
ENV RPCALLOWIP          "::/0"
ENV RPCUSER              rELZLXHBNGnCNK9c
ENV RPCPASSWORD          SEuL5DlKT66o9uhC

RUN apt-get update && apt-get install -qq \
  wget

RUN wget https://github.com/Jenova7/dev_bins/releases/download/dev_temp/omnixep-cli
RUN echo  "Downloaded omnixep-cli"
RUN wget https://github.com/Jenova7/dev_bins/releases/download/dev_temp/omnixepd
RUN echo  "Downloaded omnixepd"
RUN wget https://github.com/Jenova7/dev_bins/releases/download/dev_temp/omnixep-tx
RUN echo  "Downloaded omnixep-tx"

EXPOSE 17017-17116/tcp 18332-18333/tcp
VOLUME ["${DATA_DIR}"]

ADD entrypoint.sh /entrypoint.sh

RUN chmod u+x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
CMD ["omnicored"]
