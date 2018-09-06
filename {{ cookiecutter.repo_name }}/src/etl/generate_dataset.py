"""Dataset generation example."""

import os
import logging
import shutil

logger = logging.getLogger(__name__)


def main():
    """Generate a dataset using raw input data.

    :param model_name: the name of the
    """
    logger.info('Copying iris dataset from raw to tranformed')
    logger.info('Skipping staging, not relevant for this example')
    print(os.environ)
    os.listdir(os.getenv('DATA_RAW'))
    shutil.copyfile(
        os.path.join(os.getenv('DATA_RAW'), 'iris.csv'),
        os.path.join(os.getenv('DATA_TRANSFORMED'), 'iris.csv')
    )

    logger.info('Done')


if __name__ == '__main__':
    main()
