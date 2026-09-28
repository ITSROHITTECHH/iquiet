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
            print("ERROR: OPENROUTER_API_KEY is not set in the environment")
            return "API key not configured \U0001F6AB"

        client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=api_key,
            timeout=20,       # never hang the request forever
            max_retries=1,
            default_headers={
                             "HTTP-Referer": "https://iquiet.vercel.app",
                             "X-Title": "iQuiet"
                        }
        )

        messages = [
            {
                "role": "system",
                "content": "You are a calm and emotionally supportive AI companion."
            }
        ]

        # history comes from the browser, so never trust its shape
        for chat in (history if isinstance(history, list) else []):
            if not isinstance(chat, dict):
                continue
            user_msg = chat.get("user")
            ai_msg = chat.get("ai")
            if isinstance(user_msg, str) and isinstance(ai_msg, str):
                messages.append({"role": "user", "content": user_msg})
                messages.append({"role": "assistant", "content": ai_msg})

        messages.append({"role": "user", "content": message})

        response = client.chat.completions.create(
            model="openai/gpt-4o-mini",
            messages=messages
        )

        reply = response.choices[0].message.content
        return reply or "I'm here with you. Could you say that again?"

    except Exception as e:
        # Real error goes to the server logs only, not to the visitor.
        print("ERROR:", repr(e))
        return "I'm having trouble connecting right now. Please try again in a moment."



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
    # The frontend always reads `data.reply`, so every response (even errors)
    # carries a `reply` key - otherwise the chat bubble shows "undefined".
    try:
        if request.method == "POST":
            try:
                data = json.loads(request.body or b"{}")
            except (ValueError, UnicodeDecodeError):
                return JsonResponse(
                    {"error": "Invalid JSON", "reply": "Sorry, I couldn't read that message."},
                    status=400,
                )

            if not isinstance(data, dict):
                data = {}

            message = data.get("message")
            history = data.get("history", [])

            if not isinstance(message, str) or not message.strip():
                return JsonResponse(
                    {"error": "Message is required", "reply": "I didn't catch that - could you type it again?"},
                    status=400,
                )

            reply = get_ai_reply(message, history)

            return JsonResponse({"reply": reply})

        return JsonResponse({"error": "Invalid request"}, status=400)

    except Exception as e:
        print("ERROR in chat_api:", repr(e))
        return JsonResponse(
            {"error": "Server error", "reply": "Something went wrong on my side. Please try again."},
            status=500,
        )
