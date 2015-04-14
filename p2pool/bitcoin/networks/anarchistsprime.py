mport os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'f666b4d9'.decode('hex')
P2P_PORT = 9666
ADDRESS_VERSION = 0
RPC_PORT = 9667
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            (yield helper.check_genesis_block(bitcoind, '000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f')) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        ))
SUBSIDY_FUNC = lambda height: 50*100000000 >> (height + 1)//210000
POW_FUNC = data.hash256
BLOCK_PERIOD = 180 # s
SYMBOL = 'APC'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'anarchistsprime') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/AnarchistsPrime/') if platform.system() == 'Darwin' else os.path.expanduser('~/.anarchistsprime'), 'anarchistsprime.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://acp.explorer.ssdpool.com:9150/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'http://acp.explorer.ssdpool.com:9150/address/12KcfJ6wrtoyYm9PTiHtSw5UbqMohRxptc'
TX_EXPLORER_URL_PREFIX = 'http://acp.explorer.ssdpool.com:9150/tx/'
SANE_TARGET_RANGE = (2**256//2**32//1000000 - 1, 2**256//2**32 - 1)
DUMB_SCRYPT_DIFF = 1
DUST_THRESHOLD = 0.001e8