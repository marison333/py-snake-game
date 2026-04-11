def create_game_state(player: object) -> dict:
    return {
        "player": player,
        "active_monster": None,
        "current_scene": "start",
        "pending_event": None,
        "flags": {}
    }


def trigger_event(state: dict, event_name: str) -> None:
    state["pending_event"] = event_name


def consume_event(state: dict) -> str | None:
    event = state["pending_event"]
    state["pending_event"] = None
    return event


