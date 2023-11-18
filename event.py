from enum import Enum

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