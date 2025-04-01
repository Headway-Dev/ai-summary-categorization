class StatisticsLogger:
    def __init__(self) -> None:
        self._prompt_tokens = []
        self._completion_tokens = []
        self._costs = []
    
    def log(self, prompt_tokens: int, completion_tokens: int, cost: float) -> None:
        self._prompt_tokens.append(prompt_tokens)
        self._completion_tokens.append(completion_tokens)
        self._costs.append(cost)
    
    @property
    def total_prompt_tokens(self) -> int:
        return sum(self._prompt_tokens)

    @property
    def average_prompt_tokens(self) -> float:
        return sum(self._prompt_tokens) / len(self._prompt_tokens)
    
    @property
    def total_completion_tokens(self) -> int:
        return sum(self._completion_tokens)
    
    @property
    def average_completion_tokens(self) -> float:
        return sum(self._completion_tokens) / len(self._completion_tokens)
    
    @property
    def total_cost(self) -> float:
        return sum(self._costs)
    
    @property
    def average_cost(self) -> float:
        return sum(self._costs) / len(self._costs)
    
    @property
    def total_inferences(self) -> int:
        return len(self._costs)
    
    def __str__(self) -> str:
        return (
            "Statistics:\n"
            f"\tNum inferences: {self.total_inferences}\n"
            f"\tAverage Prompt Tokens: {self.average_prompt_tokens}\n"
            f"\tAverage Completion Tokens: {self.average_completion_tokens}\n"
            f"\tAverage Cost: {self.average_cost}\n"
            f"\tTotal Prompt Tokens: {self.total_prompt_tokens}\n"
            f"\tTotal Completion Tokens: {self.total_completion_tokens}\n"
            f"\tTotal Cost: {self.total_cost}"
        )