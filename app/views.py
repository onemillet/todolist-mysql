#encoding:utf-8
from app import app,db
from flask import  render_template,request,redirect,url_for
from models import TodoList
from forms import TodoListForm,ModifyForm

#这里被迫使用正则和编码转化
# import sys
# sys.getdefaultencoding()
# reload(sys)
# sys.setdefaultencoding('UTF-8')
# sys.getdefaultencoding()
# import re

#regex = re.compile('<.*?value="(.*?)">')
#这里被迫使用正则和编码转化

@app.route('/')
def index():
    page_index = request.args.get('page',1,type=int)
    query=TodoList.query.order_by(TodoList.create_time.desc())
    pagination=query.paginate(page_index,per_page=10,error_out=False)
    #todolists=TodoList.query.all()
    todolists=pagination.items
    form=TodoListForm()
    return render_template('index.html',todolists=todolists,form=form,
                           pagination=pagination)

@app.route('/add',methods=['POST','GET'])
def add():
    #form=request.form
    #直接使用前端request传来的数据实例化form
    #form=TodoListForm(request.form)
    form=TodoListForm()
    #form.content=request.form['content']

    if form.validate_on_submit():
        form.content = request.form['content']
        todolist=TodoList()
        todolist.content=form.content
        db.session.add(todolist)
        db.session.commit()

    # todolists=TodoList.query.order_by(TodoList.create_time.desc())
    # todolists=todolists.all()
    # return render_template('index.html', todolists=todolists, form=form)

    #翻页的时候会报错
    # page_index = request.args.get('page', 1, type=int)
    # query = TodoList.query.order_by(TodoList.create_time.desc())
    # pagination = query.paginate(page_index, per_page=10, error_out=False)
    # todolists = pagination.items
    # return render_template('index.html',todolists=todolists,form=form,
    #                        pagination=pagination)
    return redirect(url_for('index'))

@app.route('/finish/<int:todolist_id>')
def finish(todolist_id):
    form=TodoListForm()
    todolist=TodoList.query.get_or_404(todolist_id)
    todolist.status=1
    db.session.add(todolist)
    db.session.commit()

    #todolists=TodoList.query.all()
    # page_index = request.args.get('page', 1, type=int)
    # query = TodoList.query.order_by(TodoList.create_time.desc())
    # pagination = query.paginate(page_index, per_page=10, error_out=False)
    # todolists = pagination.items
    # return render_template('index.html', todolists=todolists, form=form,
    #                        pagination=pagination)
    return redirect(url_for('index'))

@app.route('/unfinish/<int:todolist_id>')
def unfinish(todolist_id):
    form=TodoListForm()
    todolist=TodoList.query.get_or_404(todolist_id)
    todolist.status=0
    db.session.add(todolist)
    db.session.commit()

    #todolists=TodoList.query.all()
    # page_index = request.args.get('page', 1, type=int)
    # query = TodoList.query.order_by(TodoList.create_time.desc())
    # pagination = query.paginate(page_index, per_page=10, error_out=False)
    # todolists = pagination.items
    # return render_template('index.html', todolists=todolists, form=form,
    #                        pagination=pagination)
    return redirect(url_for('index'))

@app.route('/delete/<int:todolist_id>')
def delete(todolist_id):
    form = TodoListForm()
    todolist=TodoList.query.get_or_404(todolist_id)
    db.session.delete(todolist)
    db.session.commit()

    # todolists = TodoList.query.order_by(TodoList.create_time.desc())
    # todolists = todolists.all()
    # return render_template('index.html', todolists=todolists, form=form)

    #翻页的时候会报错
    # page_index = request.args.get('page', 1, type=int)
    # query = TodoList.query.order_by(TodoList.create_time.desc())
    # pagination = query.paginate(page_index, per_page=10, error_out=False)
    # todolists = pagination.items
    # return render_template('index.html', todolists=todolists, form=form,
    #                        pagination=pagination)
    return redirect(url_for('index'))

@app.route('/modify/<int:todolist_id>',methods=['POST','GET'])
def modify(todolist_id):
    form_t=TodoListForm()
    form_m=ModifyForm()
    todolist=TodoList.query.get_or_404(todolist_id)
    if form_m.validate_on_submit():
        #？？？？？？？？？？？？？？？？
        #此处要用正则才能取得所需数据
        # content=re.findall(regex,str(form_m.content))[0]
        # todolist.content=u'%s' % content
        #如果使用下面这句代码替代上述2句，提交的结果是一个html标记
        #todolist.content = u'%s' % str(form_m.content)
        #？？？？？？？？？？？？？？？？？
        todolist.content=request.form['content']

        db.session.add(todolist)
        db.session.commit()
        return redirect(url_for('index'))

    #todolists=TodoList.query.all()
    page_index = request.args.get('page', 1, type=int)
    query = TodoList.query.order_by(TodoList.create_time.desc())
    pagination = query.paginate(page_index, per_page=10, error_out=False)
    todolists = pagination.items
    return render_template('index.html',todolists=todolists,form=form_t,
                           form_m=form_m,
                           pagination=pagination)
    # return redirect(url_for('index'))
