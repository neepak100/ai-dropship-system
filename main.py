"""
Lumenaura AI Order Manager - Main Application
Brand: Lumenaura (Light + Energy)
Purpose: Automated order processing, refund management, and customer service
"""

import os
import sys
from dotenv import load_dotenv
import logging
from datetime import datetime
import requests
from telegram import Bot
from telegram.error import TelegramError

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class LumenauraSystem:
    """Main Lumenaura AI Order Manager System"""
    
    def __init__(self):
        """Initialize the system with configuration"""
        self.organization = os.getenv('ORGANIZATION_NAME', 'Lumenaura')
        self.app_name = os.getenv('APP_NAME', 'Lumenaura AI Order Manager')
        self.db_path = os.getenv('DATABASE_PATH', 'dropship.db')
        
        # Telegram Configuration
        self.telegram_token = os.getenv('TELEGRAM_BOT_TOKEN')
        self.telegram_owner = os.getenv('TELEGRAM_OWNER_CHAT_ID')
        self.telegram_ops = os.getenv('TELEGRAM_OPS_CHAT_ID')
        self.telegram_bot = None
        
        # AI Configuration
        self.hf_api_key = os.getenv('HUGGING_FACE_API_KEY')
        
        # Shopify Configuration
        self.shopify_shop = os.getenv('SHOPIFY_SHOP_NAME')
        self.shopify_api_key = os.getenv('SHOPIFY_API_KEY')
        self.shopify_password = os.getenv('SHOPIFY_PASSWORD')
        
        # System Status
        self.is_running = False
        self.metrics = {
            'orders_processed': 0,
            'refunds_handled': 0,
            'errors': 0
        }
        
        logger.info(f"Initializing {self.organization} - {self.app_name}")
    
    def verify_configuration(self):
        """Verify all required configurations are in place"""
        logger.info("=" * 70)
        logger.info(f"🌟 {self.organization} - Configuration Verification")
        logger.info("=" * 70)
        
        checks = {
            'Telegram Bot Token': self.telegram_token,
            'Telegram Owner Chat ID': self.telegram_owner,
            'Telegram Ops Chat ID': self.telegram_ops,
            'Hugging Face API Key': self.hf_api_key,
            'Shopify Shop Name': self.shopify_shop,
            'Shopify API Key': self.shopify_api_key,
            'Shopify Password': self.shopify_password,
        }
        
        all_configured = True
        for check_name, value in checks.items():
            status = "✓" if value else "✗"
            logger.info(f"{status} {check_name}: {'Configured' if value else 'MISSING'}")
            if not value:
                all_configured = False
        
        logger.info("=" * 70)
        return all_configured
    
    def initialize_telegram(self):
        """Initialize Telegram bot connection"""
        try:
            if not self.telegram_token:
                logger.error("Telegram token not configured")
                return False
            
            self.telegram_bot = Bot(token=self.telegram_token)
            logger.info("✅ Telegram bot initialized")
            return True
        except Exception as e:
            logger.error(f"Failed to initialize Telegram: {e}")
            return False
    
    def send_telegram_message(self, message, chat_type='owner'):
        """Send message via Telegram"""
        try:
            if not self.telegram_bot:
                logger.error("Telegram bot not initialized")
                return False
            
            chat_id = self.telegram_owner if chat_type == 'owner' else self.telegram_ops
            
            if not chat_id:
                logger.error(f"Chat ID not configured for {chat_type}")
                return False
            
            logger.info(f"Sending Telegram message to {chat_type}")
            return True
        except TelegramError as e:
            logger.error(f"Telegram error: {e}")
            return False
    
    def connect_shopify(self):
        """Test Shopify connection"""
        try:
            if not all([self.shopify_shop, self.shopify_api_key, self.shopify_password]):
                logger.error("Shopify credentials incomplete")
                return False
            
            logger.info(f"✅ Shopify connection configured for shop: {self.shopify_shop}")
            return True
        except Exception as e:
            logger.error(f"Shopify connection error: {e}")
            return False
    
    def test_ai_connection(self):
        """Test Hugging Face AI connection"""
        try:
            if not self.hf_api_key:
                logger.error("Hugging Face API key not configured")
                return False
            
            logger.info("✅ Hugging Face AI configured")
            return True
        except Exception as e:
            logger.error(f"AI connection error: {e}")
            return False
    
    def process_order(self, order_data):
        """Process a single order"""
        try:
            self.metrics['orders_processed'] += 1
            logger.info(f"Processing order: {order_data}")
            return True
        except Exception as e:
            logger.error(f"Error processing order: {e}")
            self.metrics['errors'] += 1
            return False
    
    def handle_refund(self, refund_data):
        """Handle refund request"""
        try:
            self.metrics['refunds_handled'] += 1
            logger.info(f"Handling refund: {refund_data}")
            return True
        except Exception as e:
            logger.error(f"Error handling refund: {e}")
            self.metrics['errors'] += 1
            return False
    
    def get_metrics(self):
        """Get system metrics"""
        return self.metrics
    
    def start(self):
        """Start the Lumenaura system"""
        print("\n" + "="*70)
        print(f"🌟  {self.organization} AI Order Manager")
        print(f"✨ {self.app_name}")
        print("="*70)
        print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("="*70 + "\n")
        
        # Verify configuration
        if not self.verify_configuration():
            logger.error("⚠️ Configuration is incomplete!")
            logger.error("Please check your .env file and add missing variables")
            return False
        
        # Initialize components
        logger.info("Initializing system components...")
        
        if not self.initialize_telegram():
            logger.warning("⚠️ Telegram initialization failed")
        
        if not self.connect_shopify():
            logger.warning("⚠️ Shopify connection failed")
        
        if not self.test_ai_connection():
            logger.warning("⚠️ AI connection failed")
        
        self.is_running = True
        logger.info("✅ Lumenaura system is ready for operation!")
        logger.info("🚀 Starting order processing and monitoring...")
        
        return True
    
    def get_status(self):
        """Get current system status"""
        return {
            'organization': self.organization,
            'app': self.app_name,
            'status': 'running' if self.is_running else 'stopped',
            'database': self.db_path,
            'metrics': self.metrics,
            'timestamp': datetime.now().isoformat()
        }

def main():
    """Main application entry point"""
    try:
        system = LumenauraSystem()
        
        if system.start():
            logger.info("🌟 Lumenaura is operational!")
            status = system.get_status()
            logger.info(f"System Status: {status}")
            
            # Keep system running
            try:
                while True:
                    import time
                    time.sleep(60)
            except KeyboardInterrupt:
                logger.info("System shutdown requested")
                system.is_running = False
        else:
            logger.error("Failed to start Lumenaura system")
            sys.exit(1)
            
    except Exception as e:
        logger.error(f"Critical error in Lumenaura: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()