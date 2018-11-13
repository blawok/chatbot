import random
import re

bot_template = "BOT : {0}"
user_template = "USER : {0}"
name = "Bartek"
weather = "super duper"

responses = {
  "what's your name?": [
      "my name is {0}".format(name),
      "they call me {0}".format(name),
      "I go by {0}".format(name)
   ],
  "what's today's weather?": [
      "the weather is {0}".format(weather),
      "it's {0} today".format(weather)
    ]
}

rules = {
    'I want (.*)': [
        'What would it mean if you got {0}',
        'Why do you want {0}',
        "What's stopping you from getting {0}"
    ],
    'do you remember (.*)': [
        'Did you think I would forget {0}',
        "Why haven't you been able to forget {0}",
        'What about {0}',
        'Yes .. and?'
    ],
    'do you think (.*)': [
        'if {0}? Absolutely.',
        'No chance'
    ],
    'if (.*)': [
        "Do you really think it's likely that {0}",
        'Do you wish that {0}',
        'What do you think about {0}',
        'Really--if {0}'
    ]
}


def replace_pronouns(message):
    """Replacing pronouns to alternatives"""

    message = message.lower()
    if 'me' in message:
        return re.sub('me', 'you', message)
    if 'my' in message:
        return re.sub('my', 'your', message)
    if 'your' in message:
        return re.sub('your', 'my', message)
    if 'you' in message:
        return re.sub('you', 'me', message)

    return message


def match_rule(rules, message):
    """Matching patterns in user's queries.

    Returns: Defaults if there is no match,
        if pattern is matched, random response is being chosen
        and matched group is assigned to phrase variable.
    """

    response, phrase = "fuck u", None

    for pattern, responses in rules.items():
        match = re.search(pattern, message)
        if match is not None:
            response = random.choice(responses)
            if '{0}' in response:
                # extracting group inside parenthesis from match
                phrase = match.group(1)

    return response, phrase


def respond(message):
    """Creating respond.

    Returns: Response if there is no {0}
        and response with inserted phrase elif.
    """

    response, phrase = match_rule(rules, message)
    # if there is an option to include the phrase in response: 
    #   replace pronouns and insert phrase
    if '{0}' in response:
        phrase = replace_pronouns(phrase)
        # Include the phrase in the response
        response = response.format(phrase)
    return response


def send_message(message):
    """Printing messages """

    print(user_template.format(message))
    # Get the bot's response to the message
    if message in responses:
        response = random.choice(responses[message])
    else: 
        response = respond(message)
    print(bot_template.format(response))
    print("\n")


send_message("dupa")
send_message("what's today's weather?")
send_message("do you remember your last birthday")

# send_message("do you think humans should be worried about AI")
# send_message("I want a robot friend")
# send_message("what if you could be anything you wanted")