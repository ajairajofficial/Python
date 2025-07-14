# functions useful for memory management as a embedded systems developer


# These modules are powerful tools for memory management:

# Memory leak detection
# Object lifecycle management 
# Memory usage optimization
# Reference counting analysis
# System resource monitoring


# 1) memory management and monitoring

import psutil # import the psutil module
# psutil (Python System and Process Utilities) is a powerful cross-platform library for retrieving 
# information on running processes and system utilization in Python
import sys # import the sys module. Provide system specific parameters and functions
import gc # import the garbage collector module (automatic memory allocation and deallocation)

# get the current memory usage of the program
#gets real memory usage (Resident set size)
print(psutil.Process().memory_info().rss/1024/1024) # in MB # eg 14.9
# get the virtual memory usage (Virtual memory size)
print(psutil.Process().memory_info().vms/1024/1024) # in MB # eg 14.9
# force garbage collection to free unused memory.
print(gc.collect())
#Shows the number of references to an object.
x=2
print(sys.getrefcount(x)) # eg 21000000 # shows how many reference point to the object x
# why this reference number is so high?
#Python internally maintains an integer cache (typically for integers between -5 and 256) for optimization purposes.
# These small integers are pre-allocated and reused throughout the Python runtime environment. 
# When you create a reference to 2, you're actually getting a reference to this cached value that's already being used by:
# The Python interpreter itself
# Built-in functions and modules
# The integer cache system
# Your current reference
#####################################################################
# CPU Information
import psutil

# CPU usage per core
cpu_per_core = psutil.cpu_percent(percpu=True)
print(f"CPU Usage Per Core: {cpu_per_core}")

# CPU frequency
cpu_freq = psutil.cpu_freq()
print(f"CPU Frequency - Current: {cpu_freq.current:.1f}MHz")
print(f"CPU Frequency - Min: {cpu_freq.min:.1f}MHz")
print(f"CPU Frequency - Max: {cpu_freq.max:.1f}MHz")

# Memory Information
memory = psutil.virtual_memory()
print(f"Total Memory: {memory.total/1024/1024/1024:.2f}GB")
print(f"Available Memory: {memory.available/1024/1024/1024:.2f}GB") 
print(f"Memory Usage: {memory.percent}%")
"""
Important note ::run this code only through python interpreter not through this powershell. it wont work

# Disk Information
disk = psutil.disk_usage('C:\\')
print(f"Total Disk Space: {disk.total/1024/1024/1024:.2f}GB")
print(f"Used Disk Space: {disk.used/1024/1024/1024:.2f}GB")
print(f"Free Disk Space: {disk.free/1024/1024/1024:.2f}GB")

# Network Information
network = psutil.net_io_counters()
print(f"Bytes Sent: {network.bytes_sent/1024/1024:.2f}MB")
print(f"Bytes Received: {network.bytes_recv/1024/1024:.2f}MB")

# Process Information
for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
    try:
        print(proc.info)
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        pass
    """
###########################################################################################################
############################################################################################################
# obect Memory/size Analysis:
from sys import getsizeof
from collections import defaultdict

def get_size(obj, seen=None):
    """Recursively find size of objects and their children"""
    size = getsizeof(obj) # get base size
    if seen is None:   ##Track seen object to avoid cycles 
        seen = set()
    obj_id = id(obj) # get unique object id.
    if obj_id in seen:  # prevent counting same object twice
        return 0
    seen.add(obj_id)
    if hasattr(obj, '__dict__'): # add size of object attributes if it has any
        size += get_size(obj.__dict__, seen)
    return size
number =[1,2,3,4,5,6,7,8,9,10]
size =get_size(number)
print(size) # 136 this is the memory footprint needed to store the 10 integers in bytes
###################################################################
#####################################################################
#install the modules 
# pip install memory_profiler
# pip install psutil
# pip install numpy
#####################################################################
# 2) Memory Profiling

import numpy as np
from memory_profiler import profile

