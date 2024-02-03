#
# (c) 2024, Yegor Yakubovich, yegoryakubovich.com, personal@yegoryakybovich.com
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


from addict import Dict
from aiohttp import ClientSession
from furl import furl

from mybody_api_client.utils.exceptions import ApiException
from mybody_api_client.utils.exceptions_manager import exceptions


class RequestTypes:
    GET = 'get'
    POST = 'post'


class BaseRoute:
    url: str = ''
    prefix: str = ''
    token: str = None

    def __init__(self, url: str = None, token: str = None):
        if not url:
            return

        self.url = url + self.prefix
        self.token = token
        for i in dir(self):
            if issubclass(eval(f'type(self.{i})'), BaseRoute):
                route: BaseRoute = eval(f'self.{i}')
                route.__init__(url=self.url, token=self.token)

    async def create_url(self, prefix: str, parameters: dict) -> str:
        f = furl(url=self.url+prefix)
        f.set(args=parameters)
        return f.url

    async def request(
            self,
            type_: str = RequestTypes.GET,
            prefix: str = '/',
            token_required: bool = True,
            parameters: dict = None,
            response_key: str = None,
    ):
        parameters = parameters or {}
        json = {}
        if (token_required and self.token) or self.token:
            parameters['token'] = self.token

        if type_ == RequestTypes.POST:
            json = parameters
            parameters = {}

        url = await self.create_url(
            prefix=prefix,
            parameters=parameters,
        )

        async with ClientSession() as session:

            if type_ == RequestTypes.GET:
                response = await session.get(url=url)
            elif type_ == RequestTypes.POST:
                response = await session.post(url=url, json=json)

        response_json = await response.json()
        response = Dict(**response_json)

        if response.state == 'successful':
            if response_key:
                response = response.get(response_key)

            return response
        elif response.state == 'error':
            try:
                raise exceptions[response.error.code](message=response.error.message, kwargs=response.error.kwargs)
            except TypeError:
                raise ApiException(message=response.error.message or response.message, kwargs=response.error.kwargs)