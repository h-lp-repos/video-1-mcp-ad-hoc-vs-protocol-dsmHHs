def create_ticket(order_id: str, reason: str):
    """Simulación de la creación de un ticket en el sistema de tickets."""

    print("Calling Ticket API")

    return {
        "ticket_id": "TICKET-123",
        "status": "created",
        "order_id": order_id
    }
