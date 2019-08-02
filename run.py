from mammothflaskblog import create_app
from flask_talisman import Talisman

csp = {
        'default-src': ['\'self\'',
                '*.facebook.com',
                '*.facebook.net',
                '*.twitter.com',
                '*.bootstrapcdn.com',
                '*.jquery.com',
                ],
        'script-src': ['\'self\'',
                '*.facebook.com',
                '*.facebook.net',
                '*.twitter.com',
                '*.bootstrapcdn.com',
                '*.jquery.com',
                '*.cloudflare.com']
        }

app = create_app()

talisman = Talisman(app,
        content_security_policy=csp,
        content_security_policy_nonce_in=['script-src']
        )

if __name__ == '__main__':
        app.run(
                host="127.0.0.1",
                port=5001,
                threaded=True,
                debug=True)