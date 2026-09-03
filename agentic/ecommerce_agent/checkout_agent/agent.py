from google.adk.agents import LlmAgent
from google.adk.tools.tool_context import ToolContext


def save_user_profile(name: str, email: str, tool_context: ToolContext) -> dict[str, str]:
    """Save the user profile in the current session."""
    profile = {"name": name, "email": email}
    tool_context.state["user_profile"] = profile
    return profile


def save_shipping_address(
    street: str,
    city: str,
    state: str,
    postal_code: str,
    tool_context: ToolContext,
) -> dict[str, str]:
    """Save the shipping address in the current session."""
    address = {
        "street": street,
        "city": city,
        "state": state,
        "postal_code": postal_code,
    }
    tool_context.state["shipping_address"] = address
    return address


checkout_agent = LlmAgent(
    name="checkout_agent",
    model="gemini-3.5-flash-lite",
    description="Collects and stores the customer profile and shipping address.",
    instruction=(
        "Ask for name and email, then call save_user_profile. Ask for street, city, "
        "state, and postal code, then call save_shipping_address. Do not invent details."
    ),
    tools=[save_user_profile, save_shipping_address],
)
