import scrap_working, pos_processing
import asyncio

loop = asyncio.new_event_loop()
x = loop.run_until_complete(scrap_working.scrap_handler().run())

pos_processing.filters(x).process()