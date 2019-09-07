
from watson_bots_communicator.core.watson import Watson


class BaseBot(object):
    
    def __init__(self):
        
        self.watson = Watson()
        
    
    def register(self):
        raise NotImplementedError('class %s' % self.__class__.__name__)
        