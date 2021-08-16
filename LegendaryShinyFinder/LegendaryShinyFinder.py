from datetime import datetime
import cv2
import os
import sys
import time
# Shared bot functionality
dirPath = os.path.dirname(os.path.realpath(__file__))
sys.path.append("{}\\..".format(dirPath))
import BotCore as Bot
from Config import *


def HomeRegielekiRoom():
    Bot.SendCommandForSeconds(Bot.Controller.LSTICK_U_L, 5.0)


def ActivateRegielekiPattern():
    Bot.SendCommandForSeconds(Bot.Controller.lstick_angle(0, 0x1E), 2.25)
    Bot.ShowLive(0.5)
    Bot.SendCommandForSeconds(Bot.Controller.lstick_angle(270, 0x1E), 5.4)
    Bot.ShowLive(0.5)
    Bot.SendCommandForSeconds(Bot.Controller.lstick_angle(90, 0x1E), 1.3)
    Bot.ShowLive(0.5)
    Bot.SendCommandForSeconds(Bot.Controller.lstick_angle(0, 0x1E), 4.2)
    Bot.ShowLive(0.5)
    Bot.SendCommandForSeconds(Bot.Controller.lstick_angle(270, 0x1E), 1.3)
    Bot.ShowLive(0.5)
    # This is where the room shakes
    Bot.SendCommandForSeconds(Bot.Controller.LSTICK_U, 5.0)
    Bot.SendCommandOnce(Bot.Controller.BTN_A)
    Bot.ShowLive(2.0)
    Bot.SendCommandForSeconds(Bot.Controller.LSTICK_U, 2.0)
    Bot.ShowLive(0.5)
    Bot.SendCommandForSeconds(Bot.Controller.lstick_angle(180, 0x1E), 2.0)
    Bot.ShowLive(0.5)
    Bot.SendCommandOnce(Bot.Controller.LSTICK_U)
    Bot.ShowLive(0.5)


GolurkGo = cv2.imread('Resources\\GolurkGo.jpg', cv2.IMREAD_GRAYSCALE)
GolurkGo = GolurkGo[590:590+30, 140:140+210]
GolurkGoThreshold = 0.95


def IsGolurkGoing():
    frame = Bot.GetFrameGrayscale()
    frame = frame[569:569+76, 116:116+271]
    return Bot.GetMatchScore(frame, GolurkGo) > GolurkGoThreshold


def IsRegielekiShiny():
    Bot.SendCommandOnce(Bot.Controller.BTN_A)
    Bot.ShowLive(2.0)
    Bot.SendCommandOnce(Bot.Controller.BTN_A)
    Bot.ShowLive(2.0)
    Bot.SendCommandOnce(Bot.Controller.BTN_A)
    Bot.ShowLive(10.743)

    golurkGoing = False
    start = time.time()
    now = start
    while now - start < 0.6:
        if IsGolurkGoing():
            golurkGoing = True
        now = time.time()

    if not golurkGoing:
        return True

    Bot.ShowLive(10.0)
    Bot.SendCommandOnce(Bot.Controller.LSTICK_U)
    Bot.ShowLive(0.5)
    Bot.SendCommandOnce(Bot.Controller.BTN_A)
    Bot.ShowLive(1.0)
    Bot.SendCommandOnce(Bot.Controller.BTN_B)
    Bot.ShowLive(5.0)
    Bot.SendCommandOnce(Bot.Controller.BTN_B)
    Bot.ShowLive(1.0)

    return False


# Application -----------------------------------------------------------------

Bot.OpenVideoCapture(VideoCaptureNum)
Bot.OpenController(ComPort)

NumEncounters = 0

Bot.SendCommandForSeconds(Bot.Controller.LSTICK_U, 3.0)
while True:
    NumEncounters += 1
    print("Encounter {}".format(NumEncounters))

    HomeRegielekiRoom()
    ActivateRegielekiPattern()
    if (IsRegielekiShiny()):
        print('Shiny Regieleki found!')
        Bot.SendEmail(
            EmailTo, EmailFrom, 'Shiny Regieleki found!',
            "Time: {}\nEncounter: {}".format(datetime.now(), NumEncounters))
        break

Bot.CloseController()
Bot.CloseVideoCapture()
