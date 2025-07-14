############################################################################

#                    Stacks and Queue
#                    FILO   and FIFO data structure

############################################################################
# Stacks and queues are simple yet powerful data structure that
# help you deal with a variety of situations where
# some ordered operation or logic is needed and your data fits neatly into
# the stack or queue analogy.

############################################################################

# Adding and Removing items in list using
# 1) append                  @ add
# 2) pop                     @ remove

############################################################################

#                           stacks

# behaviour is  Last In First Out data structure
# Example is like browser
# basically we can use a list of objects as stack

from collections import deque  # importing for queue object
browsing_section = []
browsing_section.append(1)
browsing_section.append(1.1)
browsing_section.append("one.two")
browsing_section.append(2)  # takes only one argument at a time
print(browsing_section)
print("Redirect browsing section to last object {}".format(
    browsing_section[-1]))

print(f"poping the last object {browsing_section.pop()}")
print(f"poping the last object {browsing_section.pop()}")
print(f"poping the last object {browsing_section.pop()}")
print(f"poping the last object {browsing_section.pop()}")


if not browsing_section:   # browsing_section is Flase when empty
    print('browsing section is empty now')

############################################################################

#                          Queue

# behaviour is First in First out
# just like queue of people standing
# so a bit of issue with performance issues like once the first element is
# poped then all the other elements needs to be shifted.

# first want to import deque object from collections # check on top

# instead of calling an empty list we can wrap it up with deque function
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(3)
queue.append(3)
queue.append(4)
queue.append(5)
queue.append(6)
queue.popleft()
print(queue)
print(len(queue))                        # length of the list
print(queue.count(3))                    # count a specific item in lists

name = ["ajai", "anu", "nakshathra"]
queue.extend(name)                       # adding a bunch  of items together
print(queue)
queue.reverse()                          # reverse the whole lists
print(queue)
queue.rotate(1)                          # rotate one element
print(queue)
queue.rotate(2)                          # rotate two elements
print(queue)

for x in queue:
    if(x == 'ajai'):
        print("ajai is in the list")

    else:
        ("ajai is not in the list")


#############################################################################
