from hexbytes import HexBytes

# Only thing important for the trace filter are the `transactionHash` that will use to call `trace_transaction`
trace_filter_result = [
    {'action': {'from': '0x76E2cFc1F5Fa8F6a5b3fC4c8F4788F0116861F9B',
                'gas': 470747,
                'value': 0,
                'init': HexBytes('0x608060405234801561001057600080fd5b506040516101e73803806101e78339818101604052602081101561003357600080fd5b8101908080519060200190929190505050600073ffffffffffffffffffffffffffffffffffffffff168173ffffffffffffffffffffffffffffffffffffffff1614156100ca576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004018080602001828103825260248152602001806101c36024913960400191505060405180910390fd5b806000806101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055505060aa806101196000396000f3fe608060405273ffffffffffffffffffffffffffffffffffffffff600054167fa619486e0000000000000000000000000000000000000000000000000000000060003514156050578060005260206000f35b3660008037600080366000845af43d6000803e60008114156070573d6000fd5b3d6000f3fea265627a7a72315820d8a00dc4fe6bf675a9d7416fc2d00bb3433362aa8186b750f76c4027269667ff64736f6c634300050e0032496e76616c6964206d617374657220636f707920616464726573732070726f766964656400000000000000000000000034cfac646f301356faa8b21e94227e3583fe3f5f')},
     'blockHash': '0x39ba45ad930dece3aec537c8c5cd615daf7ee39a2513475e7680ec226e90b923',
     'blockNumber': 6045252,
     'result': {'gasUsed': 55109,
                'code': HexBytes('0x608060405273ffffffffffffffffffffffffffffffffffffffff600054167fa619486e0000000000000000000000000000000000000000000000000000000060003514156050578060005260206000f35b3660008037600080366000845af43d6000803e60008114156070573d6000fd5b3d6000f3fea265627a7a72315820d8a00dc4fe6bf675a9d7416fc2d00bb3433362aa8186b750f76c4027269667ff64736f6c634300050e0032'),
                'address': '0x673Fd582FED2CD8201d58552B912F0D1DaA37bB2'},
     'subtraces': 0,
     'traceAddress': [0],
     'transactionHash': '0x18f8eb25336203d4e561229c08a3a0ef88db1dd9767b641301d9ea3121dfeaea',
     'transactionPosition': 0,
     'type': 'create'},
    {'action': {'from': '0x76E2cFc1F5Fa8F6a5b3fC4c8F4788F0116861F9B',
                'gas': 415719,
                'value': 0,
                'callType': 'call',
                'input': HexBytes('0xb63e800d0000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000140000000000000000000000000d5d82b6addc9027b22dca772aa68d5d74cdbdf440000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001000000000000000000000000198c09f30dba1494c741c510400cfe93b82875130000000000000000000000000000000000000000000000000000000000000000'),
                'to': '0x673Fd582FED2CD8201d58552B912F0D1DaA37bB2'},
     'blockHash': '0x39ba45ad930dece3aec537c8c5cd615daf7ee39a2513475e7680ec226e90b923',
     'blockNumber': 6045252,
     'result': {'gasUsed': 150098, 'output': HexBytes('0x')},
     'subtraces': 1,
     'traceAddress': [1],
     'transactionHash': '0x18f8eb25336203d4e561229c08a3a0ef88db1dd9767b641301d9ea3121dfeaea',
     'transactionPosition': 0,
     'type': 'call'},
    {'action': {'from': '0x198C09f30dBa1494C741c510400cFE93B8287513',
                'gas': 13077,
                'value': 133700000000000000,
                'callType': 'call',
                'input': HexBytes('0x'),
                'to': '0x673Fd582FED2CD8201d58552B912F0D1DaA37bB2'},
     'blockHash': '0x08df561efd3d242263d8a117e32c1beb08454c87df0a287cf93fa39f0675cf04',
     'blockNumber': 6045275,
     'result': {'gasUsed': 1718, 'output': HexBytes('0x')},
     'subtraces': 1,
     'traceAddress': [],
     'transactionHash': '0xf554b52dcb336b83bf31e7e2e7aa94853a456f01a139a6b7dec71329460dfb61',
     'transactionPosition': 2,
     'type': 'call'},
    {'action': {'from': '0x5aC255889882aCd3da2aA939679E3f3d4cea221e',
                'gas': 976392,
                'value': 0,
                'callType': 'call',
                'input': HexBytes(
                    '0x6a761202000000000000000000000000e5738c4cf66f7d288ef4fe3cabd678ffb39cff8a000000000000000000000000000000000000000000000000000854c3dbff900000000000000000000000000000000000000000000000000000000000000001400000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000160000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000410000000000000000000000005ac255889882acd3da2aa939679e3f3d4cea221e00000000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000'),
                'to': '0x673Fd582FED2CD8201d58552B912F0D1DaA37bB2'},
     'blockHash': '0x842df51860be4dc03bbd1a08812f13db00bfe70cdaa0f68b3b29facb1a5bf283',
     'blockNumber': 6067026,
     'result': {'gasUsed': 40133,
                'output': HexBytes('0x0000000000000000000000000000000000000000000000000000000000000001')},
     'subtraces': 1,
     'traceAddress': [],
     'transactionHash': '0x304fa041d09c6d61295d479e4d0d0ac93f957c048feaf61e18d8322ec379fd3b',
     'transactionPosition': 3,
     'type': 'call'}
]

