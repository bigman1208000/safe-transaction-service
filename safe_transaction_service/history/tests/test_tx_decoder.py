import logging

from django.test import TestCase

from hexbytes import HexBytes

from ..indexers.tx_decoder import (SafeTxDecoder, TxDecoder,
                                   get_safe_tx_decoder, get_tx_decoder)

logger = logging.getLogger(__name__)


class TestTxDecoder(TestCase):
    def test_singleton(self):
        self.assertTrue(isinstance(get_tx_decoder(), TxDecoder))
        self.assertTrue(isinstance(get_safe_tx_decoder(), SafeTxDecoder))

    def test_supported_fn_selectors(self):
        for tx_decoder in (TxDecoder(), get_tx_decoder(), get_safe_tx_decoder()):
            self.assertIn(b'jv\x12\x02', tx_decoder.supported_fn_selectors)  # execTransaction for Safe >= V1.0.0
            self.assertIn(b'\xb6>\x80\r', tx_decoder.supported_fn_selectors)  # setup for Safe V1.1.0
            self.assertIn(b'\xa9z\xb1\x8a', tx_decoder.supported_fn_selectors)  # setup for Safe V1.0.0

    def test_decode_execute_transaction(self):
        tx_data = HexBytes('0x6a761202000000000000000000000000d9ab7371432d7cc74503290412618c948cddacf200000000000000000'
                           '0000000000000000000000000000000002386f26fc1000000000000000000000000000000000000000000000000'
                           '0000000000000000014000000000000000000000000000000000000000000000000000000000000000000000000'
                           '000000000000000000000000000000000000000000000000000030d400000000000000000000000000000000000'
                           '0000000000000000000000000186a000000000000000000000000000000000000000000000000000000004a817c'
                           '8000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
                           '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
                           '0000000000180000000000000000000000000000000000000000000000000000000000000000000000000000000'
                           '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
                           '00000000000000000000041512215e7f982c8f8e8429c9008068366dcb96bb3abd9c969f3bf2f97f013da6941e1'
                           '59f13ca524a6b449accf1ce6765ad811ee7b7151f74749e38ac8bc94fb3b1c00000000000000000000000000000'
                           '000000000000000000000000000000000')

        tx_decoder = TxDecoder()
        function_name, arguments = tx_decoder.decode_transaction(tx_data)
        self.assertEqual(function_name, 'execTransaction')
        self.assertIn('baseGas', arguments)
        self.assertEqual(type(arguments['data']), str)

    def test_decode_execute_transaction_with_types(self):
        tx_data = HexBytes('0x6a7612020000000000000000000000005592ec0cfb4dbc12d3ab100b257153436a1f0fea0000'
                           '000000000000000000000000000000000000000000000000000000000000000000000000000000'
                           '000000000000000000000000000000000000000000014000000000000000000000000000000000'
                           '000000000000000000000000000000000000000000000000000000000000000000000000000000'
                           '000000000000000000000000000000000000000000000000000000000000000000000000000000'
                           '000000000000000000000000000000000000000000000000000000000000000000000000000000'
                           '000000000000000000000000000000000000000000000000000000000000000000000000000000'
                           '000000000000000000000000000000000000000000000000000000000000000000000000000000'
                           '000000000000000000000001c00000000000000000000000000000000000000000000000000000'
                           '000000000044a9059cbb0000000000000000000000000dc0dfd22c6beab74672eade5f9be5234a'
                           'aa43cc00000000000000000000000000000000000000000000000000005af3107a400000000000'
                           '000000000000000000000000000000000000000000000000000000000000000000000000000000'
                           '00000000000000000000000000000000820000000000000000000000000dc0dfd22c6beab74672'
                           'eade5f9be5234aaa43cc0000000000000000000000000000000000000000000000000000000000'
                           '00000001000000000000000000000000c791cb32ddb43de8260e6a2762b3b03498b615e5000000'
                           '000000000000000000000000000000000000000000000000000000000001000000000000000000'
                           '000000000000000000000000000000000000000000')

        tx_decoder = TxDecoder()
        function_name, arguments = tx_decoder.decode_transaction_with_types(tx_data)
        self.assertEqual(function_name, 'execTransaction')
        self.assertEqual(arguments, [{'name': 'to',
                                      'type': 'address',
                                      'value': '0x5592EC0cfb4dbc12D3aB100b257153436a1f0FEa'},
                                     {'name': 'value', 'type': 'uint256', 'value': 0},
                                     {'name': 'data',
                                      'type': 'bytes',
                                      'value': '0xa9059cbb0000000000000000000000000dc0dfd22c6beab74672eade5f9be5234aaa4'
                                               '3cc00000000000000000000000000000000000000000000000000005af3107a4000'},
                                     {'name': 'operation', 'type': 'uint8', 'value': 0},
                                     {'name': 'safeTxGas', 'type': 'uint256', 'value': 0},
                                     {'name': 'baseGas', 'type': 'uint256', 'value': 0},
                                     {'name': 'gasPrice', 'type': 'uint256', 'value': 0},
                                     {'name': 'gasToken',
                                      'type': 'address',
                                      'value': '0x0000000000000000000000000000000000000000'},
                                     {'name': 'refundReceiver',
                                      'type': 'address',
                                      'value': '0x0000000000000000000000000000000000000000'},
                                     {'name': 'signatures',
                                      'type': 'bytes',
                                      'value': '0x0000000000000000000000000dc0dfd22c6beab74672eade5f9be5234aaa43cc00000'
                                               '00000000000000000000000000000000000000000000000000000000000010000000000'
                                               '00000000000000c791cb32ddb43de8260e6a2762b3b03498b615e500000000000000000'
                                               '0000000000000000000000000000000000000000000000001'}]
                         )

    def test_decode_old_execute_transaction(self):
        data = HexBytes('0x6a761202000000000000000000000000a8cc2fc5756f1cba332fefa093ea1d3c6faf559c00000000000000000000'
                        '0000000000000000000000000000002386f26fc1000000000000000000000000000000000000000000000000000000'
                        '0000000000014000000000000000000000000000000000000000000000000000000000000000000000000000000000'
                        '000000000000000000000000000000000000000000030d400000000000000000000000000000000000000000000000'
                        '0000000000000186a000000000000000000000000000000000000000000000000000000004a817c800000000000000'
                        '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
                        '0000000000000000000000000000000000000000000000000000000000000000000000000000000000018000000000'
                        '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
                        '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
                        '000000000000000000000000000000000000000000000000000000000000')

        tx_decoder = TxDecoder()
        function_name, arguments = tx_decoder.decode_transaction(data)
        self.assertEqual(function_name, 'execTransaction')
        # self.assertIn('dataGas', arguments)
        self.assertIn('baseGas', arguments)  # Signature of the tx is the same
