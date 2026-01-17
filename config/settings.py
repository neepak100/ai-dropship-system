"""
Configuration management for AI Dropship System
Loads environment variables and provides centralized config access
"""

import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

class Config:
    """Central configuration class"""
    
    # === SHOPIFY ===
    SHOPIFY_STORE_URL = os.getenv('SHOPIFY_STORE_URL', '')
    SHOPIFY_API_KEY = os.getenv('SHOPIFY_API_KEY', '')
    SHOPIFY_API_PASSWORD = os.getenv('SHOPIFY_API_PASSWORD', '')
    SHOPIFY_ACCESS_TOKEN = os.getenv('SHOPIFY_ACCESS_TOKEN', '')
    
    # === TELEGRAM ===
    TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN', '')
    TELEGRAM_OWNER_CHAT_ID = os.getenv('TELEGRAM_OWNER_CHAT_ID', '')
    TELEGRAM_OPS_CHAT_ID = os.getenv('TELEGRAM_OPS_CHAT_ID', '')
    
    # === OPENAI ===
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', '')
    OPENAI_MODEL = os.getenv('OPENAI_MODEL', 'gpt-4-turbo')
    OPENAI_MAX_TOKENS = int(os.getenv('OPENAI_MAX_TOKENS', '3500'))
    
    # === BUSINESS ===
    SYSTEM_OWNER = os.getenv('SYSTEM_OWNER', 'Owner')
    OPS_PARTNER = os.getenv('OPS_PARTNER', 'Ops Partner')
    MARKET_UK_ENABLED = os.getenv('MARKET_UK_ENABLED', 'true').lower() == 'true'
    MARKET_INDIA_ENABLED = os.getenv('MARKET_INDIA_ENABLED', 'true').lower() == 'true'
    TIMEZONE_OWNER = os.getenv('TIMEZONE_OWNER', 'Europe/London')
    TIMEZONE_OPS = os.getenv('TIMEZONE_OPS', 'Asia/Kolkata')
    
    # === DATABASE ===
    DATABASE_PATH = os.getenv('DATABASE_PATH', './data/dropship.db')
    LOG_PATH = os.getenv('LOG_PATH', './data/logs')
    DEBUG_MODE = os.getenv('DEBUG_MODE', 'false').lower() == 'true'
    
    # === COST MONITORING ===
    MONTHLY_BUDGET_USD = float(os.getenv('MONTHLY_BUDGET_USD', '60'))
    OPENAI_DAILY_BUDGET_USD = float(os.getenv('OPENAI_DAILY_BUDGET_USD', '0.50'))
    REFUND_THRESHOLD_PERCENT = float(os.getenv('REFUND_THRESHOLD_PERCENT', '5'))
    
    # === KILL SWITCH THRESHOLDS ===
    KILL_SWITCH_REFUND_RATE = float(os.getenv('KILL_SWITCH_REFUND_RATE', '0.06'))
    KILL_SWITCH_CHARGEBACK_RATE = float(os.getenv('KILL_SWITCH_CHARGEBACK_RATE', '0.03'))
    KILL_SWITCH_API_FAILURES = int(os.getenv('KILL_SWITCH_API_FAILURES', '10'))
    
    # === SYSTEM SETTINGS ===
    SYSTEM_ENABLED = os.getenv('SYSTEM_ENABLED', 'true').lower() == 'true'
    AUTO_ESCALATION_ENABLED = os.getenv('AUTO_ESCALATION_ENABLED', 'true').lower() == 'true'
    AI_DECISIONS_ENABLED = os.getenv('AI_DECISIONS_ENABLED', 'true').lower() == 'true'

    @staticmethod
    def validate():
        """Validate that all required configs are set"""
        required = [
            'SHOPIFY_STORE_URL',
            'SHOPIFY_ACCESS_TOKEN',
            'TELEGRAM_BOT_TOKEN',
            'TELEGRAM_OWNER_CHAT_ID',
            'OPENAI_API_KEY'
        ]
        
        missing = []
        for key in required:
            if not getattr(Config, key, None):
                missing.append(key)
        
        if missing:
            raise ValueError(f"Missing required environment variables: {', '.join(missing)}")
        
        return True

# Export config instance
config = Config()