trace_transactions_result = [
    [
        {'action': {'from': '0x198C09f30dBa1494C741c510400cFE93B8287513',
                    'gas': 511126,
                    'value': 0,
                    'callType': 'call',
                    'input': HexBytes('0x61b69abd00000000000000000000000034cfac646f301356faa8b21e94227e3583fe3f5f00000000000000000000000000000000000000000000000000000000000000400000000000000000000000000000000000000000000000000000000000000164b63e800d0000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000140000000000000000000000000d5d82b6addc9027b22dca772aa68d5d74cdbdf440000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001000000000000000000000000198c09f30dba1494c741c510400cfe93b8287513000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'),
                    'to': '0x76E2cFc1F5Fa8F6a5b3fC4c8F4788F0116861F9B'},
         'blockHash': '0x39ba45ad930dece3aec537c8c5cd615daf7ee39a2513475e7680ec226e90b923',
         'blockNumber': 6045252,
         'result': {'gasUsed': 240081,
                    'output': HexBytes('0x000000000000000000000000673fd582fed2cd8201d58552b912f0d1daa37bb2')},
         'subtraces': 2,
         'traceAddress': [],
         'transactionHash': '0x18f8eb25336203d4e561229c08a3a0ef88db1dd9767b641301d9ea3121dfeaea',
         'transactionPosition': 0,
         'type': 'call'},
        {'action': {'from': '0x76E2cFc1F5Fa8F6a5b3fC4c8F4788F0116861F9B',
                    'gas': 470747,
                    'value': 0,
                    'init': HexBytes('0x608060405234801561001057600080fd5b506040516101e73803806101e78339818101604052602081101561003357600080fd5b8101908080519060200190929190505050600073ffffffffffffffffffffffffffffffffffffffff168173ffffffffffffffffffffffffffffffffffffffff1614156100ca576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004018080602001828103825260248152602001806101c36024913960400191505060405180910390fd5b806000806101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055505060aa806101196000396000f3fe608060405273ffffffffffffffffffffffffffffffffffffffff600054167fa619486e0000000000000000000000000000000000000000000000000000000060003514156050578060005260206000f35b3660008037600080366000845af43d6000803e60008114156070573d6000fd5b3d6000f3fea265627a7a72315820d8a00dc4fe6bf675a9d7416fc2d00bb3433362aa8186b750f76c4027269667ff64736f6c634300050e0032496e76616c6964206d617374657220636f707920616464726573732070726f766964656400000000000000000000000034cfac646f301356faa8b21e94227e3583fe3f5f')},
         'blockHash': '0x39ba45ad930dece3aec537c8c5cd615daf7ee39a2513475e7680ec226e90b923',
         'blockNumber': 6045252,
         'result': {'gasUsed': 55109,
                    'code': HexBytes('0x608060405273ffffffffffffffffffffffffffffffffffffffff600054167fa619486e0000000000000000000000000000000000000000000000000000000060003514156050578060005260206000f35b3660008037600080366000845af43d6000803e60008114156070573d6000fd5b3d6000f3fea265627a7a72315820d8a00dc4fe6bf675a9d7416fc2d00bb3433362aa8186b750f76c4027269667ff64736f6c634300050e0032'),
                    'address': '0x673Fd582FED2CD8201d58552B912F0D1DaA37bB2'},
         'subtraces': 0,
         'traceAddress': [0],
         'transactionHash': '0x18f8eb25336203d4e561229c08a3a0ef88db1dd9767b641301d9ea3121dfeaea',
         'transactionPosition': 0,
         'type': 'create'},
        {'action': {'from': '0x76E2cFc1F5Fa8F6a5b3fC4c8F4788F0116861F9B',
                    'gas': 415719,
                    'value': 0,
                    'callType': 'call',
                    'input': HexBytes('0xb63e800d0000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000140000000000000000000000000d5d82b6addc9027b22dca772aa68d5d74cdbdf440000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001000000000000000000000000198c09f30dba1494c741c510400cfe93b82875130000000000000000000000000000000000000000000000000000000000000000'),
                    'to': '0x673Fd582FED2CD8201d58552B912F0D1DaA37bB2'},
         'blockHash': '0x39ba45ad930dece3aec537c8c5cd615daf7ee39a2513475e7680ec226e90b923',
         'blockNumber': 6045252,
         'result': {'gasUsed': 150098, 'output': HexBytes('0x')},
         'subtraces': 1,
         'traceAddress': [1],
         'transactionHash': '0x18f8eb25336203d4e561229c08a3a0ef88db1dd9767b641301d9ea3121dfeaea',
         'transactionPosition': 0,
         'type': 'call'},
        {'action': {'from': '0x673Fd582FED2CD8201d58552B912F0D1DaA37bB2',
                    'gas': 407604,
                    'value': 0,
                    'callType': 'delegatecall',
                    'input': HexBytes('0xb63e800d0000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000140000000000000000000000000d5d82b6addc9027b22dca772aa68d5d74cdbdf440000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001000000000000000000000000198c09f30dba1494c741c510400cfe93b82875130000000000000000000000000000000000000000000000000000000000000000'),
                    'to': '0x34CfAC646f301356fAa8B21e94227e3583Fe3F5F'},
         'blockHash': '0x39ba45ad930dece3aec537c8c5cd615daf7ee39a2513475e7680ec226e90b923',
         'blockNumber': 6045252,
         'result': {'gasUsed': 148410, 'output': HexBytes('0x')},
         'subtraces': 0,
         'traceAddress': [1, 0],
         'transactionHash': '0x18f8eb25336203d4e561229c08a3a0ef88db1dd9767b641301d9ea3121dfeaea',
         'transactionPosition': 0,
         'type': 'call'}],
    [
        {'action': {'from': '0x198C09f30dBa1494C741c510400cFE93B8287513',
                    'gas': 13077,
                    'value': 133700000000000000,
                    'callType': 'call',
                    'input': HexBytes('0x'),
                    'to': '0x673Fd582FED2CD8201d58552B912F0D1DaA37bB2'},
         'blockHash': '0x08df561efd3d242263d8a117e32c1beb08454c87df0a287cf93fa39f0675cf04',
         'blockNumber': 6045275,
         'result': {'gasUsed': 1718, 'output': HexBytes('0x')},
         'subtraces': 1,
         'traceAddress': [],
         'transactionHash': '0xf554b52dcb336b83bf31e7e2e7aa94853a456f01a139a6b7dec71329460dfb61',
         'transactionPosition': 2,
         'type': 'call'},
        {'action': {'from': '0x673Fd582FED2CD8201d58552B912F0D1DaA37bB2',
                    'gas': 11315,
                    'value': 133700000000000000,
                    'callType': 'delegatecall',
                    'input': HexBytes('0x'),
                    'to': '0x34CfAC646f301356fAa8B21e94227e3583Fe3F5F'},
         'blockHash': '0x08df561efd3d242263d8a117e32c1beb08454c87df0a287cf93fa39f0675cf04',
         'blockNumber': 6045275,
         'result': {'gasUsed': 93, 'output': HexBytes('0x')},
         'subtraces': 0,
         'traceAddress': [0],
         'transactionHash': '0xf554b52dcb336b83bf31e7e2e7aa94853a456f01a139a6b7dec71329460dfb61',
         'transactionPosition': 2,
         'type': 'call'}],
    [
        {'action': {'from': '0x5aC255889882aCd3da2aA939679E3f3d4cea221e',
                    'gas': 976392,
                    'value': 0,
                    'callType': 'call',
                    'input': HexBytes('0x6a761202000000000000000000000000e5738c4cf66f7d288ef4fe3cabd678ffb39cff8a000000000000000000000000000000000000000000000000000854c3dbff900000000000000000000000000000000000000000000000000000000000000001400000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000160000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000410000000000000000000000005ac255889882acd3da2aa939679e3f3d4cea221e00000000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000'),
                    'to': '0x673Fd582FED2CD8201d58552B912F0D1DaA37bB2'},
         'blockHash': '0x842df51860be4dc03bbd1a08812f13db00bfe70cdaa0f68b3b29facb1a5bf283',
         'blockNumber': 6067026,
         'result': {'gasUsed': 40133,
                    'output': HexBytes('0x0000000000000000000000000000000000000000000000000000000000000001')},
         'subtraces': 1,
         'traceAddress': [],
         'transactionHash': '0x304fa041d09c6d61295d479e4d0d0ac93f957c048feaf61e18d8322ec379fd3b',
         'transactionPosition': 3,
         'type': 'call'},
        {'action': {'from': '0x673Fd582FED2CD8201d58552B912F0D1DaA37bB2',
                    'gas': 959492,
                    'value': 0,
                    'callType': 'delegatecall',
                    'input': HexBytes('0x6a761202000000000000000000000000e5738c4cf66f7d288ef4fe3cabd678ffb39cff8a000000000000000000000000000000000000000000000000000854c3dbff900000000000000000000000000000000000000000000000000000000000000001400000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000160000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000410000000000000000000000005ac255889882acd3da2aa939679e3f3d4cea221e00000000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000'),
                    'to': '0x34CfAC646f301356fAa8B21e94227e3583Fe3F5F'},
         'blockHash': '0x842df51860be4dc03bbd1a08812f13db00bfe70cdaa0f68b3b29facb1a5bf283',
         'blockNumber': 6067026,
         'result': {'gasUsed': 38418,
                    'output': HexBytes('0x0000000000000000000000000000000000000000000000000000000000000001')},
         'subtraces': 1,
         'traceAddress': [0],
         'transactionHash': '0x304fa041d09c6d61295d479e4d0d0ac93f957c048feaf61e18d8322ec379fd3b',
         'transactionPosition': 3,
         'type': 'call'},
        {'action': {'from': '0x673Fd582FED2CD8201d58552B912F0D1DaA37bB2',
                    'gas': 910006,
                    'value': 2345000000000000,
                    'callType': 'call',
                    'input': HexBytes('0x'),
                    'to': '0xe5738C4cF66f7d288Ef4fe3CaBd678FfB39CFF8A'},
         'blockHash': '0x842df51860be4dc03bbd1a08812f13db00bfe70cdaa0f68b3b29facb1a5bf283',
         'blockNumber': 6067026,
         'result': {'gasUsed': 1636, 'output': HexBytes('0x')},
         'subtraces': 1,
         'traceAddress': [0, 0],
         'transactionHash': '0x304fa041d09c6d61295d479e4d0d0ac93f957c048feaf61e18d8322ec379fd3b',
         'transactionPosition': 3,
         'type': 'call'},
        {'action': {'from': '0xe5738C4cF66f7d288Ef4fe3CaBd678FfB39CFF8A',
                    'gas': 894258,
                    'value': 2345000000000000,
                    'callType': 'delegatecall',
                    'input': HexBytes('0x'),
                    'to': '0xb6029EA3B2c51D09a50B53CA8012FeEB05bDa35A'},
         'blockHash': '0x842df51860be4dc03bbd1a08812f13db00bfe70cdaa0f68b3b29facb1a5bf283',
         'blockNumber': 6067026,
         'result': {'gasUsed': 40, 'output': HexBytes('0x')},
         'subtraces': 0,
         'traceAddress': [0, 0, 0],
         'transactionHash': '0x304fa041d09c6d61295d479e4d0d0ac93f957c048feaf61e18d8322ec379fd3b',
         'transactionPosition': 3,
         'type': 'call'}
    ]
]

