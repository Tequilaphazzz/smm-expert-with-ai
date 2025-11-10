from openai import OpenAI

class PostGenerator:
    def __init__(self, openai_key, tone, topic):
        self.client = OpenAI(api_key=openai_key)
        self.tone = tone
        self.topic = topic

    def generate_post(self):
        response = self.client.chat.completions.create(
          model="gpt-4o",
          messages=[
            {"role": "system", "content": "You are a highly qualified SMM specialist who will help generate text for posts on a given topic and with a given tone."},
            {"role": "user", "content": f"Generate a post for social media with the topic {self.topic}, using the tone: {self.tone}"}
          ]
        )
        return response.choices[0].message.content

    def generate_post_image_description(self):
        response = self.client.chat.completions.create(
          model="gpt-4o",
          messages=[
            {"role": "system", "content": "You are an assistant who will create a prompt for a neural network that generates images. You must create the prompt on the given topic."},
            {"role": "user", "content": f"Generate an image for social media with the topic {self.topic}"}
          ]
        )
        return response.choices[0].message.content