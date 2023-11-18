from task import task
from event import event
from task import Priority
from task import TaskType
from datetime import datetime
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
        
    def sortTask(self):
        remainder = (x.deadline-datetime.now()).hour*4
        sorted_tasks = sorted(self.myTasks, key=lambda x: x.priority.value + remainder)

        return sorted_tasks
        
    def updateTasks(self):
        return
    
    def __str__(self):
        for something in self.myTasks:
            print(something)
        
if __name__ == "__main__":
    
    t1=task(60,Priority.very_high,TaskType.school,datetime(2023,12,20,14,30))
    t2=task(60,Priority.low,TaskType.school,datetime(2023,12,23,19,30))
    t3=task(30,Priority.very_high,TaskType.school,datetime(2023,12,16,14,30))
    t4=task(120,Priority.neutral,TaskType.school,datetime(2023,12,19,19,30))
    
    mySchedule=Schedule([t1,t2,t3,t3],[])
    mySchedule.sortTask()
    print(mySchedule)