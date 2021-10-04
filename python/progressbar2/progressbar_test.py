from time import sleep
import progressbar as pgb

for i in pgb.progressbar(range(100), redirect_stdout=True):
    sleep(.1)
