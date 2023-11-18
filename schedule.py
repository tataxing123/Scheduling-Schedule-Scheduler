from task import task
from event import event
from task import Priority
from task import TaskType
from datetime import datetime, time
from enum import Enum


product_func = lambda x: x.priority.value *  x.time_remaining_to_deadline()
sum_func_opt_deadline = lambda x: -(2*x.time_remaining_to_deadline()/x.priority.value)
sum_func_opt_priotity = lambda x: -(0.5*x.time_remaining_to_deadline()/x.priority.value)
sum_func_opt_both     = lambda x: -(x.time_remaining_to_deadline()/x.priority.value)


class Schedule:

    def __init__(self,myTasks=[],myEvents=[],wakeup_time=None, sleep_time=None, prefered_function=product_func):
    

        self.myTasks=myTasks
        self.myEvents=myEvents
        self.prefered_function = prefered_function
        self.wakeup_time = wakeup_time
        self.sleep_time = sleep_time
        
        if wakeup_time is None:  
            self.wakeup_time = time(8, 0, 0)
        else : 
            self.wakeup_time = wakeup_time

        if sleep_time is None:    
            self.sleep_time = time(0, 0, 0)
        else : 
            self.sleep_time = sleep_time

    def addTask(self,newTask):
        
        self.myTasks.append(newTask)
        
    def addEvent(self,newEvent):
        
        self.myEvent.append(newEvent)
        
    def sortTask(self):
        
        sorted_tasks = sorted(self.myTasks, key=self.prefered_function) 
        self.myTasks = sorted_tasks
    
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


    t1=task("t1",60, datetime(2023,11,18, 22,00),Priority.low,TaskType.school)
    t2=task("t2",60, datetime(2023,11,18, 22,00),Priority.very_high,TaskType.school)
    t3=task("t3",60, datetime(2023,11,19, 2, 00),Priority.very_high,TaskType.school)
    t4=task("t4",120,datetime(2023,11,20, 19,30),Priority.low, TaskType.school)
    
    t5=task("t1",60, datetime(2023,11,18, 22,00),Priority.low,TaskType.school)
    t6=task("t2",60, datetime(2023,11,18, 23,59),Priority.very_high,TaskType.school)
    t7=task("t3",60, datetime(2023,11,19, 2, 00),Priority.low,TaskType.school)
    t8=task("t4",120,datetime(2023,11,20, 19,30),Priority.low, TaskType.school)
    
    print("t1")
    print(t1.time_remaining_to_deadline())
    print(t1.time_remaining_to_deadline()/t1.priority.value)
    print("t2")
    print(t2.time_remaining_to_deadline())
    print(t2.time_remaining_to_deadline()/t2.priority.value)
    print("t3")
    print(t3.time_remaining_to_deadline())
    print(t3.time_remaining_to_deadline()/t3.priority.value)
    print("t4")
    print(t4.time_remaining_to_deadline())
    print(t4.time_remaining_to_deadline()/t4.priority.value)
    
    # title,duration,deadline,priority,type,description
    test1=[t1,t2,t3,t4]

    fs = [sum_func_non_opt, sum_func_opt_deadline, sum_func_opt_priotity]
    for f in fs: 
        print('----------')
        mySchedule=Schedule([t1,t2,t3,t4],[],prefered_function=f)
        mySchedule.sortTask()
        for something in mySchedule.myTasks:
                print(something)