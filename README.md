# UrbanData Analytics Test Application


## Description
Small app to manage real state assets data through a REST interface.


## Development
The project supports development via `Docker` containers but a *virtualenv* can
always be created to go without containers.

### Docker
Since the applications requires several containers the project supports
[docker-compose][docker-compose] to help with local containers orchestration.

The *Dockerfile* makes use of multi-stage builds so it's recommended (on
development/local environment only!) to enable [Buildkit][buildkit] in order to
get faster builds. To enable it these two env-vars should be set before running
*docker*/*docker-compose*.

```shell
DOCKER_BUILDKIT=1
COMPOSE_DOCKER_CLI_BUILD=1
```


## Configuration
The application supports configuration via environment variables. In particular,
`docker-compose` can pick values from the `.env` [file][env-files] that should
be placed on the same directory of the `docker-compose-yml` file lives. More info
regarding *docker-compose* support for *.env* files [here][env-files-compose].

Sample `.env` file:
```shell
#### DJANGO APP
DJANGO_SETTINGS_MODULE=config.settings.dev
DJANGO_SECRET_KEY=valid-secret-key
DJANGO_LOG_LEVEL=DEBUG

#### DATABASE CLIENT/SERVER
DB_HOST=postgres
DB_DATABASE=urbandata
DB_USER=postgres
DB_PASS=valid-password
```


## Dev tooling
There is a set of tools that make developer's lives better while enforcing our
set of Python styling rules:

* [flake8][flake8]: a linter/style enforcer.
  ```shell
  $ docker-compose run [--rm] flake8
  ```
* [black][black]: a code formatter.

  To only make a check/diff (don't write files back)
  ```shell
  $ docker-compose run [--rm] black [directory|file]
  ```
  After inspecting changes you can let black modify files by itself:
  ```shell
  $ docker-compose run [--rm] format [directory|file]
  ```
* [mypy][mypy]: a static type checker for Python.
  ```shell
  $ docker-compose run [--rm] mypy [directory|file]
  ```





[black]: https://github.com/psf/black
[buildkit]: https://docs.docker.com/develop/develop-images/build_enhancements/
[docker-compose]: https://docs.docker.com/compose/
[env-files]: https://vsupalov.com/docker-arg-env-variable-guide/#the-dot-env-file-env
[env-files-compose]: https://docs.docker.com/compose/env-file/
[flake8]: https://github.com/PyCQA/flake8
[mypy]: https://mypy.readthedocs.io/en/stable/
