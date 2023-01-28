import random
import json
import os

async def get_random():
    with open(os.getcwd() + '/src/bot_app/words.json') as f:
        words = json.load(f)
    res = random.choice(words)
    return res
