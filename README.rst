Introduction
============

This addon override collective.googleanalytics to support translated domains.

It can also be used in the case you don't want to use oauth binding between
Plone and Google Analytics but just configure the code.


How to use
==========

Once the addon is installed you have a controlpanel where you can configure
each url for languages. Be warned no redirection happens if the url is not
configured.

Example::

    http://www.brussels.irisnet.be|UA-XXXXX-Y
    http://www.brussel.irisnet.be|UA-YYYYY-Z
    http://www.bruxelles.irisnet.be|UA-ZZZZZ-X

Credits
=======

Companies
---------

|cirb|_ CIRB / CIBG

* `Contact us <mailto:irisline@irisnet.be>`_


Authors

- JeanMichel FRANCOIS aka toutpt <toutpt@gmail.com>

.. Contributors

.. |cirb| image:: http://www.cirb.irisnet.be/logo.jpg
.. _cirb: http://cirb.irisnet.be
.. _sitemap: http://support.google.com/webmasters/bin/answer.py?hl=en&answer=183668&topic=8476&ctx=topic
