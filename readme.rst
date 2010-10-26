Usage
=====

Basic Usage::

	from alert_grid.base import ping
	ping('YOUR API ID', 'YOUR RECEIVER NAME')
	
Returns `True` if successful or raises one of the excpetions in
`alert_grid.exceptions`.