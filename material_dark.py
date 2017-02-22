#!/usr/bin/env python3

"""
Material Dark theme generator.
"""

from utils import print_theme, SOLID_ALPHA
from utils.material import *

ACCENT_COLOR = BLUE_A200
ACTIVE_ICON_COLOR = LIGHT_ICON_COLOR | LIGHT_ICON_ACTIVE_ALPHA
APP_BAR_COLOR = DARK_APP_BAR_COLOR | SOLID_ALPHA
BACKGROUND_COLOR = DARK_BACKGROUND_COLOR | SOLID_ALPHA
DIVIDER_COLOR = LIGHT_TEXT_COLOR | LIGHT_TEXT_DIVIDER_ALPHA
HINT_COLOR = LIGHT_TEXT_COLOR | LIGHT_TEXT_HINT_ALPHA
LIGHT_ACCENT_COLOR = BLUE_A100
LIGHT_SELECTED_COLOR = LIGHT_TEXT_COLOR | RIPPLE_ALPHA
PRIMARY_TEXT_COLOR = LIGHT_TEXT_COLOR | LIGHT_TEXT_PRIMARY_ALPHA
SECONDARY_TEXT_COLOR = LIGHT_TEXT_COLOR | LIGHT_TEXT_SECONDARY_ALPHA
SOLID_ACCENT_COLOR = ACCENT_COLOR | SOLID_ALPHA
SOLID_LIGHT_ACCENT_COLOR = LIGHT_ACCENT_COLOR | SOLID_ALPHA

