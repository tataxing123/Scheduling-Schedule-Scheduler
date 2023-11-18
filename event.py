from enum import Enum
from datetime import datetime

class EventType(Enum):
    
    social = 1
    school = 2
    work = 3
    personal = 4
    appointments = 5
    other = 6
    
class EventRepetition(Enum):
    
    weekly = 1
    weekday = 2
    weekend = 3
    once = 4
    
    
class event:

    def __init__(self,start,end,description="",title="No Title",type=EventType.other,repetition=EventRepetition.once):
        
        self.start=start
        self.end=end
        self.description=description
        self.title=title
        self.type=type
        self.repetition=repetition
        
        
    def updateStartEnd(self, start_year, start_month, start_day, start_hour, start_minute, end_year, end_month, end_day, end_hour, end_minute):
        self.start = datetime(start_year, start_month, start_day, start_hour, start_minute)
        self.end = datetime(end_year, end_month, end_day, end_hour, end_minute)
        
    def __str__(self) -> str:
        
        return (
            f'''{self.title} is a {self.type.name} task about {self.description}. 
            It starts on {self.start.hour}:{self.start.minute} on {self.start.month}/{self.start.day} 
            It ends at {self.end.hour}:{self.end.minute} on {self.end.month}/{self.end.day}. 
            It occurs {self.repetition.name}''')
        
        
if __name__ == "__main__":
    
    start=datetime(2023,11,17,14,30)
    end=datetime(2023,11,17,15,30)
    
    e1=event(start,end,"Finish Assignment 4 for COMP 251","Assignment 4",EventType.personal,EventRepetition.once)
    
    print(e1)
    
    e1.updateStartEnd(2023,12,17,14,30,2023,12,17,15,30)
    
    print(e1)

