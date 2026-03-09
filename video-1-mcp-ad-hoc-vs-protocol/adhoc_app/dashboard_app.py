from ticket_api import create_ticket


def dashboard_create_ticket():
    """Función que simula la creación de un ticket desde un dashboard de agentes."""

    result = create_ticket(
        order_id="ORDER-1",
        reason="Agent created ticket"
    )

    print("DASHBOARD RESULT:", result)


if __name__ == "__main__":
    dashboard_create_ticket()
