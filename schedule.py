from event import *
from task import *
from datetime import datetime, time,timedelta
from enum import Enum
from collections import deque
import pandas as pd

ID=0

def sort_by_priority_then_deadline(t):
    return (t.priority.value, - t.time_remaining_to_deadline())
    
def sort_by_deadline_then_priority(t):
    return (- t.time_remaining_to_deadline(), t.priority.value)

class Schedule:

    def __init__(self,myTasks=[],myEvents=[],wakeup_time=None, sleep_time=None, prefered_function=sort_by_priority_then_deadline):

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
            self.sleep_time = time(23, 0, 0)
        else : 
            self.sleep_time = sleep_time
        
    def __str__(self):
        
        for this_task in self.myTasks:
            print(this_task)
        
    def get_first_upcomming_event(self,curr_time):
        
        filtered_events = [event for event in self.myEvents if event.start > curr_time]
        
        if len(filtered_events) == 0 :
            return None
        
        return min(filtered_events, key=lambda event: event.start)
        
    # Splits a task into two tasks
    def split(self,this_task,duration,curr_time):
        
        duration = duration.total_seconds() / 60
        new_task = None
        old_task=task(this_task.title,duration,this_task.deadline,this_task.priority,this_task.task_type,this_task.description)
        old_task.updateStart_End_Time(curr_time,curr_time + timedelta(hours=old_task.duration))
        
        if this_task.duration!=duration:
            new_task=task(this_task.title,(this_task.duration-duration),\
                this_task.deadline,this_task.priority,this_task.task_type,this_task.description)
        
        return old_task,new_task
        
    def sortTask(self):
        
        self.myTasks = sorted(self.myTasks, key=self.prefered_function) 
        
    def sortEvent(self):
        
        self.myEvents = sorted(self.myEvents, key=lambda event: event.start)
    
    # if a task is not complete before the deadline: Throw this
    def notify_task_incompete(): 

        print("Task is incomplete. Do better next time!")
        
    # returns the time in which the schedule is available for tasks
    def jump_to_valid(self,curr_time):
        
        curr_time_time = curr_time.time()
        
        while(True):
            
            # if curr_time overlap with any events
            if any(event.start <= curr_time < event.end for event in self.myEvents):
                
                curr_time = min(event.end for event in self.myEvents if event.start <= curr_time < event.end) 
                
            
            # if curr_time overlap with sleeping schedule
            if curr_time_time >= self.sleep_time or curr_time_time < self.wakeup_time:
                
                curr_time = datetime.combine(curr_time.date(), self.wakeup_time)
                
                # before midnight then need to add date
                if curr_time_time>=self.sleep_time:
                    
                    # Increment the date by one day
                    curr_time += timedelta(days=1)
                    curr_time_time = curr_time.time()
                    
            if not (curr_time_time >= self.sleep_time and curr_time_time < self.wakeup_time ) and not(any(event.start <= curr_time < event.end for event in self.myEvents)) :  
                break
            
        return curr_time
    
    def deadline_in_available_duration(self,available_duration,first_upcomming_event,sorted_tasks,curr_time,breaked):

        for i in range(3): 
            
            # if one of top 3 's deadline is within available duration
            if sorted_tasks[i].deadline < first_upcomming_event.start :
                
                picked_task = sorted_tasks[i]
                old, new = self.split(picked_task, available_duration,curr_time) 
                old.updateStart_End_Time(curr_time,curr_time+timedelta(hours=old.duration))
                schedule.append(old)
                # if the task is not completed after deadline: throw notification
                # TODO: if not (new is None) : self.notify_task_incompete()
                curr_time += old.duration
                curr_time = self.jump_to_valid(curr_time)
                sorted_tasks.pop(i)
                breaked = True
                break
            
        return available_duration,first_upcomming_event,sorted_tasks,curr_time,breaked
    
    def find_fit(self,available_duration,sorted_tasks,curr_time,breaked,schedule):
        
        # else if one of top 3 fits properly
        for i in range(3): 

            if sorted_tasks[i].duration <= (available_duration.total_seconds() / 60): 
                picked_task = sorted_tasks[i]
                sorted_tasks.pop(i)
                schedule.append(picked_task)
                picked_task.updateStart_End_Time(curr_time,curr_time+timedelta(hours=picked_task.duration))
                curr_time += timedelta(hours=picked_task.duration)
                curr_time = self.jump_to_valid(curr_time)
                break
            
        return available_duration,sorted_tasks,curr_time,breaked,schedule
    
    def add_until_sleep_time(self,sorted_tasks,curr_time,schedule):
        
        i=0
        while (len(sorted_tasks)!=0):
            
            this_task = sorted_tasks.pop(i)
            # available_duration is in delta
            available_duration = abs(datetime.combine(curr_time.date(), self.sleep_time)-curr_time)
            
            # if we have to split: the tack's duration is longer or equal to the available duration
            if this_task.duration >= int(available_duration.total_seconds()/60):
                
                old, new = self.split(this_task, available_duration,curr_time)
                old.updateStart_End_Time(curr_time,curr_time+timedelta(minutes=this_task.duration))
                curr_time += timedelta(minutes=old.duration) 
                curr_time = self.jump_to_valid(curr_time)
                schedule.append(old)
                sorted_tasks.insert(i,new)

            else:
                schedule.append(this_task)
                this_task.updateStart_End_Time(curr_time,curr_time+timedelta(minutes=this_task.duration))
                curr_time += timedelta(hours=this_task.duration)
                curr_time = self.jump_to_valid(curr_time)
                i+=1
 
        return schedule  

    # Our Algorithm :)
    def greedy_sort(self): 
        
        self.sortTask()
        sorted_tasks=self.myTasks.copy()
        
        self.sortEvent()
        schedule = []
        
        curr_time = datetime.now()
    
        while (len(sorted_tasks)!=0):
            
            curr_time=self.jump_to_valid(curr_time)
            first_upcomming_event = self.get_first_upcomming_event(curr_time)

            # Get to The Last Event: we are done and we can return the schedule
            if first_upcomming_event == None:
                i=0
                while (len(sorted_tasks)!=0):
                    this_task = sorted_tasks.pop(0)
                    #print(this_task)
                    # available_duration is in delta
                    available_duration = abs(datetime.combine(curr_time.date(), self.sleep_time)-curr_time)
                    
                    # if we have to split: the tack's duration is longer or equal to the available duration
                    if this_task.duration >= int(available_duration.total_seconds()/60):
                        
                        old, new = self.split(this_task, available_duration,curr_time)
                        old.updateStart_End_Time(curr_time,curr_time+timedelta(minutes=this_task.duration))
                        curr_time += timedelta(minutes=old.duration) 
                        curr_time = self.jump_to_valid(curr_time)
                        schedule.append(old)
                        sorted_tasks.insert(0,new)

                    else:
                        schedule.append(this_task)
                        this_task.updateStart_End_Time(curr_time,curr_time+timedelta(minutes=this_task.duration))
                        curr_time += timedelta(hours=this_task.duration)
                        curr_time = self.jump_to_valid(curr_time)
                        i+=1
                        
                return schedule
            
            available_duration = first_upcomming_event.start - curr_time
            print(available_duration.total_seconds()/60)
            breaked = False # to keep the structure
            
            # if one of top 3 's deadline is within available duration
            for i in range(3): 
                # if can't complete the task
                if sorted_tasks[i].deadline < first_upcomming_event.start and (sorted_tasks[i].duration > available_duration.total_seconds()/60):
                    picked_task = sorted_tasks[i]
                    old, new = self.split(picked_task, available_duration,curr_time) 
                    old.updateStart_End_Time(curr_time,curr_time+timedelta(minutes=old.duration))
                    schedule.append(old)
                    sorted_tasks.insert(i,new)
                    # if the task is not completed after deadline: throw notification
                    # TODO: if not (new is None) : self.notify_task_incompete()
                    curr_time += timedelta(minutes=old.duration)
                    curr_time = self.jump_to_valid(curr_time)
                    breaked = True
                    break
            
            if breaked : continue 
            
            # else if one of top 3 fits properly
            for i in range(3): 
                
                if sorted_tasks[i].duration <= (available_duration.total_seconds() / 60): 
                    picked_task = sorted_tasks[i]
                    sorted_tasks.pop(i)
                    schedule.append(picked_task)
                    picked_task.updateStart_End_Time(curr_time,curr_time+timedelta(hours=picked_task.duration))
                    curr_time += timedelta(hours=picked_task.duration)
                    curr_time = self.jump_to_valid(curr_time)
                    break
            
                
            if breaked : continue 

            # else pick first priority 
            picked_task = sorted_tasks[0]
            old, new = self.split(picked_task,available_duration,curr_time) 
            old.updateStart_End_Time(curr_time,curr_time+timedelta(minutes=old.duration))
            curr_time += timedelta(minutes=old.duration)
            curr_time = self.jump_to_valid(curr_time)
            if new is not None : sorted_tasks[0] = new 
            else : sorted_tasks.pop(0)
            schedule.append(old)
            

        # end of while 
        return schedule
        
