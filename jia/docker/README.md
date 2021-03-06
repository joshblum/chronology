#Deploying with Docker

## Quick usage HOWTO

We've already pushed a working [Dockerfile to Docker Hub](https://registry.hub.docker.com/u/chronology/jia/), so you can do something like the following:

  * On a host machine, put a `settings.py` in `/etc/jia/settings.py`.  Note that the port in `settings.py` is ignored, as we communicate via nginx.
  * Run `docker run -v /etc/jia:/etc/jia -v /var/log/jia/:/var/log/jia/ -p PUBLIC_PORT:80 chronology/jia:v0.7.1`
  * Check `/var/log/jia` for app/nginx logs.

## How to build/push future versions

  * `./build.sh [git hash or tag you want to build] chronology/jia:v[version]`
  * `python ../../docker_tools/manage_docker.py push --tag chronology/jia:v[version]`
