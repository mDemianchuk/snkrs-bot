import util
import logging
from bot import Bot
import time


def main():
    logging.basicConfig(format="%(levelname)s: %(asctime)s - %(message)s",
                        datefmt="%I:%M:%S", level=logging.INFO)
    settings = util.get_settings()
    item = settings["item"]
    personal_info = settings["personalInfo"]

    bot = Bot("https://www.nike.com/launch?s=in-stock")
    logging.info("Initialized a bot instance")

    bot.go_to_start_page()
    if bot.select_shoe(item["shoePosition"]) and bot.select_shoe_size(item["sizePosition"]):
        if bot.add_to_cart():
            time.sleep(1)
            if bot.go_to_checkout():
                if bot.log_in(personal_info["email"], personal_info["password"]):
                    time.sleep(6)
                    bot.fill_in_cvv(personal_info["cvv"])


if __name__ == "__main__":
    main()
