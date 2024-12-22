from openai import OpenAI
import user_config as uc

client = OpenAI(api_key=uc.openai_key)

# def send_requests(query):
#     completion = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[
#             {
#                 "role": "user",
#                 "content": query
#             }
#         ]
#     )
#     return completion.choices[0].message.content


def send_requests(query):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=query
    )
    return completion.choices[0].message.content