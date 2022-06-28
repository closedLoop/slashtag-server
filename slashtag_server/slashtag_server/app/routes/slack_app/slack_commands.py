import logging

from slack import AsyncWebClient
from slack_bolt.context.say.async_say import AsyncSay

from .helpers import download_file
from .slack_app_config import slack_app
from .slack_models import SlackCommandPayload, SlackFileObject

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


@slack_app.command("/echo")
async def repeat_text(ack, say, command):
    # Acknowledge command request
    await ack()
    await say(f"{command['text']}")


@slack_app.command("/tag")
async def tag_command(ack, say: AsyncSay, command):
    await ack()
    logger.info(f"command: {SlackCommandPayload(**command)}")
    client: AsyncWebClient = say.client
    response = await client.files_info(file="F03MTTV5U0H")
    f = SlackFileObject(**response["file"])
    file_name = download_file(
        f.url_private_download, temp_dir=None, token=say.client.token, prefix=f.user
    )
    print(f"file saved to: {file_name}")

    await say(f"SlashTag :partying_face: {command['text']}\nfile saved to: {file_name}")
