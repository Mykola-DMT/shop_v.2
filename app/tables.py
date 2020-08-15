from flask_table import Table, Col, LinkCol, ButtonCol, BoolCol

class Result(Table):
    id=Col('Id', show=False)
    #numb=Col('Number')
    typename=Col('Type')
    itemname=Col('Name')
    size_i=Col('Size')
    price=Col('Price')
    day=Col('Date')
    issold=BoolCol('Sold')
    edit=LinkCol('Edit','edit',url_kwargs=dict(id='id'))
    dalete=ButtonCol('Delete','delete',url_kwargs=dict(id='id'))
    #isold=Col('Is sold')