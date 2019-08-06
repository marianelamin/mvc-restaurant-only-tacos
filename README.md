# mvc-restaurant-only-tacos

An example for my NEIU CSSI X students.  You can find the website on https://mvc-restaurant-only-tacos.appspot.com/

1. HTML
2. CSS
3. JS
4. Python and Jinja2
5. AppEngine - routes and handlers
6. DataStore

All my static/dynamic html files currently are in the folder named ```template```.


### There are 4 handlers:
```
('/', HelloHandler), #this is the landing page
('/tacos', TacosHandler), #this shows the type of taco selected for you, also a POST request to add a new filling
('/bill', BillHandler), #this selects a random amount to pay for the bill
('/fillings', AllFillingsHandler) #this shows the recommended fillings that the restaurant has so far.
```

### Data Model
The FillingTaco data model has only one property: ```inTaco``` (the filling)