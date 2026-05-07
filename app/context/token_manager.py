import tiktoken


class TokenBudgetManager:

    def __init__(self, model_name="gpt-4"):
        self.encoder = tiktoken.encoding_for_model(model_name)

    def count_tokens(self, text: str) -> int:
        return len(self.encoder.encode(text))

    def remaining_budget(
        self,
        used_tokens: int,
        max_budget: int
    ) -> int:
        return max_budget - used_tokens

    def exceeds_budget(
        self,
        used_tokens: int,
        max_budget: int
    ) -> bool:
        return used_tokens > max_budget