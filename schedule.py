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
sum_func_opt_deadline = lambda x: x.priority.value       + 0.5 * x.time_remaing_to_deadline()
sum_func_opt_priotity = lambda x: 0.5 * x.priority.value + x.time_remaing_to_deadline()
sum_func_non_opt =  lambda x: 0.5 * x.priority.value + x.time_remaing_to_deadline()

class Schedule:

    def __init__(self,myTasks=[],myEvents=[],wakeup_time=datetime.time(8, 0, 0) , sleep_time=datetime.time(0, 0, 0), prefered_function=product_func):
        
        self.myTasks=myTasks
        self.myEvents=myEvents
        self.prefered_function = prefered_function
        self.wakeup_time = wakeup_time
        self.sleep_time = sleep_time

    def addTask(self,newTask):
        
        self.myTasks.append(newTask)
        
    def addEvent(self,newEvent):
        
        self.myEvent.append(newEvent)
        
    def sortTask(self):
        
        sorted_tasks = sorted(self.myTasks, key= self.func_to_use) 

        return sorted_tasks
        
    def updateTasks(self):
        return
    
    def update_preference(self, new_preference): 

        self.prefered_function = new_preference
    
    def update_sleep_time(self, sleep_time): 

        self.sleep_time = sleep_time
    
    def update_wakeup_time(self, wakeup_time): 

        self.wakeup_time = wakeup_time
    

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