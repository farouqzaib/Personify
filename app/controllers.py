from flask.views import MethodView
from flask import request

from services import EventService

import json

def index():
	return 'index'


class Events(MethodView):

	def post(self):
		payload = request.json
		#at the very least, events should have; action, user, item.
		errors = []
		if 'action' not in payload:
			errors.append('Event must be associated with an action')

		if 'user' not in payload:
			errors.append('Event must be associated with a user')

		if 'item' not in payload:
			errors.append('Event must be associated with an item')

		if 'created_at' not in payload:
			errors.append('Event must be associated with a date and time')

		if errors:
			return json.dumps({'status': 'error', 'message': errors, 'code': 'P01'})

		try:
			EventService.create(payload)
		except Exception as e:
			return json.dumps({'status': 'error', 'message': e.message})

		return json.dumps({'status': 'success', 'data': payload})
