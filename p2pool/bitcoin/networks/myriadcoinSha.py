import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack

        P2P_PREFIX='af4576ee'.decode('hex'),
        P2P_PORT=10888,
        ADDRESS_VERSION=50,
        RPC_PORT=10889,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'myriadcoinaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: 1000*2000000000000 >> (height + 1)//967680,
        BLOCKHASH_FUNC=data.hash256,
        POW_FUNC=data.hash256,
        BLOCK_PERIOD=30, # s
        SYMBOL='MYR',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Myriadcoin') if platform.system() == 'Windows' else os.path.expanuser('~/Library/Application Support/Myriadcoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.myriadcoin'), 'myriadcoin.conf'),
        BLOCK_EXPLORER_URL_PREFIX='http://insight-myr.cryptap.us/block/',
        ADDRESS_EXPLORER_URL_PREFIX='http://insight-myr.cryptap.us/address/',
        TX_EXPLORER_URL_PREFIX='http://insight-myr.cryptap.us/tx/',
### Neisklar: normally 2**24 should be 2**20 BUT the quark enabled minerd is coded so that it only detects hashes below 0x000000xxxxxxx
        ###           and 2*20 would be 0x00000FFFF, maybe changing that in the miner  would be a good idea for slower ones... 
                ### Update:   the minerd is (at least in GitHub) updated so that it would also detect targets below 2**24 (0x000000xxxx..), (Quark$
                ###           maybe for new standalone p2pools it's a good choice at the beginning, but ONLY when new hashing power is gradually a$
        #SANE_TARGET_RANGE=(2**256//2**32//1000 - 1, 2**256//2**24 - 1), 
        SANE_TARGET_RANGE=(2**256//2**32//1000 - 1, 2**256//2**20 - 1),
        DUMB_SCRYPT_DIFF=1,
        DUST_THRESHOLD=0.001e8,
    ),
