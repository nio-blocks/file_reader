from nio.block.base import Block
from nio.properties import StringProperty, VersionProperty, FileProperty
from nio.block.mixins import EnrichSignals


class FileReader(EnrichSignals, Block):

    """ Reads contents of a file.

    Input signals trigger a read from a file. The contents of that file are
    placed on the notified signal in a configurable attribute.
    """
    file = FileProperty(title='File', default='/tmp/file.txt')
    file_attr = StringProperty(title='File Field', default='file')
    contents_attr = StringProperty(title='File Contents Field',
                                   default='contents')
    version = VersionProperty("0.1.0")

    def process_signals(self, signals, input_id='default'):
        out_sigs = []
        for signal in signals:
            signal_data = {}
            try:
                file = self.file(signal).value
            except:
                self.logger.exception('Failed to evaluate file location')
                continue
            try:
                self.logger.debug('Opening file: {}'.format(file))
                with open(file) as openfile:
                    self.logger.debug('Reading from file: {}'.format(file))
                    signal_data[self.contents_attr()] = openfile.read()
                    signal_data[self.file_attr()] = file
            except:
                self.logger.exception(
                    'Failed to open/read file: {}'.format(file))
                continue
            # Use EnrichSignals mixin to build output signal
            out_sigs.append(self.get_output_signal(signal_data, signal))
        if out_sigs:
            self.notify_signals(out_sigs)
