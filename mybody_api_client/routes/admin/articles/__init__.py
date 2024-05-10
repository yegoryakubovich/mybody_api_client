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
from .translations import AdminArticleTranslationRoute


class AdminArticleRoute(BaseRoute):
    _prefix = '/articles'

    translations = AdminArticleTranslationRoute()

    async def create(
            self,
            name: str,
    ):
        return await self._request(
            type_=RequestTypes.POST,
            prefix='/create',
            parameters={
                'name': name,
            },
            response_key='id',
        )

    async def delete(
            self,
            id_: int,
    ):
        return await self._request(
            type_=RequestTypes.POST,
            prefix='/delete',
            parameters={
                'id': id_,
            },
        )

    async def update(
            self,
            id_: int,
            is_hide: bool,
            can_guest: bool,
    ):
        return await self._request(
            type_=RequestTypes.POST,
            prefix='/update',
            parameters={
                'id': id_,
                'is_hide': is_hide,
                'can_guest': can_guest,
            },
        )

    async def update_md(
            self,
            id_: int,
            md: str,
            language: str = None,
            name: str = None,
    ):
        return await self._request(
            type_=RequestTypes.POST,
            prefix='/md/update',
            parameters={
                'id': id_,
                'language': language,
                'md': md,
                'name': name,
            },
        )
