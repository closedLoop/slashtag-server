from typing import Optional

from fastapi import Request
from fastapi.routing import APIRouter
from pydantic import BaseModel
from slack_bolt.adapter.fastapi.async_handler import AsyncSlackRequestHandler

from .slack_app import get_slack_app

# https://api.slack.com/apis/connections/events-api


class ActionEndpoint(BaseModel):
    token: Optional[str]
    challenge: Optional[str]
    type: Optional[str]


app_handler = AsyncSlackRequestHandler(get_slack_app())


router = APIRouter()


# BOLT
@router.post("/events")
async def endpoint(req: Request):
    return await app_handler.handle(req)


@router.post("/tag")
async def commands(req: Request):
    return await app_handler.handle(req)


@router.get("/install")
async def install(req: Request):
    return await app_handler.handle(req)


@router.get("/oauth_redirect")
async def oauth_redirect(req: Request):
    return await app_handler.handle(req)


# Potentially deprecated if using above
# Move into app
@router.get("/interactive-endpoint")
def interactive_endpoint():
    return {"message": "Hello World"}


# @router.post("/command")
# async def slash_command(req: Request):
#     body = await app_handler.handle(req)


# @router.post("/command")
# async def slash_command(req: Request):
#     payload = await app_handler.handle(req)


@router.post("/action-endpoint")
async def action_endpoint(req: Request):
    message = ActionEndpoint(**await req.json())
    print(message)
    if message.type == "url_verification":
        return message.challenge
    return await app_handler.handle(req)


# For interactions with select menus where type is set to external_select,
# Slack will send an HTTP POST request with information to load options from
# this URL upon user invocation.
@router.post("/options-load-endpoint")
def load_options_endpoint():
    return {"message": "load_options_endpoint"}