@profile  # Decorator that enables memory profiling.
def data_structure_comparison(n=1000000):
    print("Starting memory analysis...")
    # you can run the memory profiling analysis on your data structures. 
    # The code will track memory usage for each line of the decorated function, 
    # giving you detailed insights into memory consumption patterns.
    # creates and compares memory usage of different data structures
    print("Creating list...")  #list comprehension
    result_list = [i * i for i in range(n)]
    
    print("Creating generator...")  #generator expression
    result_gen = (i * i for i in range(n))
    next(result_gen)
    
    print("Creating NumPy array...")
    result_array = np.arange(n) ** 2
    
    print("Creating dictionary...") #dictionary comprehension
    result_dict = {i: i * i for i in range(n)}
    
    print("Cleaning up...")
    del result_list
    del result_gen
    del result_array
    del result_dict
    
    return "Memory analysis complete"

if __name__ == "__main__":
    result = data_structure_comparison()
    print(result)
##################################################
#Starting memory analysis...
#Creating list...
#Creating generator...
#Creating NumPy array...
#Creating dictionary...
#Cleaning up...
#Filename: c:\Users\ajair\Desktop\Python\Python\core_concepts\3memory management.py

#Line #    Mem usage    Increment  Occurrences   Line Contents
#=============================================================
#    46     58.2 MiB     58.2 MiB           1   @profile         
#    47                                         def data_structure_comparison(n=1000000):
#    48     58.2 MiB      0.0 MiB           1       print("Starting memory analysis...")
#    49
#    50     58.2 MiB      0.0 MiB           1       print("Creating list...")
#    51     96.5 MiB   -844.4 MiB     1000003       result_list = [i * i for i in range(n)]
#    52
#    53     96.5 MiB      0.0 MiB           1       print("Creating generator...")
#    54    169.9 MiB      0.0 MiB           4       result_gen = (i * i for i in range(n))
#    55     96.5 MiB      0.0 MiB           1       next(result_gen)
#    56
#    57     96.5 MiB      0.0 MiB           1       print("Creating NumPy array...")
#    58    104.2 MiB      7.6 MiB           1       result_array = np.arange(n) ** 2
#    59
#    60    104.2 MiB      0.0 MiB           1       print("Creating dictionary...")
#    61    205.6 MiB    101.4 MiB     1000003       result_dict = {i: i * i for i in range(n)}
#    62
#    63    205.6 MiB      0.0 MiB           1       print("Cleaning up...")
#    64    169.9 MiB    -35.7 MiB           1       del result_list
#    65    169.9 MiB      0.0 MiB           1       del result_gen
#    66    162.3 MiB     -7.6 MiB           1       del result_array
#    67     61.2 MiB   -101.0 MiB           1       del result_dict
#    68
#    69     61.2 MiB      0.0 MiB           1       return "Memory analysis complete"


#Memory analysis complete

# just a short explanation
#Let me break down what's happening in this memory profiling 
#output:

#Initial Memory State:
#Program starts with 58.2 MiB of memory usage
#This is your base Python environment memory footprint
#List Creation (Line 51):
#Memory jumps to 96.5 MiB
#Creates 1 million squared numbers in a list
#Shows 1,000,003 occurrences (loop iterations)
#Generator Creation (Lines 54-55):
#Temporarily spikes to 169.9 MiB
#Generator itself is memory efficient
#next() function just gets first value
#NumPy Array (Line 58):
#Increases by 7.6 MiB
#More memory efficient than the list
#Better for numerical operations
#Dictionary Creation (Line 61):
#Biggest memory jump to 205.6 MiB
#Additional 101.4 MiB used
#Dictionaries need more memory for hash tables
#Cleanup Phase (Lines 64-67):
#del result_list: Frees 35.7 MiB
#del result_array: Releases 7.6 MiB
#del result_dict: Recovers 101.0 MiB
#Final memory usage: 61.2 MiB
#Key Insights:

#Dictionaries use most memory
#NumPy arrays are memory efficient
#Generators use minimal memory
#Python's garbage collection works effectively
#The 'Occurrences' column shows how many times each line executed, 
# helping track loops and iterations.
########################################################
# 4) Array Memory Management (using NumPy):
import numpy as np

# First create a sample array to work with
original_array = np.array([1, 2, 3, 4, 5], dtype='float64')

