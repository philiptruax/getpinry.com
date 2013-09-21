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
    ('About', '/about/'),
    ('Code', 'https://github.com/pinry/pinry'),
    ('Issues', 'https://github.com/pinry/pinry/issues'),
    ('Deployment', 'https://github.com/pinry/docker-pinry'),
)
