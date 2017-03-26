from controllers import Events, index

def register_routes(app):
	app.add_url_rule('/', 'index', index)
	app.add_url_rule('/events', view_func=Events.as_view('events'))
