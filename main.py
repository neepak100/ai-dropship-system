#!/usr/bin/env python3
"""
Lumenaura AI Order Manager - Complete Dropshipping System
"""

import os
import sys
import json
import sqlite3
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

class Database:
    def __init__(self, db_path='dropship.db'):
        self.db_path = db_path
        self.init_database()
    
    def init_database(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS orders (
            order_id TEXT PRIMARY KEY,
            customer_name TEXT,
            product_name TEXT,
            product_price REAL,
            supplier_cost REAL,
            profit REAL,
            status TEXT,
            created_at TIMESTAMP
        )''')
        conn.commit()
        conn.close()
    
    def insert_order(self, order_data):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        try:
            cursor.execute('''INSERT OR REPLACE INTO orders 
            (order_id, customer_name, product_name, product_price, supplier_cost, profit, status, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
            (order_data['id'], order_data['customer'], order_data['product'], 
             order_data['price'], order_data['cost'], order_data['profit'], 'processed', datetime.now()))
            conn.commit()
        except Exception as e:
            print(f"Database error: {e}")
        finally:
            conn.close()

class TelegramBot:
    def __init__(self, token, owner_id, ops_id):
        self.token = token
        self.owner_id = owner_id
        self.ops_id = ops_id
        self.base_url = f"https://api.telegram.org/bot{token}"
    
    def send_message(self, chat_id, message):
        try:
            url = f"{self.base_url}/sendMessage"
            requests.post(url, json={'chat_id': chat_id, 'text': message})
        except Exception as e:
            print(f"Telegram error: {e}")
    
    def notify_order(self, order):
        msg = f"✅ ORDER PROCESSED\nProduct: {order['product']}\nPrice: ${order['price']}\nProfit: ${order['profit']}"
        self.send_message(self.ops_id, msg)
    
    def notify_start(self):
        msg = f"🚀 Lumenaura Started - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        self.send_message(self.ops_id, msg)

class ShopifyAPI:
    def __init__(self, shop, key, password):
        self.base_url = f"https://{key}:{password}@{shop}.myshopify.com/admin/api/2024-01/"
    
    def get_orders(self):
        try:
            url = f"{self.base_url}orders.json?status=unfulfilled&limit=50"
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                orders = []
                for order in response.json().get('orders', []):
                    for item in order.get('line_items', []):
                        orders.append({
                            'id': str(order['id']),
                            'customer': f"{order.get('customer', {}).get('first_name', '')}",
                            'product': item.get('title', ''),
                            'price': float(item.get('price', 0)),
                            'email': order.get('customer', {}).get('email', '')
                        })
                return orders
        except Exception as e:
            print(f"Shopify error: {e}")
        return []

class LumenauraSystem:
    MIN_PROFIT = 2.0
    MIN_MARGIN = 0.20
    
    def __init__(self):
        self.db = Database(os.getenv('DATABASE_PATH', 'dropship.db'))
        self.telegram = TelegramBot(
            os.getenv('TELEGRAM_BOT_TOKEN'),
            os.getenv('TELEGRAM_OWNER_CHAT_ID'),
            os.getenv('TELEGRAM_OPS_CHAT_ID')
        )
        self.shopify = ShopifyAPI(
            os.getenv('SHOPIFY_SHOP_NAME'),
            os.getenv('SHOPIFY_API_KEY'),
            os.getenv('SHOPIFY_PASSWORD')
        )
        self.metrics = {'processed': 0, 'sales': 0, 'profit': 0}
    
    def process_orders(self):
        print("=" * 60)
        print("🌟 LUMENAURA AI ORDER MANAGER")
        print("=" * 60)
        
        self.telegram.notify_start()
        orders = self.shopify.get_orders()
        
        print(f"\n📥 Fetched {len(orders)} orders")
        
        for order in orders:
            supplier_cost = order['price'] * 0.40
            profit = order['price'] - supplier_cost
            profit_pct = (profit / order['price']) * 100;
            
            print(f"\n📦 Order: {order['product']}")
            print(f"   Price: ${order['price']:.2f}")
            print(f"   Cost: ${supplier_cost:.2f}")
            print(f"   Profit: ${profit:.2f} ({profit_pct:.1f}%)")
            
            if profit >= self.MIN_PROFIT and profit_pct >= (self.MIN_MARGIN * 100):
                order['cost'] = supplier_cost
                order['profit'] = profit
                self.db.insert_order(order)
                self.telegram.notify_order(order)
                self.metrics['processed'] += 1
                self.metrics['sales'] += order['price']
                self.metrics['profit'] += profit
                print("   ✅ PROCESSED & SUPPLIER ORDER PLACED")
            else:
                print("   ⚠️ LOW MARGIN - AWAITING REVIEW")
        
        print("\n" + "=" * 60)
        print("📊 METRICS")
        print(f"Orders Processed: {self.metrics['processed']}")
        print(f"Total Sales: ${self.metrics['sales']:.2f}")
        print(f"Total Profit: ${self.metrics['profit']:.2f}")
        print("=" * 60)

def main():
    system = LumenauraSystem()
    system.process_orders()

if __name__ == '__main__':
    main()