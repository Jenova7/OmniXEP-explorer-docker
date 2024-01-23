# Omni explorer in Docker

  This is setup in docker-compose for OmniXEP  explorer. Several services are launched:
  * [OmniXEP node](https://github.com/ElectraProtocol/OmniXEP)
  * [OmniXEP api](https://github.com/Jenova7/OmniXEP-API)
  * [OmniXEP engine](https://github.com/Jenova7/OmniXEP-engine)
  * [OmniXEP explorer](https://github.com/Jenova7/OmniXEP-explorer)
  * Redis
  * Postgres

## Prerequisite
 * docker 
 * docker-compose
 
 
## Install


```
git clone https://github.com/Jenova7/OmniXEP-explorer-docker.git
cd OmniXEP-explorer-docker
// edit configurations if you want
docker-compose build
docker-compose up -d
```

## Configuration
  Each service has own configuration (list are below)

### API configuration

 - ./api/omnixep.conf - Setup credetials to your OmniXEP node
 - ./api/sql.conf - Setup credetials to your postgres instance


### Engine configuration

 - ./engine/omnixep.conf - Setup credetials to your OmniXEP node
 - ./engine/sql.conf - Setup credetials to your postgres instance

ENV variables:
 - NETWORK - `testnet` or any other value. Depents on your OmniXEP node configuration
 - FLYWAY_PLACEHOLDERS_OMNIAPIPASSWORD - password for omni api postgres user
 - FLYWAY_PLACEHOLDERS_OMNIENGINEPASSWORD - password for omni engine postgres user
 - PGUSER - default postgres user
 - PGPASSWORD - password for default postgres user
 - PGHOST - postgres instance host
 - PGPORT - postgres instance port
 - OMNIDB_DATABASE - omni database name


### Explorer configuration
 - [./explorer/addDevMiddlewares.js](https://github.com/APshenkin/omnilayer-explorer-docker/blob/master/explorer/addDevMiddlewares.js#L36) - set target in proxy to your api instance 
 - [./explorer/constants.js](https://github.com/APshenkin/omnilayer-explorer-docker/blob/master/explorer/constants.js#L20)  - set change api url rule to your api instance

### Postgres configuration
ENV variables:
 - POSTGRES_PASSWORD - set postgres default password
 
### Known issues

