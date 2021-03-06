# PISMA - Pega Infinity SMA (System Management Application)
[![CodeFactor](https://www.codefactor.io/repository/github/mishankov/pega-infinity-sma/badge)](https://www.codefactor.io/repository/github/mishankov/pega-infinity-sma)
[![Django CI](https://github.com/mishankov/pega-infinity-sma/workflows/Django%20CI/badge.svg)](https://github.com/mishankov/pega-infinity-sma/actions?query=workflow%3A%22Django+CI%22)

System Management Application for multiple Pega Infinity nodes based on Pega API

Currently application in its early alpha stage. In the future it will cover all Pega API system management capabilities

Available features:
- Requestor management: interrupt and stop  
- Agent management: start, stop and restart

## Instalation

```bash
git clone https://github.com/mishankov/pega-infinity-sma.git
cd pega-infinity-sma
scripts/init.sh
```
Then follow instructions to create super user

For Windows use `init.bat`

## Get up and running
To run SMA do
```bash
scripts/runserver.sh
```
and then go to http://0.0.0.0:8000/ in your browser

For Windows use `runserver.bat`

## Add new node
To add new node:
 1. Go to http://0.0.0.0:8000/admin
 2. Log in with your super user account
 3. Under PISMA application go to "Pega nodes" and click "Add Pega node" button
 4. Fill the form: displayed name, url in format `http://{host}:{port}`, select production level and enter login and password to access Pega API on your node
 5. Click "Save"
 
Then you can access you node on home page http://0.0.0.0:8000/

## Node access permissions
To access node with *not* super user you should add permission with name `Can access {PegaNode.name}` to this user or to one of his groups

## Settings
All project wide settings should be done through environment variables

### Common settings
- `PISMA_PEGAAPI_TIMEOUT` - timeout for PegaAPI services. Default is `5`
- `PISMA_DJANGO_DEBUG` - debug mode for Django. Default is `False`
- `PISMA_DJANGO_SECRET_KEY` - Django secret key. Default is `SECRET_KEY`. You **must** change it, if you use PISMA with production environments

### Server settings
- `PISMA_HOST` - host to run application server. Default is `0.0.0.0`
- `PISMA_PORT` - port to run application server. Default is `8000`

### Logging level settings
- `PISMA_DJANGO_ROOT_LOGGING_LEVEL` - root logging level setting. Default is `ERROR`. Sends logs to `logs/errors.log` and console
- `PISMA_DJANGO_PISMA_LOGGING_LEVEL` - PISMA logging level setting. Default is `INFO`. Sends logs to `logs/pisma.log` and console
- `PISMA_DJANGO_CONSOLE_LOGGING_LEVEL` - console logging level setting. Default is `WARNING`. Doesn't print messages with logging level lower then its
- `PISMA_DJANGO_FILE_LOGGING_LEVEL` - `logs/pisma.log` logging level setting. Default is `INFO`. Doesn't print messages with logging level lower then its

## Technologies
- Web framework: Django https://www.djangoproject.com/
- CSS, JS: Bootstrap 4 https://getbootstrap.com/
- Tables on UI: DataTables https://datatables.net/
- Icons: Feather https://feathericons.com/
