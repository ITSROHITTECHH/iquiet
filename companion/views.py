from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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"
)




def home(request):
    return render(request, "index.html")


def chat(request):
    return render(request,"chat.html")



def get_ai_reply(message, history):

    messages = [
        {"role": "system", "content": "You are a calm and emotionally supportive AI companion. You remember past conversations and talk like a real human friend."
    }

    ]

    # 🧠 past chat add
    for chat in history:
        messages.append({"role": "user", "content": chat["user"]})
        messages.append({"role": "assistant", "content": chat["ai"]})

    # current message
    messages.append({"role": "user", "content": message})

    response = client.chat.completions.create(
        model="meta-llama/llama-3-8b-instruct",
        messages=messages
    )

    return response.choices[0].message.content


        
@csrf_exempt
def chat_api(request):

    if request.method == "POST":

        data = json.loads(request.body)

        message = data.get("message")
        history = data.get("history", [])

        reply = get_ai_reply(message, history)

        return JsonResponse({"reply": reply})       