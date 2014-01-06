django CMS Twitter plugin
=========================


.. image:: https://badge.fury.io/py/djangocms-twitter.png
    :target: http://badge.fury.io/py/djangocms-twitter

.. image:: https://pypip.in/d/djangocms-twitter/badge.png
        :target: https://crate.io/packages/djangocms-twitter?version=latest



``djangocms-twitter`` is a upgrade-friendly plugin, mostly derived from original
implementation in **django CMS** core.

Due to the switch from v 1.0 to v 1.1 in the twitter API, the original plugin no
longer works, and it's going to be removed.

Other plugin exists (or you could just switch to plain twitter widgets), althogh,
it's still a bit frustrating to throw away existing plugins.

Contrary to the 1.0 API, Twitter 1.1 API requires you to create client side
plugins in your profile and ``djangocms-twitter`` can do very little to avoid
this. It delivers data-compatible plugins for straightforward upgrade.

Some field has been deprecated as no longer used by the twitter widgets. They
have been left for easier upgrade.

Installation
------------

First-time installation
#######################

#. Add ``djangocms_twitter`` to ``INSTALLED_APPS``
#. Apply migrations::

    $ python manage.py migrate djangocms_twitter

#. Insert the plugins in the page and configure them as stated in Usage_.

Upgrade from the in-core plugin
###############################

#. Remove ``cms.plugins.twitter`` from ``INSTALLED_APPS``
#. Add ``djangocms_twitter`` to ``INSTALLED_APPS``
#. Apply migrations::

    $ python manage.py migrate djangocms_twitter

#. Modify the plugins instances according to Usage_.
#. Check your Templates_.

.. _Usage:

Usage
-----

TwitterRecentEntriesPlugin
##########################

For this plugin it's not necessary to create a widget for every plugin in your
website; you could just consider the widget you create on the Twitter website
as *templates* for this django CMS plugin:

##############################
Create the twitter-side widget
##############################

#. Login in your twitter account;
#. Go to https://twitter.com/settings/widgets;
#. Create new widget;
#. Select "**user timeline**" as source;
#. Configure the options (theme, colours etc) as described in https://dev.twitter.com/docs/embedded-timelines;
#. Create widget;
#. get the value of ``data-widget-id`` in the embed code;

#####################
Plugin instances data
#####################

``data-widget-id`` value can be shared by any number of plugins instances, the
plugin-provided user timeline will be shown, while the twitter widget graphics
appearance will be used.

#. Add or edit the **Twitter** plugin in you placeholders;
#. Fill in the Twitter widget it field using the ``data-widget-id`` value from
   the previous step;
#. Save the plugin;


TwitterSearchPlugin
###################

The twitter widget used by this plugin is entirely configured on the twitter
website.

##############################
Create the twitter-side widget
##############################

#. Login in your twitter account;
#. Go to https://twitter.com/settings/widgets;
#. Create new widget;
#. Select "**Search**" as source;
#. Configure the search query;
#. Configure the options (theme, colours etc) as described in https://dev.twitter.com/docs/embedded-timelines;
#. Create widget;
#. get the value of ``data-widget-id`` in the embed code;

#####################
Plugin instances data
#####################

#. Add or edit the **Twitter Search** plugin in you placeholders;
#. Fill in the Twitter widget it field using the ``data-widget-id`` value from
   the previous step;
#. Optionally fill-in the query field in the plugin form; this is only used for
   non-javascript enabled browser, as the ``data-widget-id`` will take over on
   javascript-enabled ones;
#. Save the plugin;


.. _Templates:

Templates
---------

Older templates it's no longer valid. Most of the graphic configuration must be
done in when creating the widget on the Twitter website.

A limited set of client-side options exists to configure the widgets; see
https://dev.twitter.com/docs/embedded-timelines#options for further info.

To apply them you need to modify the plugin templates:

- ``cms/plugins/twitter_timeline.html``: for ``TwitterRecentEntriesPlugin``
- ``cms/plugins/twitter_search_widget.html``: for ``TwitterSearchPlugin``

.. image:: https://d2weczhvl823v0.cloudfront.net/nephila/djangocms_twitter/trend.png
   :alt: Bitdeli badge
   :target: https://bitdeli.com/free

