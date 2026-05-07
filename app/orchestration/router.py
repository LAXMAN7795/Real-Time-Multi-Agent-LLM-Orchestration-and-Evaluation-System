def dynamic_router(state):

    query = state["user_query"].lower()

    if "compare" in query:
        return "decomposition"

    if "why" in query:
        return "retrieval"

    return "retrieval"