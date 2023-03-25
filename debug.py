import ipdb
from lib import *

# Test your code below...


r1= Role("Inspector Lee")
r2= Role("Officer Carter")


a1= Audition("Jackie Chan", "LA", False, r1)
a2= Audition("Chris Tucker", "LA", False, r2)
a3= Audition("Daniel Wu", "LA", False, r1)
a4= Audition("Eddie Murphy", "LA", False, r2)
a5= Audition("Ice T", "LA", False, r2)







# the below line allows us to stop & try stuff!
ipdb.set_trace()