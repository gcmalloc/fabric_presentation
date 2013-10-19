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

###Writing doc

```python
def uname():
    """print the name of the system to stdout
    """
    run("uname -a")
```

###Reading it

```shell
>>>fab -l

Available commands:

    uname  print the name of the system to stdout
```

Also make a list of available commands

###Going faster

Can manage ssh connection to the hosts and run trough the rules n at a time

###mandatory demo

###Going even faster

* puppet + Mcollective
