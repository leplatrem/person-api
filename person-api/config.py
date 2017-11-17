"""
:mod:`person-api.config` -- PersonAPI configuration
* Environment variables used
 * API_AUDIENCE
 * AUTH0_URL
"""


from everett.manager import ConfigManager
from everett.manager import ConfigOSEnv


def get_config():
    return ConfigManager(
        [
            ConfigOSEnv()
        ]
)
