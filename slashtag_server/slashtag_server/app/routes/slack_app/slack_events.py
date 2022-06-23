from pydantic import BaseModel

from .slack_app_config import slack_app


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


@slack_app.event("app_home_opened")
async def event_app_home_opened(body, say, logger):
    """User clicked into your App Home"""
    logger.info(body)
    say("event!")


@slack_app.event("app_mention")
async def event_app_mention(body, say, logger):
    """Subscribe to only the message events that mention your app or bot"""
    logger.info(body)
    say("event!")


@slack_app.event("app_rate_limited")
async def event_app_rate_limited(body, say, logger):
    """Indicates your app's event subscriptions are being rate limited"""
    logger.info(body)
    say("event!")


@slack_app.event("app_requested")
async def event_app_requested(body, say, logger):
    """User requested an app"""
    logger.info(body)
    say("event!")


@slack_app.event("app_uninstalled")
async def event_app_uninstalled(body, say, logger):
    """Your Slack app was uninstalled."""
    logger.info(body)
    say("event!")


@slack_app.event("call_rejected")
async def event_call_rejected(body, say, logger):
    """A Call was rejected"""
    logger.info(body)
    say("event!")


@slack_app.event("channel_archive")
async def event_channel_archive(body, say, logger):
    """A channel was archived"""
    logger.info(body)
    say("event!")


@slack_app.event("channel_created")
async def event_channel_created(body, say, logger):
    """A channel was created"""
    logger.info(body)
    say("event!")


@slack_app.event("channel_deleted")
async def event_channel_deleted(body, say, logger):
    """A channel was deleted"""
    logger.info(body)
    say("event!")


@slack_app.event("channel_history_changed")
async def event_channel_history_changed(body, say, logger):
    """Bulk updates were made to a channel's history"""
    logger.info(body)
    say("event!")


@slack_app.event("channel_id_changed")
async def event_channel_id_changed(body, say, logger):
    """A channel ID changed"""
    logger.info(body)
    say("event!")


@slack_app.event("channel_left")
async def event_channel_left(body, say, logger):
    """You left a channel"""
    logger.info(body)
    say("event!")


@slack_app.event("channel_rename")
async def event_channel_rename(body, say, logger):
    """A channel was renamed"""
    logger.info(body)
    say("event!")


@slack_app.event("channel_shared")
async def event_channel_shared(body, say, logger):
    """A channel has been shared with an external workspace"""
    logger.info(body)
    say("event!")


@slack_app.event("channel_unarchive")
async def event_channel_unarchive(body, say, logger):
    """A channel was unarchived"""
    logger.info(body)
    say("event!")


@slack_app.event("channel_unshared")
async def event_channel_unshared(body, say, logger):
    """A channel has been unshared with an external workspace"""
    logger.info(body)
    say("event!")


@slack_app.event("dnd_updated")
async def event_dnd_updated(body, say, logger):
    """Do not Disturb settings changed for the current user"""
    logger.info(body)
    say("event!")


@slack_app.event("dnd_updated_user")
async def event_dnd_updated_user(body, say, logger):
    """Do not Disturb settings changed for a member"""
    logger.info(body)
    say("event!")


@slack_app.event("email_domain_changed")
async def event_email_domain_changed(body, say, logger):
    """The workspace email domain has changed"""
    logger.info(body)
    say("event!")


@slack_app.event("emoji_changed")
async def event_emoji_changed(body, say, logger):
    """A custom emoji has been added or changed"""
    logger.info(body)
    say("event!")


@slack_app.event("file_change")
async def event_file_change(body, say, logger):
    """A file was changed"""
    logger.info(body)
    say("event!")


@slack_app.event("file_comment_added")
async def event_file_comment_added(body, say, logger):
    """A file comment was added"""
    logger.info(body)
    say("event!")


@slack_app.event("file_comment_deleted")
async def event_file_comment_deleted(body, say, logger):
    """A file comment was deleted"""
    logger.info(body)
    say("event!")


@slack_app.event("file_comment_edited")
async def event_file_comment_edited(body, say, logger):
    """A file comment was edited"""
    logger.info(body)
    say("event!")


@slack_app.event("file_created")
async def event_file_created(body, say, logger):
    """A file was created"""
    logger.info(body)
    say("event!")


@slack_app.event("file_deleted")
async def event_file_deleted(body, say, logger):
    """A file was deleted"""
    logger.info(body)
    say("event!")


@slack_app.event("file_public")
async def event_file_public(body, say, logger):
    """A file was made public"""
    logger.info(body)
    say("event!")


@slack_app.event("file_shared")
async def event_file_shared(body, say, logger):
    """A file was shared"""
    logger.info(body)
    say("event!")


@slack_app.event("file_unshared")
async def event_file_unshared(body, say, logger):
    """A file was unshared"""
    logger.info(body)
    say("event!")


@slack_app.event("grid_migration_finished")
async def event_grid_migration_finished(body, say, logger):
    """An enterprise grid migration has finished on this workspace."""
    logger.info(body)
    say("event!")


