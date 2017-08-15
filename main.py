import sys
import os
import time




def start_new_sprint():
  print 'start hacking away brooo'
  minutes_worked = 0
  while True:
    time.sleep(60)
    os.system('clear')
    minutes_worked +=1
    print "you have been hustling for %d minutes. Keep it up!"%minutes_worked

  
  


try:
  command = sys.argv[1]
except KeyError, e:
  print e
  pass
else:
  functionDict = {
    'startSprint': start_new_sprint,
  }
  functionDict[command]()