THEME = [
    ("actionBarActionModeDefault", APP_BAR_COLOR),
    ("actionBarActionModeDefaultIcon", ACTIVE_ICON_COLOR),
    ("actionBarActionModeDefaultTop", DARK_STATUS_BAR_COLOR | SOLID_ALPHA),
    ("actionBarDefault", APP_BAR_COLOR),
    ("actionBarDefaultIcon", ACTIVE_ICON_COLOR),
    ("actionBarDefaultSearch", PRIMARY_TEXT_COLOR),
    ("actionBarDefaultSearchPlaceholder", HINT_COLOR),
    ("actionBarDefaultSelector", LIGHT_SELECTED_COLOR),
    ("actionBarDefaultSubtitle", SECONDARY_TEXT_COLOR),
    ("actionBarDefaultTitle", PRIMARY_TEXT_COLOR),
    ("avatar_actionBarIconBlue", ACTIVE_ICON_COLOR),
    ("avatar_backgroundActionBarBlue", APP_BAR_COLOR),
    ("avatar_backgroundBlue", BLUE_500 | SOLID_ALPHA),
    ("avatar_backgroundCyan", CYAN_700 | SOLID_ALPHA),
    ("avatar_backgroundGreen", GREEN_500 | SOLID_ALPHA),
    ("avatar_backgroundOrange", ORANGE_800 | SOLID_ALPHA),
    ("avatar_backgroundPink", PINK_500 | SOLID_ALPHA),
    ("avatar_backgroundRed", RED_500 | SOLID_ALPHA),
    ("avatar_backgroundViolet", PURPLE_500 | SOLID_ALPHA),
    ("avatar_nameInMessageBlue", BLUE_400 | SOLID_ALPHA),
    ("avatar_nameInMessageCyan", CYAN_500| SOLID_ALPHA),
    ("avatar_nameInMessageGreen", GREEN_500 | SOLID_ALPHA),
    ("avatar_nameInMessageOrange", ORANGE_500 | SOLID_ALPHA),
    ("avatar_nameInMessagePink", PINK_200 | SOLID_ALPHA),
    ("avatar_nameInMessageRed", RED_300 | SOLID_ALPHA),
    ("avatar_nameInMessageViolet", PURPLE_200 | SOLID_ALPHA),
    ("avatar_subtitleInProfileBlue", SECONDARY_TEXT_COLOR),
    ("avatar_text", PRIMARY_TEXT_COLOR),
    ("avatar_text", PRIMARY_TEXT_COLOR),
    ("chat_inBubble", DARK_CARD_COLOR | SOLID_ALPHA),
    ("chat_inBubbleSelected", LIGHT_SELECTED_COLOR),
    ("chat_inBubbleShadow", BACKGROUND_COLOR),
    ("chat_inInstant", ACTIVE_ICON_COLOR),
    ("chat_inPreviewInstantText", SOLID_LIGHT_ACCENT_COLOR),
    ("chat_inTimeText", SECONDARY_TEXT_COLOR),
    ("chat_messageLinkIn", SOLID_LIGHT_ACCENT_COLOR),
    ("chat_messageLinkOut", SOLID_LIGHT_ACCENT_COLOR),
    ("chat_messagePanelBackground", DARK_CARD_COLOR | SOLID_ALPHA),
    ("chat_messagePanelHint", HINT_COLOR),
    ("chat_messagePanelIcons", ACTIVE_ICON_COLOR),
    ("chat_messagePanelShadow", BACKGROUND_COLOR),
    ("chat_messagePanelText", PRIMARY_TEXT_COLOR),
    ("chat_messageTextIn", PRIMARY_TEXT_COLOR),
    ("chat_messageTextOut", PRIMARY_TEXT_COLOR),
    ("chat_muteIcon", ACTIVE_ICON_COLOR),
    ("chat_outBubble", GREY_700 | SOLID_ALPHA),
    ("chat_outBubbleSelected", LIGHT_SELECTED_COLOR),
    ("chat_outBubbleShadow", BACKGROUND_COLOR),
    ("chat_outTimeText", SECONDARY_TEXT_COLOR),
    ("chat_selectedBackground", LIGHT_SELECTED_COLOR),
    ("chat_wallpaper", BACKGROUND_COLOR),
    ("chats_actionBackground", SOLID_ACCENT_COLOR),
    ("chats_actionIcon", ACTIVE_ICON_COLOR),
    ("chats_actionMessage", SOLID_LIGHT_ACCENT_COLOR),
    ("chats_actionPressedBackground", LIGHT_SELECTED_COLOR),
    ("chats_date", SECONDARY_TEXT_COLOR),
    ("chats_menuBackground", BACKGROUND_COLOR),
    ("chats_menuCloud", ACTIVE_ICON_COLOR),
    ("chats_menuItemIcon", ACTIVE_ICON_COLOR),
    ("chats_menuItemText", PRIMARY_TEXT_COLOR),
    ("chats_menuName", PRIMARY_TEXT_COLOR),
    ("chats_menuPhone", SECONDARY_TEXT_COLOR),
    ("chats_message", SECONDARY_TEXT_COLOR),
    ("chats_muteIcon", ACTIVE_ICON_COLOR),
    ("chats_name", PRIMARY_TEXT_COLOR),
    ("chats_nameIcon", ACTIVE_ICON_COLOR),
    ("chats_nameMessage", SOLID_LIGHT_ACCENT_COLOR),
    ("chats_pinnedIcon", ACTIVE_ICON_COLOR),
    ("chats_pinnedOverlay", LIGHT_TEXT_COLOR | LIGHT_TEXT_DIVIDER_ALPHA),
    ("chats_sendClock", GREEN_500 | SOLID_ALPHA),
    ("chats_sentCheck", GREEN_500 | SOLID_ALPHA),
    ("chats_unreadCounter", SOLID_ACCENT_COLOR),
    ("chats_unreadCounterMuted", LIGHT_TEXT_COLOR | LIGHT_TEXT_DIVIDER_ALPHA),
    ("chats_unreadCounterText", PRIMARY_TEXT_COLOR),
    ("chats_verifiedBackground", SOLID_ACCENT_COLOR),
    ("chats_verifiedCheck", ACTIVE_ICON_COLOR),
    ("divider", DIVIDER_COLOR),
    ("emptyListPlaceholder", SECONDARY_TEXT_COLOR),
    ("graySection", DARK_CARD_COLOR | SOLID_ALPHA),
    ("profile_actionBackground", SOLID_ACCENT_COLOR),
    ("profile_actionIcon", ACTIVE_ICON_COLOR),
    ("profile_actionPressedBackground", LIGHT_SELECTED_COLOR),
    ("profile_title", PRIMARY_TEXT_COLOR),
    ("progressCircle", SOLID_ACCENT_COLOR),
    ("switchThumb", SWITCH_THUMB_OFF_COLOR | SWITCH_THUMB_OFF_ALPHA),
    ("switchThumbChecked", ACCENT_COLOR | SWITCH_THUMB_ON_ALPHA),
    ("switchTrack", SWITCH_TRACK_OFF_COLOR | SWITCH_TRACK_OFF_ALPHA),
    ("switchTrackChecked", ACCENT_COLOR | SWITCH_TRACK_ON_ALPHA),
    ("windowBackgroundGray", DIVIDER_COLOR),
    ("windowBackgroundGrayShadow", BACKGROUND_COLOR),
    ("windowBackgroundWhite", BACKGROUND_COLOR),
    ("windowBackgroundWhiteBlackText", PRIMARY_TEXT_COLOR),
    ("windowBackgroundWhiteBlueHeader", LIGHT_ACCENT_COLOR | LIGHT_TEXT_SECONDARY_ALPHA),
    ("windowBackgroundWhiteGrayIcon", ACTIVE_ICON_COLOR),
    ("windowBackgroundWhiteGrayText", SECONDARY_TEXT_COLOR),
    ("windowBackgroundWhiteGrayText2", SECONDARY_TEXT_COLOR),
    ("windowBackgroundWhiteGrayText3", SECONDARY_TEXT_COLOR),
    ("windowBackgroundWhiteGrayText4", SECONDARY_TEXT_COLOR),
    ("windowBackgroundWhiteGrayText5", SECONDARY_TEXT_COLOR),
    ("windowBackgroundWhiteValueText", SECONDARY_TEXT_COLOR),
]


if __name__ == "__main__":
    print_theme(THEME)
