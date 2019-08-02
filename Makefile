PROJECT_NAME=config_server
APPS_DIRECTORY=apps
ENV=dev
APP_NAME=
APP_FULLNAME=$(APPS_DIRECTORY).$(APP_NAME)
SETTINGS_FILE=$(PROJECT_NAME)/settings/base.py
CONTAINER_BUILD_IMAGE=config_server

export DJANGO_SETTINGS_MODULE := $(PROJECT_NAME).settings.$(ENV)

REQ_FILE=requirements.txt

startapp:
	mkdir -p $(APPS_DIRECTORY)/$(APP_NAME) 
	python manage.py $@ $(APP_NAME) $(APPS_DIRECTORY)/$(APP_NAME) --settings=$(PROJECT_NAME).settings.$(ENV)
	sed -i 's/$(APP_NAME)/$(APP_FULLNAME)/g' $(APPS_DIRECTORY)/$(APP_NAME)/apps.py
	gawk -i inplace '/PROJECT_APPS \= \[/{print;print "    '\''$(APP_FULLNAME)'\'',";next}1' $(SETTINGS_FILE)

freeze_requirements:
	pip freeze > $(REQ_FILE) 

install_requirements:
	pip install -r $(REQ_FILE) 	

migrate:
	python manage.py $@ --settings=$(PROJECT_NAME).settings.$(ENV)

runserver:
	python manage.py $@ 0:8000 --settings=$(PROJECT_NAME).settings.$(ENV)

test:
	python manage.py $@ --settings=$(PROJECT_NAME).settings.$(ENV) -v 3

coverage:
	coverage run --source='./apps' manage.py test --settings=$(PROJECT_NAME).settings.$(ENV) -v 3

build:
	docker build -t $(CONTAINER_BUILD_IMAGE) .	

makemigrations:
	python manage.py $@ --settings=$(PROJECT_NAME).settings.$(ENV)

collectstatic:
	python manage.py $@ --settings=$(PROJECT_NAME).settings.$(ENV)

createsuperuser:
	python manage.py $@ --settings=$(PROJECT_NAME).settings.$(ENV)


