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


from .admin import Account
from .admin import Country
from .admin import Currency
from .admin import Language
from .admin import ServiceNotification
from .admin import Service
from .admin import Role
from .admin import Session
from .admin import Text
from .admin import Article
from .admin import Product
from .admin import Timezone
from .admin import Training
from .admin import Exercise
from .admin import Permission
from .admin import Meal


admin = [
    Account,
    Article,
    Country,
    Currency,
    Language,
    ServiceNotification,
    Role,
    Service,
    Session,
    Text,
    Timezone,
    Product,
    Training,
    Exercise,
    Permission,
    Meal,
]
