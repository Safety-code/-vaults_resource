from slot import Classrooms
from slot import ClassroomType as ct
from slot import Weekday as wd
from slot import Period as pd
from slot import Slot as sl
from slot import Session as se
import json
#import numpy as np


ads = []
def convert_to_json(array_data):
    for ad in array_data:
        ada = json.dumps(ad.__dict__)
        ads.append(ada)
    return ads


ED1 = Classrooms("ED1", 25, ct(1).value)
ED2 = Classrooms("ED2", 20, ct(1).name)
classrooms = [ED1, ED2]

print(classrooms[0])
print(classrooms[1])

cls = convert_to_json(classrooms)
# for cl in Classrooms:
#     cla = json.dumps(cl.__dict__)
#     cls.append(cla)

# print(cls)

#period
p1 = pd(1, "08:00-09:00")
p2= pd(2, "09:00-10:00")
periods = [1, 2]


slots = []

for day in wd:
    for classroom in classrooms:
        for period in periods:
            ss = sl(day.value, classroom.id, period.id)
            slots.append(ss)

#print slots
sls = convert_to_json(slots)
print("Slot", len(sls))
print(sls)

#sessions
S1 = se("RN 1","1023", "RN170", 54 )
S2 = se("RN 2","1023", "RN170", 54 )
S3 = se("RN 3","7468", "RN270", 47 )
S4 = se("RN 4","1023", "RN188", 48 )
S5 = se("RN 5","4384", "RN188", 48 )
S6 = se("RN 6","1367", "RN187", 49 )

sessions = [S1, S2, S3, S4, S5, S6]
ses = convert_to_json(sessions)

print("Sessions", len(ses))

# nar = np.array(ses)
# print(nar)



