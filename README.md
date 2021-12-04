# Laser Security System with Bolt IoT and Telegram messaging
### Created by Vinay Vinod Hariya
#### finished on 14<sup>th</sup> April, 2020
<br>

Please refer to the [hackster](https://www.hackster.io/vinay-hariya/laser-security-system-with-bolt-iot-and-telegram-messaging-6d1f83) link for full explanation on the project and the step by step process on how to use the code.
<br>

### Note: The Ubuntu software is NOT required for the project. Instead create a python virtual environment to install the packages and run the code.

<br>

 Follow the steps perfectly for successful installation:

   - Ensure python is installed on your system. (Version 3.9 and above)
   - Open the command promt (or equivalent) on the system.
   - Navigate inside to the outer folder housing the project folders and files.
   - Type the following command (instead of ```.env```, you can give any name)
     
     ```
     python -m venv .env
     ```

   - Activate the ```.env``` virutal environment
        - For Windows, type the following
          ```
          .\.env\scripts\activate
          ```
        - For Mac and Linux, type the following
          ```
          source .env/bin/activate
          ```
   - To install all the related packages, type ```pip3```:
     
     ```
     pip3 install -r requirements.txt
     ```

   - Ensure the ```config.py``` data is set properly.

   - Run the following command to start up the website: (```python3``` for mac and linux users)
     
     ```
     python burglar_alarm.py
     ```

I will update the hackster .io website in the future.