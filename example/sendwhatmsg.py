"""
Version 5.2
Status: Stable
Documentation: https://github.com/Ankit404butfound/PyWhatKit/wiki
Report Bugs and Feature Requests here: https://github.com/Ankit404butfound/PyWhatKit/issues
For further Information, Join our Discord: https://discord.gg/62Yf5mushu

This is a Python 3.x script to send Whatsapp Messages.
This code is written by Ankit404butfound and published on GitHub.
"""


# Import the package
import pywhatkit

# Send a message

# These are the parameters
# phone_no: str, message: str, time_hour: int, time_min: int, wait_time: int = 15, tab_close: bool = False, close_time: int = 3
pywhatkit.sendwhatmsg("+918098989898", "Hello World", 10, 30)
