from aiohttp import web


async def get(request):
    return web.Response(text="pong")
