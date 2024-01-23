RECAPTCHA_PRIVATE = None #replace private key text here
DOMAIN = None     #Replace with domain to override email domain lookup, otherwise system hostname is used
EMAILFROM = None  #Is set to None, use noreply@domain
SMTPUSER = None   #If your smtp server requires authentication define it here
SMTPPASS = None   #If your smtp server requires authentication define it here
SMTPDOMAIN = 'localhost'  #smtp server to use for sending, default    'localhost'
SMTPPORT = 25     #smtp port,  default 25
SMTPSTARTTLS = False  # Use starttls before SMTP login
WELCOMECID = None #mailgun campaign id for welcome email stats

#For wallets and session store you can switch between disk and the database
LOCALDEVBYPASSDB = 0    #Set to 1 to use local storage/file system, Set to 0 to use database
#local data dir if not using db
LOCALDATADIR = '../data'

#Used to generate challange/response hash
SERVER_SECRET = 'SoSecret!'
SESSION_SECRET = 'SuperSecretSessionStuff'
WEBSOCKET_SECRET = 'SocketSecret!'

#used for encrypting/decrypting secure values.
#NOTE: If these values change, anything previously encrypted with them will need to be updated / encrypted with the new values
AESKEY='2SlccIMZmqAqFPUn'
AESIV='ObPa3IpFj1SQ4OsD'

#Donation Address Pubkey  (We need the pubkey so that if an address hasn't sent a tx before we don't need the private key to get the pubkey)
D_PUBKEY = '03dddadd66e9fece9ad22e744c23b73178b6397f19eddc99ad1e4f5537d0cff749'

#Blocktrail API Key (used for lookups of utxo's)
BTAPIKEY = None

#Redis Connection Info
REDIS_HOST='omni_redis'
REDIS_PORT=6379
REDIS_DB=0
REDIS_DB_LOCAL=10

DISABLE_RATE_LIMITS='true'
#Use if you want custom address namespace (multiple servers on same box)
#Must prefix custom name with :  example ":stage"
REDIS_ADDRSPACE=""
#How long, in seconds, to cache BTC balance info for new addresses, Default 10min (600)
BTCBAL_CACHE=600
#Debug level (2: errors only,3: 2+ratelimit info 4: 3+general info, 7: 4+cache debugging)
DEBUG_LEVEL=3
#CORS config for websocket
WEBSOCKET_CORS=""

#Cloudflare acct id and apikey
CFID = None
CFKEY = None

#Testnet
TESTNET=0

def apiLookup(id):
  try:
    convert={"tokenid":""
            }
    return convert[id]
  except KeyError:
    return -1
