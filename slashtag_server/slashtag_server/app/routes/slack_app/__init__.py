# noqa: F401
from .slack_actions import *  # noqa: F401
from .slack_app_config import slack_app
from .slack_commands import *  # noqa: F401
from .slack_events import *  # noqa: F401
from .slack_messages import *  # noqa: F401


def get_slack_app():
    return slack_app
