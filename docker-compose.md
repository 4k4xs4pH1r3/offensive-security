# Upgrade docker-compose to 1.29.2 version

At the moment the safest way to upgrade docker-compose to last release as root

```ShellSession
sudo -i
```

# Is by deleting it and reinstalling it
```ShellSession
rm /usr/bin/docker-compose && curl -L https://github.com/docker/compose/releases/download/1.29.2/docker-compose-`uname -s`-`uname -m` > /usr/bin/docker-compose && chmod +x /usr/bin/docker-compose && docker-compose --version
```
