# Prueba Ingeniería Resuelve (backend)
This project is a proposed solution to the [**Prueba Ingeniería Resuelve**](https://github.com/resuelve/prueba-ing-backend).

## Description
This project exposes an endpoint to calculate the final salary of a list of teams and players.

## Requirements
* [Git](https://git-scm.com/downloads)
* [python 3.10](https://www.python.org/downloads/)

## Installation

1. We clone the project.

```bash
git clone git@github.com:tuticapi/prueba-ing-backend.git
```

2. We enter the project.
```bash
cd prueba-ing-backend
```
3. We install pipenv.
```bash
pip3.10 install pipenv
```
4. We create the virtual environment and install the dependencies.
```bash
pipenv install
```
5. We activate the virtual environment.
```bash
pipenv shell
```
6. We run the migrations
```bash
python ./team_salary/manage.py migrate
```

7. We run the project.
```bash
python ./team_salary/manage.py runserver
```
## Quick Setup

### Testing



