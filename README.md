# snkrs-bot
A free to use bot for SNKRS website

\* Before using the bot please make sure you pre-saved a credit card in your account.

## Requirements
- Python 3
- Google Chrome
- ChromeDriver

## Usage
1. Clone the project:
   ```
   $ git clone https://github.com/mDemianchuk/snkrs-bot.git
   ```

2. Install dependencies:
    ```
    $ cd snkrs-bot
    $ pip3 install -r requirements.txt   
    ```

3. Download [ChromDriver](https://chromedriver.chromium.org/downloads) for your version of Google Chrome, extract the executable, and place it in the root directory:

    ```
    snkrs-bot/
    ├── bot.py
    ├── ...
    ├── chromedriver (or chromedriver.exe for Windows users)
    ```

4. Fill in the `settings.json`:

    ```  
    "item": {
        "shoePosition": "",       - shoe position in the "In Stock" grid (1-based indexig)
        "sizePosition": ""        - size position in the sizes grid (1-based indexig)
    },
    "personalInfo": {
        "email": "",
        "password": "",
        "cvv": ""
    }
    ```
    \* All properties must be strings (enclosed in double quotation marks)

5. Run the bot:
   ```
   $ python3 main.py
   ```
   \* To avoid accidental charges, "Proceed to order overview" needs to be clicked **manually**

