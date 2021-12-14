options = list()
genre = input("Vems önskelista?: ")
print("Skrive klar, när du är färdig")
option = ""
count = 1
while option != "klar":
   option = input("Option "+str(count)+": ")
   if option != "klar":
      options.append(option)
      count += 1

with open(genre+'.txt', 'w+') as text_file:
  text_file.write("\n".join(options))
