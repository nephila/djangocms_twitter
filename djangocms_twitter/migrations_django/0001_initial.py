# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_auto_20151112_1654'),
    ]

    operations = [
        migrations.CreateModel(
            name='TwitterRecentEntries',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=75, verbose_name='title', blank=True)),
                ('twitter_user', models.CharField(max_length=75, verbose_name='twitter user')),
                ('count', models.PositiveSmallIntegerField(default=3, help_text='Number of entries to display', verbose_name='count')),
                ('link_hint', models.CharField(help_text='Deprecated: no longer used by Twitter widgets.', max_length=75, verbose_name='link hint', blank=True)),
                ('twitter_id', models.CharField(help_text='See https://twitter.com/settings/widgets on how to obtain one', max_length=75, verbose_name='twitter id')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='TwitterSearch',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=75, verbose_name='title', blank=True)),
                ('query', models.CharField(default=b'', help_text='Deprecated: no longer used by Twitter widgets. Define one when creating widgets.', max_length=200, verbose_name='query', blank=True)),
                ('count', models.PositiveSmallIntegerField(default=3, help_text='Number of entries to display', verbose_name='count')),
                ('twitter_id', models.CharField(help_text='See https://twitter.com/settings/widgets on how to obtain one', max_length=75, verbose_name='twitter id')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
