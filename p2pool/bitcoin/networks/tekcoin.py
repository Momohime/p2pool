import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'e4e8e9e5'.decode('hex')
P2P_PORT = 8514
ADDRESS_VERSION = 26
RPC_PORT = 18514
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'tekcoinaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        ))
SUBSIDY_FUNC = lambda height: 1
POW_FUNC = data.hash256
BLOCK_PERIOD = 60 # s
SYMBOL = 'TEK'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'tekcoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/tekcoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.tekcoin'), 'tekcoin.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://tek.blockchain.lt/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'http://tek.blockchain.lt/address/'
TX_EXPLORER_URL_PREFIX = 'http://tek.blockchain.lt/tx/'
SANE_TARGET_RANGE = (2**256//2**32//1000000 - 1, 2**256//2**32 - 1)
DUMB_SCRYPT_DIFF = 1
DUST_THRESHOLD = 0.001e8
