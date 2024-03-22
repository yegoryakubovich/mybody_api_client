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


from mybody_api_client.utils import BaseRoute
from .accounts import ClientAccountRoute
from .articles import ClientArticleRoute
from .payments import ClientPaymentRoute
from .promocodes import ClientPromocodeRoute
from .countries import ClientCountryRoute
from .currencies import ClientCurrencyRoute
from .exercises import ClientExerciseRoute
from .images import ClientImageRoute
from .languages import ClientLanguageRoute
from .meals import ClientMealRoute
from .products import ClientProductRoute
from .services import ClientServiceRoute
from .sessions import ClientSessionRoute
from .texts import ClientTextRoute
from .timezones import ClientTimezoneRoute
from .trainings import ClientTrainingRoute
from .urls import ClientUrlRoute


class ClientRoute(BaseRoute):
    accounts = ClientAccountRoute()
    articles = ClientArticleRoute()
    payments = ClientPaymentRoute()
    promocodes = ClientPromocodeRoute()
    countries = ClientCountryRoute()
    currencies = ClientCurrencyRoute()
    exercises = ClientExerciseRoute()
    images = ClientImageRoute()
    languages = ClientLanguageRoute()
    meals = ClientMealRoute()
    products = ClientProductRoute()
    services = ClientServiceRoute()
    sessions = ClientSessionRoute()
    texts = ClientTextRoute()
    timezones = ClientTimezoneRoute()
    trainings = ClientTrainingRoute()
    urls = ClientUrlRoute()
