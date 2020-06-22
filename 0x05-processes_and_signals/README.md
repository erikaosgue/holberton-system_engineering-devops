# Resources
### Read or watch:

* [Linux PID](./http://www.linfo.org/pid.html)
* [Linux process](./https://www.thegeekstuff.com/2012/03/linux-processes-environment/)
* [Linux signal](./https://www.thegeekstuff.com/2012/03/linux-signals-fundamentals/)
### man or help:

* ps
* pgrep
* pkill
* kill
* exit
* trap
## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

## General
* What is a PID 
* What is a process
* How to find a process’ PID
* How to kill a process
* What is a signal
* What are the 2 signals that cannot be ignored

## Tasks
## [0. What is my PID mandatory](./)
Write a Bash script that displays its own PID.

## [1. List your processes mandatory](./)
Write a Bash script that displays a list of currently running processes.

Requirements:

Must show all processes, for all users, including those which might not have a TTY
Display in a user-oriented format
Show process hierarchy

## [2. Show your Bash PID mandatory](./)
Using your previous exercise command, write a Bash script that displays lines containing the bash word, thus allowing you to easily get the PID of your Bash process.

Requirements:

You cannot use pgrep
The third line of your script must be # shellcheck disable=SC2009 (for more info about ignoring shellcheck error here)

## [3. Show your Bash PID made easy mandatory](./)
Write a Bash script that displays the PID, along with the process name, of processes whose name contain the word bash.

Requirements:

You cannot use ps

## [4. To infinity and beyond mandatory](./)
Write a Bash script that displays To infinity and beyond indefinitely.

Requirements:

In between each iteration of the loop, add a sleep 2

## [5. Kill me now](./)
We killed our 4-to_infinity_and_beyond process using ctrl+c in the previous task, there is actually another way to do this.

Write a Bash script that kills 4-to_infinity_and_beyond process.

Requirements:

You must use kill
Terminal #0

## [6. Kill me now made easy](./)
Write a Bash script that kills 4-to_infinity_and_beyond process.

Requirements:

You cannot use kill or killall
Terminal #0


## [7. Highlander](./)
Write a Bash script that displays:

To infinity and beyond indefinitely
With a sleep 2 in between each iteration
I am invincible!!! when receiving a SIGTERM signal
Make a copy of your 6-kill_me_now_made_easy script, name it 67-kill_me_now_made_easy, that kills the 7-highlander process instead of the 4-to_infinity_and_beyond one.

Terminal #0

## [8. Beheaded process](./)
Write a Bash script that kills the process 7-highlander.

Terminal #0

## [9. Process and PID file](./)
Write a Bash script that:

Creates the file /var/run/holbertonscript.pid containing its PID
Displays To infinity and beyond indefinitely
Displays I hate the kill command when receiving a SIGTERM signal
Displays Y U no love me?! when receiving a SIGINT signal
Deletes the file /var/run/holbertonscript.pid and terminates itself when receiving a SIGQUIT or SIGTERM signal

## [10. Manage my process](./)

Read:

&
init.d
Daemon
Positional parameters
man: sudo

Programs that are detached from the terminal and running in the background are called daemons or processes, need to be managed. The general minimum set of instructions is: start, restart and stop. The most popular way of doing so on Unix system is to use the init scripts.

Write a manage_my_process Bash script that:

Indefinitely writes I am alive! to the file /tmp/my_process
In between every I am alive! message, the program should pause for 2 seconds
Write Bash (init) script 101-manage_my_process that manages manage_my_process. (both files need to be pushed to git)

Requirements:

When passing the argument start:
Starts manage_my_process
Creates a file containing its PID in /var/run/my_process.pid
Displays manage_my_process started
When passing the argument stop:
Stops manage_my_process
Deletes the file /var/run/my_process.pid
Displays manage_my_process stopped
When passing the argument restart
Stops manage_my_process
Deletes the file /var/run/my_process.pid
Starts manage_my_process
Creates a file containing its PID in /var/run/my_process.pid
Displays manage_my_process restarted
Displays Usage: manage_my_process {start|stop|restart} if any other argument or no argument is passed
Note that this init script is far from being perfect (but good enough for the sake of manipulating process and PID file), for example we do not handle the case where we check if a process is already running when doing ./101-manage_my_process start, in our case it will simply create a new process instead of saying that it is already started.

## [11. Zombie](./)

## [12. Screencast](./)
Now that you have mastered signals, how about sharing your knowledge?

Create a screencast where you live-code/demo something related to Unix signals.

Requirements:

Step by step video
Two minutes of above
Done in English
Published to Youtube
While you are free to choose the recording system to record the screencast, I highly recommend screencast-o-matic.

Once you are done, please share the Youtube URL in your answer file and below.

We’ll be watching you!

# Author 
* Erika Osorio Guerrero - [erikaosgue](./https://github.com/erikaosgue)


