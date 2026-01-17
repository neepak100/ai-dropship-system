class LumenauraSystem:
    def __init__(self):
        self.orders = []  # List to hold orders
        self.configuration = {}  # Configuration settings
        self.metrics = {'processed_orders': 0, 'refunds': 0}  # Metrics tracking

    def process_order(self, order_id, customer_data):
        # Simulate order processing
        order = {'id': order_id, 'customer': customer_data, 'status': 'processed'}
        self.orders.append(order)
        self.metrics['processed_orders'] += 1
        print(f'Order {order_id} processed for {customer_data}.')

    def handle_refund(self, order_id):
        # Simulate refund handling
        for order in self.orders:
            if order['id'] == order_id:
                order['status'] = 'refunded'
                self.metrics['refunds'] += 1
                print(f'Refund processed for order {order_id}.')
                return
        print(f'Order {order_id} not found for refund.')

    def verify_configuration(self):
        # Placeholder for configuration verification logic
        if not self.configuration:
            print('Configuration is not set. Please verify.')
        else:
            print('Configuration is valid.')

    def track_metrics(self):
        # Display current metrics
        print(f'Total processed orders: {self.metrics['processed_orders']}')
        print(f'Total refunds processed: {self.metrics['refunds']}')

    def main_loop(self):
        while True:
            # Simulated main loop for processing orders
            user_input = input('Enter order ID to process or "exit" to quit: ')
            if user_input.lower() == "exit":
                break
            customer_data = input('Enter customer information: ')
            self.process_order(user_input, customer_data)
            self.track_metrics()

if __name__ == '__main__':
    system = LumenauraSystem()
    system.verify_configuration()
    system.main_loop()