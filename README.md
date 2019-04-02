[![CircleCI](https://circleci.com/gh/lcpojr/sbg-rj/tree/master.svg?style=svg)](https://circleci.com/gh/lcpojr/sbg-rj/tree/master)

# sbg-rj

Website for SBG (Sociedade Brasileira de Geologia).

## Requiriments

- [Python](https://www.python.org/downloads/) (v3.7+);
- [Django](https://www.djangoproject.com/download/) (v2.2+);
- [Docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/);
- [Docker-compose](https://docs.docker.com/compose/install/);

## How to use (Developent)

To use in development env you should just execute the commands bellow.

```shell
docker-compose build
docker-compose up -d
```

**Working with containers**

- To check containers status use `docker-compose ps`;
- To disable containers use `docker-compose down`;
- To clean the container use `docker container prune -f`;
- To clean the database use `docker volume prune -f`;
- To clean the network use `docker network prune -f`;
- To access the application container use `docker-compose exec web sh`;

