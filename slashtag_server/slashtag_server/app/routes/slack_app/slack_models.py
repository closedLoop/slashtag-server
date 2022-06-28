from typing import Any, Dict, List, Optional

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


class SlackShares(BaseModel):
    reply_users: List[str]
    reply_users_count: int  # ": 1,
    reply_count: int  # ": 1,
    ts: str  # ": "1531763348.000001",
    thread_ts: Optional[str]  # ": "1531763273.000015",
    latest_reply: Optional[str]  # ": "1531763348.000001",
    channel_name: str  # ": "file-under",
    team_id: str  # ": "T061EG9R6"


class SlackSharesObject(BaseModel):
    public: Dict[str, List[SlackShares]]


class SlackFileObject(BaseModel):
    id: str  # "F0S43PZDF",
    created: int  # 1531763342,
    timestamp: int  # 1531763342,
    name: str  # "tedair.gif",
    title: str  # "tedair.gif",
    mimetype: str  # "image/gif",
    filetype: str  # "gif",
    pretty_type: str  # "GIF",
    user: str  # "U061F7AUR",
    editable: bool  # false,
    size: int  # 137531,
    mode: str  # "hosted",
    is_external: bool  # false,
    external_type: str  # "",
    is_public: bool  # true,
    public_url_shared: bool  # false,
    display_as_bot: bool  # false,
    username: str  # "",
    url_private: str  # "https://.../tedair.gif",
    url_private_download: str  # "https://.../tedair.gif",
    thumb_64: Optional[str]  # "https://.../tedair_64.png",
    thumb_80: Optional[str]  # "https://.../tedair_80.png",
    thumb_360: Optional[str]  # "https://.../tedair_360.png",
    thumb_360_w: Optional[str]  # 176,
    thumb_360_h: Optional[str]  # 226,
    thumb_160: Optional[str]  # "https://.../tedair_=_160.png",
    thumb_360_gif: Optional[str]  # "https://.../tedair_360.gif",
    image_exif_rotation: Optional[str]  # 1,
    original_w: Optional[str]  # 176,
    original_h: Optional[str]  # 226,
    deanimate_gif: Optional[str]  # ": "https://.../tedair_deanimate_gif.png",
    pjpeg: Optional[str]  # ": "https://.../tedair_pjpeg.jpg",
    permalink: str  # ": "https://.../tedair.gif",
    permalink_public: str  # ": "https://.../...",
    comments_count: int
    is_starred: bool
    shares: SlackSharesObject
    channels: List[str]
    groups: List[Any]
    ims: List[Any]
    has_rich_preview: bool
