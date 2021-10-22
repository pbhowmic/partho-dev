Storing and retrieving session data
===================================

``Session`` objects are stored in a *backend*, typically a SQL database (like PostgreSQL or MySQL) or an in-memory
key-value store (like Redis or Memcached). Session data is typically identified only by the primary key ``sessionid``
and as such, lends itself well to key-value stores like Redis and Memcached. There are other possible backends such as
files (in which case Django will create a file per session in a temporary directory like ``/tmp`` ) but it is slow and
not useful where there are multiple Django instances running in different servers or containerized environments
because each Django instance will only have access to their own file-based cache so if the client returns with a
subsequent request to a different instance, this instance will look at the ``sessionid``, do a search in its file-cache
and not find the session-file for the said ``sessionid``, conclude that the old session may have expired
and thus been cleared out and then proceed to give the client a new session, thus restarting the session cycle.

*Side note: You could try and be a bit too clever by half and mount an NFS filesystem to be shared as the file-based*
*cache but please don't*

``Session`` objects can be used to store arbitrary data. Doing so causes the session object to be saved to DB but the
``sessionid`` cookie is unchanged. Where session data is stored is determined by the backing store. Django, by default,
sets the default database as the the backing store but it is inadvisable.

The case for in-memory KV backends
----------------------------------

#. Session data is frequently accessed and if the database that is used to store all Django models is the same as the session store, it will exact a performance penalty on the DB.
#. Even if you configured Django to use a different DB just for sessions, there is a catch. Session-associated data once it goes in a SQL DB is permanent even when the session expires and the keep the table size manageable and not growing into infinity, expired session rows must be periodically cleared out (usually by a cron job). Compare that to a caching backend such Redis where this action can be be made automatic by using least recently used (LRU) eviction policies.

At any rate, I consider it a must that a KV-store be used for storing sessions data.

Out of the box, Django has better support for Memcached than it does for Redis.
This is expected to `change with Django 4.0 <https://github.com/django/django/pull/14437>`_
For a comprehensive guide to caching, check out
`Django's documentation on caching <https://docs.djangoproject.com/en/3.2/topics/cache/>`_.

*Side note: Django uses caching for more than just caching sessions data. Most notably, it uses it for caching views (essentially memoizing the view)*
