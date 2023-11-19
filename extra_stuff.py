def scale_to_unit_float(num):
    '''' scaled to the form x.xxxx '''
    # Calculate the scaling factor to represent num in x.xxx format
    magnitude = len(str(abs(num)).split('.')[0])
    scale_factor = 10 ** (magnitude - 1)  # Calculate the scale factor dynamically
    scaled_num = num / scale_factor
    return scaled_num

def weighted_sort(t):
    priority_weight = 3
    deadline_weight = 4
    
    normalized_priority = t.priority.value/5        # normalized by max priority 
    normalized_remaining_time = scale_to_unit_float(t.time_remaing_to_deadline())

    priority_score = t.priority.value * priority_weight
    deadline_score = -t.time_remaining_to_deadline() * deadline_weight
    return priority_score + deadline_score

def sum_func_opt_both(t):
    priority_weight = 1
    time_remaining_weight = -1
    normalized_priority = t.priority.value/5        # normalized by max priority 
    normalized_time_remaining = t.time_remaining_to_deadline() / (15*4*24) # normalized by (1 day) # could change to max deadline
    combined_score = (normalized_time_remaining + time_remaining_weight)/(normalized_priority + priority_weight)  
    print(combined_score)
    return combined_score

def sum_func_opt_deadline(t):
    priority_weight = 1
    time_remaining_weight = 5 # deadline weight
    normalized_priority = t.priority.value/5        # normalized by max priority 
    normalized_time_remaining = t.time_remaining_to_deadline() / (15*4*24) # normalized by (1 day) # could change to max deadline
    combined_score = (normalized_time_remaining + time_remaining_weight)/(normalized_priority + priority_weight)  
    print(combined_score)
    return combined_score

def sum_func_opt_priotity(t):
    priority_weight = 5 
    time_remaining_weight = 1
    normalized_priority = t.priority.value/5        # normalized by max priority 
    normalized_time_remaining = t.time_remaining_to_deadline() / (15*4*24) # normalized by (1 day) # could change to max deadline
    combined_score = (normalized_time_remaining + time_remaining_weight)/(normalized_priority + priority_weight)  
    print(combined_score)
    return combined_score


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
    
    
def update_preference(self, new_preference): 

    self.prefered_function = new_preference
    
def update_sleep_time(self, sleep_time): 

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
    
def update_wakeup_time(self, wakeup_time): 
    self.wakeup_time = wakeup_time

#product_func = lambda x: x.priority.value *  x.time_remaining_to_deadline()
#sum_func_opt_deadline = lambda x: -(2*x.time_remaining_to_deadline()/x.priority.value)
#sum_func_opt_priotity = lambda x: -(0.5*x.time_remaining_to_deadline()/x.priority.value)
#sum_func_opt_both     = lambda x: -(x.time_remaining_to_deadline()/x.priority.value)

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