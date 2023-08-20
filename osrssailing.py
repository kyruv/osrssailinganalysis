chaters = {}
positive_chats = []
negative_chats = []
neutral_chats = []

def classify_sentiment(chat):
    # Very sure of vote - using an emote that indicates preference
    if "voteyea" in chat:
        return "positive"
    if "votenay" in chat:
        return "negative"
    if "notlikethis" in chat:
        return "negative"
    if "kreygasm" in chat:
        return "positive"
    
    # Fairly impossible to misinterpret one word chats
    chat_is_one_word = " " not in chat
    if chat_is_one_word and "yes" in chat:
        return "positive"
    if chat_is_one_word and "no" in chat:
        return "negative"
    if chat_is_one_word and "residentsleeper" in chat:
        return "negative"
    if chat_is_one_word and "boo" in chat:
        return "negative"
    if chat_is_one_word and "nah" in chat:
        return "negative"
    if chat_is_one_word and "voteyay" in chat:
        return "negative"
    if chat_is_one_word and "yea" in chat:
        return "negative"
    if len(chat) > 0 and all(c == 'w' for c in chat):
        return "positive"
    if len(chat) > 0 and all(c == 'l' for c in chat):
        return "negative"
    
    # These are likely correct interpretations
    if "pog" in chat:
        return "positive"
    if "dont vote yes" in chat or "don't vote yes" in chat:
        return "negative"
    if "vote yes" in chat:
        return "positive"
    if "voted yes" in chat:
        return "positive"
    if "voting yes" in chat:
        return "positive"
    if "yes vote" in chat:
        return "positive"
    if "dont vote no" in chat or "don't vote no" in chat:
        return "positive"
    if "vote no" in chat:
        return "negative"
    if "voted no" in chat:
        return "negative"
    if "voting no" in chat:
        return "negative"
    if "garbage" in chat:
        return "negative"
    if "trash" in chat:
        return "negative"
    if "shamanism" in chat:
        return "negative"
    if "cool" in chat:
        return "positive"
    if "amazing" in chat:
        return "positive"
    if "minigame" in chat:
        return "negative"
    if "team sailing" in chat:
        return "positive"
    if "yas" in chat:
        return "positive"
    if "yes to" in chat:
        return "positive"
    if "no th" in chat:
        return "negative"
    if "yes pl" in chat:
        return "positive"
    if "hype" in chat:
        return "positive"
    

    return "unsure"
    


with open('Documents\Code\[8-19-23] OldSchoolRS - August 19th - The Summer Summit! - Chat.txt', 'r', encoding='utf8') as chat_log:
    # EXAMPLE CHAT... [2023-08-19 20:33:09 UTC] papayamusician: This is cool
    for chat in chat_log:

        # find the 3rd colon - helps split up the username
        colon_location = -1
        for i in range(0, 3):
            colon_location = chat.find(":", colon_location + 1)
        user = chat[25:colon_location]
        message = chat[colon_location+2:-1].lower()

        # Using simple rules, classify the chat as "postive", "negative", or "unsure"
        chat_sentiment = classify_sentiment(message)

        # Record the decision
        if chat_sentiment == "positive":
            positive_chats.append(message)
        elif chat_sentiment == "negative":
            negative_chats.append(message)
        else:
            neutral_chats.append(message)

        # Update the user's preference based on recent sentiment
        if chat_sentiment != "unsure":
            chaters[user] = chat_sentiment
        elif user not in chaters:
            chaters[user] = "unsure"

yes=0
no=0
unsure=0
for user, sentiment in chaters.items():
    if sentiment == "positive":
        yes+=1
    elif sentiment == "negative":
        no+=1
    else:
        unsure+=1

with open('positive_chats.txt', 'w', encoding='utf8') as f:
    for line in positive_chats:
        f.write(f"{line}\n")

with open('negative_chats.txt', 'w', encoding='utf8') as f:
    for line in negative_chats:
        f.write(f"{line}\n")

with open('unsure_chats.txt', 'w', encoding='utf8') as f:
    for line in neutral_chats:
        f.write(f"{line}\n")

with open('chaters.txt', 'w', encoding='utf8') as f:
    for user, sentiment in chaters.items():
        f.write(f"{user}:{sentiment}\n")

print(yes)
print(no)
print(unsure)

