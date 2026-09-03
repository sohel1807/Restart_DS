from google.adk.agents import LlmAgent

from .catalog_agent import catalog_agent
from .checkout_agent import checkout_agent
from .order_summary_agent import order_summary_agent


ecommerce_agent = LlmAgent(
    name="ecommerce_agent",
    model="gemini-3.5-flash-lite",
    description="Coordinates catalog, checkout, and order-summary tasks.",
    instruction=(
        "You are the ecommerce assistant. Delegate product searches and cart changes "
        "to catalog_agent, customer profile and shipping details to checkout_agent, "
        "and order summaries to order_summary_agent. Session state is shared between "
        "agents. Do not ask the user to repeat details already stored."
    ),
    sub_agents=[catalog_agent, checkout_agent, order_summary_agent],
)

root_agent = ecommerce_agent
