#Gustav Wallin
#Teinf20
#14/12/2021


#meny VVVVVVV

meny=input("""
   Välj vad du vill göra:
   
   1. Skriv en önskelista
   2. Läs en önskelista
   3. Stäng ner

   """)

#skapa önskelista VVVVVV

if "1" in meny:
   önskor = list()
   önskelista = input("Vems önskelista?: ")
   print("Skriv 'klar', när du är färdig")
   önska = ""
   count = 1

   while önska != "klar":
      önska = input("Önska "+str(count)+": ")
      if önska != "klar":
         önskor.append(önska)
         count += 1

   with open(önskelista+'.txt', 'w+') as text_file:
      text_file.write("\n".join(önskor))

#läsa önskelista VVVVVVV      

elif "2" in meny:
   önskor = list()
   önskelista = input("Vems önskelista?: ")
   with open(önskelista+'.txt', 'r') as text_file:
         lines = text_file.readlines()
         for line in lines:
            print(line, end="")

#shutdown  VVVVVVVV     

elif "3" in meny:
   exit()

elif "" in meny:
   exit()