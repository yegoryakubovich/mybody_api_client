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


class ClientCurrencyRoute(BaseRoute):
    _prefix = '/currencies'

    async def get(self, id_str: str):
        return await self._request(
            type_=RequestTypes.GET,
            prefix='/get',
            token_required=False,
            parameters={
                'id_str': id_str,
            },
            response_key='currency',
        )

    async def get_list(self):
        return await self._request(
            type_=RequestTypes.GET,
            prefix='/list/get',
            token_required=False,
            response_key='currencies',
        )

