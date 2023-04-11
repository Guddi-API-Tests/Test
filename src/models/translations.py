# generated by datamodel-codegen:
#   filename:  de_DE.json
#   timestamp: 2023-04-11T18:18:39+00:00

from __future__ import annotations

from typing import List

from models.model_base import BaseModel


class ReplyEmbed(BaseModel):
    title: str
    description: str


class Misc(BaseModel):
    test: str
    thing: str
    this: str


class Help(BaseModel):
    name: str
    description: str
    replyEmbed: ReplyEmbed
    misc: Misc


class Field(BaseModel):
    name: str
    value: str
    inline: bool


class ReplyEmbed1(BaseModel):
    title: str
    description: str
    fields: List[Field]


class Info(BaseModel):
    name: str
    description: str
    replyEmbed: ReplyEmbed1


class ReplyEmbed2(BaseModel):
    title: str
    description: str


class Invite(BaseModel):
    name: str
    description: str
    replyEmbed: ReplyEmbed2


class Banner(BaseModel):
    name: str
    description: str


class Misc1(BaseModel):
    activated: str
    deactivated: str
    guild_banner: str
    not_set: str
    custom_background: str
    old_image: str
    without_text: str
    roles: str
    channels: str
    blacklist: str


class BannerSettings(BaseModel):
    name: str
    description: str
    replyNoGuildData: str
    replyEmbed: ReplyEmbed2
    misc: Misc1


class Display(BaseModel):
    name: str
    description: str
    option_1: str
    option_2: str


class Args(BaseModel):
    display: Display


class BannerActivate(BaseModel):
    name: str
    description: str
    args: Args
    replyAlreadyActivated: str
    replySuccess: str
    replyTextChannel: str
    replyNoBanner: str


class Delete(BaseModel):
    name: str
    description: str


class Args1(BaseModel):
    delete: Delete


class BannerDeactivate(BaseModel):
    name: str
    description: str
    args: Args1
    replyAlreadyDeactivated: str
    replySuccess: str
    replySuccessDelete: str


class Role(BaseModel):
    name: str
    description: str


class Remove(BaseModel):
    name: str
    description: str


class Args2(BaseModel):
    role: Role
    remove: Remove


class BannerRole(BaseModel):
    name: str
    description: str
    args: Args2
    errorToManyArgs: str
    errorRoleAlreadySet: str
    errorCantManageRole: str
    errorUnexpected: str
    replySet: str
    replyRemoved: str


class TimeRange(BaseModel):
    name: str
    description: str


class Args3(BaseModel):
    time_range: TimeRange


class BannerTimerange(BaseModel):
    name: str
    description: str
    args: Args3
    replyIsAlreadySet: str
    replySuccess: str


class BannerColors(BaseModel):
    name: str
    description: str


class Title(BaseModel):
    name: str
    description: str


class Username(BaseModel):
    name: str
    description: str


class Discriminator(BaseModel):
    name: str
    description: str


class Args4(BaseModel):
    title: Title
    username: Username
    discriminator: Discriminator


class BannerColorsCustomize(BaseModel):
    name: str
    description: str
    args: Args4
    replyNoOption: str
    replyChange: str
    replyChanges: str


class BannerColorsReset(BaseModel):
    name: str
    description: str
    reply: str


class BannerFonts(BaseModel):
    name: str
    description: str


class FontFile(BaseModel):
    name: str
    description: str


class Args5(BaseModel):
    font_file: FontFile


class BannerFontsUpload(BaseModel):
    name: str
    description: str
    args: Args5
    errorWrongFileFormat: str
    replySuccess: str


class BannerFontsReset(BaseModel):
    name: str
    description: str
    replyNoFontUploaded: str
    replySuccess: str


class BannerBackground(BaseModel):
    name: str
    description: str


class Image(BaseModel):
    name: str
    description: str


class Args6(BaseModel):
    image: Image


class BannerBackgroundSelection(BaseModel):
    name: str
    description: str
    args: Args6
    replyRemovedUploadedImage: str


class Args7(BaseModel):
    image: Image


class BannerBackgroundUpload(BaseModel):
    name: str
    description: str
    args: Args7
    errorWrongFileFormat: str
    errorInvalidAspectRatio: str
    errorImageSizeToSmall: str
    replySuccess: str
    replyQuestion: str


