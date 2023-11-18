from task import task
from event import event
from task import Priority
from task import TaskType
from datetime import datetime, time
from enum import Enum

# list of task and events of the day
class Day:

    def __init__(self,todays_events=[]):
    
        self.todays_schedule=todays_events
    
    def __str__(self):
        for this in self.todays_schedule:
            print(this)
        
# if __name__ == "__main__":
