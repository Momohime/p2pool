import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = '25174c22'.decode('hex')
P2P_PORT = 8698
ADDRESS_VERSION = 0
RPC_PORT = 8697
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'titcoinaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        ))
SUBSIDY_FUNC = lambda height: 69*69000000 >> (height + 1)//500000
POW_FUNC = data.hash256
BLOCK_PERIOD = 60 # s
SYMBOL = 'TIT'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'titcoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/titcoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.titcoin'), 'titcoin.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://blockexperts.com/tit/height/'
ADDRESS_EXPLORER_URL_PREFIX = 'http://blockexperts.com/tit/address/'
TX_EXPLORER_URL_PREFIX = 'http://blockexperts.com/tit/tx/'
SANE_TARGET_RANGE = (2**256//2**32//1000000 - 1, 2**256//2**32 - 1)
DUMB_SCRYPT_DIFF = 1
DUST_THRESHOLD = 0.001e8
