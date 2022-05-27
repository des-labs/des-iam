# DES OpenID Connect Provider

## Overview

This is the source code for [the OpenID Connect (OIDC) server](https://deslabs.ncsa.illinois.edu/iam) that supports [the DESaccess services](https://des.ncsa.illinois.edu/releases/dr2/dr2-access) of the Dark Energy Survey Data Management (DESDM) group at the National Center for Supercomputing Applications (NCSA) at the University of Illinois at Urbana-Champaign (UIUC).

The identity and access management (IAM) system used by DES relies on an Oracle database backend for authentication. This OIDC provider service allows third-party applications, such as a JupyterHub deployment, to authenticate users following OAuth2 web standard protocols. It supports role-based access control (RBAC) via the OIDC `groups` claim and the Django native user and group configuration.

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
