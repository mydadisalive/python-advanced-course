import asyncio
import aiohttp

async def fetch_page(session, url):
    print(f"Starting to fetch {url}")
    async with session.get(url) as response:
        await asyncio.sleep(1)  # Simulate network latency
        content = await response.text()
        print(f"Finished fetching {url}")
        return content

async def main():
    urls = [
        "http://example.com",
        "http://example.org",
        "http://example.net"
    ]

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_page(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        print("All pages fetched")

asyncio.run(main())

# comment