if __name__ == "__main__":


    greedy_sort=task("Complete greedy sort",60, datetime(2023,11,20,12,00),Priority.very_high,TaskType.school)
    convert_to_js=task("Covert Code to JS",60, datetime(2023,11,20, 12,00),Priority.high,TaskType.school)
    send_email=task("Send email",15, datetime(2023,11,19,22,00),Priority.low,TaskType.school,"send an email to the guidance counselor about course selection")
    buy_bd_gift=task("Buy B-Day Gift",60, datetime(2023,11,19,15,00),Priority.neutral,TaskType.personal)
    task1=[greedy_sort,convert_to_js,send_email,buy_bd_gift]
    
    #supper=event(datetime(2023,11,29,19,00),datetime(2023,11,29,20,00),"FOOD!","Supper",EventType.personal,EventRepetition.everyday)
    #workout=event(datetime(2023,11,29,22,00),datetime(2023,11,29,22,30),"GRIND :)!","Workout",EventType.personal,EventRepetition.weekly)
    #breakfast=event(datetime(2023,11,30,9,30),datetime(2023,11,30,10,00),"MORE FOOD!","Breakfast",EventType.personal,EventRepetition.everyday)
    event1=[]
    
    curr_time=datetime(2023,11,19,18,30)
    
    my_schedule=Schedule(task1,event1,time(7, 0, 0),time(23, 0, 0), sort_by_deadline_then_priority)
    #sortesTask=my_schedule.sortTask
    #some_tasks=my_schedule.add_until_sleep_time(my_schedule.myTasks,curr_time,[])
    #for this in some_tasks:
    #   print(this)
    this =  my_schedule.greedy_sort()
    


    d = []
    # Convert the list of tuples to a DataFrame
    for t in this: 
        d.append((t.deadline, t.priority,t.duration, t.start_time, t.end_time))
    # Create a DataFrame from the list of dictionaries
    df = pd.DataFrame(d, columns=['deadline', 'priority','duration', 'start_time', 'end_time'])

    pd.set_option('display.width', 9000)
    pd.set_option('display.max_colwidth', None)  # Display full column width


    # Display the DataFrame
    print(df)

    

    
    
        
   
    