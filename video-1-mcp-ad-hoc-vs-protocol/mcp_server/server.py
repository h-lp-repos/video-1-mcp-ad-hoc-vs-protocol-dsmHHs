from mcp.server import FastMCP


# Definir el servidor MCP
mcp = FastMCP("support-server")


@mcp.tool()
def create_ticket(order_id: str, reason: str):
    """Simulación de la creación de un ticket en el sistema de tickets."""

    print("Ticket created via MCP")

    return {
        "ticket_id": "TICKET-123",
        "status": "created",
        "order_id": order_id
    }


if __name__ == "__main__":
    mcp.run()
