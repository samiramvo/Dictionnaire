class dictobj(object):
    def __init__(self) :
        self.x='red'
        self.y='Yellow'
        self.z='Green'
    def do_nothing(self):
        pass

test=dictobj()
print(test.__dict__)