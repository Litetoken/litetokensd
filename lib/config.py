import sys
import os

"""Variables prefixed with `DEFAULT` should be able to be overridden by
configuration file and command‐line arguments."""

UNIT = 100000000        # The same across assets.


# Versions
VERSION_MAJOR = 9
VERSION_MINOR = 45
VERSION_REVISION = 0
VERSION_STRING = str(VERSION_MAJOR) + '.' + str(VERSION_MINOR) + '.' + str(VERSION_REVISION)


# Litetokens protocol
TXTYPE_FORMAT = '>I'

TWO_WEEKS = 2 * 7 * 24 * 3600
MAX_EXPIRATION = 4 * 2016   # Two months

MEMPOOL_BLOCK_HASH = 'mempool'
MEMPOOL_BLOCK_INDEX = 9999999


# SQLite3
MAX_INT = 2**63 - 1


# Litecoin Core
OP_RETURN_MAX_SIZE = 40 # bytes


# Currency agnosticism
LTC = 'LTC'
XLT = 'XLT'

LTC_NAME = 'Litecoin'
LTC_CLIENT = 'litecoind'
XLT_NAME = 'Litetokens'
XLT_CLIENT = 'litetokensd'

DEFAULT_RPC_PORT_TESTNET = 17740
DEFAULT_RPC_PORT = 7740

DEFAULT_BACKEND_RPC_PORT_TESTNET = 19332
DEFAULT_BACKEND_RPC_PORT = 9332

UNSPENDABLE_TESTNET = 'mvCounterpartyXXXXXXXXXXXXXXW24Hef'
UNSPENDABLE_MAINNET = 'LiTETokensxxxxxxxxxxxxxxxxxxWCmCEQ'

# TODO: Update Testnet Specifications
ADDRESSVERSION_TESTNET = b'\x6f'
PRIVATEKEY_VERSION_TESTNET = b'\xef'
ADDRESSVERSION_MAINNET = b'\x30'
PRIVATEKEY_VERSION_MAINNET = b'\xb0'
MAGIC_BYTES_TESTNET = b'\xfc\xc1\xb7\xdc'   # For bip-0010
MAGIC_BYTES_MAINNET = b'\xfb\xc0\xb6\xdb'   # For bip-0010

BLOCK_FIRST_TESTNET_TESTCOIN = 154908
BURN_START_TESTNET_TESTCOIN = 154908
BURN_END_TESTNET_TESTCOIN = 4017708     # Fifty years, at ten minutes per block.

BLOCK_FIRST_TESTNET = 154908
BURN_START_TESTNET = 154908
BURN_END_TESTNET = 4017708              # Fifty years, at ten minutes per block.

BLOCK_FIRST_MAINNET_TESTCOIN = 278270
BURN_START_MAINNET_TESTCOIN = 278310
BURN_END_MAINNET_TESTCOIN = 2500000     # A long time.

BLOCK_FIRST_MAINNET = 743330
BURN_START_MAINNET = 743331
BURN_END_MAINNET = 743374 # Possibly A World Record

MAX_BURN_BY_ADDRESS = 1000000 * UNIT 	# 1M LTC.
BURN_MULTIPLIER = 750000000000 # 750 B

# Issuance Fee
DEFAULT_ISSUANCE_FEE = 0.5 # Initializing at 1/2

# Protocol defaults
# NOTE: If the DUST_SIZE constants are changed, they MUST also be changed in liteblockd/lib/config.py as well
    # TODO: This should be updated, given their new configurability.
# TODO: The dust values should be lowered by 90%, once transactions with smaller outputs start confirming faster: <https://github.com/mastercoin-MSC/spec/issues/192>
DEFAULT_REGULAR_DUST_SIZE = 5011 	  # LTC;
DEFAULT_MULTISIG_DUST_SIZE = 6011     # LTC.
DEFAULT_OP_RETURN_VALUE = 0 		  # LTC.
DEFAULT_FEE_PER_KB = 100000            # LTC.


# UI defaults
DEFAULT_FEE_FRACTION_REQUIRED = .009   # 0.90%
DEFAULT_FEE_FRACTION_PROVIDED = .01    # 1.00%


# Custom exit codes
EXITCODE_UPDATE_REQUIRED = 5

CONSENSUS_HASH_SEED = 'Knowledge unqualified is knowledge simply of something learned.'

# (ledger_hash, txlist_hash)
CHECKPOINTS_MAINNET = {
    BLOCK_FIRST_MAINNET: ('94071336ca62d38b7b2cce919c97906372ed32e6e55994a219e63659b5ef2089', '86925a0ea3b1190796cc2d6811fdbd8e43d6ac7e952cacb08614a88bc634aace'),
    743350: ('7abf6c8bdf5ec9f687d505d31f3aa26d79a86e61f09599c9dfaaa7864fd86f43', '7774f8fdf0ac866176c929fc2b97a0a306291a8994cdf713cfb9f706eb4dbdc9'),
    743375: ('b360817d7ca0b3c0af427514f0a05436468794db03af27252e727327da49d461', '7a7512b48edc960482ff5bbe537eabc2f01eef190a7401dc121622e1dcd6dc2c')
}

CHECKPOINTS_TESTNET = {
    BLOCK_FIRST_TESTNET: ('538b3c4512b8f85d7f5d1d44bcad36a86dcf7d735610dcd17ff906ff74c914ab', '538b3c4512b8f85d7f5d1d44bcad36a86dcf7d735610dcd17ff906ff74c914ab'),
    160000: ('a9e226d9034bbf890e45b58bdf806a812b74efbe5e4645458780d3b12994e1b2', '7d6cbcfc9a910693e0effb4c3295bce26a6aa35fa95433bf28d4752b716e1bd9'),
    180000: ('e45dd29fca891633a4ff3eb1a3437544bacf0100a7916e300cbaa192c26e1f3b', '114f419b00298effbf3877fdfaf9f11e3142dc0fe9e869e1e8e0e0a427fa867a'),
    200000: ('09715be67a24cf4173d29bbc8e734f1ccb80cea5b108c672ed4398fc0dbfefe3', 'f220a7802b00faa13af4ed87712f381e32b64685f907e2ae272e3e6287a79191'),
    250000: ('233cbfcfc2826b23027d77295efab1264762017d0bc54ea856c7d727afcb2559', '694b3dbfab00329df34434fa376bcc87f9e670a8b015600f0384195e30cbe742'),
    300000: ('832bd9342448453f27b765c60aacb0c89b4e2779db394c49db3abf2d38df594a', 'fd66973e15540adf84fec68d3acb4fe4c3dd529646993dc1d007972a160b18ec')
}

FIRST_MULTISIG_BLOCK_TESTNET = 303000
