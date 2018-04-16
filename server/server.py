'''
Created on 15 апр. 2018 г.

@author: eq
'''

class MyClass(object):
    '''
    classdocs
    '''
    def __init__(self):
        MyClass.message = 'Hello'
        print(id(self))
    
    @classmethod
    def construct(cls):
        heading = input('Input heading: ')
        print(cls.message, heading)
        print(id(cls))
        
    def print_user(self):
        print(id(''))