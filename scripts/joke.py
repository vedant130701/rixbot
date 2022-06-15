from jokeapi import Jokes # Import the Jokes class
import asyncio

async def print_joke(entityVal):
    j = await Jokes()  # Initialise the class
    print(entityVal)
    if entityVal == "":
        joke = await j.get_joke()
    else:
        joke = await j.get_joke(category = [entityVal])
    # joke = await j.get_joke()  # Retrieve a random joke
    if joke["type"] == "single": # Print the joke
        return joke["joke"]
    else:
        return joke["setup"] + "\n" + joke["delivery"]