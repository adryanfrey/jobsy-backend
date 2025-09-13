from agents import Agent, models
from instructions import instructions
from pydantic import BaseModel


class CoverLetterAgent:
    def __init__(self, model: str = models.get_default_model()):
        self.agent = Agent(
            name="Cover letter Agent",
            instructions=instructions,
            model=model,
        )

    def run(self):
        self.agent.run()
        return "Job matcher agent is running"
