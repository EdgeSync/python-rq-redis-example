# Sample Main Program
# Sets up the queues and workers and passes functions to them.
#
#
# Copyright Chris Staunton
# https://github.com/EdgeSync/python-rq-redis-example

import os
import rq
from redis import Redis
import time

def create_worker():
    pass
    # First we create a worker, and tell it what job queue it needs to listen to.
    # I like to use screen for my workers - however if you want to just run in a normal terminal window
    # comment out create_worker() in the main function and then type the following:
    # rq worker sample_queue

    #Kills all previous running screens
    os.system('pkill screen')
    #Creates a new screen called "sample screen" and executes the command "rq worker sample_queue"
    os.system('/usr/bin/screen -S sample_screen -d -m /usr/local/bin/rq worker sample_queue')

def worker_a():
    a_queue = rq.Queue('sample_queue', connection=Redis.from_url('redis://'))
    a_job = a_queue.enqueue('main_program.function_a', timeout=60)  # We create a job variable.
                                                                    # We tell it to push a_job job into a_queue
                                                                    # We then pass it the function which is in main_program.py, function_a().
                                                                    # As a sample i have put in a Timeout - this will kill the job if it takes more than 30 seconds.
def function_a():
    count = 1
    while count <= 20:
        print count
        count += 1
        time.sleep(1)

def main():
    # Used to run the above functions
    print "Creating worker..."
    create_worker()
    time.sleep(5) # not required - just for this example. gives us time to attach to the screen before the worker starts.
    print "Starting function a"
    worker_a()

if __name__ == '__main__':
    main()


