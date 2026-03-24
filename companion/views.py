from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

import os
from openai import OpenAI

# client = OpenAI(
#     base_url="https://openrouter.ai/api/v1",
#     api_key=os.environ.get("OPENAI_API_KEY"),
#     default_headers={
#         "HTTP-Referer": "https://iquiet-production.up.railway.app",
#         "X-Title": "iQuiet"

#     }
# )  




def home(request):
    return render(request, "index.html")


def chat(request):
    return render(request,"chat.html")



def get_ai_reply(message, history):
    try:
        api_key = os.environ.get("OPENROUTER_API_KEY")

        if not api_key:
            return "API key not configured 🚫"

        client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=api_key,
            default_headers={
                "HTTP-Referer": "https://iquiet-production.up.railway.app",
                "X-Title": "iQuiet"
            }
        )

        messages = [
            {
                "role": "system",
                "content": "You are a calm and emotionally supportive AI companion."
            }
        ]

        for chat in history:
            messages.append({"role": "user", "content": chat["user"]})
            messages.append({"role": "assistant", "content": chat["ai"]})

        messages.append({"role": "user", "content": message})

        response = client.chat.completions.create(
            model="openai/gpt-4o-mini",
            messages=messages
        )

        return response.choices[0].message.content

    except Exception as e:
        print("ERROR:", e)
        return f"Error: {str(e)}"



# def get_ai_reply(message, history):
#     try:
#         messages = [
#             {
#                 "role": "system",
#                 "content": "You are a calm and emotionally supportive AI companion."
#             }
#         ]

#         for chat in history:
#             messages.append({"role": "user", "content": chat["user"]})
#             messages.append({"role": "assistant", "content": chat["ai"]})

#         messages.append({"role": "user", "content": message})

#         response = client.chat.completions.create(
#             model="openai/gpt-3.5-turbo",  # ⚠️ change model
#             messages=messages
#         )

#         return response.choices[0].message.content

#     except Exception as e:
#         print("ERROR:", e)
#         return f"Error: {str(e)}"




        
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