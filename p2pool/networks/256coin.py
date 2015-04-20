from p2pool.bitcoin import networks

# CHAIN_LENGTH = number of shares back client keeps
# REAL_CHAIN_LENGTH = maximum number of shares back client uses to compute payout
# REAL_CHAIN_LENGTH must always be <= CHAIN_LENGTH
# REAL_CHAIN_LENGTH must be changed in sync with all other clients
# changes can be done by changing one, then the other

PARENT = networks.nets['256coin']
SHARE_PERIOD = 30 # seconds
CHAIN_LENGTH = 24*60*60//1 # server keeps 1 day of shares
REAL_CHAIN_LENGTH = 12*60*60//4 # 3 Hour share chain
TARGET_LOOKBEHIND = 30 # Difficulty adjusts every 10 minutes
SPREAD = 30 # 1 hour payout adjustment at 3 minute blocks
IDENTIFIER = 'fc70035c7a81666f'.decode('hex')
PREFIX = '247666181efcd37b'.decode('hex')
P2P_PORT = 25255
MIN_TARGET = 0
MAX_TARGET = 2**256//2**32 - 1
PERSIST = False
WORKER_PORT = 9256
BOOTSTRAP_ADDRS = 'rav3n.dtdns.net mining.p2pools.com pool.hostv.pl p2pool.org 67.187.1.175'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-alt'
VERSION_CHECK = lambda v: True
