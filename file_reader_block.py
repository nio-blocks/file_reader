from nio.common.block.base import Block
from nio.common.discovery import Discoverable, DiscoverableType


@Discoverable(DiscoverableType.block)
class FileReader(Block):

    """ Reads contents of a file.

    Input signal trigger a read from a file. The contents of that file are
    placed on the notified signal in a configurable attribute.
    """

    def process_signals(self, signals, input_id='default'):
        pass
