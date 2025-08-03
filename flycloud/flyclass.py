

class MyBaseClass(object):
    def __init__(self):
        self.my_type="base"
    def do_something(self,fname):
        pass

class GCPFly(MyBaseClass):
    def __init__(self):
        self.my_type="gcp1"
    def do_something(self,fname):
        print("2"+self.my_type+fname)


class AWSFly(MyBaseClass):
    def __init__(self):
        self.my_type="aws1"
    def do_something(self,fname):
        print("3"+self.my_type+fname)
