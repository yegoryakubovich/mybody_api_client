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


class ClientProductRoute(BaseRoute):
    _prefix = '/products'

    async def get(self, id_: int):
        return await self._request(
            type_=RequestTypes.GET,
            prefix='/get',
            token_required=False,
            parameters={
                'id': id_,
            },
            response_key='product',
        )

    async def get_list(self, type_: str = None):
        return await self._request(
            type_=RequestTypes.GET,
            prefix='/list/get',
            token_required=False,
            parameters={
                'type': type_,
            },
            response_key='products',
        )
