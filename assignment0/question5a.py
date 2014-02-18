from urllib import urlopen
from json import load
from datetime import datetime, date, timedelta
from pytz import timezone

def quadMassAve():
    #handle = urlopen("http://shuttleboy.cs50.net/api/1.2/trips?a=Quad&b=Mass+Ave+Garden+St&output=json")
    sched = load(urlopen("http://shuttleboy.cs50.net/api/1.2/trips?a=Quad&b=Mass+Ave+Garden+St&output=json"))
    for shuttle in sched[-3:]:
        depart = datetime.strptime(shuttle['departs'], "%Y-%m-%dT%H:%M:%S")
        #depart = timezone("US/Eastern").localize(depart)
        time_diff = timezone("US/Eastern").localize(depart) - datetime.now(timezone("US/Eastern"))
        print("Departs at " + date.strftime(depart, "%I:%M %p") + ", " + 
              str(time_diff) + " from now")

quadMassAve()

