import asyncio

#@asyncio.coroutine
async def wget(host):
    print('wget %s...' % host)
    #connect =
    #reader, writer = yield from asyncio.open_connection(host, 80)
    reader, writer = await asyncio.open_connection(host, 80)
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    #yield from writer.drain()
    await writer.drain()
    while True:
        #line = yield from reader.readline()
        line = await reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    writer.close()

loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()