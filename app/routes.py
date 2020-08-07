# -*- coding: utf-8 -*-
from app import app
from flask import render_template,flash, redirect, request
from app.forms import AddForm,SearchForm
from datetime import date,datetime
from app.db_setup import init_db, db_session
from app.models import Item
from app import db
from app.tables import Result

@app.route('/')
@app.route('/index')
def index():
    today=date.today()
    items=Item.query.filter(Item.day==today).all()
    table=Result(items)
    table.border = True
    totaltoday = 0
    count=0
    for i in items:
        if i.day == date.today():
            totaltoday+=i.price
            count+=1
    return render_template('index.html',table=table,today=today,total=totaltoday,count=count)

@app.route('/additems', methods=['GET','POST'])
def additems():
    form = AddForm()
    if request.method=='POST' and form.validate():
        #save item:
        item = Item()
        save_changes(item, form, new=True)
        flash('Item added successfully')
        return redirect('/index')
    return render_template('additems.html', form=form)

def save_changes(item,form, new=False):
    item.typename=form.typename.data
    item.itemname=form.itemname.data
    item.size_i=form.size_i.data
    item.price=form.price.data
    if new:
        item.day=date.today()
    #item.numb=form.numb.data
    #item.isold=False

    if new:
        db.session.add(item)

    db.session.commit()

@app.route('/item/<int:id>', methods=['GET','POST'])
def delete(id):
    qry = db.session.query(Item).filter(Item.id==id)
    item = qry.first()
    db.session.delete(item)
    db.session.commit()
    flash('Deleted succesfuly!')
    return redirect('/')

@app.route('/item/<int:id>', methods=['GET','POST'])
def edit(id):
    qry=db.session.query(Item).filter(Item.id==id)
    items=qry.first()
    if items:
        form = AddForm(formdata=request.form, obj=items)
        if request.method=='POST'and form.validate():
            #save edited
            save_changes(items,form)
            flash('Edited succesfuly!')
            return redirect('/')
        return render_template('edititem.html',form=form)
    else:
        return 'Error loading #{id}'.format(id=id)

def clear_data():
    meta = db.metadata
    for table in reversed(meta.sorted_tables):
        db.session.execute(table.delete())
    db.session.commit()

@app.route('/search',methods=['GET','POST'])
def search():
    form=SearchForm()
    search=SearchForm(request.form)
    if request.method=='POST':
        return result(search)
    return render_template('search.html',form=form)

@app.route('/result')
def result(search):
    results=[]
    #search_type=search.get('select')
    search_string=search.data['search']

    if search.data['search']=='':
        qry=db.session.query(Item)
        results=qry.all()
    else:
        select=search.data['select']
        items=[]
        qry=db.session.query(Item)
        items=qry.all()
        count_in_date=0
        for i in items:
            if select=='Type':
                if i.typename == search_string:
                    results.append(i)
                    count_in_date += 1
            elif select=='Name':
                if i.itemname == search_string:
                    results.append(i)
                    count_in_date += 1
            elif select=='Size':
                if i.size_i==int(search_string):
                    results.append(i)
                    count_in_date += 1
            elif select == 'Price':
                if i.price == int(search_string):
                    results.append(i)
                    count_in_date += 1
            elif select == 'Date':
                if search_string in str(i.day):
                    count_in_date += 1
                    results.append(i)
            # if i.Type==search_string:
            #     results.append(i)
    if not results:
        flash('Not found!')
        return redirect('/')
    
    else:
        table=Result(results)
        table.border=True
        totalprice=0
        for i in results:
            totalprice+=i.price
        return render_template('result.html',table=table,totalprice=totalprice,count_in_date=count_in_date)

@app.route('/showitems', methods=['GET','POST'])
def showitems():
    items=[]
    #items_string=AddForm.data
    qry = db.session.query(Item)
    items = qry.all()
    table = Result(items)
    table.border = True
    totaltoday = 0
    for i in items:
        if i.day == date.today():
            totaltoday+=i.price
    if request.method == 'POST':
        clear_data()
        flash('Cleaned!')
        return redirect('/index')
    return render_template('showitems.html',table=table,totaltoday=totaltoday)

# if __name__ == '__main__':
#     app.run(debug=True, host="0.0.0.0", port=8000)


# >>> db.session.delete(me)
# >>> db.session.commit()

    # typename='aaa'
    # itemname='blue'
    # size_i=38
    # price=700
    # db='dataset'
    # con = pymysql.connect(typename=typename,itemname=itemname,size_i=size_i,price=price,db=db, use_unicode=True, charset='utf8')
    # #con = pymysql.connect(use_unicode=True, charset='utf8')
    # cur = con.cursor()
    # cur.execute("SELECT * FROM dataset")
    # data = cur.fetchall()   
    # return render_template("showitems.html", value=data)