block_result = [
    {'author': '0x0000000000000000000000000000000000000000',
     'difficulty': 1,
     'gasLimit': 10003834,
     'gasUsed': 2405566,
     'hash': HexBytes('0x842df51860be4dc03bbd1a08812f13db00bfe70cdaa0f68b3b29facb1a5bf283'),
     'logsBloom': HexBytes('0x0000000040004008000001000000000300000002100800000000000004100000000000010400000000000000000000000800000000008100000000200004008000000000000000002000000800000040000000080004020080010000000000002020004402000000001000000000080000000100000000000200001000000000000000000010000010000000a000000000000000000000000000000001000000000000000000000000000000000004400000000000000000000000000000000000000003000800000000000400000001000000000180000000020800000060000000004021000000000801010000000008000000000010024000000000000002'),
     'miner': '0x0000000000000000000000000000000000000000',
     'mixHash': HexBytes('0x0000000000000000000000000000000000000000000000000000000000000000'),
     'nonce': HexBytes('0x0000000000000000'),
     'number': 6067026,
     'parentHash': HexBytes('0xb7fa22be4fdc62780e022b8c66d38f4af39208cdeaa7da132cf0bc2576436b21'),
     'receiptsRoot': HexBytes('0x66a8961fcc5d2130298eb6caa061bee57f5582c357392e4a03803923e7c81128'),
     'sealFields': ['0xa00000000000000000000000000000000000000000000000000000000000000000',
                    '0x880000000000000000'],
     'sha3Uncles': HexBytes('0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347'),
     'size': 8093,
     'stateRoot': HexBytes('0xf4a52396ef0a1e5f1b35d1e21cb5313e0e51b183871da70ced7da5025fc645b4'),
     'timestamp': 1583146255,
     'totalDifficulty': 10893697,
     'transactions': [HexBytes('0xf65e0ed93640a6405614c6ed6aa3afbe344b01bbb0d75c8d5683eb2317bc24ff'),
                      HexBytes('0x51418f51ce8ea8763a928a165040622dc82dcf5c73ace3aa2894d61d37a27db6'),
                      HexBytes('0xefb8b297bf871854ecc5f186af967d28afe4376259268817e79a603abefafe6b'),
                      HexBytes('0x304fa041d09c6d61295d479e4d0d0ac93f957c048feaf61e18d8322ec379fd3b'),
                      HexBytes('0x34d153cd5d0a9bbda4a6bf135ed8b1372cf224765579d986edd1a7f9c9633f1d'),
                      HexBytes('0xc61d773aaa48301c71fc00bb51d554a939b3b9d4c70aab137624661234f82cb0')],
     'transactionsRoot': HexBytes('0xec62da89ece444f7d908f92ed3f449e6609bf4750a267447aacd819e44a53a2b'),
     'uncles': []},
    {'author': '0x0000000000000000000000000000000000000000',
     'difficulty': 1,
     'gasLimit': 9990236,
     'gasUsed': 765379,
     'hash': HexBytes('0x08df561efd3d242263d8a117e32c1beb08454c87df0a287cf93fa39f0675cf04'),
     'logsBloom': HexBytes('0x04000000000000400100000002000000004000012000000000000000002000000000000000001010010000000002000010000000024080404000000000800040000000000000400000000008000000200001010000140000182020000000200000000000420000000000000001000c00000200010000000000000010200600000008000400000000000100000000200200100000020000041000000024000200000000000020008000400200000402000000010000800000000080800000401100000002000800000000000000000000010000004005880000000820400020100040100000040000000000200080000000000008000000000000000000000000'),
     'miner': '0x0000000000000000000000000000000000000000',
     'mixHash': HexBytes('0x0000000000000000000000000000000000000000000000000000000000000000'),
     'nonce': HexBytes('0x0000000000000000'),
     'number': 6045275,
     'parentHash': HexBytes('0xe00ebe27186dd315897fe23f102c3828515a98285f9e3a41400d2845154d78a2'),
     'receiptsRoot': HexBytes('0x4f0734766b89d2d2a154b7962fb12a04123b109ea2cb989ccf5bdbd8b2fe3c42'),
     'sealFields': ['0xa00000000000000000000000000000000000000000000000000000000000000000',
                    '0x880000000000000000'],
     'sha3Uncles': HexBytes('0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347'),
     'size': 4531,
     'stateRoot': HexBytes('0x0a9f60138855264a50b53602a0aa4fca8452646efbed02065eaab27e2ced32b0'),
     'timestamp': 1582819812,
     'totalDifficulty': 10863879,
     'transactions': [HexBytes('0xe73443debf4eeb4b413f633697aa5849432bbec970bf403618927e364637716f'),
                      HexBytes('0x8be7e3281d9a03257a8c4bedf21a098fc03f6d3cec6e4acdcae565060704872d'),
                      HexBytes('0xf554b52dcb336b83bf31e7e2e7aa94853a456f01a139a6b7dec71329460dfb61'),
                      HexBytes('0xd740c97fc8c2b8f36113a2e7e048f11111b20ab7127bd807b40c87dc2959df00'),
                      HexBytes('0x8da111d5bc99f11d304acfbe1fa9b35d55308281be7ac9ade9151477f91055d6'),
                      HexBytes('0x4473cba16b542064484bd0759b7cc567e8a9a78ea25d2ad310b807057a7c297c'),
                      HexBytes('0x95780dc747a0d5760995bd5a6d6dfcc569c258560b1a409c5a7c0297b7947095'),
                      HexBytes('0xc8f5165706e97df8b87cab3fbbb9df3308ea738763601627d95b4684eaad4644'),
                      HexBytes('0xa213f9b612aa5b7ff62dc80fa409f039873fb2d4c9195614fea19b76b13ce6ed'),
                      HexBytes('0x2a5fea77c890060b897ef6a50b0470b414a32789fd85346e510e65ab1ebf255f')],
     'transactionsRoot': HexBytes('0xfb2ac6665384a718b8f77679fe415861436bf509acbddc7c38c1192e96432836'),
     'uncles': []},
    {'author': '0x0000000000000000000000000000000000000000',
     'difficulty': 2,
     'gasLimit': 10000000,
     'gasUsed': 518179,
     'hash': HexBytes('0x39ba45ad930dece3aec537c8c5cd615daf7ee39a2513475e7680ec226e90b923'),
     'logsBloom': HexBytes('0x0001000000000008000400000000000100000000000000000000000000000000000000000400000000100000001000000800000000000008000000000020008000000000000000000000000800000000000000010000000000000000000000000000000000000000000000000200000400000000000000800200001000000000000000000000000000000000200000000000100000000004000000000c000000000000000020000000002000000600000000000000000200000000000000000000000002000000000000000000000000000100000080080080000000000000002000004000000000000000200000004000000000000000000000000000800000'),
     'miner': '0x0000000000000000000000000000000000000000',
     'mixHash': HexBytes('0x0000000000000000000000000000000000000000000000000000000000000000'),
     'nonce': HexBytes('0x0000000000000000'),
     'number': 6045252,
     'parentHash': HexBytes('0x4f303258046f61f34fdc2498df3bc941c7d5c289f35fbd7db1301a17d573d303'),
     'receiptsRoot': HexBytes('0x9a1b95b8483f5ffc3fc1fbf8616594ad89a17275f86728410e84b2601a035ae1'),
     'sealFields': ['0xa00000000000000000000000000000000000000000000000000000000000000000',
                    '0x880000000000000000'],
     'sha3Uncles': HexBytes('0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347'),
     'size': 2440,
     'stateRoot': HexBytes('0x516e1d580931160fed498af46951958cf35f5bf82f140696ec33b8e707b5a2bd'),
     'timestamp': 1582819467,
     'totalDifficulty': 10863846,
     'transactions': [HexBytes('0x18f8eb25336203d4e561229c08a3a0ef88db1dd9767b641301d9ea3121dfeaea'),
                      HexBytes('0xd020b3807f87a0ca7392209b09c822281ab6abb28fe81718aa14afea28ed5962'),
                      HexBytes('0xf67735eb33bf983b5585541fa69078cbbf31e7f8bdc5544e9b3d04405348744e'),
                      HexBytes('0x59b87e5d93185a7d5c79771cf380342d2ccac60bd8aaa7ec5081dc633111e328'),
                      HexBytes('0x6f576357733618b328e14518d3bf2940427fbd74945ed1abcce0b6147fb631e7'),
                      HexBytes('0x0af66669ae391e3762d7993b039962c4105594387be0c9e0ca0d8ba0ef44f7e0')],
     'transactionsRoot': HexBytes('0x1284b972b8e1ead0533c425d2ece1640dcceafb72366aa2f997681fd7171d12d'),
     'uncles': []},
]

