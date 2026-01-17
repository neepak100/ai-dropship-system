import logging
from datetime import datetime
from integrations.shopify import ShopifyAPI
from integrations.telegram import TelegramBot
from integrations.openai_client import OpenAIClient

logger = logging.getLogger(__name__)

class OrderProcessor:
    def __init__(self, shopify_api, telegram_bot, openai_client, database):
        self.shopify_api = shopify_api
        self.telegram_bot = telegram_bot
        self.openai_client = openai_client
        self.database = database
    
    def process_new_orders(self):
        """Process new orders from Shopify"""
        try:
            orders = self.shopify_api.get_orders()
            logger.info(f"Processing {len(orders)} new orders")
            for order in orders:
                order_id = order.get('id')
                self.telegram_bot.notify_new_order(order)
            return True
        except Exception as e:
            logger.error(f"Error: {e}")
            return False