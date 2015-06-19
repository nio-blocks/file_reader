from nio.common.block.base import Block
from nio.common.discovery import Discoverable, DiscoverableType
from nio.metadata.properties import ExpressionProperty, StringProperty, \
    VersionProperty


@Discoverable(DiscoverableType.block)
class FileReader(Block):

    """ Reads contents of a file.

    Input signal trigger a read from a file. The contents of that file are
    placed on the notified signal in a configurable attribute.
    """
    file = ExpressionProperty(title='File', default='/tmp/file.txt')
    file_attr = StringProperty(title='File Field', default='file')
    contents_attr = StringProperty(title='File Contents Field',
                                   default='contents')
    version = VersionProperty('0.1.0')

    def process_signals(self, signals, input_id='default'):
        for signal in signals:
            try:
                file = self.file(signal)
            except:
                self._logger.exception('Failed to evaluate file location')
                continue
            try:
                self._logger.debug('Opening file: {}'.format(file))
                with open(file) as openfile:
                    self._logger.debug('Reading from file: {}'.format(file))
                    setattr(signal, self.contents_attr, openfile.read())
                    setattr(signal, self.file_attr, file)
            except:
                self._logger.exception('Failed to open/read file'.format(file))
                continue
        self.notify_signals(signals)
