from typing import Dict, List, Optional

from pydantic import BaseModel


class LoggingChannel(BaseModel):
    exclude_channels: Optional[List[int]] = None
    include_channels: Optional[List[int]] = None
    exclude: Optional[List[str]] = None
    include: Optional[List[str]] = None


class LoggingFormats(BaseModel):
    timestamp: str = "%Y-%m-%d %H:%M:%S"
    INFRACTION_NOTE: str = "`[#(infraction_id)]` Infraction of type #(infraction_type) was created for user #(infraction_member) by moderator #(infraction_mod): #(infraction_reason)"
    INFRACTION_WARN: str = "`[#(infraction_id)]` Infraction of type #(infraction_type) was created for user #(infraction_member) by moderator #(infraction_mod): #(infraction_reason)"
    INFRACTION_MUTE: str = "`[#(infraction_id)]` Infraction of type #(infraction_type) was created for user #(infraction_member) by moderator #(infraction_mod): #(infraction_reason)"
    INFRACTION_KICK: str = "`[#(infraction_id)]` Infraction of type #(infraction_type) was created for user #(infraction_member) by moderator #(infraction_mod): #(infraction_reason)"
    INFRACTION_BAN: str = "`[#(infraction_id)]` Infraction of type #(infraction_type) was created for user #(infraction_member) by moderator #(infraction_mod): #(infraction_reason)"
    INFRACTION_MISC: str = "`[#(infraction_id)]` Infraction of type #(infraction_type) was created for user #(infraction_member) by moderator #(infraction_mod): #(infraction_reason)"
    INFRACTION_MUTE_REMOVE: str = (
        "`[#(infraction_id)]` Mute has been removed for user #(infraction_member)"
    )
    INFRACTION_BAN_REMOVE: str = (
        "`[#(infraction_id)]` Ban has been removed for user #(infraction_member)"
    )
    INFRACTION_CREATED: str = "`[#(infraction_id)]` Infraction of type #(infraction_type) was created for user #(infraction_member) by moderator #(infraction_mod): #(infraction_reason)"
    INFRACTION_DELETED: str = "`[#(infraction_id)]` Infraction of type #(infraction_type) was updated for user #(infraction_member): #(infraction_reason)"
    INFRACTION_UPDATED: str = "`[#(infraction_id)]` Infraction was deleted by #(member)"
    MEMBER_JOIN: str = ":inbox_tray: #(member_mention) (**#(member_name)##(member_disc)**, `#(member_id)`) joined (created #(member_created_at))"
    MEMBER_LEAVE: str = ":outbox_tray: #(member_mention) (**#(member_name)##(member_disc)**, `#(member_id)`) left"
    MEMBER_ROLES_ADD: str = (
        ":key: #(member_name)##(member_dics) (`#(member_id)`) gained roles: #(roles)"
    )
    MEMBER_ROLES_REMOVE: str = (
        ":key: #(member_name)##(member_dics) (`#(member_id)`) lost roles: #(roles)"
    )
    MEMBER_ROLES_DIFF: str = ":key: #(member_name)##(member_dics) (`#(member_id)`) gained roles: #(roles_gained), lost roles: #(roles_lost)"
    MEMBER_NICK_UPDATE: str = ":arrows_counterclockwise: Member nickname updated, before: `#(nick_before)`, after: `#(nick_after)`, id: `#(member_id)"
    MEMBER_NAME_UPDATE: str = ":arrows_counterclockwise: Member name updated, before: `#(name_before)`, after: `#(name_after)`, id: `#(member_id)"
    MEMBER_VOICE_JOIN: str = ":arrow_up: Member #(member_name)##(member_disc) (`#(member_id)`) joined voice channel #(voice_channel_mention) (`#(voice_channel_id)`)"
    MEMBER_VOICE_MOVE: str = ":arrows_counterclockwise: Member #(member_name)##(member_disc) (`#(member_id)`) moved from voice channel #(before_mention) (`#(before_id)`) to voice channel #(after_mention) (`#(after_id)`)"
    MEMBER_VOICE_LEAVE: str = ":arrow_down: Member #(member_name)##(member_disc) (`#(member_id)`) left voice channel #(voice_channel_mention) (`#(voice_channel_id)`)"
    CHANNEL_CREATE: str = ":arrow_up: Channel #(channel_name) #(channel_mention) (`#(channel_id)`) was created"
    CHANNEL_UPDATE: str = ":arrows_counterclockwise: Channel #(channel_name) #(channel_mention) (`#(channel_id)`) was updated: #(details)"
    CHANNEL_DELETE: str = (
        ":arrow_down: Channel #(channel_name) (`#(channel_id)`) was deleted"
    )
    THREAD_CREATE: str = ":arrow_up: Thread #(thread_name) #(thread_mention) (`#(thread_id)`) was created under parent #(thread_parent_name) (`#(thread_parent_id)`)"
    THREAD_UPDATE: str = ":arrows_counterclockwise: Thread #(thread_name) #(thread_mention) (`#(thread_id)`) was updated: #(details)"
    THREAD_DELETE: str = (
        ":arrow_down: Thread #(thread_name) (`#(thread_id)`) was deleted"
    )
    ROLE_CREATE: str = ":arrow_up: Role #(role_name) (`#(role_id)`) was created"
    ROLE_UPDATE: str = ":arrows_counterclockwise: Role #(role_name) (`#(role_id)`) was updated: #(details)"
    ROLE_DELETE: str = ":arrow_down: Role #(role_name) (`#(role_id)`) was deleted"
    MESSAGE_EDIT: str = ":arrows_counterclockwise: Message #(before_id) in #(before_channel_id) from #(before_author_name)##(before_author_disc) (`#(before_author_id)`) was edited, before:```#(before_content)\n```after:```#(after_content)\n```"
    MESSAGE_DELETE: str = ":arrow_down: Message #(message_id) in #(message_channel_id) from #(message_author_name)##(message_author_disc) (`#(message_author_id)`) was deleted, content:```#(message_content)\n```"
    MESSAGE_DELETE_BULK: str = ""
    MESSAGE_DELETE_AUTO: str = ""
    EMOJI_CREATE: str = "Emoji was created (id: `#(emoji_id)`, name: `#(emoji_name)`)"
    EMOJI_UPDATE: str = "Emoji was created (id: `#(emoji_id)`, name: `#(emoji_name)`)"
    EMOJI_DELETE: str = "Emoji was created (id: `#(emoji_id)`, name: `#(emoji_name)`), before: `#(before_name)`, after: `#(after_name)`"
    STICKER_CREATE: str = (
        "Sticker was created (id: `#(sticker_id)`, name: `#(sticker_name)`)"
    )
    STICKER_DELETE: str = (
        "Sticker was created (id: `#(sticker_id)`, name: `#(sticker_name)`)"
    )
    STICKER_UPDATE: str = "Sticker was created (id: `#(sticker_id)`, name: `#(sticker_name)`), before: `#(before_name)`, after: `#(after_name)`"


class LoggingModel(BaseModel):
    guild_id: int
    channels: Dict[int, LoggingChannel] = {}
    formats: LoggingFormats = LoggingFormats()
