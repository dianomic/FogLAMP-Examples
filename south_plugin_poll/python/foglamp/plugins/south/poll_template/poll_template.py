# -*- coding: utf-8 -*-

# FOGLAMP_BEGIN
# See: http://foglamp.readthedocs.io/
# FOGLAMP_END

""" Template module for 'poll' mode south plugin """

import copy
from datetime import datetime, timezone
import random
import uuid

from foglamp.common import logger
from foglamp.services.south import exceptions

__author__ = "Stefano Simonelli"
__copyright__ = "Copyright (c) 2017 OSIsoft, LLC"
__license__ = "Apache 2.0"
__version__ = "${VERSION}"

_DEFAULT_CONFIG = {
    'plugin': {
         'description': 'Python module name of the plugin to load',
         'type': 'string',
         'default': 'poll_template'
    },
    'pollInterval': {
        'description': 'The interval between polling calls (in milliseconds)',
        'type': 'integer',
        'default': '500'
    }

}

_LOGGER = logger.setup(__name__)


def plugin_info():
    """ Returns information about the plugin

    Args:
    Returns:
        dict: plugin information
    Raises:
    """

    return {
        'name': 'Poll plugin',
        'version': '1.0',
        'mode': 'poll', ''
        'type': 'south',
        'interface': '1.0',
        'config': _DEFAULT_CONFIG
    }


def plugin_init(config):
    """ Initialise the plugin.

    Args:
        config: JSON configuration document for the South plugin configuration category
    Returns:
        handle: JSON object to be used in future calls to the plugin
    Raises:
    """

    handle = config
    return handle


def plugin_poll(handle):
    """ Extracts data from the sensor and returns it in a JSON document as a Python dict.

    Available for poll mode only.

    Args:
        handle: handle returned by the plugin initialisation call
    Returns:
        returns a sensor reading in a JSON document;
        A Python dict - if it is available,
        None - If no reading is available
    Raises:
        DataRetrievalError
    """

    timestamp = str(datetime.now(tz=timezone.utc))

    try:
        data = {
                'asset': 'poll_template',
                'timestamp': timestamp,
                'key': str(uuid.uuid4()),
                'readings':  {'value': random.randint(0, 1000)}
        }

    except Exception as ex:
        raise exceptions.DataRetrievalError(ex)

    return data


def plugin_reconfigure(handle, new_config):
    """ Reconfigures the plugin,

    it should be called when the configuration of the plugin is changed during the operation of the South plugin service
    The new configuration category should be passed.

    Args:
        handle: handle returned by the plugin initialisation call
        new_config: JSON object representing the new configuration category
    Returns:
        new_handle: new handle to be used in the future calls
    Raises:
    """

    # Find diff between old config and new config
    diff = dict()  # get diff(handle, new_config)

    # Plugin should re-initialize and restart if key configuration is changed
    # e.g. port / uri / management_host or BLE address etc.
    if 'port' in diff or 'uri' in diff or 'management_host' in diff:
        # write necessary code to stop the plugin here
        new_handle = plugin_init(new_config)
        new_handle['restart'] = 'yes'
        _LOGGER.info("Restarting <name> plugin due to change in configuration keys [{}]".format(', '.join(diff)))
    else:
        new_handle = copy.deepcopy(handle)
        new_handle['restart'] = 'no'
    return new_handle


def plugin_shutdown(handle):
    """ Shutdown the plugin and does required cleanup

    To be called prior to the South service being shut down.

    Args:
        handle: handle returned by the plugin initialisation call
    Returns:
    Raises:
    """
    # disconnect the communication with the thing
    # cleanup
    _LOGGER.info('<name> poll plugin shut down.')
