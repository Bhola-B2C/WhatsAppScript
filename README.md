# WhatsAppScript
Automate Whatsapp

## Requirements

+ Python 3.x
+ python-pip
+ virtualenv
+ selenium
+ Mozilla Firefox or Google Chrome

## Setup

1. Clone the app ``` git clone https://github.com/Bhola-B2C/WhatsAppScript.git ```
2. ```mkdir project && cd project```
3. ```virtualenv .```
4. ```source bin/activate```
5. ```pip install selenium```
6. Download the webdriver (for chrome: chromedriver and for firefox: geckodriver)
7. Change the path accordingly in the whatsapp.py

## Usage

``` python schedule.py "Friend's Name" "message" "HH:MM DD.MM.YYY" ```

For instant message,

``` python schedule.py "Firend's Name" "message" ```
