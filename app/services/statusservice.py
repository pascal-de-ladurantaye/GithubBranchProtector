import json

import aiohttp

from configs import GITHUB_USERNAME, GITHUB_PERSONAL_ACCESS_TOKEN


class StatusService:
    @staticmethod
    async def set_status(status, description, context, repo_full_name, commit_sha):
        if status not in ['success', 'failure', 'error', 'pending']:
            raise ValueError('invalid status')

        payload = {
            'state': status,
            'description': description,
            'context': context
        }

        url = 'https://api.github.com/repos/{}/statuses/{}'.format(repo_full_name, commit_sha)
        headers = {'content-type': 'application/json'}
        async with aiohttp.ClientSession(auth=aiohttp.BasicAuth(GITHUB_USERNAME, GITHUB_PERSONAL_ACCESS_TOKEN)) as session:
            async with session.post(url, headers=headers, data=json.dumps(payload)) as r:
                await r.json()
