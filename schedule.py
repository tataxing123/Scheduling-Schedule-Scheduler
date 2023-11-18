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
        
        sorted_tasks = sorted(self.myTasks, key=lambda x:
            x.priority + (datetime.now()-x.deadline).total_seconds() / 900
            )

        return sorted_tasks
        
    def updateTasks(self):
        return
    
    def __str__(self):
        for something in self.myTasks:
            print(something)
        
if __name__ == "__main__":
    
    t1=task("t1",60,datetime(2023,11,18,22,00),Priority.low,TaskType.school)
    t2=task("t2",60,datetime(2023,11,18,22,00),Priority.very_high,TaskType.school)
    t3=task("t3",60,datetime(2023,11,19,2,00),Priority.very_high,TaskType.school)
    # t4=task(120,Priority.neutral,TaskType.school,datetime(2023,11,18,19,30))
    # title,duration,deadline,priority,type,description
    
    mySchedule=Schedule([t1,t2,t3],[])
    mySchedule.sortTask()
    for something in mySchedule.myTasks:
            print(something)