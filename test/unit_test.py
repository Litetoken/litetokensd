#! /usr/bin/python3
import sys, os, time
import pytest
import util_test
from util_test import CURR_DIR
from fixtures.fixtures import UNITTEST_VECTOR, DEFAULT_PARAMS as DP

from lib import (config, util, api)
import counterpartyd

def setup_module():
    counterpartyd.set_options(rpc_port=9999, database_file=CURR_DIR + '/fixtures/fixtures.unittest.db', testnet=True, testcoin=False, backend_rpc_ssl_verify=False)
    util_test.restore_database(config.DATABASE, CURR_DIR + '/fixtures/unittest_fixture.sql')
    # start RPC server
    api_server = api.APIServer()
    api_server.daemon = True
    api_server.start()
    for attempt in range(5000): # wait until server is ready.
        if api_server.is_ready:
            break
        elif attempt == 4999:
            raise Exception("Timeout: RPC server not ready after 5s")
        else:
            time.sleep(0.001)

def teardown_module(function):
    os.remove(config.DATABASE)

@pytest.fixture
def counterpartyd_db(request):
    db = util.connect_to_db()
    cursor = db.cursor()
    cursor.execute('''BEGIN''')
    request.addfinalizer(lambda: cursor.execute('''ROLLBACK'''))
    return db

def test_vector(tx_name, method, inputs, outputs, error, records, counterpartyd_db):
    if method == 'parse':
        util_test.insert_transaction(inputs[0], counterpartyd_db)
        inputs += (inputs[0]['data'][4:],) # message arg
    util_test.check_ouputs(tx_name, method, inputs, outputs, error, records, counterpartyd_db)