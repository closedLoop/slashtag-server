import os
from typing import Optional

from fastapi import Request
from fastapi.routing import APIRouter
from pydantic import BaseModel
from slack_bolt.adapter.fastapi.async_handler import AsyncSlackRequestHandler
from slack_bolt.async_app import AsyncApp
from slack_bolt.oauth.async_oauth_settings import AsyncOAuthSettings
from slack_sdk.oauth.installation_store import FileInstallationStore
from slack_sdk.oauth.state_store import FileOAuthStateStore


class ActionEndpoint(BaseModel):
    token: Optional[str]
    challenge: Optional[str]
    type: Optional[str]


# TODO move this to non-file-store
# TODO confirm this is the proper way to do this
# https://slack.dev/bolt-python/concepts#authenticating-oauth
oauth_settings = AsyncOAuthSettings(
    client_id=os.environ["SLACK_CLIENT_ID"],
    client_secret=os.environ["SLACK_CLIENT_SECRET"],
    scopes=os.environ["SLACK_SCOPES"].split(","),
    installation_store=FileInstallationStore(base_dir="./data/installations"),
    state_store=FileOAuthStateStore(expiration_seconds=600, base_dir="./data/states"),
)

slack_app = AsyncApp(
    signing_secret=os.environ["SLACK_SIGNING_SECRET"], oauth_settings=oauth_settings
)
app_handler = AsyncSlackRequestHandler(slack_app)


@slack_app.event("app_mention")
async def handle_app_mentions(body, say, logger):
    logger.info(body)
    await say("What's up?")


@slack_app.event("message")
async def handle_message():
    pass


router = APIRouter()


# BOLT
@router.post("/events")
async def endpoint(req: Request):
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


@router.post("/command")
def slash_command(req: Request):
    print("req", req)
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
