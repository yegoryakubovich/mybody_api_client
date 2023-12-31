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


from mybody_api_client.utils.base_section import BaseSection, RequestTypes


class Training(BaseSection):
    prefix = 'trainings'

    async def get(self, id_: int):
        path = '/get'
        response = await self.request(
            type_=RequestTypes.GET,
            path=path,
            parameters={
                'id': id_,
            },
            response_key='training',
        )
        return response

    async def get_list(self, account_service_id: int):
        path = '/list/get'
        response = await self.request(
            type_=RequestTypes.GET,
            path=path,
            parameters={
                'account_service_id': account_service_id,
            },
            response_key='trainings',
        )
        return response

    async def get_exercise(self, id_: int):
        path = '/exercises/get'
        response = await self.request(
            type_=RequestTypes.GET,
            path=path,
            token_required=False,
            parameters={
                'id': id_,
            },
            response_key='training_exercise',
        )
        return response

    async def get_list_exercise(self, training_id: int):
        path = '/exercises/list/get'
        response = await self.request(
            type_=RequestTypes.GET,
            path=path,
            token_required=False,
            parameters={
                'training_id': training_id,
            },
            response_key='training_exercises',
        )
        return response
