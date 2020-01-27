# MAC-ADDRESS
MAC address REST API - to query which company the mac address belongs to
macaddress.io - REST API
mac.py is a Python program, that runs a simple REST API to talk to macaddress.io REST API services
to check the name of the company to whom the mac address belongs to and is registered with.

Prerequisite
Tested on :

Docker version 19.03.5, build 633a0ea
Docker CE 19.03 (optional) - for containerization
running on cygwin on windows

$ cygcheck --version
cygcheck (cygwin) 2.8.0
System Checker for Cygwin
Copyright (C) 1998 - 2017 Cygwin Authors
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.


Python 2.7
PIP pip 9.0.1 from /usr/lib/python2.7/site-packages (python 2.7)

Request 2.22
$ pip  list | grep requests
DEPRECATION: The default format will switch to columns in the future. You can use --format=(legacy|columns) (or define a format=(legacy|columns) in your pip.conf unde
r the [list] section) to disable this warning.
requests (2.22.0)



Installation

Use Git hub

git clone https://github.com/smitha-ss/MAC-ADDRESS.git

Standalone Usage

Run the python program

python mac.py

For Security reasons, need a better way to manage the API key.

Docker Usage

PS C:\cygwin64\home\smitha> docker.exe run -it mac-docker
Traceback (most recent call last):
  File "mac.py", line 5, in <module>
    from flask import Flask
ImportError: No module named flask
PS C:\cygwin64\home\smitha> docker build -t mac-docker .
Sending build context to Docker daemon  4.412MB
Step 1/6 : FROM python:2.7
 ---> 3c1fea91a131
Step 2/6 : LABEL version="0.1"
 ---> Using cache
 ---> 9475b25a067a
Step 3/6 : LABEL description="MAC program with Dockerfile."
 ---> Using cache
 ---> 435c3d2d613a
Step 4/6 : ADD mac.py .
 ---> c61575231086
Step 5/6 : RUN if [ $(pip list | grep requests) ]; then echo "Python package already installed"; else echo "Python packages not installed. Installing...."; pip install requests; fi
 ---> Running in 8b37a8bc43b6
DEPRECATION: Python 2.7 reached the end of its life on January 1st, 2020. Please upgrade your Python as Python 2.7 is no longer maintained. A future version of pip will drop support for Python 2.7. More details about Python 2
 support in pip, can be found at https://pip.pypa.io/en/latest/development/release-process/#python-2-support
Python packages not installed. Installing....
DEPRECATION: Python 2.7 reached the end of its life on January 1st, 2020. Please upgrade your Python as Python 2.7 is no longer maintained. A future version of pip will drop support for Python 2.7. More details about Python 2
 support in pip, can be found at https://pip.pypa.io/en/latest/development/release-process/#python-2-support
Collecting requests
  Downloading requests-2.22.0-py2.py3-none-any.whl (57 kB)
Collecting certifi>=2017.4.17
  Downloading certifi-2019.11.28-py2.py3-none-any.whl (156 kB)
Collecting chardet<3.1.0,>=3.0.2
  Downloading chardet-3.0.4-py2.py3-none-any.whl (133 kB)
Collecting idna<2.9,>=2.5
  Downloading idna-2.8-py2.py3-none-any.whl (58 kB)
Collecting urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1
  Downloading urllib3-1.25.8-py2.py3-none-any.whl (125 kB)
Installing collected packages: certifi, chardet, idna, urllib3, requests
Successfully installed certifi-2019.11.28 chardet-3.0.4 idna-2.8 requests-2.22.0 urllib3-1.25.8
Removing intermediate container 8b37a8bc43b6
 ---> 0ad133c931fa
Step 6/6 : CMD [ "python", "mac.py" ]
 ---> Running in ac47eda4b14e
Removing intermediate container ac47eda4b14e
 ---> b4ce77918c1e
Successfully built b4ce77918c1e
Successfully tagged mac-docker:latest
SECURITY WARNING: You are building a Docker image from Windows against a non-Windows Docker host. All files and directories added to build context will have '-rwxr-xr-x' permissions. It is recommended to double check and rese
t permissions for sensitive files and directories.
PS C:\cygwin64\home\smitha> docker.exe run -it mac-docker
https://api.macaddress.io/v1
Enter your MAC address:  44:38:39:ff:ef:57
 44:38:39:ff:ef:57
Success!
The company associated with MAC address  44:38:39:ff:ef:57 is : Cumulus Networks, Inc

Build your image once with API Key
