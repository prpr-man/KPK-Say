#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import websocket
import thread
import time
import os

def on_message(ws, message):
    print "debug: called on_message"
    os.system('./jsay' + message)
    print message

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


if __name__ == "__main__":

    param = sys.argv

    url = "wss://kumikomi-atk.c9users.io/websocket"

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
