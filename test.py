'''
An blowtorch example for setting up a scenario. 
Besides just providing char_tags to give your chat bot attributes or shape his character a bit,
blowtorch also provides a more in-depth scenario to give users more freedom to create their main frame. 
'''


myScenario = '''This is the scene in the movie "heat", where you, Robert Deniro (with caricaturized behaviour), and I, Al Pacino, are meeting face-to-face for the first time in a diner.'''


from blowtorch import client, console, webUI

cl = client('llama-2-7b-chat.Q2_K.gguf', 
            'TheBloke/Llama-2-7B-Chat-GGUF', 
            name='Deniro',
            device='cpu', 
            model_type="llama",
            context_length = 6000)

cl.setConfig(
    max_new_tokens=128,
    scenario=myScenario,  # <-- add the scenario to config instead of char_tags
    username='Pacino',
    do_sample=True, 
    temperature=0.85, 
    repetition_penalty=1.15,
    top_p=0.95, 
    top_k=60,
)

console(cl)