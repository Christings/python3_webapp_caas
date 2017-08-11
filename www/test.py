# -*- coding: utf-8 -*-

import www.orm, asyncio
from www.models import User, Blog, Comment

async def test(loop):
    await www.orm.create_pool(loop = loop, user = 'root', password = '421498', db = 'awesome')
    u = User(name = 'me', email = 'test2@example.nb', passwd = '1234567890',image = 'about:blank')
    await u.save()

#创建异步事件的句柄
loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()