# Create memory-mapped array
mmap_array = np.memmap('array.dat', dtype='float64', mode='w+', shape=(1000,))

# Zero-copy array operations
view_array = np.asarray(original_array)

# Let's verify our arrays
print("Original array:", original_array)
print("Memory-mapped array (first 5 elements):", mmap_array[:5])
print("View array:", view_array)

# You can also write to the memory-mapped array
mmap_array[:5] = original_array
mmap_array.flush()  # Save changes to disk
## output:
#Original array: [1. 2. 3. 4. 5.]
#Memory-mapped array (first 5 elements): [0. 0. 0. 0. 0.]
#View array: [1. 2. 3. 4. 5.]
#################################################################
####################################################################
import numpy as np
import tempfile
import os

# Create a temporary file path that's guaranteed to work
temp_dir = tempfile.gettempdir()
file_path = os.path.join(temp_dir, 'array.dat')

# Create arrays
original_array = np.array([1, 2, 3, 4, 5], dtype='float64')
mmap_array = np.memmap(file_path, dtype='float64', mode='w+', shape=(1000,))

# Copy data to memory-mapped array
mmap_array[:5] = original_array
mmap_array.flush()  # Save to disk

print("Original array:", original_array)
print("Memory-mapped array (first 5 elements):", mmap_array[:5])
print("View array:", np.asarray(original_array))

# Clean up
del mmap_array  # Close the memmap
os.remove(file_path)  # Remove the temporary file

# output:
# Original array: [1. 2. 3. 4. 5.]
# Memory-mapped array (first 5 elements): [1. 2. 3. 4. 5.]
# View array: [1. 2. 3. 4. 5.]
# this version uses:

#Uses system's temp directory
#Handles file cleanup
#Guarantees write permissions
#Works across all operating systems
#The code will now run smoothly and demonstrate memory mapping effectively!
#################################################################
####################################################################
import numpy as np

# Create a larger original array
original_array = np.arange(1000, dtype='float64')

# Create memory-mapped array
mmap_array = np.memmap('large_array.dat', dtype='float64', mode='w+', shape=(1000,))

# Fill with meaningful data
mmap_array[:] = original_array * 2  # Multiply all values by 2
mmap_array.flush()

print("First 5 elements:", mmap_array[:5])
print("Last 5 elements:", mmap_array[-5:])

# output:
#First 5 elements: [0. 2. 4. 6. 8.]
#Last 5 elements: [1990. 1992. 1994. 1996. 1998.]

#This version shows how memory-mapped arrays can handle larger datasets
#efficiently by storing them on disk while allowing you to work with them
#as if they were in memory. This is particularly useful for 
#embedded systems where RAM might be limited!

#################################################################
#resource utilisation

# pip install psutil

import psutil
import os

# Get current process
process = psutil.Process(os.getpid())

# Get memory info
memory_info = process.memory_info()

# Print current memory usage
print(f"Memory usage: {memory_info.rss / 1024 / 1024:.2f} MB")

# Get system memory limits
virtual_memory = psutil.virtual_memory()
print(f"Total system memory: {virtual_memory.total / 1024 / 1024:.2f} MB")
print(f"Available memory: {virtual_memory.available / 1024 / 1024:.2f} MB")
print(f"Memory percentage used: {virtual_memory.percent}%")

# Get CPU usage
print(f"CPU Usage: {psutil.cpu_percent()}%")


#################################################################
# 6) Buffer Management 
from array import array
import ctypes

# Create fixed-size buffer
buffer = array('i', [0] * 1000)
print(f"Buffer type: {type(buffer)}")
print(f"Buffer length: {len(buffer)}")
print(f"Buffer size in bytes: {buffer.itemsize * len(buffer)}")

# Direct memory access
ptr = (ctypes.c_int * len(buffer)).from_buffer(buffer)
print(f"Pointer address: {ctypes.addressof(ptr)}")
###############################################################
# 7) Cache Management:

from functools import lru_cache

#Cache is a high-speed temporary storage layer that holds frequently accessed 
#data so it can be retrieved quickly later. Let me explain with the code example:
@lru_cache(maxsize=128) # The maxsize parameter sets the maximum number of items the cache can hold.
def expensive_computation(n):
    return n * n # imagine this is a computationally expensive function

