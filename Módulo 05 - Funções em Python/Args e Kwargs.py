#Args recebem os valores como tuplas e kwargs como dicionário. (*args / **kwargs)
#Explicação das variáveis
    #"musica" = recebe o nome da música com o artista
    #"letra" = recebe a letra da música
    #"info" = recebe as informações da música (compositores, álbum, lançamento...)
    
def exibir_musica(musica, *letra, **info):
    #"letra_completa" = servirá para utilizar o join que fará a junção das linhas e o "\n" serve para a quebra de linha
    letra_completa = "\n".join(letra)
    #"informacoes" = cria uma lista "chave: valor para cada item do dicionário. O trecho "chave.title" serve para transformar a chave em um "Título", é para a formatação da lista na hora de exibir no terminal.
    informacoes = "\n".join([f"{chave.title()}: {valor}" for chave, valor in info.items()])
    #"extenso" = estrutura do que será exibido no terminal, utilizando \n para quebra de linha
    extenso = f"{musica}\n\n{letra_completa}\n\n{informacoes}"
    print(extenso)
    
exibir_musica("Snuff - Slipknot", "Bury all your secrets in my skin",
"Come away with innocence",
"And leave me with my sins",
"The air around me still feels like a cage",
"And love is just a camouflage",
"For what resembles rage again",

"So if you love me, let me go",
"And run away before I know",
"My heart is just too dark to care",
"I can't destroy what isn't there",
"Deliver me into my fate",
"If I'm alone, I cannot hate",
"I don't deserve to have you",
"My smile was taken long ago",
"If I can change, I hope I never know",

"I still press your letters to my lips",
"And cherish them in parts of me",
"That savor every kiss",
"I couldn't face a life without your light",
"But all of that was ripped apart",
"When you refused to fight",

"So save your breath, I will not hear",
"I think I made it very clear",
"You couldn't hate enough to love",
"Is that supposed to be enough?",
"I only wish you weren't my friend",
"Then I could hurt you in the end",
"I never claimed to be a saint",
"My own was banished long ago",
"It took the death of hope to let you go",

"So break yourself against my stones",
"And spit your pity in my soul",
"You never needed any help",
"You sold me out to save yourself",
"And I won't listen to your shame",
"You ran away, you're all the same",
"Angels lie to keep control",
"My love was punished long ago",
"If you still care, don't ever let me know",
"If you still care, don't ever let me know",
composição="Craig Jones / Corey Taylor / Chris Fehn / Jim Root / Joey Jordison / Mick Thomson / Paul Gray / Shawn / Sid Wilson",
lançamento=2008,
álbum="All hope is gone")