@slack_app.event("grid_migration_started")
async def event_grid_migration_started(body, say, logger):
    """An enterprise grid migration has started on this workspace."""
    logger.info(body)
    say("event!")


@slack_app.event("group_archive")
async def event_group_archive(body, say, logger):
    """A private channel was archived"""
    logger.info(body)
    say("event!")


@slack_app.event("group_close")
async def event_group_close(body, say, logger):
    """You closed a private channel"""
    logger.info(body)
    say("event!")


@slack_app.event("group_deleted")
async def event_group_deleted(body, say, logger):
    """A private channel was deleted"""
    logger.info(body)
    say("event!")


@slack_app.event("group_history_changed")
async def event_group_history_changed(body, say, logger):
    """Bulk updates were made to a private channel's history"""
    logger.info(body)
    say("event!")


@slack_app.event("group_left")
async def event_group_left(body, say, logger):
    """You left a private channel"""
    logger.info(body)
    say("event!")


@slack_app.event("group_open")
async def event_group_open(body, say, logger):
    """You created a group DM"""
    logger.info(body)
    say("event!")


@slack_app.event("group_rename")
async def event_group_rename(body, say, logger):
    """A private channel was renamed"""
    logger.info(body)
    say("event!")


@slack_app.event("group_unarchive")
async def event_group_unarchive(body, say, logger):
    """A private channel was unarchived"""
    logger.info(body)
    say("event!")


@slack_app.event("im_close")
async def event_im_close(body, say, logger):
    """You closed a DM"""
    logger.info(body)
    say("event!")


@slack_app.event("im_created")
async def event_im_created(body, say, logger):
    """A DM was created"""
    logger.info(body)
    say("event!")


@slack_app.event("im_history_changed")
async def event_im_history_changed(body, say, logger):
    """Bulk updates were made to a DM's history"""
    logger.info(body)
    say("event!")


@slack_app.event("im_open")
async def event_im_open(body, say, logger):
    """You opened a DM"""
    logger.info(body)
    say("event!")


@slack_app.event("invite_requested")
async def event_invite_requested(body, say, logger):
    """User requested an invite"""
    logger.info(body)
    say("event!")


@slack_app.event("link_shared")
async def event_link_shared(body, say, logger):
    """A message was posted containing one or more links relevant to your application"""
    logger.info(body)
    say("event!")


@slack_app.event("member_joined_channel")
async def event_member_joined_channel(body, say, logger):
    """A user joined a public or private channel"""
    logger.info(body)
    say("event!")


@slack_app.event("member_left_channel")
async def event_member_left_channel(body, say, logger):
    """A user left a public or private channel"""
    logger.info(body)
    say("event!")


@slack_app.event("message")
async def event_message(body, say, logger):
    """A message was sent to a channel"""
    logger.info(body)
    say("event!")


@slack_app.event("message_metadata_deleted")
async def event_message_metadata_deleted(body, say, logger):
    """Message metadata was deleted"""
    logger.info(body)
    say("event!")


@slack_app.event("message_metadata_posted")
async def event_message_metadata_posted(body, say, logger):
    """Message metadata was posted"""
    logger.info(body)
    say("event!")


@slack_app.event("message_metadata_updated")
async def event_message_metadata_updated(body, say, logger):
    """Message metadata was updated"""
    logger.info(body)
    say("event!")


# @slack_app.event("message")
async def unsupported_event_message(body, say, logger):
    """app_home	A user sent a message to your Slack app"""
    """channels	A message was posted to a channel"""
    """groups	A message was posted to a private channel"""
    """im	A message was posted in a direct message channel"""
    """mpim	A message was posted in a multiparty direct message channel"""
    logger.info(body)
    say("event!")


@slack_app.event("pin_added")
async def event_pin_added(body, say, logger):
    """A pin was added to a channel"""
    logger.info(body)
    say("event!")


@slack_app.event("pin_removed")
async def event_pin_removed(body, say, logger):
    """A pin was removed from a channel"""
    logger.info(body)
    say("event!")


@slack_app.event("reaction_added")
async def event_reaction_added(body, say, logger):
    """A member has added an emoji reaction to an item"""
    logger.info(body)
    say("event!")


@slack_app.event("reaction_removed")
async def event_reaction_removed(body, say, logger):
    """A member removed an emoji reaction"""
    logger.info(body)
    say("event!")


@slack_app.event("scope_denied")
async def event_scope_denied(body, say, logger):
    """OAuth scopes were denied to your app"""
    logger.info(body)
    say("event!")


@slack_app.event("scope_granted")
async def event_scope_granted(body, say, logger):
    """OAuth scopes were granted to your app"""
    logger.info(body)
    say("event!")


@slack_app.event("shared_channel_invite_accepted")
async def event_shared_channel_invite_accepted(body, say, logger):
    """A shared channel invite was accepted"""
    logger.info(body)
    say("event!")


