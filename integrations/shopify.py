import requests

class ShopifyAPI:
    def __init__(self, shop_name, api_key, password):
        self.shop_name = shop_name
        self.api_key = api_key
        self.password = password
        self.base_url = f"https://{api_key}:{password}@{shop_name}.myshopify.com/admin/api/2021-10/"

    def get_orders(self):
        """Retrieve orders from the Shopify store."""
        response = requests.get(self.base_url + 'orders.json')
        return response.json()

    def get_customer_messages(self):
        """Retrieve customer messages."""
        # Depending on your implementation you need to customize this function.
        pass

    def reply_to_customer(self, customer_id, message):
        """Send a reply to a customer."""
        # Implementation is dependent on how your messages are stored and managed.
        pass

    def update_tracking_number(self, order_id, tracking_number):
        """Update tracking number for an order."""
        tracking_info = {
            "fulfillment": {
                "tracking_number": tracking_number
            }
        }
        response = requests.put(self.base_url + f'fulfillments/{order_id}.json', json=tracking_info)
        return response.json()