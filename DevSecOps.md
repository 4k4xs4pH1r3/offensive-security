## Install Commander for Amazon AWS in Linux with LocalStack

```ShellSession
pip install --upgrade pip
```
#
```ShellSession
cd && apt isntall gconf-service gconf-service-backend gconf2 gconf2-common libappindicator1 libgconf-2-4 libindicator7 -y
```
#
Download and install from https://getcommandeer.com/ for Linux and install with

```ShellSession
dpkg -i commandeer_0.2.5_amd64.deb
```
#
```ShellSession
pip install --ignore-installed localstack[full]
```
