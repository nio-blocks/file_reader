from collections import defaultdict
from unittest.mock import patch, MagicMock, mock_open
from nio.common.signal.base import Signal
from nio.util.support.block_test_case import NIOBlockTestCase
from ..file_reader_block import FileReader


class TestFileReader(NIOBlockTestCase):

    def setUp(self):
        super().setUp()
        # This will keep a list of signals notified for each output
        self.last_notified = defaultdict(list)

    def signals_notified(self, signals, output_id='default'):
        self.last_notified[output_id].extend(signals)

    def test_defaults(self):
        blk = FileReader()
        self.configure_block(blk, {})
        mock = mock_open(read_data='this is my amazing file')
        with patch('builtins.open', mock):
            blk.process_signals([Signal({'a': 1})])
        self.assert_num_signals_notified(1)
        self.assertDictEqual(self.last_notified['default'][0].to_dict(),
                             {'file': '/tmp/file.txt',
                              'contents': 'this is my amazing file'})

    def test_properties(self):
        blk = FileReader()
        file = '/text.txt'
        file_contents = 'this is not a test... actually, it is.'
        file_attr = 'my_file'
        contents_attr = 'file_contents'
        self.configure_block(blk, {'file': file,
                                   'file_attr': file_attr,
                                   'contents_attr': contents_attr})
        mock = mock_open(read_data=file_contents)
        with patch('builtins.open', mock):
            blk.process_signals([Signal({'a': 1})])
        self.assert_num_signals_notified(1)
        self.assertDictEqual(self.last_notified['default'][0].to_dict(),
                             {file_attr: file,
                              contents_attr: file_contents})

    def test_enrich_signals_mixin(self):
        blk = FileReader()
        file_contents = 'mixin'
        self.configure_block(blk, {'enrich':
                                   {'enrich_field': 'new_field',
                                    'exclude_existing': False}})
        mock = mock_open(read_data=file_contents)
        with patch('builtins.open', mock):
            blk.process_signals([Signal({'a': 1})])
        self.assert_num_signals_notified(1)
        self.assertDictEqual(self.last_notified['default'][0].to_dict(),
                             {'a': 1,
                              'new_field':
                              {'file': '/tmp/file.txt',
                               'contents': file_contents}})
