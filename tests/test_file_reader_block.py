from unittest.mock import patch, MagicMock, mock_open

from nio.signal.base import Signal
from nio.testing.block_test_case import NIOBlockTestCase
from nio.block.terminals import DEFAULT_TERMINAL

from ..file_reader_block import FileReader


class TestFileReader(NIOBlockTestCase):

    def test_defaults(self):
        blk = FileReader()
        blk._get_filename = MagicMock(return_value='/tmp/file.txt')
        self.configure_block(blk, {})
        mock = mock_open(read_data='this is my amazing file')
        with patch('builtins.open', mock):
            blk.process_signals([Signal({'a': 1})])
        self.assert_num_signals_notified(1)
        self.assertDictEqual(self.last_notified[DEFAULT_TERMINAL][0].to_dict(),
                             {'file': '/tmp/file.txt',
                              'contents': 'this is my amazing file'})

    def test_properties(self):
        blk = FileReader()
        file = '/text.txt'
        file_contents = 'this is not a test... actually, it is.'
        file_attr = 'my_file'
        contents_attr = 'file_contents'
        blk._get_filename = MagicMock(return_value=file)
        self.configure_block(blk, {'file': file,
                                   'file_attr': file_attr,
                                   'contents_attr': contents_attr})
        mock = mock_open(read_data=file_contents)
        with patch('builtins.open', mock):
            blk.process_signals([Signal({'a': 1})])
        self.assert_num_signals_notified(1)
        self.assertDictEqual(self.last_notified[DEFAULT_TERMINAL][0].to_dict(),
                             {file_attr: file,
                              contents_attr: file_contents})

    def test_enrich_signals_mixin(self):
        blk = FileReader()
        file_contents = 'mixin'
        blk._get_filename = MagicMock(return_value='/tmp/file.txt')
        self.configure_block(blk, {'enrich':
                                   {'enrich_field': 'new_field',
                                    'exclude_existing': False}})
        mock = mock_open(read_data=file_contents)
        with patch('builtins.open', mock):
            blk.process_signals([Signal({'a': 1})])
        self.assert_num_signals_notified(1)
        self.assertDictEqual(self.last_notified[DEFAULT_TERMINAL][0].to_dict(),
                             {'a': 1,
                              'new_field':
                              {'file': '/tmp/file.txt',
                               'contents': file_contents}})
