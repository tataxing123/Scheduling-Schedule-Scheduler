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

product_func = lambda x: x.priority.value *  x.time_remaing_to_deadline()
sum_func = lambda x, rate: x.priority.value + rate * x.time_remaing_to_deadline()
#TODO add rate function 

class Schedule:
    
    def __init__(self,myTasks=[],myEvents=[],habits=SleepingHabits.both, funct_to_use=product_func, rate=1):
        
        self.myTasks=myTasks
        self.myEvents=myEvents
        self.habits=habits
        self.funct_to_use = funct_to_use
        self.rate =rate
    
    def addTask(self,newTask):
        
        self.myTasks.append(newTask)
        
    def addEvent(self,newEvent):
        
        self.myEvent.append(newEvent)
        
    def sortTask(self):
        
        sorted_tasks = sorted(self.myTasks, key= self.func_to_use) 

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
    print(t1.priority.value)


    mySchedule=Schedule([t1,t2,t3],[])
    mySchedule.sortTask()
    for something in mySchedule.myTasks:
            print(something)