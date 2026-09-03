from google.adk.agents import LlmAgent
from google.adk.tools.tool_context import ToolContext


def get_order_summary(tool_context: ToolContext) -> dict:
    """Return the order summary from the current session state."""
    profile = dict(tool_context.state.get("user_profile", {}))
    cart = dict(tool_context.state.get("cart", {}))
    address = dict(tool_context.state.get("shipping_address", {}))
    items = list(cart.values())
    subtotal = sum(float(item["price"]) * int(item["quantity"]) for item in items)
    shipping = 0.0 if subtotal >= 500 or not items else 25.0
    return {
        "user_profile": profile,
        "items": items,
        "shipping_address": address,
        "subtotal": round(subtotal, 2),
        "shipping": shipping,
        "total": round(subtotal + shipping, 2),
        "ready_for_checkout": bool(profile and items and address),
    }


order_summary_agent = LlmAgent(
    name="order_summary_agent",
    model="gemini-3.5-flash-lite",
    description="Displays a complete order summary from session state.",
    instruction=(
        "Call get_order_summary for an order summary. Display the customer, items, "
        "shipping address, subtotal, shipping, total, and checkout readiness."
    ),
    tools=[get_order_summary],
)
