from bs4 import BeautifulSoup
from playwright.async_api import async_playwright
from playwright_stealth import stealth_async
import aiohttp, asyncio



class scrap_handler:
    def __init__(self):

        self.results = list()

        self.websites_without_automation_part1 = {
            "animefire": {
                "url": "https://animefire.plus/proc/quicksearch", 
                "method": "POST",
                "headers": {"user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:130.0) Gecko/20100101 Firefox/130.0"},
                "data": {"word": "steins"},
                "params": {},
                "wordPressDefault": True,
                "browser_mode": False
            },
            
            "goyaby": {
                "url": "https://goyabu.to/wp-json/animeonline/search/?",
                "method": "GET",
                "headers": {"user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:130.0) Gecko/20100101 Firefox/130.0"},
                "data": {},
                "params": {"keyword": "steins", "nonce": "5ecb5079b5"},
                "wordPressDefault": False,
                "browser_mode": False
            },    
            
            "animesbr": {
                "url": "https://animesbr.tv/?",
                "method": "GET",
                "headers": {"user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:130.0) Gecko/20100101 Firefox/130.0"},
                "data": {},
                "params": {"s": "steins"},
                "wordPressDefault": False,
                "browser_mode": False
            }
        } 
            
        self.websites_without_automation_part2 = {
            "aniwatch": {
                "url": "https://aniwatchtv.to/ajax/search/suggest?",
                "method": "GET",
                "headers": {"user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:130.0) Gecko/20100101 Firefox/130.0"},
                "data": {},
                "params": {"keyword": "steins"},
                "wordPressDefault": False,
                "browser_mode": False
            },     
            
            "aniwatch": {
                "url": "	https://9animetv.to/search?",
                "method": "GET",
                "headers": {"user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:130.0) Gecko/20100101 Firefox/130.0"},
                "data": {},
                "params": {"keyword": "steins"},
                "wordPressDefault": False,
                "browser_mode": False
            }
        }

        self.websites_with_normal_automation = {}
        

        self.websites_with_custom_automation = {
            "kissanime": {
                "url": "https://kissanime.com.ru/Search/?",
                "method": "GET",
                "headers": {"user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:130.0) Gecko/20100101 Firefox/130.0"},
                "data": {},
                "params": {"s": "steins"},
                "wordPressDefault": False,
                "browser_mode": True
            }
        }

    async def run(self):
        #await self.playwrightAutomation()

        tasks = [
            asyncio.create_task(self.beautifulscrap(obs=self.websites_without_automation_part1)),
            asyncio.create_task(self.beautifulscrap(obs=self.websites_without_automation_part2))
        ]
        
        await asyncio.gather(*tasks)

        
        return self.results

    async def beautifulscrap(self, obs: dict, proxy=None, auth=None) -> list:        
        
        async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(3), proxy=proxy, auth=None) as requests:
            for obj in obs.items():
                await asyncio.sleep(0.1)

                if obj[1]['method'] == "POST":
                    request_obj = await requests.post(
                        url=obj[1].get("url"),
                        data=obj[1].get("data"),
                        params=obj[1].get("params"),
                        headers=obj[1].get("headers")
                        )
                
                else:
                    request_obj = await requests.get(
                        url=obj[1].get("url"),
                        data=obj[1].get("data"),
                        params=obj[1].get("params"),
                        headers=obj[1].get("headers")
                        )
                

                if request_obj.status == 200:
                    
                    #print(await request_obj.text())
                    self.results.append((obj[0], await request_obj.text()))
        
    async def playwrightAutomation(self):
        async with async_playwright() as sw:
            browser = await sw.chromium.launch_persistent_context(headless=False, user_data_dir="/tmp/persist_context_borwsers")
            page = await browser.new_page()
            await stealth_async(page)
            await page.wait_for_load_state()
            await page.pause()
            await page.goto()
            print("ok")


            
                


loop = asyncio.new_event_loop()
x = loop.run_until_complete(scrap_handler().run())

print(x)