transactions_result = [
    {'blockHash': HexBytes('0x39ba45ad930dece3aec537c8c5cd615daf7ee39a2513475e7680ec226e90b923'),
     'blockNumber': 6045252,
     'chainId': '0x4',
     'condition': None,
     'creates': None,
     'from': '0x5aC255889882aCd3da2aA939679E3f3d4cea221e',
     'gas': 534974,
     'gasPrice': 4000000000,
     'hash': HexBytes('0x18f8eb25336203d4e561229c08a3a0ef88db1dd9767b641301d9ea3121dfeaea'),
     'input': '0x61b69abd00000000000000000000000034cfac646f301356faa8b21e94227e3583fe3f5f00000000000000000000000000000000000000000000000000000000000000400000000000000000000000000000000000000000000000000000000000000164b63e800d0000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000140000000000000000000000000d5d82b6addc9027b22dca772aa68d5d74cdbdf4400000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010000000000000000000000005ac255889882acd3da2aa939679e3f3d4cea221e000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
     'nonce': 383,
     'publicKey': HexBytes('0x5848c6556133fcb815b2b5f7dc7ef966c84997c00970176980962f00b107448bfc0b2d2270d758259526afb906f27485d9be235f842a205067a857b9935e6633'),
     'r': HexBytes('0xb851af4de5e696451bf8c4351e24ea6f6a14ccb980115867b525885b4f7ef445'),
     'raw': HexBytes('0xf9024c82017f84ee6b2800830829be9476e2cfc1f5fa8f6a5b3fc4c8f4788f0116861f9b80b901e461b69abd00000000000000000000000034cfac646f301356faa8b21e94227e3583fe3f5f00000000000000000000000000000000000000000000000000000000000000400000000000000000000000000000000000000000000000000000000000000164b63e800d0000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000140000000000000000000000000d5d82b6addc9027b22dca772aa68d5d74cdbdf4400000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010000000000000000000000005ac255889882acd3da2aa939679e3f3d4cea221e0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002ca0b851af4de5e696451bf8c4351e24ea6f6a14ccb980115867b525885b4f7ef445a07c06da6780e24fa74788f4c90bf023107df4353c70ba42e52a1fd2b10e743e87'),
     's': HexBytes('0x7c06da6780e24fa74788f4c90bf023107df4353c70ba42e52a1fd2b10e743e87'),
     'standardV': 1,
     'to': '0x76E2cFc1F5Fa8F6a5b3fC4c8F4788F0116861F9B',
     'transactionIndex': 0,
     'v': 44,
     'value': 0},
    {'blockHash': HexBytes('0x08df561efd3d242263d8a117e32c1beb08454c87df0a287cf93fa39f0675cf04'),
     'blockNumber': 6045275,
     'chainId': '0x4',
     'condition': None,
     'creates': None,
     'from': '0x5aC255889882aCd3da2aA939679E3f3d4cea221e',
     'gas': 34077,
     'gasPrice': 5000000000,
     'hash': HexBytes('0xf554b52dcb336b83bf31e7e2e7aa94853a456f01a139a6b7dec71329460dfb61'),
     'input': '0x',
     'nonce': 384,
     'publicKey': HexBytes('0x5848c6556133fcb815b2b5f7dc7ef966c84997c00970176980962f00b107448bfc0b2d2270d758259526afb906f27485d9be235f842a205067a857b9935e6633'),
     'r': HexBytes('0xbf9deafa678debae1daaa568ff90fbd7ca92ac299b7dc7288036636bd30ea7fd'),
     'raw': HexBytes('0xf86e82018085012a05f20082851d94673fd582fed2cd8201d58552b912f0d1daa37bb28801daff710e784000802ba0bf9deafa678debae1daaa568ff90fbd7ca92ac299b7dc7288036636bd30ea7fda07fb6477909024dc65bd202596154cb0e6df5e59e6a5bcfda24d933f83c6a7a03'),
     's': HexBytes('0x7fb6477909024dc65bd202596154cb0e6df5e59e6a5bcfda24d933f83c6a7a03'),
     'standardV': 0,
     'to': '0x673Fd582FED2CD8201d58552B912F0D1DaA37bB2',
     'transactionIndex': 2,
     'v': 43,
     'value': 133700000000000000},
    {'blockHash': HexBytes('0x842df51860be4dc03bbd1a08812f13db00bfe70cdaa0f68b3b29facb1a5bf283'),
     'blockNumber': 6067026,
     'chainId': '0x4',
     'condition': None,
     'creates': None,
     'from': '0x5aC255889882aCd3da2aA939679E3f3d4cea221e',
     'gas': 1000000,
     'gasPrice': 1000000000,
     'hash': HexBytes('0x304fa041d09c6d61295d479e4d0d0ac93f957c048feaf61e18d8322ec379fd3b'),
     'input': '0x6a761202000000000000000000000000e5738c4cf66f7d288ef4fe3cabd678ffb39cff8a000000000000000000000000000000000000000000000000000854c3dbff900000000000000000000000000000000000000000000000000000000000000001400000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000160000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000410000000000000000000000005ac255889882acd3da2aa939679e3f3d4cea221e00000000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000',
     'nonce': 385,
     'publicKey': HexBytes('0x5848c6556133fcb815b2b5f7dc7ef966c84997c00970176980962f00b107448bfc0b2d2270d758259526afb906f27485d9be235f842a205067a857b9935e6633'),
     'r': HexBytes('0x31ae56587fb376fdfdd9fd303e86bc78cd4248575b7e9262518a46c983a4bfb4'),
     'raw': HexBytes('0xf9024c820181843b9aca00830f424094673fd582fed2cd8201d58552b912f0d1daa37bb280b901e46a761202000000000000000000000000e5738c4cf66f7d288ef4fe3cabd678ffb39cff8a000000000000000000000000000000000000000000000000000854c3dbff900000000000000000000000000000000000000000000000000000000000000001400000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000160000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000410000000000000000000000005ac255889882acd3da2aa939679e3f3d4cea221e000000000000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000000000000000002ca031ae56587fb376fdfdd9fd303e86bc78cd4248575b7e9262518a46c983a4bfb4a01218c330d8ecea4494521a61b532951f7aa77ac95607eda6d5f6ec846c0c5a76'),
     's': HexBytes('0x1218c330d8ecea4494521a61b532951f7aa77ac95607eda6d5f6ec846c0c5a76'),
     'standardV': 1,
     'to': '0x673Fd582FED2CD8201d58552B912F0D1DaA37bB2',
     'transactionIndex': 3,
     'v': 44,
     'value': 0}
]

