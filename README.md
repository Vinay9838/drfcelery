# Django Restframework Prioritizing celery task

---

>Please execute following command in sequence for seamless configuration

### Activate virtual environment

````shell
virtualenv -p python3 /home/myproject/venv
source venv/bin/activate
````

### Application dependencies
```shell
pip install -r requirements.txt
```

### Application setup

```shell
./manage.py migrate

./manage.py runserver
```

### Run celery
```shell
celery -A CeleryTaskService worker -Q priority_queue -c 1 -l info
```

