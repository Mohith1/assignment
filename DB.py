import threading #library to construct high level threading interfaces
import time #used to handle time based functions/applications
from threading import*

dictionary = {} # maps unique key-value pairs 


def create(key,value,runtime=0): # performs create operation in the database
    if key in dictionary:
        print("ERROR: Key already present") # checks for duplicate keys
    else:
        if(key.isalpha()):
            if len(dictionary)<(1024*1020*1024) and value<=(16*1024*1024): 
                if runtime==0:
                    z=[value,runtime]
                else:
                    z=[value,time.time()+runtime]
                if len(key)<=32: 
                    dictionary[key]=z
            else:
                print("ERROR: The memory limit has exceeded ")
        else:
            print("ERROR: Keyname INVALID, it should contain alphabets only, no special characters or numerics allowed")


            
def read(key): # performs read operation in the database
    if key not in dictionary:
        print("ERROR: Enter a valid key, the given key does not exist in DB") 
    else:
        x=dictionary[key]
        if x[1]!=0:
            if time.time()<x[1]: 
                arr=str(key)+":"+str(x[0]) 
                return arr
            else:
                print("ERROR: time_to_live of the",key,"has terminated") 
        else:
            arr=str(key)+":"+str(x[0])
            return arr



def delete(key): # performs delete operation in the database
    if key not in dictionary:
        print("ERROR: Enter a valid key, the given key does not exist in DB") 
    else:
        x=dictionary[key]
        if x[1]!=0:
            if time.time()<x[1]: 
                del dictionary[key]
                print("Key has been deleted")
            else:
                print("ERROR: time_to_live of the",key,"has terminated") 
        else:
            del dictionary[key]
            print("Key has been deleted")



def modify(key,value): # performs modify operation in the database
    x=dictionary[key]
    if x[1]!=0:
        if time.time()<x[1]:
            if key not in dictionary:
                print("ERROR: Enter a valid key, the given key does not exist in DB") 
            else:
                z=[]
                z.append(value)
                z.append(x[1])
                dictionary[key]=z
        else:
            print("ERROR: time_to_live of the",key,"has terminated") 
    else:
        if key not in dictionary:
            print("ERROR: Enter a valid key, the given key does not exist in DB") 
        else:
            z=[]
            z.append(value)
            z.append(x[1])
            dictionary[key]=z
