from SwSpotify import spotify
from pycaw.pycaw import AudioUtilities
import win32gui

# This is for the few ads that aren't using the name "Advertisement"
adNames = ['Explore Nail Biting Topics In Sport',
           'The Easy Way to Turn Old Tech into CASH.',
           'Graduate careers in consulting']
isAd = False
titles = []


def winEnumHandler(hwnd, ctx):
    if win32gui.IsWindowVisible(hwnd):
        titles.append(win32gui.GetWindowText(hwnd))


if __name__ == "__main__":
    while True:
        try:
            win32gui.EnumWindows(winEnumHandler, None)

            for title in titles:
                for ad in adNames:
                    if title == ad:
                        print("This is an ad")
                        isAd = True
                        break
                    else:
                        isAd = False
                if isAd == True:
                    break

            if spotify.current()[0] == 'Advertisement' or isAd == True:
                sessions = AudioUtilities.GetAllSessions()
                titles = []
                for session in sessions:
                    if session.Process and session.Process.name() == "Spotify.exe":
                        volume = session.SimpleAudioVolume
                        volume.SetMute(1, None)

            else:
                sessions = AudioUtilities.GetAllSessions()
                for session in sessions:
                    if session.Process and session.Process.name() == "Spotify.exe":
                        volume = session.SimpleAudioVolume
                        volume.SetMute(0, None)

        except:
            pass
