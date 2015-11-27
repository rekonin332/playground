import orm,asyncio
from models import User,Blog,Comment
import random
def test(loop):
    yield from orm.create_pool(loop=loop,user='root',password='123456',db='awesome')
    email_d = random.randrange(1,100)
    emailTxt = 'test%s@test.com' % email_d
    u=User(name='test3',email=emailTxt,passwd='test',image='about:blank')
    yield from u.save()
def run():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test(loop))
    loop.close()