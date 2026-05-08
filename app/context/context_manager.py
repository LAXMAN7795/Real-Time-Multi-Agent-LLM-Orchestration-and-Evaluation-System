MAX_CONTEXT_TOKENS = 3000

APPROX_CHARS_PER_TOKEN = 4


def estimate_tokens(text: str):

    return len(text) // APPROX_CHARS_PER_TOKEN


def apply_context_budget(chunks):

    selected_chunks = []

    total_tokens = 0

    for chunk in chunks:

        content = chunk["content"]

        estimated_tokens = estimate_tokens(content)

        if (
            total_tokens + estimated_tokens
            > MAX_CONTEXT_TOKENS
        ):

            break

        selected_chunks.append(chunk)

        total_tokens += estimated_tokens

    return {

        "selected_chunks": selected_chunks,

        "estimated_tokens": total_tokens

    }