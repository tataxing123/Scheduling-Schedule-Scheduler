from enum import Enum

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
    
    def __init__(self,duration,priority=Priority.low,description="",title="No Title",type=TaskType.other):
        
        self.duration=duration
        self.priority=priority
        self.description=description
        self.title=title
        self.type=type
        
    def updateDuration(self,remainingDuration):
        
        self.duration=remainingDuration
        
    def updatePriority(self):
        
        self.priority=Priority(self.priority.value+1)
        
    def __str__(self) -> str:
        print(f" ")
        
        
if __name__ == "__main__":
    
    t1=task(60,Priority.very_high,"Finish Assignment 4 for COMP 251","Assignment 4",TaskType.school)
    
    t1.updateDuration(30)
    print(t1.priority.value)
    
    t1.updatePriority()
    print(t1.priority.value)
    
    print(t1)