transaction_receipts_result = [
    {'blockHash': HexBytes('0x39ba45ad930dece3aec537c8c5cd615daf7ee39a2513475e7680ec226e90b923'),
     'blockNumber': 6045252,
     'contractAddress': None,
     'cumulativeGasUsed': 263929,
     'from': '0x5aC255889882aCd3da2aA939679E3f3d4cea221e',
     'gasUsed': 263929,
     'logs': [{'address': '0x76E2cFc1F5Fa8F6a5b3fC4c8F4788F0116861F9B',
               'blockHash': HexBytes('0x39ba45ad930dece3aec537c8c5cd615daf7ee39a2513475e7680ec226e90b923'),
               'blockNumber': 6045252,
               'data': '0x000000000000000000000000673fd582fed2cd8201d58552b912f0d1daa37bb2',
               'logIndex': 0,
               'removed': False,
               'topics': [HexBytes('0xa38789425dbeee0239e16ff2d2567e31720127fbc6430758c1a4efc6aef29f80')],
               'transactionHash': HexBytes('0x18f8eb25336203d4e561229c08a3a0ef88db1dd9767b641301d9ea3121dfeaea'),
               'transactionIndex': 0,
               'transactionLogIndex': '0x0',
               'type': 'mined'}],
     'logsBloom': HexBytes('0x00010000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000080000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000002000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002000000000000000000000000000004000000000000000000000000000000000'),
     'status': 1,
     'to': '0x76E2cFc1F5Fa8F6a5b3fC4c8F4788F0116861F9B',
     'transactionHash': HexBytes('0x18f8eb25336203d4e561229c08a3a0ef88db1dd9767b641301d9ea3121dfeaea'),
     'transactionIndex': 0},
    {'blockHash': HexBytes('0x08df561efd3d242263d8a117e32c1beb08454c87df0a287cf93fa39f0675cf04'),
     'blockNumber': 6045275,
     'contractAddress': None,
     'cumulativeGasUsed': 95430,
     'from': '0x5aC255889882aCd3da2aA939679E3f3d4cea221e',
     'gasUsed': 22718,
     'logs': [],
     'logsBloom': HexBytes('0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'),
     'status': 1,
     'to': '0x673Fd582FED2CD8201d58552B912F0D1DaA37bB2',
     'transactionHash': HexBytes('0xf554b52dcb336b83bf31e7e2e7aa94853a456f01a139a6b7dec71329460dfb61'),
     'transactionIndex': 2},
    {'blockHash': HexBytes('0x842df51860be4dc03bbd1a08812f13db00bfe70cdaa0f68b3b29facb1a5bf283'),
     'blockNumber': 6067026,
     'contractAddress': None,
     'cumulativeGasUsed': 1442004,
     'from': '0x5aC255889882aCd3da2aA939679E3f3d4cea221e',
     'gasUsed': 63741,
     'logs': [{'address': '0x673Fd582FED2CD8201d58552B912F0D1DaA37bB2',
               'blockHash': HexBytes('0x842df51860be4dc03bbd1a08812f13db00bfe70cdaa0f68b3b29facb1a5bf283'),
               'blockNumber': 6067026,
               'data': '0x2c33121a2f432d6cec593c2d756bd8d69a4833eb55ae993428cf50c748a1ab4d0000000000000000000000000000000000000000000000000000000000000000',
               'logIndex': 1,
               'removed': False,
               'topics': [HexBytes('0x442e715f626346e8c54381002da614f62bee8d27386535b2521ec8540898556e')],
               'transactionHash': HexBytes('0x304fa041d09c6d61295d479e4d0d0ac93f957c048feaf61e18d8322ec379fd3b'),
               'transactionIndex': 3,
               'transactionLogIndex': '0x0',
               'type': 'mined'}],
     'logsBloom': HexBytes('0x00000000400000000000000000000000000000001000000000000000040000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000800000000800000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000004000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'),
     'status': 1,
     'to': '0x673Fd582FED2CD8201d58552B912F0D1DaA37bB2',
     'transactionHash': HexBytes('0x304fa041d09c6d61295d479e4d0d0ac93f957c048feaf61e18d8322ec379fd3b'),
     'transactionIndex': 3}
]
