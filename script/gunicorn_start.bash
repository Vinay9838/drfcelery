#!/bin/bash

NAME="CeleryTaskService"                        # Name of the application
DJANGODIR=/home/vinay/project/drfcelery        # Django project directory
SOCKFILE=/home/vinay/project/drfcelery/run/gunicorn.sock  # communicate through unix socket
USER=root                              # the user to run as
GROUP=root                            # the group to run as
NUM_WORKERS=3                            # processes Gunicorn spawn
DJANGO_SETTINGS_MODULE=CeleryTaskService.settings      # which settings file should Django use
DJANGO_WSGI_MODULE=CeleryTaskService.wsgi              # WSGI module name
echo "Starting $NAME as `whoami`"

# Activate the virtual environment

cd $DJANGODIR
source /home/vinay/project/drfcelery/venv/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist

RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)

exec gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=unix:$SOCKFILE \
  --log-level=debug \
  --access-logfile /var/log/CeleryTaskService/info/info.log \
  --error-logfile /var/log/CeleryTaskService/info/error.log