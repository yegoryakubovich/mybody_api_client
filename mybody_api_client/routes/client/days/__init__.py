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


class ClientDayRoute(BaseRoute):
    _prefix = '/days'

    async def update_water_intake(
            self,
            id_: int,
            water_intake: int,
    ):
        return await self._request(
            type_=RequestTypes.POST,
            prefix='/water-intake/update',
            parameters={
                'id': id_,
                'water_intake': water_intake,
            },
        )

    async def get(
            self,
            id_: int,
    ):
        return await self._request(
            type_=RequestTypes.GET,
            prefix='/get',
            parameters={
                'id': id_,
            },
            response_key='day',
        )

    async def get_by_date(
            self,
            account_service_id: int,
            date: str,
    ):
        return await self._request(
            type_=RequestTypes.GET,
            prefix='/by-date/get',
            parameters={
                'account_service_id': account_service_id,
                'date': date,
            },
            response_key='day',
        )

    async def get_list(
            self,
            account_service_id: int,
    ):
        return await self._request(
            type_=RequestTypes.GET,
            prefix='/list/get',
            parameters={
                'account_service_id': account_service_id,
            },
            response_key='days',
        )
