Django sessions
===============

Django's sessions support is one the load-bearing structures in Django. Almost every Django project you will be
involved in will likely involve Django's session support. In fact when you invoke ``django-admin startproject`` the
default ``settings.py`` file will have Django sessions autoconfigured. You will find it in

.. code-block:: python

   INSTALLED_APPS = [
       .
       .
       .
       'django.contrib.sessions',
       .
       .
       .
   ]
   MIDDLEWARE = [
    .
    .
    .
    'django.contrib.sessions.middleware.SessionMiddleware',
    .
    .
    .
]

As you can see Django sessions is autoincluded in ``INSTALLED_APPS`` and in ``MIDDLEWARE``. I recommend reading through
the source code for ``SessionMiddleware`` but not just yet. But before we can understand Django sessions, what
constitutes a session? To quote `MDN <https://developer.mozilla.org/en-US/docs/Web/HTTP/Session>`_
In client-server protocols, like HTTP, sessions consist of three phases:

1. The client establishes a TCP connection (or the appropriate connection if the transport layer is not TCP).
2.  The client sends its request, and waits for the answer.
3. The server processes the request, sending back its answer, providing a status code and appropriate data.

Thus, it a user's interaction with your website or API server that constitutes a session. As such, the session could be
through a browser or an app (or another web service but we will not concern ourselves with that).
Note that I never claimed that a user had to authenticate himself/herself to the website to establish a session.
Just interaction is enough. Now one must ask the question when does a session end?

Is it enough to close the browser?
Or is it when there is no user activity for a period of time?
If the user closes the browser and then comes back and re-engages with the website, is it the start of a new session
or the continuation of a new one?
The short answer is "it depends". It depends on both the browser being used and the webserver.
Django typically uses session management by way of a cookie. Sometimes it is just an identifier.
Other times, it may be a signed cookie. It depends on which session backend was configured.

It is possible to set things at the server end that `requests` that the browser clear the session information.
The browser may ignore that. So that's no good.
