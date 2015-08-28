from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models.pluginmodel import CMSPlugin


class TwitterRecentEntries(CMSPlugin):
    title = models.CharField(_('title'), max_length=75, blank=True)
    twitter_user = models.CharField(_('twitter user'), max_length=75)
    count = models.PositiveSmallIntegerField(_('count'), default=3,
                                             help_text=_('Number of entries to display'))
    link_hint = models.CharField(_('link hint'), max_length=75, blank=True,
                                 help_text=_('Deprecated: no longer used by Twitter widgets.'))
    twitter_id = models.CharField(_('twitter id'), max_length=75,
                                 help_text=_(u'See https://twitter.com/settings/widgets on how to obtain one'))

    def __unicode__(self):
        return self.title


class TwitterSearch(CMSPlugin):
    title = models.CharField(_('title'), max_length=75, blank=True)
    query = models.CharField(_('query'), max_length=200, blank=True, default='',
                             help_text=_('Deprecated: no longer used by Twitter widgets. Define one when creating widgets.'))
    count = models.PositiveSmallIntegerField(_('count'), default=3,
                                             help_text=_('Number of entries to display'))
    twitter_id = models.CharField(_('twitter id'), max_length=75,
                                 help_text=_(u'See https://twitter.com/settings/widgets on how to obtain one'))

    def __unicode__(self):
        return self.title
