%Fabric, easy deploy !
%Malik Bougacha

###deployment

* Shell script to install dependencies
\pause
* Manage the set of host (ssh config)
\pause
* Manage template (sed)
\pause
* Manage doc and format of the doc. (wait what)
\pause
* Manage parallel setup on multiple host.(wait what)

###Writing rules

```python
def uname():
    run("uname -a")
```

* In a "fabfile.py" file

###calling the rule

```
fab -H 127.0.0.1 uname

###Writing doc

```python
def uname():
    """print the name of the system to stdout"""
    run("uname -a")
```

###Reading it

```shell
>>>fab -l

Available commands:

    uname  print the name of the system to stdout
```

List of available commands

###Extension for commands
```
def run_service(service):
    sudo("service {} start".format(service)
```
*either called with

```python
run_service("rabbitmq-server")
```

* Or 

```
fab run_service:rabbitmq-server
```

###Going faster

Can manage ssh connection to the hosts and run trough the rules n at a time


###mandatory demo

###Going even faster

* puppet + Mcollective