@slack_app.event("shared_channel_invite_approved")
async def event_shared_channel_invite_approved(body, say, logger):
    """A shared channel invite was approved"""
    logger.info(body)
    say("event!")


@slack_app.event("shared_channel_invite_declined")
async def event_shared_channel_invite_declined(body, say, logger):
    """A shared channel invite was declined"""
    logger.info(body)
    say("event!")


@slack_app.event("shared_channel_invite_received")
async def event_shared_channel_invite_received(body, say, logger):
    """A shared channel invite was sent to a Slack user"""
    logger.info(body)
    say("event!")


@slack_app.event("star_added")
async def event_star_added(body, say, logger):
    """A member has starred an item"""
    logger.info(body)
    say("event!")


@slack_app.event("star_removed")
async def event_star_removed(body, say, logger):
    """A member removed a star"""
    logger.info(body)
    say("event!")


@slack_app.event("subteam_created")
async def event_subteam_created(body, say, logger):
    """A User Group has been added to the workspace"""
    logger.info(body)
    say("event!")


@slack_app.event("subteam_members_changed")
async def event_subteam_members_changed(body, say, logger):
    """The membership of an existing User Group has changed"""
    logger.info(body)
    say("event!")


@slack_app.event("subteam_self_added")
async def event_subteam_self_added(body, say, logger):
    """You have been added to a User Group"""
    logger.info(body)
    say("event!")


@slack_app.event("subteam_self_removed")
async def event_subteam_self_removed(body, say, logger):
    """You have been removed from a User Group"""
    logger.info(body)
    say("event!")


@slack_app.event("subteam_updated")
async def event_subteam_updated(body, say, logger):
    """An existing User Group has been updated or its members changed"""
    logger.info(body)
    say("event!")


@slack_app.event("team_access_granted")
async def event_team_access_granted(body, say, logger):
    """Access to a set of teams was granted to your org app"""
    logger.info(body)
    say("event!")


@slack_app.event("team_access_revoked")
async def event_team_access_revoked(body, say, logger):
    """Access to a set of teams was revoked from your org app"""
    logger.info(body)
    say("event!")


@slack_app.event("team_domain_change")
async def event_team_domain_change(body, say, logger):
    """The workspace domain has changed"""
    logger.info(body)
    say("event!")


@slack_app.event("team_join")
async def event_team_join(body, say, logger):
    """A new member has joined"""
    logger.info(body)
    say("event!")


@slack_app.event("team_rename")
async def event_team_rename(body, say, logger):
    """The workspace name has changed"""
    logger.info(body)
    say("event!")


@slack_app.event("tokens_revoked")
async def event_tokens_revoked(body, say, logger):
    """API tokens for your app were revoked."""
    logger.info(body)
    say("event!")


@slack_app.event("url_verification")
async def event_url_verification(body, say, logger):
    """Verifies ownership of an Events API Request URL"""
    logger.info(body)
    say("event!")


@slack_app.event("user_change")
async def event_user_change(body, say, logger):
    """A member's data has changed"""
    logger.info(body)
    say("event!")


@slack_app.event("user_huddle_changed")
async def event_user_huddle_changed(body, say, logger):
    """A user's huddle status has changed"""
    logger.info(body)
    say("event!")


@slack_app.event("user_profile_changed")
async def event_user_profile_changed(body, say, logger):
    """A user's profile data has changed"""
    logger.info(body)
    say("event!")


@slack_app.event("user_resource_denied")
async def event_user_resource_denied(body, say, logger):
    """User resource was denied to your app"""
    logger.info(body)
    say("event!")


@slack_app.event("user_resource_granted")
async def event_user_resource_granted(body, say, logger):
    """User resource was granted to your app"""
    logger.info(body)
    say("event!")


@slack_app.event("user_resource_removed")
async def event_user_resource_removed(body, say, logger):
    """User resource was removed from your app"""
    logger.info(body)
    say("event!")


@slack_app.event("user_status_changed")
async def event_user_status_changed(body, say, logger):
    """A user's status has changed"""
    logger.info(body)
    say("event!")


@slack_app.event("workflow_deleted")
async def event_workflow_deleted(body, say, logger):
    """A workflow that contains a step supported by your app was deleted"""
    logger.info(body)
    say("event!")


@slack_app.event("workflow_published")
async def event_workflow_published(body, say, logger):
    """A workflow that contains a step supported by your app was published"""
    logger.info(body)
    say("event!")


@slack_app.event("workflow_step_deleted")
async def event_workflow_step_deleted(body, say, logger):
    """A workflow step supported by your app was removed from a workflow"""
    logger.info(body)
    say("event!")


@slack_app.event("workflow_step_execute")
async def event_workflow_step_execute(body, say, logger):
    """A workflow step supported by your app should execute"""
    logger.info(body)
    say("event!")


@slack_app.event("workflow_unpublished")
async def event_workflow_unpublished(body, say, logger):
    """A workflow that contains a step supported by your app was unpublished"""
    logger.info(body)
    say("event!")
