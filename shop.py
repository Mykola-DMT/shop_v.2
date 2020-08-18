from app import app
from app.models import Item,User

@app.shell_context_processor
def make_shell_context():
    return {'db':db, 'Item':Item, 'User':User}