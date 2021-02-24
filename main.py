from pypresence import Presence
import time
import json
from pywinauto import Desktop

logging_enabled = True

def log(out: str):
    if logging_enabled:
        print(out)


f = open("sites.json", "r")
sites = json.loads(f.read())
f.close()
sites = tuple(sites)
print(sites)
rpc = Presence(814199889118232616)
rpc_closed = True
while True:
    found_opera = False
    opera_windows = []
    windows = Desktop(backend="uia").windows()
    for window in windows:
        if "- Opera" in window.window_text():
            if rpc_closed:
                log("Trying to connect to RPC...")
                rpc.connect()
                log("Connected!")
                rpc_closed = False
            found_opera = True
            page_title = window.window_text()
            page_title = page_title[:-8]
            opera_windows.append(page_title)
            multiple_windows_open = False
            if len(opera_windows) > 1:
                multiple_windows_open = True
            else:
                found = False
                for site in sites:
                    if str.lower(site) in str.lower(page_title):
                        rpc.update(details="Browing the web", state=f"Using {site}", large_image="epiklogo")
                        found = True
                    else:
                        pass
                if not found:
                    rpc.update(details="Browing the web", state=None, large_image="epiklogo")
                if multiple_windows_open:
                    rpc.update(details="Browing the web", state=None, large_image="epiklogo")
    if not found_opera:
        if not rpc_closed:
            rpc.close()
            log("RPC Closed!")
            rpc_closed = True
    time.sleep(1)
