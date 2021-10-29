import websockets
import asyncio
import subprocess
import os

async def handler(ws, path):
  print("connected")

async def _main():

  # initialize the websockets server that receives IO from front end
  async with websockets.serve(handler, host=os.environ["CLIENT_HOST"], port=os.environ["CLIENT_PORT_WS"]):
    # initialize the server process that serves our front end
    with subprocess.Popen(["python3", "tgar/serveclient.py"]):
      # block this coroutine
      await asyncio.Future()
      

def main():

  import importlib

  importlib.import_module("testfile")
  loop = asyncio.get_event_loop()
  loop.create_task(_main())
  loop.run_forever()