import time
import util
import logging

from bot import Bot


def main():
    logging.basicConfig(format="%(levelname)s: %(asctime)s - %(message)s",
                        datefmt="%I:%M:%S", level=logging.INFO)
    settings = util.load_settings()
    item = settings["item"]
    personal_info = settings["personalInfo"]

    bot = Bot("https://www.nike.com/launch?s=in-stock")
    bot.go_to_start_page()
    start_time = time.time()
    if bot.select_shoe(item["shoePosition"]) and bot.select_shoe_size(item["sizePosition"]):
        if bot.add_to_cart():
            time.sleep(1)
            if bot.go_to_checkout():
                if bot.log_in(personal_info["email"], personal_info["password"]):
                    bot.wait_till_on_checkout_page()
                    bot.fill_in_cvv(personal_info["cvv"])
    logging.info(f"Total time: {time.time() - start_time}s.")


if __name__ == "__main__":
    main()
