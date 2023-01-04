class Project():
    favs = [] #class

    def __init__(self, title, details,total_target,start_time,end_time):
        self.title = title
        self.details = details
        self.total_target = total_target
        self.start_time = start_time
        self.end_time = end_time

    # def is_short(self):
    #     if self.pages < 100:
    #         return True

    #What happens when you pass object to print?
    def __str__(self):
        return f"{self.title}, {self.details}, {self.total_target} {self.start_time} {self.end_time} "

    #What happens when you use ==?
    def __eq__(self, other):
        if(self.title == other.title and self.details == other.details and self.total_target == other.total_target and self.start_time == other.start_time and self.end_time == other.end_time):
            return True
    
    #It's appropriate to give something for __hash__ when you override __eq__
    # #This is the recommended way if mutable (like it is here):
    __hash__ = None

    def __repr__(self): #added to make list of items invoke str
        return self.__str__()