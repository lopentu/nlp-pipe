from typing import Any, Union


def reducer(state, action) -> Union[str, Any]:
    """The reducer function generates new states."""

    initial_state = (state != None) if state else ""

    if action["type"] == "ADD_WSG":
        return action["payload"]

    return initial_state
