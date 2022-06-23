# Create fastapi routes

from typing import Optional

from fastapi.routing import APIRouter
from pydantic import BaseModel


class ActionEndpoint(BaseModel):
    token: Optional[str]
    challenge: Optional[str]
    type: Optional[str]


router = APIRouter()


# Move into app
@router.get("/interactive-endpoint")
def interactive_endpoint():
    return {"message": "Hello World"}


@router.get("/command")
def slash_command():
    return {"message": "SlashCommand"}


@router.get("/redirect")
def auth_redirect():
    return {"message": "auth_redirect"}


@router.post("/action-endpoint")
def action_endpoint(message: ActionEndpoint):
    print(message)
    return message.challenge if message.type == "url_verification" else message


# For interactions with select menus where type is set to external_select,
# Slack will send an HTTP POST request with information to load options from
# this URL upon user invocation.
@router.post("/options-load-endpoint")
def load_options_endpoint():
    return {"message": "load_options_endpoint"}
