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


from mybody_api_client.utils import BaseRoute, RequestTypes
from .services import AdminAccountServiceRoute
from .roles import AdminAccountRolesRoute


class AdminAccountRoute(BaseRoute):
    _prefix = '/accounts'

    services = AdminAccountServiceRoute()
    roles = AdminAccountRolesRoute()

    async def update(
            self,
            id_: int,
            username: str,
            firstname: str,
            lastname: str,
            surname: str,
            country: str,
            language: str,
            timezone: str,
            currency: str,
    ):
        return await self._request(
            type_=RequestTypes.POST,
            prefix='/update',
            parameters={
                'id': id_,
                'username': username,
                'firstname': firstname,
                'lastname': lastname,
                'surname': surname,
                'country': country,
                'language': language,
                'timezone': timezone,
                'currency': currency,
            },
        )

    async def get(self, id_: int = None):
        return await self._request(
            type_=RequestTypes.POST,
            prefix='/get',
            parameters={
                'id': id_,
            },
            response_key='account',
        )

    async def search(self, id_: int = None, username: str = None, page: int = None):
        return await self._request(
            type_=RequestTypes.POST,
            prefix='/search',
            parameters={
                'id': id_,
                'username': username,
                'page': page,
            },
        )

    async def change_password(self, account_id: int):
        return await self._request(
            type_=RequestTypes.POST,
            prefix='/password/change',
            parameters={
                'account_id': account_id,
            },
            response_key='new_password',
        )

