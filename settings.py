import os

##### Web server settings

HOST = os.environ.get('HOST', '127.0.0.1')
PORT = os.environ.get('PORT', 8080)
DEBUG = os.environ.get('OMNIC_ENV', 'dev') == 'prod'


##### Security settings

# Whitelist allowed foreign hosts. This should point to your app servers, your
# CDN, or cloud hosting such as your S3 buckets.
ALLOWED_LOCATIONS = {
    'github.com',
    'michaelb.org',
    'omnic.michaelb.org',
    'whiteboard.michaelb.org',
    'openlab.org',
    'michaelpb.github.io',
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
