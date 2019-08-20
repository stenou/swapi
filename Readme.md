## Overview

This script will return the starships and their pilots for a given Star Wars episode number.

## Docker
```
$ docker run stenou/swapi [1-7]
```

## Minikube
```
$ helm install --debug ./helm
```

The helm chart keeps the docker container open using a do..while loop.  You can create a shell into the container and run the application

```
$ kubectl exec -it {container_name} /bin/bash
$ python main.py 1
```