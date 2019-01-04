# -*- coding: utf-8 -*-

# FOGLAMP_BEGIN
# See: http://foglamp.readthedocs.io/
# FOGLAMP_END

from python.foglamp.plugins.south.poll_template import poll_template

__author__ = "Praveen Garg"
__copyright__ = "Copyright (c) 2018 Dianomic Systems"
__license__ = "Apache 2.0"
__version__ = "${VERSION}"

config = poll_template._DEFAULT_CONFIG


def test_plugin_contract():
    # check the plugin has all the required methods
    assert callable(getattr(poll_template, 'plugin_info'))
    assert callable(getattr(poll_template, 'plugin_init'))
    assert callable(getattr(poll_template, 'plugin_poll'))
    assert callable(getattr(poll_template, 'plugin_shutdown'))
    assert callable(getattr(poll_template, 'plugin_reconfigure'))


def test_plugin_info():
    pass


def test_plugin_init():
    pass


def test_plugin_poll():
    pass


def test_plugin_reconfigure():
    pass


def test_plugin_shutdown():
    pass
