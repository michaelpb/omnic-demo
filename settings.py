import os

##### Web server settings

HOST = os.environ.get('HOST', '127.0.0.1')
PORT = int(os.environ.get('DOKKU_DOCKERFILE_PORTS', '8080'))
DEBUG = os.environ.get('OMNIC_ENV', 'dev') == 'prod'

EXTERNAL_HOST = os.environ.get('DOMAIN') or None
EXTERNAL_PORT = 80

if os.environ.get('DOKKU_APP_TYPE'):
    DEBUG = False


##### Security settings

ALLOWED_LOCATIONS = {
    'github.com',
    'michaelb.org',
    'omnic.michaelb.org',
    'whiteboard.michaelb.org',
    'openlab.org',
    'michaelpb.github.io',
    'raw.githubusercontent.com',
}


SECURITY = 'omnic.web.security.HmacSha1'
HMAC_SECRET = os.environ.get('HMAC_SECRET')
if not HMAC_SECRET or len(HMAC_SECRET) < 8:
    raise Exception('Invalid secret, stopping')


##### Conversion settings

# Conversion graph settings
CONVERSION_PROFILES = {
    # Add in profiles here, like the following:
    # 'media-gallery-thumb.png': ('PNG', 'thumb.png:300x300'),
}

# Where to store cache
PATH_PREFIX = '/var/tmp/omnic/'
