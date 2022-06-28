import logging

from slashtag_server.app.routes.slack_app.slack_models import SlackCommandPayload

from .slack_app_config import slack_app

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


@slack_app.command("/echo")
async def repeat_text(ack, say, command):
    # Acknowledge command request
    await ack()
    await say(f"{command['text']}")


@slack_app.command("/tag")
async def tag_command(ack, say, command):
    await ack()
    logger.info("command:", SlackCommandPayload(**command))
    await say(f"SlashTag :partying_face: {command['text']}")
