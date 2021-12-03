import config  # config.py has important imformation
import json  # library for handling JSON data
import time  # module for sleep operation
import requests  # for making HTTP requests
from boltiot import Bolt  # importing Bolt from boltiot module

myBolt = Bolt(config.API_KEY, config.DEVICE_ID)


def get_LDR_reading():
    pin = "A0"
    try:
        response = myBolt.analogRead(pin)  # Reading data from LDR

        data = json.loads(response)  # Extracting the data from response

        if(data["success"] != 1):  # Failure in Reading
            print("Request to Read Unsuccessful")
            print("\nResponse got --> ", data)
            return -1  # -1 means failure
        sensor_value = int(data["value"])  # Getting the LDR value
        return sensor_value
    except Exception as e:
        print("Something went wrong while returning value")
        print(e)
        return -1


def send_telegram_message(message):
    url = "https://api.telegram.org/" + config.telegram_bot_id + "/sendMessage"
    data = {"chat_id": config.telegram_chat_id, "text": message}

    try:
        response = requests.request("POST", url, params=data)
        telegram_data = json.loads(response.text)
        return telegram_data["ok"]
    except Exception as e:
        print("Error occured while sending Telegram Message")
        print(e)
        return False


while(True):
    sensor_value = get_LDR_reading()
    print("Reading LDR Sensor Value:: --> ", sensor_value)

    if sensor_value == -1:
        print("\nCould not read. Skipping\n")
        time.sleep(10)
        continue

    if sensor_value < 500:  # 500 is the threshold value
        print("\nIntruder!!!!!!!\n")
        print("Buzzer Activated\n")

        myBolt.digitalWrite(1, "HIGH")  # Activating Buzzer
        message = "Alert !! Burglar has entered the premises. Contact the police !!"
        telegram_status = send_telegram_message(
            message)  # Sending Message via Telegram
        print(telegram_status)
        time.sleep(15)  # Buzzer buzzes for 15 seconds
        myBolt.digitalWrite('1', "LOW")  # Buzzer deactivated

        print("Buzzer Deactivated")

    else:
        print("\nNo Burglar Yet")
        # Since in free account, only limited API calls are allowed
        # if using pro bolt account, then make time.sleep(1) for more accuracy
        time.sleep(10)
