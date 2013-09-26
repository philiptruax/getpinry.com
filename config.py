from __future__ import unicode_literals


AUTHOR = 'Pinry Contributors'
SITENAME = 'Pinry'
SITEURL = 'http://getpinry.com'
RELATIVE_URLS = True
THEME = 'theme'


JINJA_EXTENSIONS = (
    'jinja2.ext.loopcontrols',
)


TEMPLATE_PAGES = {
    'about.html': 'about/index.html',
}
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/apple-touch-icon-114x114-precomposed.png': {'path': 'apple-touch-icon-114x114-precomposed.png'},
    'extra/apple-touch-icon-57x57-precomposed.png': {'path': 'apple-touch-icon-57x57-precomposed.png'},
    'extra/apple-touch-icon-72x72-precomposed.png': {'path': 'apple-touch-icon-72x72-precomposed.png'},
    'extra/apple-touch-icon.png': {'path': 'apple-touch-icon.png'},
    'extra/apple-touch-icon-precomposed.png': {'path': 'apple-touch-icon-precompsed.png'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/humans.txt': {'path': 'humans.txt'},
    'extra/robots.txt': {'path': 'robots.txt'},
}
STATIC_PATHS = (
    'extra/CNAME',
    'extra/apple-touch-icon-114x114-precomposed.png',
    'extra/apple-touch-icon-57x57-precomposed.png',
    'extra/apple-touch-icon-72x72-precomposed.png',
    'extra/apple-touch-icon.png',
    'extra/apple-touch-icon-precomposed.png',
    'extra/favicon.ico',
    'extra/humans.txt',
    'extra/robots.txt',
)


LINKS = (
    ('About', '/about/'),
    ('Docs', 'https://pinry.readthedocs.org/'),
    ('Issues', 'https://github.com/pinry/pinry/issues'),
)

