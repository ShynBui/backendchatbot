
from openai import OpenAI

# Thay đổi API key của bạn tại đây
OPENAI_API_KEY = "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"

# Khởi tạo client OpenAI
client = OpenAI(api_key=OPENAI_API_KEY)

# Tạo hoàn thành trò chuyện
def callGpt(question):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": question,
            }
        ],
        model="gpt-3.5-turbo",
        )
    return chat_completion.choices[0].message.content

chat_completion = callGpt('hồ chí minh là ai ')
# In kết quả hoàn thành trò chuyện
print(chat_completion)