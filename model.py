import web, datetime

db = web.database(dbn='mysql', db='webpy', user='root', pw='justdoit')
dbtable = 'entries'

def get_posts():
	return db.select(dbtable, order='id DESC')

def get_post(id):
	try:
		return db.select(dbtable, where='id=$id', vars=locals())[0]
	except IndexError:
		return None

def new_post(title, text):
	db.insert(dbtable, title=title, content=text, posted_on=datetime.datetime.utcnow())

def del_post(id):
	db.delete(dbtable, where="id=$id", vars=locals())

def update_post(id, title, text):
	db.update(dbtable, where="id=$id", vars=locals(), title=title, content=text)
