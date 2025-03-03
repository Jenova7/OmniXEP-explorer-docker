FROM ubuntu:16.04

# install deps
RUN apt-get update
RUN apt-get install -y software-properties-common
RUN add-apt-repository ppa:openjdk-r/ppa
RUN apt-get update
RUN apt-get install -y git-core \
                     # python-dev \
                      libffi-dev \
                      libpq-dev \
                      postgresql \
                      libcurl4-openssl-dev \
                     # python-pip \
                      supervisor \
                      curl \
                      openjdk-8-jre
RUN apt-get install -y wget build-essential && wget https://www.python.org/ftp/python/2.7.18/Python-2.7.18.tgz && tar xf Python-2.7.18.tgz && cd Python-2.7.18 && ./configure && make && make install
RUN curl https://bootstrap.pypa.io/pip/2.7/get-pip.py --output get-pip.py \
&&  python get-pip.py \
&& python -m pip install python-crontab==2.5.1

#RUN python2 -m pip install python-crontab==2.5.1


# install flyway to use it for applying migration (omni team use bad practice - just setup sql files on database. We will use flyway for that)
WORKDIR /flyway

ENV FLYWAY_VERSION 5.2.1

RUN curl -L https://repo1.maven.org/maven2/org/flywaydb/flyway-commandline/${FLYWAY_VERSION}/flyway-commandline-${FLYWAY_VERSION}.tar.gz -o flyway-commandline-${FLYWAY_VERSION}.tar.gz \
  && tar -xzf flyway-commandline-${FLYWAY_VERSION}.tar.gz --strip-components=1 \
  && rm flyway-commandline-${FLYWAY_VERSION}.tar.gz \
  && ln -s /flyway/flyway /usr/local/bin/flyway

# Install engine
WORKDIR /root

#ARG OMNILAYER_VERSION=d855a49dfe4fb61f75f7c7e30356cc9031190365

#RUN git clone https://github.com/OmniLayer/omniEngine.git
#ARG SSH_PRIVATE_KEY
COPY omniEngine /root/omniEngine
#RUN git clone git@github.com:VXXL-Project/omniEngine.git
WORKDIR /root/omniEngine

#RUN git checkout ${OMNILAYER_VERSION}

#RUN pip install --upgrade pip

RUN python -m pip install -r requirements.txt

#Setup configs
COPY bitcoin.conf /root/.bitcoin/
COPY sql.conf /root/.omni/
COPY run.sh /root/omniEngine/run.sh
COPY config.py /root/omniEngine/config.py

# Patch installOmniEngineCronJob to forward network variable and pass logs to docker stdout
COPY installOmniEngineCronJob.py /root/omniEngine/install/installOmniEngineCronJob.py

# Patch omniEngine to force stdout print and use other configuration for testnet
#COPY omniEngine.py /root/omniEngine/omniEngine.py
#COPY sql.py /root/omniEngine/sql.py
#COPY db /flyway/sql/

RUN chmod +x /root/omniEngine/run.sh

RUN mkdir /root/omniEngine/logs

# add supervisor conf to launch nginx and api
COPY supervisord.conf /etc/supervisor/conf.d/

CMD ["/usr/bin/supervisord"]
