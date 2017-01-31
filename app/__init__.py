from aiohttp import web

from .handlers.hook import hook
from .handlers.index import get as index
from .handlers.ping import get as ping

APP = web.Application()

APP.router.add_route('GET', '/', index)
APP.router.add_route('GET', '/ping', ping)
APP.router.add_route('POST', '/hook', hook)
