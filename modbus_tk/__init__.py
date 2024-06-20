import logging

formatter = "%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s"
logging.basicConfig(format=formatter, level=logging.DEBUG)


LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)
