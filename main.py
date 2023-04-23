
import time
import plyer;
import currenttime
print(plyer);
from plyer import notification

wanted_time = int(input("After how many minutes do you want to be reminded? :"))

wanted_time_min = int(wanted_time)


for x in range(0,wanted_time_min):
    currenttime.curent_time_teller(time=time)
    time.sleep(60)

currenttime.curent_time_teller(time)
notification.notify(
    app_name="Reminder",
    title="Time is up",
    message=f"{wanted_time_min} minutes are over",
    timeout=2
)
time.sleep(5)






