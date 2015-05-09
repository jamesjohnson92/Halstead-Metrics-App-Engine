from gaesessions import SessionMiddleware
from google.appengine.ext.appstats import recording

COOKIE_KEY = """\x13\xa7~!!\xcd\xae\x88\x93\xff\x0bU\x92\x96J\xe9\xb1g\xb4\xb1@\xfc\xf4\x07U@z\x14C\x88\x1b\xf5*2%\x08v\x0b\xb7~\x15.\xc5#X\x9d\x97\x928\xe6\xa5\x07d\xebn\xc6\xab\x97K\xcf\x19\xb7\xb0D"""

def webapp_add_wsgi_middleware(app):
    app = SessionMiddleware(app,cookie_key = COOKIE_KEY)
    app = recording.appstats_wsgi_middleware(app)
    return app
