from dataclasses import dataclass, field


@dataclass()
class TrainingParams:
    model_type: str = field(default='LogisticRegression')
    random_state: int = field(default=17)
    grid_search: bool = field(default=True)
