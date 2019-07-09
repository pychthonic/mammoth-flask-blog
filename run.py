from mammothflaskblog import create_app
from flask_talisman import Talisman

csp = {
        'default-src': ['\'self\'',
        	'*.facebook.com',
        	'*.paypal.com',
        	'*.facebook.net',
        	'*.paypalobjects.com',
        	'*.twitter.com',
                '*.bootstrapcdn.com',
                '*.jquery.com',

                ],
        'script-src': ['\'self\'',
        	'*.facebook.com',
        	'*.paypal.com',
        	'*.facebook.net',
        	'*.paypalobjects.com',
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
	app.run(threaded=True, debug=True)

        # host="10.0.0.101", 