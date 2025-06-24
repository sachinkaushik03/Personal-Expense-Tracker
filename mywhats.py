import pywhatkit as kit

# Phone number (with country code), message
phone = "+918529074767"  # Replace with your number
message = "Hi! This is an automated message sent using pywhatkit."

# Send message instantly without scheduled time
kit.sendwhatmsg_instantly(phone, message, wait_time=10, tab_close=True)

