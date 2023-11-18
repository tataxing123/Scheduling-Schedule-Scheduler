import task as t
import event as e

class Schedule:
    
    def __init__(self,myTasks=[],myEvents=[]):
        
        self.myTasks=myTasks
        self.myEvents=myEvents
    
    def addTask(self,newTask):
        self.myTasks.append(newTask)
        
    def addEvent(self,newEvent):
        self.myEvent.append(newEvent)