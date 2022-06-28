from typing import List, Optional

from pydantic import BaseModel


class EventDetails(BaseModel):
    type: str


class UninstallEvent(BaseModel):
    token = str
    team_id = str
    api_app_id = str
    event = EventDetails
    type = str
    event_id = str
    event_time = int


class SlackAuthorizationAttributes(BaseModel):
    enterprise_id: Optional[str]  # ': None,
    team_id: str  # ': 'T03LKLSMYB0',
    user_id: str  # ': 'U03MLR4MUCQ',
    is_bot: bool  # ': True,
    is_enterprise_install: bool  # ': False


class SlackEventFileDetails(BaseModel):
    id: str


class SlackEventFileAttributes(BaseModel):
    file_id: str
    user_id: str
    file: SlackEventFileDetails
    type: str
    event_ts: str


class PublicFileEvent(BaseModel):
    token: str  # ': 'XzOzCl2CGCootaANVERwJCnr',
    team_id: str  # ': 'T03LKLSMYB0',
    api_app_id: str  # ': 'A03LKMA65UN',
    event: SlackEventFileAttributes
    type: str  # ': 'event_callback',
    event_id: str  # ': 'Ev03M0LH5TEK',
    event_time: str  # ': 1656411416,
    authorizations: List[SlackAuthorizationAttributes]
    is_ext_shared_channel: bool  # ': False,
    event_context: str  # ': '4-eyJldCI6ImZpbGVfcHVibGljIiwidGlkIjoiVDAzTEtMU01ZQjAiLCJhaWQiOiJBMDNMS01BNjVVTiIsImZpZCI6IkYwM01UVFY1VTBIIn0'


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
