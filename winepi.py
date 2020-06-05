# Input a Sequences of Episodes
sequences = [
    'A', 'B', 'R', 'B', 'A', 'K', 'A', 'D', 'A', 'B', 'R', 'A'
]
# Input size of Window
winSize = 5
# Min Fraction

# Empty Window with no Sequences
baseWindow = []
for i in range (0, winSize):
    baseWindow.append(0)

class Windows:
    # Episodes
    windowsList = []

    # Push each signal into Windows
    def pushing(self):
        lastWin = baseWindow.copy()
        for signal in sequences:
            currentWindow = lastWin.copy()
            for i in range(1, len(currentWindow)):
                currentWindow[i - 1] = currentWindow[i]
            currentWindow[len(currentWindow) - 1] = signal
            lastWin = currentWindow.copy()
            self.windowsList.append(lastWin)
        # COntinue Pushing until the only the last signal remains
        nextStageLastWin = self.windowsList[len(self.windowsList) - 1].copy()
        for i in range(1, len(baseWindow)):
            currentWindow = nextStageLastWin.copy()
            for i in range(1, len(currentWindow)):
                currentWindow[i - 1] = currentWindow[i]
            currentWindow[len(currentWindow) - 1] = 0
            nextStageLastWin = currentWindow.copy()
            self.windowsList.append(nextStageLastWin)

def count():
    print("")

def main():
    windowsObj = Windows()
    windowsObj.pushing()
    windows = windowsObj.windowsList
    for i in range(0, len(windows)):
        print(windows[i])

main()