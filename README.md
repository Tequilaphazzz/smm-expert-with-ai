# SMM Expert with AI

This project is a Python application that automates the work of an SMM specialist using artificial intelligence. The application assists in generating posts, images, scheduling publications, and collecting statistics from social networks like VKontakte.

## Features
- **Post Generation**: Automatically creates text posts on given topics in a specific style using the OpenAI API.
- **Image Generation**: Creates images based on the post's context using the OpenAI API (DALL-E).
- **Auto-Publishing**: Supports scheduling and automatic publishing to VKontakte.
- **Statistics**: Collects and displays engagement statistics (views, likes, followers, etc.) from VKontakte.

## Technology Stack
- **Python**: The main programming language.
- **Flask**: Web framework for creating the application interface.
- **OpenAI API**: Used for generating text and images.
- **VK API**: For publishing posts and collecting statistics from VKontakte.
- **SQLAlchemy**: ORM for database operations.
- **Bootstrap**: Used for styling the interface.

## Project Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/username/smm-expert-ai.git
    cd smm-expert-ai
    ```

2.  **Install dependencies:**
    It is recommended to use a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3.  **Configure environment variables:**
    Create a `.env` file and add your OpenAI and VKontakte API keys:
    ```bash
    OPENAI_API_KEY=<your_openai_api_key>
    VK_API_KEY=<your_vk_api_key>
    VK_GROUP_ID=<your_vk_group_id>
    ```

4.  **Run the application:**
    ```bash
    flask run
    ```

## Core Modules
- `generators/text_gen.py`: Text generation via OpenAI.
- `generators/image_gen.py`: Image generation via OpenAI.
- `social_publishers/vk_publisher.py`: Works with the VKontakte API for publications.
- `social_stats/vk_stats.py`: Collects statistics from VKontakte.

## Project Structure
```
smm-expert-ai/
│
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── auth.py
│   ├── smm.py
│   ├── templates/
│   └── static/
│
├── generators/
│   ├── text_gen.py
│   └── image_gen.py
├── social_publishers/
│   └── vk_publisher.py
├── social_stats/
│   └── vk_stats.py
├── config.py
├── requirements.txt
└── README.md
```


## How It Works

1.  **Post Generation**: The user enters a topic and style; the application generates a post via GPT.
2.  **Image Creation**: An image description is generated based on the post, which is then created via the OpenAI API.
3.  **Publication**: The post and image are automatically published to VKontakte.
4.  **Statistics**: The application collects statistics (followers, likes, etc.) and displays them.

## License
This project is distributed under the MIT License.
