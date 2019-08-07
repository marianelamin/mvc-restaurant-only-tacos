#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
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
import webapp2
import os
import random
import jinja2
#import taco_model

from google.appengine.ext import ndb


class TacoFillingModel(ndb.Model):
    #list here all the properties of the entity
    tacoIn = ndb.StringProperty(required=True)



def get_bill():
    # Add a list of fortunes to the empty fortune_list array
    bill_list=[10, 15.5, 20, 25.5, 30]
    # Use the random library to return a random element from the array
    random_bill = random.choice(bill_list)
    return random_bill

def get_tacos():
    # Add a list of fortunes to the empty fortune_list array
    filling_list = get_all_tacos()
    # Use the random library to return a random element from the array
    if len(filling_list) == 0:
        random_filling = 'test-filling'
    else:
        random_filling = random.choice(filling_list)
    return random_filling

def get_all_tacos():
    #fillings = ['steak', 'carnitas', 'veggie', 'chicken', 'ground beef']
    fillings = TacoFillingModel.query().filter().fetch()
    only_fillings = []
    for fil in fillings:
        only_fillings.append(str(fil.tacoIn))
    return only_fillings

# Remember, you can get this by searching for jinja2 google app engine
jinja_current_directory = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class TacosHandler(webapp2.RequestHandler):
    def get(self):
        results_template = jinja_current_directory.get_template('template/tacos_results.html')
        self.response.write(results_template.render(tacoType = get_tacos()))

    #this gets executed when you use a form with POST method and /tacos route
    def post(self):
        # get input from the html form
        new_filling_from_form = self.request.get('new-filling')
        tacoFilling1 = TacoFillingModel( tacoIn = new_filling_from_form)
        k = tacoFilling1.put()
        results_template = jinja_current_directory.get_template('template/add_taco.html')
        self.response.write(results_template.render(filling = k.get().tacoIn))


class BillHandler(webapp2.RequestHandler):
    def get(self):
        results_template = jinja_current_directory.get_template('template/bill_results.html')
        self.response.write(results_template.render(total = str(get_bill())))

    # def post(self):


class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
        results_template = jinja_current_directory.get_template('template/welcome.html')
        self.response.write(results_template.render())


class AllFillingsHandler(webapp2.RequestHandler):
    def get(self):
        #results_template = jinja_current_directory.get_template('template/welcome.html')
        #self.response.write(results_template.render())
        self.response.write(get_all_tacos())

# Route mapping
app = webapp2.WSGIApplication([
    # This line routes the main url ('/')  - also know as
    # The root route - to the Fortune Handler
    ('/', WelcomeHandler),
    ('/tacos', TacosHandler), #maps '/predict' to the TacosHandler
    ('/bill', BillHandler), #maps '/farewell' to the BillHandler
    ('/fillings', AllFillingsHandler),
], debug=True)
