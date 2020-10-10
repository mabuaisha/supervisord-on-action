# supervisord-on-action

This repository contains the following:

1. Simple Flask Python App.
2. Simple Supervisor configuration.
3. Simple Python command line to control service run by Supervisor using XML-RPC interface.

### Prerequisites

In order to be able to run the code on this repository, the following items are needed:

1. [Python3](https://www.python.org/downloads/release/python-370/)
2. [pip](https://pip.pypa.io/en/stable/)
3. Unix-Like Operation System (Centos, Mac, RedHat, Ubuntu)


### Installation & Setup

1. Clone this repository `git clone https://github.com/mabuaisha/supervisord-on-action.git`
1. Create virtualenv `python3 -m venv supervisor-env`.
2. Activate virtualenv `source supervisor-env/bin/activate`.
3. Install Python packages using pip `pip install -r requirement.txt`.


### Running Program using Supervisor

1. Copy `supervisord-on-action` repository under `/opt`.
2. Run __supervisord__ main process `supervisord -n -c /opt/supervisord-on-action/app.conf &`.
3. Now, the `gunicorn` process should be started and the Hello World app should be up and running `http://0.0.0.0:5000`.


### Using Supervisorctl Client

`supervisorctl` is the command line allows you to control services run by supervisord

1. Get the status of service `supervisorctl -c /opt/supervisord-on-action/app.conf status simple-app`.
2. Stop service `supervisorctl -c /opt/supervisord-on-action/app.conf stop simple-app`.
3. Start service `supervisorctl -c /opt/supervisord-on-action/app.conf start simple-app`.


### Controlling Supervisor using XML-RPC interface

`parse.py` is a simple command line allows you to control services managed by supervisor using XML-RPC.

```
(supervisor-env) ➜  supervisord-on-action git:(master) ✗ python3 parse.py --help
usage: parse.py [-h] -a ACTION -p PROCESS_NAME

Simple arg parser for supervisor command

optional arguments:
  -h, --help       show this help message and exit
  -a ACTION        Store action value
  -p PROCESS_NAME  Store process name
```

It accepts two parameters which are:

1. `-a`: Action we need to execute on the service managed by supervisor. currently only start/stop is supported for this command.
2. `-p`: Process name we need to control and execute action.

```
(supervisor-env) ➜  supervisord-on-action git:(master) ✗ python parse.py -a stop -p simple-app
2020-10-14 22:48:17,617 DEBG killing simple-app (pid 30222) with signal SIGTERM
2020-10-14 22:48:17,617 INFO waiting for simple-app to stop
2020-10-14 22:48:17,619 DEBG 'simple-app' stderr output:
[2020-10-14 22:48:17 +0300] [30222] [INFO] Handling signal: term

2020-10-14 22:48:17,620 DEBG 'simple-app' stderr output:
[2020-10-14 22:48:17 +0300] [30225] [INFO] Worker exiting (pid: 30225)

2020-10-14 22:48:17,724 DEBG 'simple-app' stderr output:
[2020-10-14 22:48:17 +0300] [30222] [INFO] Shutting down: Master

2020-10-14 22:48:17,764 DEBG fd 13 closed, stopped monitoring <POutputDispatcher at 4386817752 for <Subprocess at 4385315304 with name simple-app in state STOPPING> (stderr)>
2020-10-14 22:48:17,764 DEBG fd 11 closed, stopped monitoring <POutputDispatcher at 4386817080 for <Subprocess at 4385315304 with name simple-app in state STOPPING> (stdout)>
2020-10-14 22:48:17,764 INFO stopped: simple-app (exit status 0)
2020-10-14 22:48:17,764 DEBG received SIGCHLD indicating a child quit
stop simple-app executed successfully
```   