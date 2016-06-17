import aiml
import os

"""
For text to speech conversion.

TODO: Configure this, or find a better alternative.
"""
import pyttsx

kernel = aiml.Kernel()

if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "jarvis_brain.brn")
else:
    kernel.bootstrap(learnFiles = "start_jarvis.xml", commands = "load aimls jarvis")
    kernel.saveBrain("jarvis_brain.brn")

# kernel now ready for use
while True:
    response = kernel.respond(raw_input("Enter your message >> "))
    print response