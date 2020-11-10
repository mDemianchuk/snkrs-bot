import json
import logging


def load_settings():
    try:
        with open("settings.json") as settings_file:
            return json.load(settings_file)
    except Exception as e:
        logging.error("Error while loading the settings file")
        raise e
