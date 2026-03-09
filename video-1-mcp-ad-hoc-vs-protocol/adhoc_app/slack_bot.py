from ticket_api import create_ticket


def slack_create_ticket():
    """Función que simula la creación de un ticket desde un bot de Slack."""

    result = create_ticket(
        order_id="ORDER-1",
        reason="Refund requested in Slack"
    )

    print("SLACK RESULT:", result)


if __name__ == "__main__":
    slack_create_ticket()
