from core.combat import fight


def create_game_state(player: object) -> dict:
    return {
        "player": player,
        "active_monster": None,
        "current_scene": "start",
        "pending_event": None,
        "flags": {}
    }


def trigger_event(state: dict) -> None:
    if state.get("active_monster"):
        fight(state["player"], state["active_monster"])
        state["active_monster"] = None

def consume_event(state: dict) -> str | None:
    event = state["pending_event"]
    state["pending_event"] = None
    return event


