%Fabric, easy deploy !
%Malik Bougacha

###Deployment

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

###Calling the rule

```
fab -H 127.0.0.1 uname
```

* Can also use the ssh config

```
fab -H test uname
```

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


###Extension for commands

```python
def run_service(service):
    sudo("service {} start".format(service)
```

List of available commands

* Either called with

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
