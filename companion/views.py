from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

import os
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ.get("OPENAI_API_KEY"),
)




def home(request):
    return render(request, "index.html")


def chat(request):
    return render(request,"chat.html")



# def get_ai_reply(message, history):

#     messages = [
#         {"role": "system", "content": "You are a calm and emotionally supportive AI companion. You remember past conversations and talk like a real human friend."
#     }

#     ]

#     # 🧠 past chat add
#     for chat in history:
#         messages.append({"role": "user", "content": chat["user"]})
#         messages.append({"role": "assistant", "content": chat["ai"]})

#     # current message
#     messages.append({"role": "user", "content": message})

#     response = client.chat.completions.create(
#         model="meta-llama/llama-3-8b-instruct",
#         messages=messages
#     )

#     return response.choices[0].message.content

def get_ai_reply(message, history):
    try:
        messages = [
            {
                "role": "system",
                "content": "You are a calm and emotionally supportive AI companion. You remember past conversations and talk like a real human friend."
            }
        ]

        for chat in history:
            messages.append({"role": "user", "content": chat["user"]})
            messages.append({"role": "assistant", "content": chat["ai"]})

        messages.append({"role": "user", "content": message})

        response = client.chat.completions.create(
            model="meta-llama/llama-3-8b-instruct",
            messages=messages
        )

        return response.choices[0].message.content

    except Exception as e:
        print("ERROR:", e)  # logs me dikhega
        return f"Error: {str(e)}"






        
# @csrf_exempt
# def chat_api(request):

#     if request.method == "POST":

#         data = json.loads(request.body)

#         message = data.get("message")
#         history = data.get("history", [])

#         reply = get_ai_reply(message, history)

#         return JsonResponse({"reply": reply})       


@csrf_exempt
def chat_api(request):
    try:
        if request.method == "POST":
            data = json.loads(request.body)

            message = data.get("message")
            history = data.get("history", [])

            reply = get_ai_reply(message, history)

            return JsonResponse({"reply": reply})

        return JsonResponse({"error": "Invalid request"}, status=400)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)