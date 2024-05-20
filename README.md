# Image Processing Telegram Bot

This Telegram bot allows users to process images with various filters and transformations.

## Getting Started

### Prerequisites

- Python 3.x
- [Flask](https://pypi.org/project/Flask/)
- [matplotlib](https://pypi.org/project/matplotlib/)
- [python-telegram-bot](https://pypi.org/project/python-telegram-bot/)
- [loguru](https://pypi.org/project/loguru/)

### Installation

1. Clone this repository:

    sh
    git clone <repository_url>
    cd <repository_directory>
    

2. Install the dependencies:

    sh
    pip install -r requirements.txt
    

### Create a Telegram Bot

1. [Download](https://desktop.telegram.org/) and install Telegram Desktop (or use the mobile app).
2. Create your own Telegram Bot by following [this guide](https://core.telegram.org/bots/features#botfather). Once you have your Telegram token, you can proceed to the next step.

*Important:* Never commit your Telegram token in the Git repo, even if the repo is private. For now, we will provide the token as an environment variable to your app. Later, we will learn better approaches to store sensitive data.

### Running the Telegram Bot Locally

The Telegram bot is a Flask-based service that provides a chat interface for users to interact with your image processing functionality. It uses the Telegram Bot API to receive user images and respond with processed images.

#### Setting Up Environment Variables

You need to set up two environment variables:

1. TELEGRAM_TOKEN: Your bot token.
2. TELEGRAM_APP_URL: Your app's public URL provided by Ngrok (discussed below).

#### Setting Up Ngrok

Setting localhost as the webhook URL is problematic because Telegram servers need to access the webhook URL over the internet to send updates. Since localhost is not externally accessible, Telegram servers won't be able to reach the webhook, and the bot won't receive updates.

[Ngrok](https://ngrok.com/) solves this problem by creating a secure tunnel between your local machine (where the bot is running) and a public URL provided by Ngrok. This exposes the local server to the internet, allowing Telegram servers to reach the webhook URL and send updates to the bot.

1. Sign up for the Ngrok service, then install the ngrok agent as [described here](https://ngrok.com/docs/getting-started/#step-2-install-the-ngrok-agent).
2. Authenticate your Ngrok agent (you only need to do this once):

    bash
    ngrok config add-authtoken <your-authtoken>
    

3. Since the Telegram bot service will be listening on port 8443, start Ngrok by running the following command:

    bash
    ngrok http 8443
    

Your bot's public URL is the URL specified in the Forwarding line (e.g. https://<ngrok-subdomain>.ngrok-free.app). Set the TELEGRAM_APP_URL environment variable to this URL.

### Running the Flask App

1. Set up the environment variables:
    - TELEGRAM_TOKEN: Your Telegram bot token.
    - TELEGRAM_APP_URL: Your application URL.

2. Run the Flask app:

    sh
    python polybot/app.py
    

3. Start chatting with your Telegram bot! Send an image along with a caption specifying the filter or transformation you want to apply.

    *Examples:*
    - Applying /start command
    - Applying the blur filter
    - Applying the segment filter

## File Structure

- app.py: Flask application handling Telegram webhook and routing.
- img_proc.py: Image processing utilities including filters and transformations.
- bot.py: Base class and subclasses for different types of Telegram bots.

## Supported Filters/Transformations

- Blur
- Contour
- Rotate
- Rotate2
- Salt and Pepper
- Segment
- Concatenation 

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Commit your changes (git commit -m 'Add some feature').
4. Push to the branch (git push origin feature-branch).
5. Open a pull request.