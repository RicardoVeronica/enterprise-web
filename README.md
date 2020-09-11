# Django Enterprise web (Restaurant)

Enterprise project with simple Blog, Category managment, CRUD (Create, Read, Update and Delete) 
in "Servicios" & contact form

### This project uses

* Template Tags
  * {% for %}
  * {% if %}
  * {% url %}
  * {% block %}
  * {% static %}
  * {% csrf_token %}
* Filters
  * |slice
  * |date
  * |linebreaks
  * |safe
* Django models
  * Relation one to one ForeignKey
  * Relation many to many
  * Users from Django contributions Auth model
* Django Admin
* Context processors
* Django-ckeditor for admin
* Django request special variable
* Django forms
* Mailtrap for email testing

### Tech

This project uses my personal stack to work:

* Django - Python Web Framework
* Divio cloud - Web platform to deploy projects easily
* Docker - Like virtual environment for Django project
* Git and Github - Version control

[This project live](https://enterprise-web.us.aldryn.io/)

### Run locally

``````sh
$ docker-compose up
# Go to 0.0.0.0:8000
``````
