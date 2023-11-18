from task import task
from event import event
from task import Priority
from task import TaskType
from datetime import datetime, time
from enum import Enum


def sort_by_priority_then_deadline(t):
    return (t.priority.value, - t.time_remaining_to_deadline())
    
def sort_by_deadline_then_priority(t):
    return (- t.time_remaining_to_deadline(), t.priority.value)



class Schedule:

    def __init__(self,myTasks=[],myEvents=[],wakeup_time=None, sleep_time=None, prefered_function=sum_func_opt_both):
    

        self.myTasks=myTasks
        self.myEvents=myEvents
        self.prefered_function = prefered_function
        self.wakeup_time = wakeup_time
        self.sleep_time = sleep_time
        self.unique_task_names = set()
        self.unique_event_names = set()

        if wakeup_time is None:  
            self.wakeup_time = time(8, 0, 0)
        else : 
            self.wakeup_time = wakeup_time

        if sleep_time is None:    
            self.sleep_time = time(0, 0, 0)
        else : 
            self.sleep_time = sleep_time

    def addTask(self,newTask):
        og_len = len(self.unique_task_names)
        self.unique_task_names.add(newTask.title) 
        new_len = len(self.unique_task_names)
        if og_len == new_len: 
            self.myTasks.append(newTask)
            return True
        return False 

        
    def addEvent(self,newEvent):
        og_len = len(self.unique_event_names)
        self.unique_event_names.add(newEvent.title) 
        new_len = len(self.unique_event_names)
        if og_len == new_len: 
            self.myEvent.append(newEvent)
            return True
        return False 
        
    def get_num_tasks(self): 
        return len(self.myTasks)
    
    def get_num_events(self): 
        return len(self.myTasks)

    def sortTask(self):
        
        self.myTasks = sorted(self.myTasks, key=self.prefered_function) 
    
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
    
    t5=task("t5",60, datetime(2023,11,19, 22,00),Priority.low,TaskType.school)
    t6=task("t6",60, datetime(2023,11,18, 23,59),Priority.very_high,TaskType.school)
    t7=task("t7",60, datetime(2023,11,19, 2, 00),Priority.low,TaskType.school)
    t8=task("t8",120,datetime(2023,11,20, 19,30),Priority.high, TaskType.school)

    all_tasks = [t1,t2,t3,t4,t5,t6,t7,t8]

    #print("t1")
    #print(t1.time_remaining_to_deadline())
    #print(t1.time_remaining_to_deadline()/t1.priority.value)
    #print("t2")
    #print(t2.time_remaining_to_deadline())
    #print(t2.time_remaining_to_deadline()/t2.priority.value)
    #print("t3")
    #print(t3.time_remaining_to_deadline())
    #print(t3.time_remaining_to_deadline()/t3.priority.value)
    #print("t4")
    #print(t4.time_remaining_to_deadline())
    #print(t4.time_remaining_to_deadline()/t4.priority.value)
    #
#
    ## title,duration,deadline,priority,type,description
    #test1=[t1,t2,t3,t4]
#
    fs = [sort_by_priority_then_deadline, sort_by_deadline_then_priority]
    for f in fs: 
        print('----------')
        mySchedule=Schedule(all_tasks,[],prefered_function=f)
        mySchedule.sortTask()
        for something in mySchedule.myTasks:
                print(something, something.time_remaining_to_deadline())
