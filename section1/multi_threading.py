'''
Multi threading is used to perform tasks concurrently
good for i/o bound tasks like reading files or fetching API data
threading.Thread(target=my_function)
'''

#consider a single thread
import threading
import time

def walk_dog():
    time.sleep(8)
    print("Finish walking the dog")

def wash_dishes(name,last):
    time.sleep(2)
    print(f"{name} Please {last} wash the dishes")

def Login():
    time.sleep(3)
    print("login to work")


walk_dog()
# wash_dishes()
Login()

# the above functions take place one aftr the other but what if i wanted to make it concurrent? u
# can create multiple threads with seperate targets
# u can see that then the execution order is dif the one with the longst sleep time executes last
chore1=threading.Thread(target=walk_dog)
chore1.start()


#if ur functiont takes args then in the Thread also u need to speicfy few a params arg as a tuple
chore2=threading.Thread(target=wash_dishes,args=("joe","jake")) # if u want to pass only a single parameter make sure to end it with comma ie args=("joe",)
chore2.start()

chore3=threading.Thread(target=Login)
chore3.start()

#now u might want to wait for all threads to finsih before u print the complete message

chore1.join()
chore2.join()
chore3.join()

print("All chores are complete")