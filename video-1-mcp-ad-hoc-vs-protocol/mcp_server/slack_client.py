import asyncio
import json

from mcp.client.session import ClientSession
from mcp.client.stdio import stdio_client, StdioServerParameters


async def main():
    """Cliente que simula una integración con Slack."""

    params = StdioServerParameters(
        command="python",
        args=["server.py"]
    )

    async with stdio_client(params) as (read, write):

        async with ClientSession(read, write) as session:

            await session.initialize()

            result = await session.call_tool(
                "create_ticket",
                {
                    "order_id": "ORDER-1",
                    "reason": "Slack user asked refund"
                }
            )

            text = result.content[0].text
            data = json.loads(text)

            print("\n=== SLACK RESULT ===")
            print(json.dumps(data, indent=2))


asyncio.run(main())
