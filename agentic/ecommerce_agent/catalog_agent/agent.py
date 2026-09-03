from google.adk.agents import LlmAgent
from google.adk.tools.tool_context import ToolContext


PRODUCTS = [
    {"id": "laptop-001", "name": "Everyday Laptop", "price": 799.0},
    {"id": "phone-001", "name": "Smartphone", "price": 599.0},
    {"id": "headphones-001", "name": "Wireless Headphones", "price": 99.0},
]


def search_products(query: str = "") -> list[dict[str, str | float]]:
    """Search products by name."""
    query = query.strip().lower()
    return [product for product in PRODUCTS if not query or query in product["name"].lower()]


def add_item_to_cart(product_id: str, quantity: int, tool_context: ToolContext) -> dict:
    """Add a product to the cart stored in the current session."""
    product = next((item for item in PRODUCTS if item["id"] == product_id), None)
    if product is None:
        return {"success": False, "message": f"Product '{product_id}' was not found."}
    if quantity < 1:
        return {"success": False, "message": "Quantity must be at least 1."}

    cart = dict(tool_context.state.get("cart", {}))
    item = dict(cart.get(product_id, product))
    item["quantity"] = int(item.get("quantity", 0)) + quantity
    cart[product_id] = item
    tool_context.state["cart"] = cart
    return {"success": True, "cart": cart}


catalog_agent = LlmAgent(
    name="catalog_agent",
    model="gemini-3.5-flash-lite",
    description="Searches products and adds selected products to the session cart.",
    instruction=(
        "Search products with search_products. When the user chooses an item, call "
        "add_item_to_cart with its product id and quantity, then confirm the cart."
    ),
    tools=[search_products, add_item_to_cart],
)
