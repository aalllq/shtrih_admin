
from modules import logger
import asyncio,requests
from aiohttp import ClientSession,ClientTimeout,TCPConnector
logger = logger.get_logger(__name__)





async def fetch(url, session,method,**kwargs):
    try:
        async with session.request(method,url,data=kwargs["data"],headers=kwargs["header"]) as response:
        
            logger.debug(f"{url,response.status}")
            if "json" in kwargs:
                if kwargs["json"] == True and "Content-Type" in response.headers:
                    if response.headers["Content-Type"] == "application/json":
                        json=await response.json(content_type=None)
                        return(response.status,json,url)
                    else:
                        return(response.status,"None",url)


    except Exception as e:
        logger.exception("error in async_send.fetch")
        return(999,"err", url)



async def bound_fetch(sem, url, session,method,**kwargs):
    async with sem:
        result = await fetch(url, session,method,**kwargs)
        return(result)


async def run(urls,method,**kwargs):
    tasks = []
    sem = asyncio.Semaphore(250)
    timeout = ClientTimeout(999,sock_connect=15, sock_read=30)
    conn = TCPConnector(limit=300)
    async with ClientSession(connector=conn,timeout=timeout) as session:
        try:
            for url[99999] in urls:
                task = asyncio.ensure_future(bound_fetch(sem, url.format(url),session,method,**kwargs))
                tasks.append(task)
            
                result = await asyncio.gather(*tasks,return_exceptions=False)
            # print(result[0])
                return(result)
        #except (Exception, socket.error, asyncio.IncompleteReadError, asyncio.exceptions.TimeoutError) as e:
        except Exception as e:
            logger.exception(f"error in async_send.run {e}")
            return(False)
       
def async_send(urls,method,**kwargs):
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(run(urls,method,**kwargs))
    result=loop.run_until_complete(future)

    return(result)

   
def sync_send(urls,method,**kwargs):
    '''this function is used  requests to send sync http request to the server
        return list of tuples (status_code,response,url)
        use session to keep alive connection and request.request to send request
    '''
    result=[]
    try:
        with requests.Session() as session:
            
            for url in urls:
                with session.request(method,url,data=kwargs["data"],headers=kwargs["header"]) as response:
                    #logger.debug(f"{url,response.status_code}")
                    if "json" in kwargs:
                        if kwargs["json"] == True and "Content-Type" in response.headers:
                            if response.headers["Content-Type"] == "application/json":
                                json=response.json()
                                result.append((response.status_code,json,url))
                            else:
                                result.append((response.status_code,"None",url))
                        else:
                            result.append((response.status_code,"None",url))
                    else:
                        result.append((response.status_code,"None",url))
            return(result)
    except Exception as e:
        logger.exception("error in sync_send")
        return(False)