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

###Writing task

```python
from fabric import run
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

with 

```python
env.use_ssh_config = True
```

###Writing doc

```python
def uname():
    """print the name of the system to stdout"""
    run("uname -a")
```

###Reading it

```shell
>>> fab -l

Available commands:

    uname  print the name of the system to stdout
```


###Template engine
* Settings the configuration for a service depending on parameters

```python
def vim_conf(color=True):
    template_upload("vimrc_template", color)
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

###Extension trough cuisine

* simple wrapper for commonly used command

```python
import cuisine
cuisine.upstart_ensure("rabbitmq-server")
cusine.package_ensure("linux-base")
```

* support multiple os under certain condition

```python
cusine.package_install("linux-base")
cusine.package_install_yum("linux-base")
cusine.package_install_apt("linux-base")
cusine.package_install_emerge("linux-base")
cusine.package_install_pacman("linux-base")
```

###Going faster

Can manage ssh connection to the hosts and run trough the rules n at a time

```sh
fab -P -z 10 deploy_task
```

###mandatory demo

###Going even faster

* puppet + Mcollective
