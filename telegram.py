#coder :- Salman Faris

import sys
import time
import random
import datetime
import telepot
import RPi.GPIO as GPIO

#LED
def on(pin):
        GPIO.output(pin,GPIO.HIGH)
        return
def off(pin):
        GPIO.output(pin,GPIO.LOW)
        return
# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)
# set up GPIO output channel
GPIO.setup(11, GPIO.OUT)

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print 'Got command: %s' % command

    if command == 'On':
       bot.sendMessage(chat_id, on(11))
       bot.sendMessage(chat_id, str("CCTV Sedang ON"))
    elif command =='Off':
       bot.sendMessage(chat_id, off(11))
       bot.sendMessage(chat_id, str("CCTV Sedang OFF"))

bot = telepot.Bot('TOKEN')
bot.message_loop(handle)
print 'I am listening...'

while 1:
         time.sleep(10)
