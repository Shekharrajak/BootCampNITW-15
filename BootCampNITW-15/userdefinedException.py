class ShortlenException(Exception):
    def __init__ (self,len):
        self.len=len

    def msg(self):
        print("the string u r inserted is very short!!:p")

try:
        a=input("enter a string:")
        if(len(a) < 3 ):
            raise ShortlenException(len(a))
except ShortlenException as details :
        print("Error occured : {}".format(details.msg))
