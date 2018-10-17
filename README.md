# python-rq-redis-example

I recently learned how to use redis to distrubte functions of a python program, and allow the program to run multiple functons in parallel. What irked me the most was how little documentation or straight-forward examples were out there to help me get up and runnning.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

python 2.7  
screen  
redis-server  
pip  
python modules rq and redis  


#### Installing necessary pre-reqs
```
sudo *package manager* install *software*
e.g.

sudo apt install screen
sudo apt install redis-server

pip installer downloaded from here: https://bootstrap.pypa.io/get-pip.py
sudo python get-pip.py

```

#### Installing required python packages


```
e.g. via pip:

pip install rq
pip install redis
```


#### Start the redis server

```
in a terminal, type:
redis-server
```

#### Run main_program.py
```
python main_program.py
```

#### What happens next
The screen starts, we can access it via a terminal like so:
```
screen -r sample_screen
```
The screen runs a worker monitoring on sample_queue

Then the job is passed to the queue sample_queue, and the worker executes function_a() 


In our screen (sample_screen) we can see function a being run - it counts 1-20.

  
#### Further Reading
###### About Redis
Redis contains 3 seperate components  
  
- The main component is the worker - this is seperate from the redis web server and is used to run the job  
- The next component is the message queue - the worker constantly checks the message queue for new jobs
- When a job appears in a message queue the worker assigns itself to the job, and run the job - then post results back to the queue 
the last component is the task queue client - this component runs as part of the application in redis-server.  
- This component posts new jobs to the message queue 
- Documentation is available here: https://redis.io/

