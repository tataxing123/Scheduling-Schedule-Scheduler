from event import *
from task import *
from datetime import datetime, time,timedelta
from enum import Enum

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
        
    def get_first_upcomming_event(self,curr_time):
        
        
    def split(self,this_task,duration):
        
        new_task = None
        old_task=task(this_task.title,duration,this_task.deadline,this_task.priority,this_task.task_type,this_task.description)
        
        if this_task.duration!=duration:
            new_task=task(this_task.title,(this_task.duration-duration),this_task.deadline,this_task.priority,this_task.task_type,this_task.description)
        
        return old_task,new_task
        
    def sortTask(self):
        
        self.myTasks = sorted(self.myTasks, key=self.prefered_function) 
        
    def sortEvent(self):
        
        self.myEvents = sorted(self.myEvents, key=lambda event: event.start)
    
    def update_preference(self, new_preference): 

        self.prefered_function = new_preference
    
    def update_sleep_time(self, sleep_time): 

        self.sleep_time = sleep_time
    def better_greedy_sort(self): 
        self.sortTask()
        sorted_tasks=self.myTasks.copy()
        
        self.sortEvent()  # TODO 
        schedule = []
        
        cur_t = datetime.now()

        while (len(sorted_tasks)!=0):
            first_upcomming_event = self.get_first_upcomming_event() # TODO 
            available_duration = first_upcomming_event - cur_t
            breaked = False
            # if one of top 3 's deadline is within available duration 
            for i in range(3): 
                if sorted_tasks[i].deadline < first_upcomming_event :
                    picked_task = sorted_tasks[i]
                    old, new = self.split(picked_task, available_duration) # TODO 
                    schedule.append(old)
                    if new is None : self.notify_task_incompete() #TODO
                    cur_t += old.duration
                    cur_t = self.jump_to_valide(cur_t)
                    sorted_tasks.pop(i)
                    breaked = True
                    break
            if breaked : continue 

            # else if one of top 3 fits properly 
            for i in range(3): 
                if sorted_tasks[i].duration <= available_duration: 
                    picked_task = sorted_tasks[i]
                    sorted_tasks.pop(i)
                    schedule.append(picked_task)
                    cur_t += picked_task.duration
                    cur_t = self.jump_to_valide(cur_t)
                    break
            if breaked : continue 

            # else pick first priority 
            picked_task = sorted_tasks[0]
            old, new = self.split(picked_task, available_duration) 
            cur_t += old.duration
            cur_t = self.jump_to_valide(cur_t)
            if new is not None : sorted_tasks[0] = new 
            else : sorted_tasks.pop(0)
            schedule.append(old)

        # end of while 
        return schedule
        

                    

    
    def update_wakeup_time(self, wakeup_time): 

        self.wakeup_time = wakeup_time
        
    def jump_to_valide(self,curr_time):
        
        curr_time_time = curr_time.time()
        
        while(True):
            
            # if curr_time overlap with any events
            if any(event.start <= curr_time < event.end for event in self.myEvents):
                
                curr_time = min(event.end for event in self.myEvents if event.start <= curr_time < event.end) 
                curr_time_time = curr_time.time()
            
            # if curr_time overlap with sleeping schedule
            if curr_time_time >= self.sleep_time or curr_time_time < self.wakeup_time:
                
                curr_time = datetime.combine(curr_time.date(), self.wakeup_time)
                
                # before midnight then need to add date
                if curr_time_time < time(0, 0, 0):
                    
                    # Increment the date by one day
                    curr_time += timedelta(days=1)
                    curr_time_time = curr_time.time()
                    
            if not (curr_time_time >= self.sleep_time and curr_time_time < self.wakeup_time ) and not(any(event.start <= curr_time < event.end for event in self.myEvents)) :  
                break
            
        return curr_time

        
    def greedy_sort(self):
        
        self.sortTask()
        # Sort tasks by descending priority and then by ascending deadline
        sorted_tasks = self.myTasks.copy()
        schedule = []
        
        while(len(sorted_tasks)!=0):
            
            current_time = datetime.now()
            task=sorted_tasks.pop()
            print(type(timedelta(minutes=task.duration)))
            duration_in_datetime=timedelta(minutes=task.duration)
            sleep_time_in_datetime=datetime.combine(current_time, self.sleep_time)
            
            # Check if the task can be scheduled before its deadline
            if current_time + duration_in_datetime <= task.deadline:
                
                # Check for overlapping events and sleep time
                while any(event.start <= current_time < event.end for event in self.myEvents) or (current_time + duration_in_datetime) > sleep_time_in_datetime:
                    
                    # Move the current time to the end of the conflicting event or sleep time
                    current_time = min(event.end for event in self.myEvents if event.start <= current_time < event.end) if any(event.start <= current_time < event.end for event in self.myEvents) else self.sleep_time

                # Check if the task needs to be split
                if task.duration > (sleep_time_in_datetime - current_time):
                    
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
                    # Schedule the entire tasks
                    schedule.append((current_time, current_time + task.duration))
                    current_time += task.duration
                    
        return []


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
    breakfast=event(datetime(2023,11,19,9,30),datetime(2023,11,19,10,00),"MORE FOOD!","Breakfast",EventType.personal,EventRepetition.everyday)
    event1=[supper,breakfast,workout]
    

    print(datetime.now() + timedelta(hours=3) <= datetime(2023,11,19, 12,00))
        
        
    my_schedule=Schedule(task1,event1,time(7, 0, 0),time(23, 0, 0), sort_by_deadline_then_priority)
    my_schedule.sortEvent()
    my_schedule.sortTask()
    for this_event in my_schedule.myEvents:
        print(this_event)
        
    #designed_schedule=my_schedule.greedy_sort()


    
            
    # fs = [sort_by_priority_then_deadline, sort_by_deadline_then_priority]
    # for f in fs: 
    #     print('----------')
    #     my_schedule.sortTask()
    #     designed_schedule=my_schedule.greedy_sort()
    #     for my_life in designed_schedule:
    #         print(my_life)
                

    
    
    
    
    # print(t1.time_remaining_to_deadline())
    # print(t1.time_remaining_to_deadline()/t1.priority.value)
    # print(t2.time_remaining_to_deadline())
    # print(t2.time_remaining_to_deadline()/t2.priority.value)
    # print(t3.time_remaining_to_deadline())
    # print(t3.time_remaining_to_deadline()/t3.priority.value)
    # print(t4.time_remaining_to_deadline())
    # print(t4.time_remaining_to_deadline()/t4.priority.value)
    