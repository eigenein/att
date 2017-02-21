#!/usr/bin/env python3

"""
Material Dark theme generator.
"""

from utils import argb, print_theme, SOLID
from utils.material import *

ACCENT_COLOR = BLUE_A200
ACTIVE_ICON_COLOR = argb(LIGHT_ICON_COLOR, LIGHT_ICON_ACTIVE_ALPHA)
APP_BAR_COLOR = argb(DARK_APP_BAR_COLOR, SOLID)
BACKGROUND_COLOR = argb(DARK_BACKGROUND_COLOR, SOLID)
DIVIDER_COLOR = argb(LIGHT_TEXT_COLOR, LIGHT_TEXT_DIVIDER_ALPHA)
HINT_COLOR = argb(LIGHT_TEXT_COLOR, LIGHT_TEXT_HINT_ALPHA)
LIGHT_SELECTED_COLOR = argb(LIGHT_TEXT_COLOR, RIPPLE_ALPHA)
PRIMARY_TEXT_COLOR = argb(LIGHT_TEXT_COLOR, LIGHT_TEXT_PRIMARY_ALPHA)
SECONDARY_TEXT_COLOR = argb(LIGHT_TEXT_COLOR, LIGHT_TEXT_SECONDARY_ALPHA)
SOLID_ACCENT_COLOR = argb(ACCENT_COLOR, SOLID)

