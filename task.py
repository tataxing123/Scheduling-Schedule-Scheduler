from enum import Enum
from datetime import datetime
import schedule

class Priority(Enum):
    
    very_high = 4
    high = 3
    neutral = 2
    low = 1
    
class TaskType(Enum):
    
    school = 1
    work = 2
    personal = 3
    errands = 4
    other = 5

 
class task:
    
    def __init__(self,title,duration,deadline,priority,task_type,description=""):
        
        self.duration=duration
        self.priority=priority
        self.description=description
        self.title=title
        self.task_type=task_type
        self.deadline=deadline
        self.start_time=None
        self.end_time=None
        self.ID=0
        
    def updateStart_End_Time(self,start,end):
        self.start_time=start
        self.end_time=end
        
    def updateDuration(self,remainingDuration):
        
        self.duration=remainingDuration
        
    def updatePriority(self):
        
        self.priority=Priority(self.priority.value+1)

    def time_remaining_to_deadline(self): 
        return (self.deadline-datetime.now()).total_seconds() / 900
        
    def __str__(self) -> str:
        
        return f'''{self.title} is a {self.task_type.name} task about {self.description}. Its gonna take {self.duration} min and has {self.priority.name} priority. It's due on {self.deadline} and done task at {self.start_time}'''
        
        
if __name__ == "__main__":
    
    t1=task(60,Priority.very_high,TaskType.school,datetime(2023,12,20,14,30))
    
    t1.updateDuration(30)
    print(t1.priority.value)
    
    t1.updatePriority()
    print(t1.priority.value)
    
    print(t1)