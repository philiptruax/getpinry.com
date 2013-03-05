#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'Pinry Contributors'
SITENAME = u'Pinry'
SITEURL = 'http://getpinry.com'

TIMEZONE = 'America/New_York'
DEFAULT_LANG = u'en'

DEFAULT_PAGINATION = 5
DEFAULT_DATE_FORMAT = '%d %b %Y'

JINJA_EXTENSIONS = (
    'jinja2.ext.loopcontrols',
)

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

FILES_TO_COPY = (
    ('extra/CNAME', 'CNAME'),
    ('extra/apple-touch-icon-114x114-precomposed.png', 'apple-touch-icon-114x114-precomposed.png'),
    ('extra/apple-touch-icon-57x57-precomposed.png', 'apple-touch-icon-57x57-precomposed.png'),
    ('extra/apple-touch-icon-72x72-precomposed.png', 'apple-touch-icon-72x72-precomposed.png'),
    ('extra/apple-touch-icon.png', 'apple-touch-icon.png'),
    ('extra/apple-touch-icon-precomposed.png', 'apple-touch-icon-precomposed.png'),
    ('extra/favicon.ico', 'favicon.ico'),
    ('extra/humans.txt', 'humans.txt'),
    ('extra/robots.txt', 'robots.txt'),
)

MENUITEMS =  (
    ('BitBucket Repo (Primary)', 'https://bitbucket.org/pinry/pinry/'),
    ('GitHub Repo (Mirror)', 'https://github.com/pinry/pinry/'),
    ('Issue Tracker', 'https://bitbucket.org/pinry/pinry/issues/'),
    ('Contact Us', 'mailto:devs@getpinry.com'),
)
