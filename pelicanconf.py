AUTHOR = u'Pinry Contributors'
SITENAME = u'Pinry'
SITEURL = 'http://getpinry.com'


TIMEZONE = 'America/New_York'
DEFAULT_LANG = u'en'
THEME = 'theme'
TYPOGRIFY = True
JINJA_EXTENSIONS = (
    'jinja2.ext.loopcontrols',
)


TEMPLATE_PAGES = {
    'about.html': 'about/index.html',
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


LINKS = (
    ('About', '/about/'),
    ('Code', 'https://github.com/pinry/pinry'),
    ('Issues', 'https://github.com/pinry/pinry/issues'),
    ('Deployment', 'https://github.com/pinry/docker-pinry'),
)
