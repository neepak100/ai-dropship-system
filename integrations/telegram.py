import requests

class TelegramBot:
    def __init__(self, token, chat_id):
        self.token = token
        self.chat_id = chat_id

    def send_message(self, message):
        url = f'https://api.telegram.org/bot{self.token}/sendMessage'
        data = {'chat_id': self.chat_id, 'text': message}
        response = requests.post(url, data=data)

        return response.json()

# Example usage:
if __name__ == '__main__':
    TOKEN = 'your_telegram_bot_token'
    CHAT_ID = 'your_chat_id'
    bot = TelegramBot(TOKEN, CHAT_ID)

    # Send a notification message
    response = bot.send_message('Hello, this is a test notification!')
    print(response)