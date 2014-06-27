from logging import getLogger
from nose.tools import eq_

from thaumcraft.main import main, process


logger = getLogger()


def test_main_anything():
    paths = process('aer', 'aer', 2)
    logger.debug('paths: {}'.format(paths))
    eq_(len(paths), 7)  # 7 is how many aspects have aer as a component
