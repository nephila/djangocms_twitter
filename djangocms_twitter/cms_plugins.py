from django.utils.translation import ugettext_lazy as _
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import TwitterRecentEntries, TwitterSearch


class TwitterRecentEntriesPlugin(CMSPluginBase):
    model = TwitterRecentEntries
    name = _("Twitter")
    render_template = "cms/plugins/twitter_timeline.html"
    
    def render(self, context, instance, placeholder):
        context.update({
            'object': instance,
        })
        return context
    
plugin_pool.register_plugin(TwitterRecentEntriesPlugin)


class TwitterSearchPlugin(CMSPluginBase):
    model = TwitterSearch
    name = _("Twitter Search")
    render_template = "cms/plugins/twitter_search_widget.html"
    admin_preview = False
    
    def render(self, context, instance, placeholder):
        context.update({
            'object': instance,
        })
        return context
plugin_pool.register_plugin(TwitterSearchPlugin)