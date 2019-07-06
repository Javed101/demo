# Project - Read Me
---
About Project

### **Application Requirements**
* Python 3.7.0
* Django==2.2.3
* django-environ==0.4.5
* Jinja2==2.10.1
* MarkupSafe==1.1.1
* pytz==2019.1
* sqlparse==0.3.0


### **Quick Setup for Deployment (Development / Staging / Production)**

**Step by Step Application Configuration**

1. Clone the repository in your Projects Home Directory.
2. Create Virtual Environment `virtualenv -p python3.7.0 venv`
4. Activate Virtual Environment `source venv/bin/activate`
5. Install all Requirements `pip install -r requirements/base.txt`
6. Create `.env` file from `.env-sample`
**_Example:_** `cp .env-sample project/.env`
8. Configure `.env` as per server settings
9. Run migrations `python manage.py migrate`
10. Generate Static Files `python manage.py collectstatic`
11. Run system checks to make sure that everything's configured properly `python manage.py check`


**Running Application in Development Mode**

1. Set `DEBUG` to `True` in `.env`
2. Set `DJANGO_SETTINGS_MODULE` to `project.settings.dev`
3. Activate Virtual Environment
4. Run the Test Server `python manage.py runserver`


**Running in Production Mode**

1. Make sure `DEBUG` is set to `False` in `.env`
2. Make sure `DJANGO_SETTINGS_MODULE` to `project.settings.prod` in `.env`
3. Make a pre-deployment test `python manage.py check --deploy`
4. Make sure that all static files are generated using `python manage.py collectstatic`

---
