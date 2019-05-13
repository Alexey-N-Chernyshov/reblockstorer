import sys

from . import arguments
from .loader import BlockLoader
from .keystore import Keystore
from .processor import Processor


def main():
    parser = arguments.init_parser()
    params = parser.parse_args()
    params = arguments.validate(parser, params)
    block_loader = BlockLoader(params.blockstore)
    keystore = Keystore(params.keydir)
    processor = Processor(block_loader, keystore)
    processor.process()


if __name__ == "__main__":
    main()
