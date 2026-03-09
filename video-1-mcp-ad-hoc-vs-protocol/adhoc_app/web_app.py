from ticket_api import create_ticket


def web_create_ticket():
    """Función que simula la creación de un ticket desde una aplicación web."""

    result = create_ticket(
        order_id="ORDER-1",
        reason="Customer requested refund"
    )

    print("WEB RESULT:", result)


if __name__ == "__main__":
    web_create_ticket()
