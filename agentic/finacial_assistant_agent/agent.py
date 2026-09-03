from google.adk.agents import LlmAgent
from google.adk.tools import google_search


def get_sample_financial_data() -> dict[str, str | int]:
    """Return sample financial data for demonstration purposes."""
    return {
        "category": "savings",
        "monthly_income": 5000,
        "monthly_savings_goal": 1000,
    }


finance_assistance_agent = LlmAgent(
    name="finance_assistance_agent",
    model="gemini-3.5-flash-lite",
    description=" A simple finance assistant that helps with user's finance goals.",
    instruction=""" You are a friendly finance assistant.
    You can help answer users generic question on finance and help plan
    their finance goals.Be more friendly and positive.
    """,
    tools=[get_sample_financial_data],
)

root_agent = finance_assistance_agent