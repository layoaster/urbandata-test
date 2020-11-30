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

### Database *Migrations* and Django *manage* command
To run migrations with **Docker** use the **docker-compose** service `manage`
with the `doker-compose run` command. Some examples:

Generating migrations:
```shell
$ docker-compose run [--rm] manage makemigrations
```
Applying migrations:
```shell
$ docker-compose run [--rm] manage migrate
```
**Note:** The use of flag `--rm` is highly recommend so the container gets
removed after run.

## Configuration
The application supports configuration via environment variables. In particular,
`docker-compose` can pick values from the `.env` [file][env-files] that should
be placed on the same directory of the `docker-compose-yml` file lives. More info
regarding *docker-compose* support for *.env* files [here][env-files-compose].

Make sure you create a `.env` file containing the following env-vars:
```shell
#### DJANGO APP
DJANGO_SETTINGS_MODULE=config.settings.dev
DJANGO_SECRET_KEY=valid-secret-key
DJANGO_LOG_LEVEL=DEBUG

#### DATABASE CLIENT/SERVER
DB_HOST=postgres
DB_DATABASE=urbandata
DB_USER=urbandata_user
DB_PASS=valid-password
```


## Testing

### Unit-tests
The project is configured to use the [pytest][pytest] framework for unit-tests
and [coverage][coverage] for test coverage reports.

* */tests/test-results/junit.xml* - pytest report in JUnit-XML format for CI systems.
* */tests/test-results/htmlcov/index.html* - coverage report in HTML format.

Reports are automatically generated by *pytest* on each run. To launch them:
```shell
$ docker-compose run [--rm] test-unit
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
  $ docker-compose run [--rm] mypy
  ```


## Test/Evaluation Notes

* The API server is listening on the port `8080`.
* The API is fully configured to support authentication with Bearer Tokens.
However, for evaluation purposes the endpoints are exposed without any auth.


[black]: https://github.com/psf/black
[buildkit]: https://docs.docker.com/develop/develop-images/build_enhancements/
[coverage]: https://coverage.readthedocs.io/
[docker-compose]: https://docs.docker.com/compose/
[env-files]: https://vsupalov.com/docker-arg-env-variable-guide/#the-dot-env-file-env
[env-files-compose]: https://docs.docker.com/compose/env-file/
[flake8]: https://github.com/PyCQA/flake8
[mypy]: https://mypy.readthedocs.io/en/stable/
[pytest]: https://docs.pytest.org/en/stable/
