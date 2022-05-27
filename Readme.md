# DES OpenID Connect Provider

## Links

* [OAuth libraries for Python](https://oauth.net/code/python/)
* [Django intro tutorial](https://docs.djangoproject.com/en/4.0/intro/)
* [Django OAuth Toolkit Tutorial](https://django-oauth-toolkit.readthedocs.io/en/latest/tutorial/tutorial_01.html)

## Local development with Docker Compose

To run locally via Docker Compose, copy `env.sample` to `.env` and customize the parameter values as desired. Then launch the application with

```bash
cd /path/to/this/repo/clone
docker-compose up
```

By default you should be able to access the service by opening http://127.0.0.1:8000 in your browser.

To start with a clean slate, run the following to destroy the database and any other persistent volumes:

```bash
docker-compose down --remove-orphans --volumes
```