THEME = [
    ("actionBarActionModeDefault", APP_BAR_COLOR),
    ("actionBarActionModeDefaultIcon", ACTIVE_ICON_COLOR),
    ("actionBarActionModeDefaultTop", argb(DARK_STATUS_BAR_COLOR, SOLID)),
    ("actionBarDefault", APP_BAR_COLOR),
    ("actionBarDefaultIcon", ACTIVE_ICON_COLOR),
    ("actionBarDefaultSearch", PRIMARY_TEXT_COLOR),
    ("actionBarDefaultSearchPlaceholder", HINT_COLOR),
    ("actionBarDefaultSelector", LIGHT_SELECTED_COLOR),
    ("actionBarDefaultSubtitle", SECONDARY_TEXT_COLOR),
    ("actionBarDefaultTitle", PRIMARY_TEXT_COLOR),
    ("avatar_actionBarIconBlue", ACTIVE_ICON_COLOR),
    ("avatar_backgroundActionBarBlue", APP_BAR_COLOR),
    ("avatar_backgroundBlue", argb(BLUE_500, SOLID)),
    ("avatar_backgroundCyan", argb(CYAN_700, SOLID)),
    ("avatar_backgroundGreen", argb(GREEN_500, SOLID)),
    ("avatar_backgroundOrange", argb(ORANGE_800, SOLID)),
    ("avatar_backgroundPink", argb(PINK_500, SOLID)),
    ("avatar_backgroundRed", argb(RED_500, SOLID)),
    ("avatar_backgroundViolet", argb(PURPLE_500, SOLID)),
    ("avatar_nameInMessageBlue", argb(BLUE_400, SOLID)),
    ("avatar_nameInMessageCyan", argb(CYAN_500, SOLID)),
    ("avatar_nameInMessageGreen", argb(GREEN_500, SOLID)),
    ("avatar_nameInMessageOrange", argb(ORANGE_500, SOLID)),
    ("avatar_nameInMessagePink", argb(PINK_200, SOLID)),
    ("avatar_nameInMessageRed", argb(RED_300, SOLID)),
    ("avatar_nameInMessageViolet", argb(PURPLE_200, SOLID)),
    ("avatar_subtitleInProfileBlue", SECONDARY_TEXT_COLOR),
    ("avatar_text", PRIMARY_TEXT_COLOR),
    ("avatar_text", PRIMARY_TEXT_COLOR),
    ("chat_inBubble", argb(DARK_CARD_COLOR, SOLID)),
    ("chat_inBubbleSelected", LIGHT_SELECTED_COLOR),
    ("chat_inBubbleShadow", BACKGROUND_COLOR),
    ("chat_inInstant", ACTIVE_ICON_COLOR),
    ("chat_inPreviewInstantText", SOLID_ACCENT_COLOR),
    ("chat_inTimeText", SECONDARY_TEXT_COLOR),
    ("chat_messageLinkIn", SOLID_ACCENT_COLOR),
    ("chat_messageLinkOut", SOLID_ACCENT_COLOR),
    ("chat_messagePanelBackground", argb(DARK_CARD_COLOR, SOLID)),
    ("chat_messagePanelHint", HINT_COLOR),
    ("chat_messagePanelIcons", ACTIVE_ICON_COLOR),
    ("chat_messagePanelShadow", BACKGROUND_COLOR),
    ("chat_messagePanelText", PRIMARY_TEXT_COLOR),
    ("chat_messageTextIn", PRIMARY_TEXT_COLOR),
    ("chat_messageTextOut", PRIMARY_TEXT_COLOR),
    ("chat_muteIcon", ACTIVE_ICON_COLOR),
    ("chat_outBubble", argb(GREY_700, SOLID)),
    ("chat_outBubbleSelected", LIGHT_SELECTED_COLOR),
    ("chat_outBubbleShadow", BACKGROUND_COLOR),
    ("chat_outTimeText", SECONDARY_TEXT_COLOR),
    ("chat_selectedBackground", LIGHT_SELECTED_COLOR),
    ("chat_wallpaper", BACKGROUND_COLOR),
    ("chats_actionBackground", SOLID_ACCENT_COLOR),
    ("chats_actionIcon", ACTIVE_ICON_COLOR),
    ("chats_actionMessage", SOLID_ACCENT_COLOR),
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
    ("chats_nameMessage", SOLID_ACCENT_COLOR),
    ("chats_pinnedIcon", ACTIVE_ICON_COLOR),
    ("chats_pinnedOverlay", argb(LIGHT_TEXT_COLOR, LIGHT_TEXT_DIVIDER_ALPHA)),
    ("chats_sendClock", argb(GREEN_500, SOLID)),
    ("chats_sentCheck", argb(GREEN_500, SOLID)),
    ("chats_unreadCounter", SOLID_ACCENT_COLOR),
    ("chats_unreadCounterMuted", argb(LIGHT_TEXT_COLOR, LIGHT_TEXT_DIVIDER_ALPHA)),
    ("chats_unreadCounterText", PRIMARY_TEXT_COLOR),
    ("chats_verifiedBackground", SOLID_ACCENT_COLOR),
    ("chats_verifiedCheck", LIGHT_TEXT_COLOR),
    ("divider", DIVIDER_COLOR),
    ("emptyListPlaceholder", SECONDARY_TEXT_COLOR),
    ("graySection", argb(DARK_CARD_COLOR, SOLID)),
    ("profile_actionBackground", SOLID_ACCENT_COLOR),
    ("profile_actionIcon", ACTIVE_ICON_COLOR),
    ("profile_actionPressedBackground", LIGHT_SELECTED_COLOR),
    ("profile_title", PRIMARY_TEXT_COLOR),
    ("progressCircle", SOLID_ACCENT_COLOR),
    ("switchThumb", argb(SWITCH_THUMB_OFF_COLOR, SWITCH_THUMB_OFF_ALPHA)),
    ("switchThumbChecked", argb(ACCENT_COLOR, SWITCH_THUMB_ON_ALPHA)),
    ("switchTrack", argb(SWITCH_TRACK_OFF_COLOR, SWITCH_TRACK_OFF_ALPHA)),
    ("switchTrackChecked", argb(ACCENT_COLOR, SWITCH_TRACK_ON_ALPHA)),
    ("windowBackgroundGray", DIVIDER_COLOR),
    ("windowBackgroundGrayShadow", BACKGROUND_COLOR),
    ("windowBackgroundWhite", BACKGROUND_COLOR),
    ("windowBackgroundWhiteBlackText", PRIMARY_TEXT_COLOR),
    ("windowBackgroundWhiteBlueHeader", SOLID_ACCENT_COLOR),
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
