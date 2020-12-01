import threading 
from threading import*
import time

d={}
def create(key,value,timeout=0):
    if key in d:
        print("error: this key exists")
    else:
        if(key.isalpha()):
            if len(d)<(1024*1020*1024) and value<=(16*1024*1024): 
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(key)<=32: 
                    d[key]=l
            else:
                print("error: Excedded memory limit ")
        else:
            print("error: Invalid keyname it must contain only alphabets ")
def read(key):
    if key not in d:
        print("error: doesnot exixt. Please enter a valid key")
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]: 
                stri=str(key)+":"+str(b[0])
                return stri
            else:
                print("error: time-to-live of",key,"has expired")
        else:
            stri=str(key)+":"+str(b[0])
            return stri
def delete(key):
    if key not in d:
        print("error: doesnot exist. Please enter a valid key") 
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]:
                del d[key]
                print("key is successfully deleted")
            else:
                print("error: time-to-live of",key,"has expired") 
        else:
            del d[key]
            print("key is successfully deleted")

def modify(key,value):
    b=d[key]
    if b[1]!=0:
        if time.time()<b[1]:
            if key not in d:
                print("error: given key does not exist in database. Please enter a valid key")
            else:
                l=[]
                l.append(value)
                l.append(b[1])
                d[key]=l
        else:
            print("error: time-to-live of",key,"has expired")
    else:
        if key not in d:
            print("error: given key does not exist in database. Please enter a valid key") 
        else:
            l=[]
            l.append(value)
            l.append(b[1])
            d[key]=l
