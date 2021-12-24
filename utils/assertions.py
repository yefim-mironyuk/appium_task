from loguru import logger
from assertpy import assert_that
from .logging import Logger

Logger()


def are_objects_equal(object1, object2):
    logger.debug(f'Checking is "{object2}" equal "{object1}"...')
    try:
        assert_that(object1).is_equal_to(object2)
    except AssertionError:
        logger.error(f'Error "{object1}" IS NOT EQUAL "{object2}"!')
        raise
    logger.debug(f'"{object2}" is equal "{object1}"...')
