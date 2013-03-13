#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'Pinry Contributors'
SITENAME = u'Pinry'
SITEURL = 'http://getpinry.com'

TIMEZONE = 'America/New_York'
DEFAULT_LANG = u'en'

DEFAULT_PAGINATION = 5
DEFAULT_DATE_FORMAT = '%d %b %Y'

THEME = 'theme'
TYPOGRIFY = True

JINJA_EXTENSIONS = (
    'jinja2.ext.loopcontrols',
)

ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

TEMPLATE_PAGES = {
    'tour.html': 'tour/index.html',
    'docs.html': 'docs/index.html',
    'blog.html': 'blog/index.html',
    'contact.html': 'contact/index.html',
}

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

LINKS = (
    ('Code', 'https://github.com/pinry/pinry/'),
    ('Tour', '/tour/'),
    ('Docs', '/docs/'),
    ('Blog', '/blog/'),
    ('Contact', '/contact/'),
)

SOCIAL = (
    ('Feed', '/feeds/all.atom.xml'),
    ('Twitter', 'https://twitter.com/getpinry'),
)

ISSUETRACKER = 'https://github.com/pinry/pinry/issues'
