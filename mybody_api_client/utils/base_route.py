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


class RequestTypes:
    GET = 'get'
    POST = 'post'
    UPDATE = 'update'
    DELETE = 'delete'


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

    def request(self, type_: RequestTypes):
        pass