# -*- coding: utf-8 -*-
import re
textos = [
"""#oomf be mine 😍""",
"""“@Lilerkk: Niggas used to love to edit they pictures with picnik back in myspace days 😂😂😂”!!!!!""",
"""'Ezra is a babe even if he is A I''ll still love him💕'""",
"""So does anyone have plans to stsre at their phones somewhere exciting tonight?""",
"""'Actually I feel cheap ... she''s never in town and here I am forgetting about it #ISuck'""",
"""I Would enjoy a job where my life is on the line.""",
"""I Have gotten the important things I want in my life.""",
"""'#mcm is Oscar. I love him. He''s perff.☺️💕 http://t.co/JFGxr09k2c'""",
"""My profile pic is actually me photobombing in the last minute hahahahahaha"""
]

def limpiaTweet():
	texto_res = list()
	for texto in textos:
		texto = texto.split(" ")
		#print(texto)
		texto_temp = list()
		for palabra in texto:		
			palabra = re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",palabra)
			palabra = palabra.replace(" ", "")
			#print(palabra)			
			if(palabra != ""):
				texto_temp.append(palabra)
			#texto_temp.append(' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",palabra).split()))		
		texto_res.append(texto_temp)
		#for linea in texto_res:
			#print(linea)
	print (texto_res)

limpiaTweet()
