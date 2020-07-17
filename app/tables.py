from flask_table import Table, Col, LinkCol

class Result(Table):
    id=Col('Id')
    #numb=Col('Number')
    typename=Col('Type')
    itemname=Col('Name')
    size_i=Col('Size')
    price=Col('Price')
    day=Col('Date')
    edit=LinkCol('Edit','edit',url_kwargs=dict(id='id'))
    #isold=Col('Is sold')