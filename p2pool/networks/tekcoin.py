from p2pool.bitcoin import networks

# CHAIN_LENGTH = number of shares back client keeps
# REAL_CHAIN_LENGTH = maximum number of shares back client uses to compute payout
# REAL_CHAIN_LENGTH must always be <= CHAIN_LENGTH
# REAL_CHAIN_LENGTH must be changed in sync with all other clients
# changes can be done by changing one, then the other

PARENT = networks.nets['tekcoin']
SHARE_PERIOD = 180 # seconds
CHAIN_LENGTH = 24*60*60//10 # shares
REAL_CHAIN_LENGTH = 24*60*60//10 # shares
TARGET_LOOKBEHIND = 200 # shares
SPREAD = 20 # blocks
IDENTIFIER = 'fc70035c7a81123f'.decode('hex')
PREFIX = '247123181efcd37b'.decode('hex')
P2P_PORT = 8514
MIN_TARGET = 0
MAX_TARGET = 2**256//2**32 - 1
PERSIST = False
WORKER_PORT = 8513
BOOTSTRAP_ADDRS = 'mining.p2pools.com rav3n.dtdns.net pool.hostv.pl p2pool.org tekcoin.securepayment.cc'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-alt'
VERSION_CHECK = lambda v: True
