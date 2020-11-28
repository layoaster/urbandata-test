# UrbanData Analytics Test Application


## Description
Small app to manage real state assets data through a REST interface.


## Development
The project supports development via `Docker` containers but a *virtualenv* can
always be created to go without containers.

### Docker
Since the applications requires several containers the project supports
[docker-compose][docker-compose] to help with local containers orchestration.


## Configuration
The application supports configuration via environment variables. In particular,
`docker-compose` can pick values from the `.env` [file][env-files] that should
be placed on the same directory of the `docker-compose-yml` file lives. More info
regarding *docker-compose* support for *.env* files [here][env-files-compose].

Sample `.env` file:
```shell
#### DJANGO APP
DJANGO_SETTINGS_MODULE=config.settings.dev

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
[docker-compose]: https://docs.docker.com/compose/
[env-files]: https://vsupalov.com/docker-arg-env-variable-guide/#the-dot-env-file-env
[env-files-compose]: https://docs.docker.com/compose/env-file/
[flake8]: https://github.com/PyCQA/flake8
[mypy]: https://mypy.readthedocs.io/en/stable/
