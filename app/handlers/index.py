from aiohttp import web
from configs import ALLOWED_BRANCHES


async def get(request):
    return web.Response(
        text="GithubBranchProtector is running and giving a success status to commits from these branches:\n{}".format(
            '\n'.join(['- ' + branch for branch in ALLOWED_BRANCHES])))
