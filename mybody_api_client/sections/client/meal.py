#
# (c) 2023, Yegor Yakubovich, yegoryakubovich.com, personal@yegoryakybovich.com
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


from mybody_api_client.sections.admin.base import RequestTypes, BaseSection


class Meal(BaseSection):
    prefix = 'meals'

    async def get(self, id_: int):
        path = '/get'
        response = await self.request(
            type_=RequestTypes.GET,
            path=path,
            parameters={
                'id': id_,
            },
        )
        return response

    async def get_list(self, account_service_id: int, date: str = None):
        path = '/list/get'
        response = await self.request(
            type_=RequestTypes.GET,
            path=path,
            parameters={
                'account_service_id ': account_service_id,
                'date': date,
            },
        )
        return response

    async def get_product(self, id_: int):
        path = '/products/get'
        response = await self.request(
            type_=RequestTypes.GET,
            path=path,
            parameters={
                'id': id_,
            },
        )
        return response

    async def get_list_products(self, meal_id: int):
        path = '/products/list/get'
        response = await self.request(
            type_=RequestTypes.GET,
            path=path,
            parameters={
                'meal_id': meal_id,
            },
        )
        return response
