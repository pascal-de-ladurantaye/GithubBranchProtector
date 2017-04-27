from aiohttp import web

from configs import PATH_PREFIX
from .handlers.hook import hook
from .handlers.index import get as index
from .handlers.ping import get as ping

APP = web.Application()

APP.router.add_route('GET', PATH_PREFIX + '/', index)
APP.router.add_route('GET', PATH_PREFIX + '/ping', ping)
APP.router.add_route('POST', PATH_PREFIX + '/hook', hook)
