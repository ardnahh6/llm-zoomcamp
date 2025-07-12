import asyncio
from fastmcp import Client

async def main():
    async with Client("agents/weather_server.py") as mcp_client:
        # Panggil get_weather untuk Berlin
        result = await mcp_client.call_tool("get_weather", {"city": "Berlin"})
        print(f"Result for get_weather('Berlin'): {result}")

if __name__ == "__main__":
    asyncio.run(main())