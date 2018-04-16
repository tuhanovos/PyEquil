'''
Created on 15 апр. 2018 г.

@author: eq
'''
from twisted.python.test.deprecatedattributes import message

class MyClass(object):
    '''
    classdocs
    '''
    def __init__(self, message):
        MyClass.message = message
    
    @classmethod
    def construct(cls):
        heading = input('Input heading: ')
        print(cls.message, heading)
        
    def print_user(self):
        pass