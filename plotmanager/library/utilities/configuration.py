import os

from plotmanager.library.utilities.exceptions import InvalidjokerLocationException, MissingImportError


def test_configuration(joker_location, notification_settings, instrumentation_settings):
    if not os.path.exists(joker_location):
        raise InvalidjokerLocationException('The joker_location in your config.yaml does not exist. Please confirm if '
                                            'you have the right version. Also confirm if you have a space after the '
                                            'colon. "joker_location: <DRIVE>" not "joker_location:<DRIVE>"')

    if notification_settings.get('notify_discord'):
        try:
            import discord_notify
        except ImportError:
            raise MissingImportError('Failed to find import "discord_notify". Be sure to run "pip install -r '
                                     'requirements-notification.txt".')
    if notification_settings.get('notify_sound'):
        try:
            import playsound
        except ImportError:
            raise MissingImportError('Failed to find import "playsound". Be sure to run "pip install -r '
                                     'requirements-notification.txt".')
    if notification_settings.get('notify_pushover'):
        try:
            import pushover
        except ImportError:
            raise MissingImportError('Failed to find import "pushover". Be sure to run "pip install -r '
                                     'requirements-notification.txt".')

    if instrumentation_settings.get('notify_telegram'):
        try:
            import telegram_notifier
        except ImportError:
            raise MissingImportError('Failed to find import "telegram_notifier". Be sure to run "pip install -r '
                                     'requirements-notification.txt".')

    if instrumentation_settings.get('notify_ifttt'):
        try:
            import requests
        except ImportError:
            raise MissingImportError('Failed to find import "requests". Be sure to run "pip install -r '
                                     'requirements-notification.txt".')

    if instrumentation_settings.get('prometheus_enabled'):
        try:
            import prometheus_client
        except ImportError:
            raise MissingImportError('Failed to find import "prometheus_client". Be sure to run "pip install -r '
                                     'requirements-notification.txt".')
