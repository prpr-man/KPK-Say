#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import websocket
import thread
import time
import os
import json

def on_message(ws, message):
    print "debug: called on_message"
    json_obj = json.loads(message)
    if json_obj["func"] == "play":
       os.system((u'jsay.sh ' + json_obj["text"]).encode('utf_8'))
    print json_obj["text"].encode('utf_8')

def on_error(ws, error):
    print "debug: called on_error"
    print error

def on_close(ws):
    print "### closed ###"

def on_open(ws):
    def run(*args):
        print("debug: websocket is opened")

        while(True):
            line = sys.stdin.readline()
            if line != "":
                print "debug: sending value is " + line
                ws.send(line)

    thread.start_new_thread(run, ())

def websocket_main():
    param = sys.argv

    url = "wss://evening-tundra-11466.herokuapp.com"

    if len(param) == 2:
        url = param[1]
        print "debug: param[1] is " + param[1]

    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(url,
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()

if __name__ == "__main__":
    websocket_main()
