from os.path import join, dirname, realpath, isfile
from nio.common.block.base import Block
from nio.common.discovery import Discoverable, DiscoverableType
from nio.metadata.properties import ExpressionProperty, StringProperty, \
    VersionProperty
from nio.util.environment import NIOEnvironment
from .mixins.enrich.enrich_signals import EnrichSignals


@Discoverable(DiscoverableType.block)
class FileReader(EnrichSignals, Block):

    """ Reads contents of a file.

    Input signals trigger a read from a file. The contents of that file are
    placed on the notified signal in a configurable attribute.
    """
    file = ExpressionProperty(title='File', default='/tmp/file.txt')
    file_attr = StringProperty(title='File Field', default='file')
    contents_attr = StringProperty(title='File Contents Field',
                                   default='contents')
    version = VersionProperty('0.1.0')

    def process_signals(self, signals, input_id='default'):
        out_sigs = []
        for signal in signals:
            signal_data = {}
            try:
                file = self._get_filename(signal)
            except:
                self._logger.exception('Failed to evaluate file location')
                continue
            try:
                self._logger.debug('Opening file: {}'.format(file))
                with open(file) as openfile:
                    self._logger.debug('Reading from file: {}'.format(file))
                    signal_data[self.contents_attr] = openfile.read()
                    signal_data[self.file_attr] = file
            except:
                self._logger.exception(
                    'Failed to open/read file: {}'.format(file))
                continue
            # Use EnrichSignals mixin to build output signal
            out_sigs.append(self.get_output_signal(signal_data, signal))
        if out_sigs:
            self.notify_signals(out_sigs)

    def _get_filename(self, signal):
        filename = self.file(signal)
        # Let's figure out where the file is
        filename = self._get_valid_file(
            # First, just see if it's maybe already a file?
            filename,
            # Next, try in the NIO environment
            NIOEnvironment.get_path(filename),
            # Finally, try relative to the current file
            join(dirname(realpath(__file__)), filename)
        )
        return filename

    def _get_valid_file(self, *args):
        """ Go through args and return the first valid file, None if none are.
        """
        for arg in args:
            if isfile(arg):
                return arg
        return None
