from langchain_core.messages import AIMessage, HumanMessage

from rag.services.query_service import QueryService


class ChatService:
    """
    Manages conversation state.
    """

    def __init__(self) -> None:
        self.query_service = QueryService()
        self.history: list = []

    def chat(self, question: str):
        self.history.append(HumanMessage(content=question))

        response = self.query_service.ask(question)

        self.history.append(
            AIMessage(content=response.answer)
        )

        return response