class BannerBlacklist(BaseModel):
    name: str
    description: str


class Channel(BaseModel):
    name: str
    description: str


class Args8(BaseModel):
    role: Role
    channel: Channel


class BannerBlacklistAdd(BaseModel):
    name: str
    description: str
    args: Args8
    errorNoOptions: str
    errorAlreadyBlacklisted: str
    replySuccess: str


class Clear(BaseModel):
    name: str
    description: str


class Args9(BaseModel):
    role: Role
    channel: Channel
    clear: Clear


class BannerBlacklistRemove(BaseModel):
    name: str
    description: str
    args: Args9
    errorNoOptions: str
    errorAllOptions: str
    errorAlreadyBlacklisted: str
    replyClear: str
    replySuccess: str


class Tempchannel(BaseModel):
    name: str
    description: str


class Misc2(BaseModel):
    activated: str
    deactivated: str
    no_hubs: str
    no_temps: str
    set_hubs: str
    current_temps: str


class TempchannelSettings(BaseModel):
    name: str
    description: str
    replyEmbed: ReplyEmbed2
    misc: Misc2
    errorNoAdminPerms: str


class Args10(BaseModel):
    channel: Channel


class TempchannelAdd(BaseModel):
    name: str
    description: str
    args: Args10
    reply: str
    errorIsHub: str
    errorIsTemp: str
    errorNoAdminPerms: str


class Args11(BaseModel):
    channel: Channel
    delete: Delete


class TempchannelRemove(BaseModel):
    name: str
    description: str
    args: Args11
    reply: str
    replyDeleted: str
    errorNotTemp: str
    errorNoOption: str


class TempchannelOptions(BaseModel):
    name: str
    description: str


class Name(BaseModel):
    name: str
    description: str


class Args12(BaseModel):
    channel: Channel
    name: Name


class TempchannelOptionsName(BaseModel):
    name: str
    description: str
    args: Args12
    reply: str
    errorNoHubsSet: str
    errorNameToLong: str
    errorUnknownOption: str


class Commands(BaseModel):
    help: Help
    info: Info
    invite: Invite
    banner: Banner
    banner_settings: BannerSettings
    banner_activate: BannerActivate
    banner_deactivate: BannerDeactivate
    banner_role: BannerRole
    banner_timerange: BannerTimerange
    banner_colors: BannerColors
    banner_colors_customize: BannerColorsCustomize
    banner_colors_reset: BannerColorsReset
    banner_fonts: BannerFonts
    banner_fonts_upload: BannerFontsUpload
    banner_fonts_reset: BannerFontsReset
    banner_background: BannerBackground
    banner_background_selection: BannerBackgroundSelection
    banner_background_upload: BannerBackgroundUpload
    banner_blacklist: BannerBlacklist
    banner_blacklist_add: BannerBlacklistAdd
    banner_blacklist_remove: BannerBlacklistRemove
    tempchannel: Tempchannel
    tempchannel_settings: TempchannelSettings
    tempchannel_add: TempchannelAdd
    tempchannel_remove: TempchannelRemove
    tempchannel_options: TempchannelOptions
    tempchannel_options_name: TempchannelOptionsName


class Misc3(BaseModel):
    message: str
    messages: str


class ActivityCheckMember(BaseModel):
    name: str
    replyAuthorCount: str
    replyMemberCount: str
    replyAuthorLeads: str
    replyMemberLeads: str
    replyDraw: str
    reply: str
    errorNoBots: str
    misc: Misc3


class ContextMenus(BaseModel):
    activity_check_member: ActivityCheckMember


class Banner1(BaseModel):
    title: str
    title_hourly: str
    title_daily: str


class ReplyEmbedError(BaseModel):
    title: str
    description: str


class Tempchannel1(BaseModel):
    channelEmpty: str
    replyEmbedError: ReplyEmbedError


class Functions(BaseModel):
    banner: Banner1
    tempchannel: Tempchannel1


class Choices(BaseModel):
    banner_activate_display_text: str
    banner_activate_display_banner: str


class TranslationsModel(BaseModel):
    langCode: str
    langName: str
    commands: Commands
    context_menus: ContextMenus
    functions: Functions
    choices: Choices
