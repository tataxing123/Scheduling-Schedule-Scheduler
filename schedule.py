from event import *
from task import *
from datetime import datetime, time,timedelta
from enum import Enum

ID=0

class SleepingHabits(Enum):
   
    morning = 1
    night = 2
    both = 3

product_func = lambda x: x.priority.value *  x.time_remaining_to_deadline()
sum_func_opt_deadline = lambda x: -(2*x.time_remaining_to_deadline()/x.priority.value)
sum_func_opt_priotity = lambda x: -(0.5*x.time_remaining_to_deadline()/x.priority.value)
sum_func_non_opt      = lambda x: -(x.time_remaining_to_deadline()/x.priority.value)


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

    def addTask(self,title,duration,deadline,priority,task_type,description=""):
        new_task = task(title,duration,deadline,priority,task_type,description)
        new_task.ID=ID
        ID+=1
        self.myTasks.append(new_task)
        
    def addEvent(self,start,end,description="",title="No Title",type=EventType.other,repetition=EventRepetition.once):
        new_event = event(start,end,description,title,type,repetition)
        new_event.ID=ID
        ID+=1
        self.myEvents.append(new_event)
        
    def sortTask(self):
        
        sorted_tasks = sorted(self.myTasks, key=self.prefered_function) 
        self.myTasks = sorted_tasks
    
    def update_preference(self, new_preference): 

        self.prefered_function = new_preference
    
    def update_sleep_time(self, sleep_time): 

        self.sleep_time = sleep_time
    
    def update_wakeup_time(self, wakeup_time): 

        self.wakeup_time = wakeup_time
        
    def greedy_sort(self):
        
        # Sort tasks by descending priority and then by ascending deadline
        sorted_tasks = self.myTasks
        schedule = []
        current_time = datetime.now()

        for task in self.myTasks:
            
            # Check if the task can be scheduled before its deadline
            if current_time + timedelta(hours=task.duration) <= task.deadline:
                
                # Check for overlapping events and sleep time
                while any(event.start_time <= current_time < event.end_time for event in self.myEvents) or (current_time + timedelta(hours=task.duration)) > self.sleep_time:
                    
                    # Move the current time to the end of the conflicting event or sleep time
                    current_time = min(event.end_time for event in self.myEvents if event.start_time <= current_time < event.end_time) if any(event.start_time <= current_time < event.end_time for event in self.myEvents) else self.sleep_time

                # Check if the task needs to be split
                if task.duration > (self.sleep_time - current_time):
                    # Calculate the remaining duration for the second part of the task
                    remaining_duration = task.duration - (self.sleep_time - current_time)

                    # Schedule the first part of the task
                    schedule.append((current_time, self.sleep_time))
                    current_time = self.sleep_time

                    # Create a new task for the second part
                    new_task = task(title=task.title,duration=remaining_duration, deadline=task.deadline)
                    new_task.priority = task.priority
                    sorted_tasks.append(new_task)

                    # Sort the tasks again after adding the new task
                    sorted_tasks = sorted(sorted_tasks, key=lambda x: (x.priority, x.deadline), reverse=True)
                else:
                    # Schedule the entire task
                    schedule.append((current_time, current_time + task.duration))
                    current_time += task.duration
                    
        return schedule


    def __str__(self):
        for this_task in self.myTasks:
            print(this_task)
        
if __name__ == "__main__":


    greedy_sort=task("Complete greedy sort",60, datetime(2023,11,19, 12,00),Priority.very_high,TaskType.school)
    convert_to_js=task("Covert Code to JS",60, datetime(2023,11,19, 12,00),Priority.high,TaskType.school)
    send_email=task("Send email",15, datetime(2023,11,18,22,00),Priority.low,TaskType.school,"send an email to the guidance counselor about course selection")
    buy_bd_gift=task("Buy B-Day Gift",60, datetime(2023,11,19,15,00),Priority.neutral,TaskType.personal)
    
    task1=[greedy_sort,convert_to_js,send_email,buy_bd_gift]
    
    supper=event(datetime(2023,11,18,19,00),datetime(2023,11,18,20,00),"FOOD!","Supper",EventType.personal,EventRepetition.everyday)
    workout=event(datetime(2023,11,18,22,00),datetime(2023,11,18,22,30),"GRIND :)!","Workout",EventType.personal,EventRepetition.weekly)
    breakfast=event(datetime(2023,11,19,9,30),datetime(2023,11,17,10,00),"MORE FOOD!","Breakfast",EventType.personal,EventRepetition.everyday)
    event1=[supper,workout,breakfast]

    my_schedule=Schedule(task1,event1,time(7, 0, 0),time(23, 0, 0), sum_func_non_opt)
    
    fs = [sum_func_non_opt, sum_func_opt_deadline, sum_func_opt_priotity]
    for f in fs: 
        print('----------')
        my_schedule.sortTask()
        designed_schedule=my_schedule.greedy_sort()
        for my_life in designed_schedule:
            print(my_life)
                

    
    
    
    
    # print(t1.time_remaining_to_deadline())
    # print(t1.time_remaining_to_deadline()/t1.priority.value)
    # print(t2.time_remaining_to_deadline())
    # print(t2.time_remaining_to_deadline()/t2.priority.value)
    # print(t3.time_remaining_to_deadline())
    # print(t3.time_remaining_to_deadline()/t3.priority.value)
    # print(t4.time_remaining_to_deadline())
    # print(t4.time_remaining_to_deadline()/t4.priority.value)
    