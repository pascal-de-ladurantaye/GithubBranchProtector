from aiohttp import web

from app.services.statusservice import StatusService
from configs import ALLOWED_BRANCHES


async def hook(request):
    data = await request.json()
    ref = data['ref']
    after_sha = data['after']
    repo = data['repository']['full_name']

    branch = ref.split('/')[-1]

    if branch in ALLOWED_BRANCHES:
        StatusService.set_status('success', 'Commit is on an allowed branch for merging', 'GithubBranchProtector:{}'.format(branch), repo, after_sha)

    return web.Response(text='')
