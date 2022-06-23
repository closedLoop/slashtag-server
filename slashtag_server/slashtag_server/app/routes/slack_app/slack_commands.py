from pydantic import BaseModel

from .slack_app_config import slack_app


class SlackCommandPayload(BaseModel):
    token: str  # "XzOzCl2CGCootaANVERwJCnr",
    team_id: str  # "T03LKLSMYB0",
    team_domain: str  # "slashtagworkspace",
    channel_id: str  # "C03LS95UYLA",
    channel_name: str  # "general",
    user_id: str  # "U03MG21NGUQ",
    user_name: str  # "sean",
    command: str  # "/tag",
    text: str  # "asdf <@U03MG21NGUQ|sean> <#C03LS7P8EFM|research>",
    api_app_id: str  # "A03LKMA65UN",
    is_enterprise_install: bool  # "false",
    response_url: str  # "https://hooks.slack.com/commands/T03LKLSMYB0/3712579649939/nQJq1jWcGowaagH4zuntKJY0",
    trigger_id: str  # "3712634787666.3699706746374.1a8c51ac046b8227be1b46801053cebf",


@slack_app.command("/echo")
async def repeat_text(ack, say, command):
    # Acknowledge command request
    await ack()
    await say(f"{command['text']}")


@slack_app.command("/tag")
async def tag_command(ack, say, command):
    await ack()
    print("command:", SlackCommandPayload(**command))
    await say(f"SlashTag :partying_face: {command['text']}")
