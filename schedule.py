import task as t
import event as e
from enum import Enum

class SleepingHabits(Enum):
    
    morning = 1
    night = 2
    both = 3

class Schedule:
    
    def __init__(self,myTasks=[],myEvents=[],habits=SleepingHabits.both):
        
        self.myTasks=myTasks
        self.myEvents=myEvents
        self.habits=habits
    
    def addTask(self,newTask):
        self.myTasks.append(newTask)
        
    def addEvent(self,newEvent):
        self.myEvent.append(newEvent)