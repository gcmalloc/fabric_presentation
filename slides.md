%Fabric, easy deploy !
%Malik Bougacha
#deployment
* shell script to install dependencies

###Writing doc
```python
def uname():
	"""print the name of the system to stdout
	"""
	run("uname -a")
```

###Reading it
```
fab -l
Available commands:

    uname  print the name of the system to stdout
```

#alternative
* puppet + Mcollective
* chef

