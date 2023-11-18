from enum import Enum
from datetime import datetime

class Priority(Enum):
    
    very_high = 1
    high = 2
    neutral = 3
    low = 4
    
class TaskType(Enum):
    
    school = 1
    work = 2
    personal = 3
    errands = 4
    other = 5

 
class task:
    
    def __init__(self,duration,priority=Priority.low,description="",title="No Title",type=TaskType.other,deadline=datetime(2023,12,30,12,30)):
        
        self.duration=duration
        self.priority=priority
        self.description=description
        self.title=title
        self.type=type
        self.deadline=deadline
        
    def updateDuration(self,remainingDuration):
        
        self.duration=remainingDuration
        
    def updatePriority(self):
        
        self.priority=Priority(self.priority.value+1)
        
    def __str__(self) -> str:
        
        return f'''{self.title} is a {self.type.name} task about {self.description}. Its gonna take {self.duration} min and has {self.priority.name} priority. It's due on {self.deadline}'''
        
        
if __name__ == "__main__":
    
    t1=task(60,Priority.very_high,TaskType.school,datetime(2023,12,20,14,30))
    
    t1.updateDuration(30)
    print(t1.priority.value)
    
    t1.updatePriority()
    print(t1.priority.value)
    
    print(t1)