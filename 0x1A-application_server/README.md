# 0x1A. Application server

In this project you will added application server to our web infrastructure, plug it to our Nginx web server and make it serve dynamic contents from our Airbnb clone project.

## Resources

* [Application server vs web server](https://www.nginx.com/resources/glossary/application-server-vs-web-server/)
* [How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu 16.04](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-16-04) (As mentioned in the video, do not install Gunicorn using virtualenv, just install everything globally)
* [Running Gunicorn](https://docs.gunicorn.org/en/latest/run.html)
* [Be careful with the way Flask manages slash](https://werkzeug.palletsprojects.com/en/0.14.x/routing/) in [route](https://flask.palletsprojects.com/en/1.0.x/api/#flask.Flask.route) - strict_slashes
* [Upstart documentation](https://doc.ubuntu-fr.org/upstart)
* [WSGI](https://www.fullstackpython.com/wsgi-servers.html)