# Test cache behavior
print(f"Cache info before: {expensive_computation.cache_info()}")
expensive_computation(5)
expensive_computation(5)  # This will be cached
print(f"Cache info after: {expensive_computation.cache_info()}")

#Key points about caching:

#Speeds up programs by storing results of expensive operations
#Reduces computational load by avoiding repeat calculations
#Trades memory for speed
#Common uses include:
#Database query results
#Web page content
#Complex mathematical calculations
#Frequently accessed files
#The @lru_cache decorator in Python implements a Least Recently Used (LRU) 
#cache strategy, which automatically removes the least recently used items 
#when the cache reaches its size limit.


# 8) system Information:

import platform
import os

# Get system details
# Print detailed system info
print(f"Architecture: {platform.architecture()}")
print(f"Machine: {platform.machine()}")
print(f"CPU Count: {os.cpu_count()}")
print(f"Total Memory (GB): {psutil.virtual_memory().total / (1024**3):.2f}")
print(f"Platform: {platform.platform()}")
print(f"Python Version: {platform.python_version()}")

# These functions are particularly useful for:

#Memory optimization
#Performance monitoring
#Resource management
#System profiling
#Buffer operations
#Cache control
#Memory mapping
#System diagnostics
#Additional Tips:
##############################################################################
#Use array module for homogeneous data instead of lists
#Implement context managers for resource cleanup
#Use generators for memory-efficient iteration
#Consider using __slots__ for classes to reduce memory overhead
#Utilize weakref for creating weak references to avoid memory leaks
#These tools help in creating efficient, resource-aware Python applications 
# for embedded systems!
#use the array module for homogeneous data instead of lists
from array import array
numbers = array('i', [1, 2, 3, 4, 5])  # More memory efficient than list for integers

# 1. Array vs List Comparison
from array import array
numbers_array = array('i', [1, 2, 3, 4, 5])
numbers_list = [1, 2, 3, 4, 5]
print(f"Memory size of array: {sys.getsizeof(numbers_array)} bytes")
print(f"Memory size of list: {sys.getsizeof(numbers_list)} bytes")

# 2. Context Manager Monitoring
class ResourceManager:
    def __enter__(self):
        print("Resource acquired")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Resource cleaned up")

with ResourceManager():
    print("Working with resource")

# 3. Generator for Memory Efficiency
def number_generator(n):
    print(f"Starting generator with n={n}")
    for i in range(n):
        print(f"Yielding value: {i}")
        yield i

gen = number_generator(5)
print(f"Generator object size: {sys.getsizeof(gen)} bytes")
for num in gen:
    print(f"Using generated value: {num}")

# 4. Using slots for reducing memory
class EfficientClass:
    __slots__ = ['name', 'value']  # Restricts attributes and reduce memory
    def __init__(self, name, value):
        self.name = name
        self.value = value

regular_obj = EfficientClass("test", 100)
print(f"Memory of slotted object: {sys.getsizeof(regular_obj)} bytes")

# 5. WeakRef Demonstration for avoiding memory leaks
import weakref

class Cache:
    def __init__(self):
        self.data = weakref.WeakKeyDictionary()
        print("Created WeakKeyDictionary")
    
    def add_item(self, key, value):
        self.data[key] = value
        print(f"Added item with key: {key}")
        print(f"Current cache size: {len(self.data)}")

# Create a class that can be weakly referenced
class DataObject:
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return f"DataObject({self.name})"

cache = Cache()
# Create an object that supports weak references
test_obj = DataObject("test_data")
cache.add_item(test_obj, "value")
print(f"Cache contents before deletion: {len(cache.data)}")
del test_obj
print(f"Cache contents after deletion: {len(cache.data)}")


#This code will work because:

#DataObject instances can be weakly referenced
#The WeakKeyDictionary will automatically remove entries when their keys are deleted
#We can track the cache size before and after deletion

#Objects that support weak references include:
#Custom class instances
#Functions
#Methods
#Sets
#Other object types that inherit from 'object'
#######################################################################################