print("Title of program: yay encouragement bot")
print()
while True:
  description = input("Could you describe how you feel in a sentence?")

  list_of_words = description.split()

  feelings_list = []
  encouragement_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "sad":
      feelings_list.append("sad")
      encouragement_list.append("it is completely human to be sad, don't be afraid to release your emotions :)")
      counter += 1
    if each_word == "happy":
      feelings_list.append("happy")
      encouragement_list.append("that's great! keep smiling love xx")
      counter += 1
    if each_word == "tired":
      feelings_list.append("tired")
      encouragement_list.append("life gets a tad too hectic at times, remember to place yourself first and take a breather")
      counter += 1
      
    if each_word == "bored":
      feelings_list.append("bored")
      encouragement_list.append("YOLO, try out something new today!! life's too short to be wasted")
      counter += 1

  if counter == 0:
    
      output = "Sorry I don't really understand. Please use different words?"

  elif counter == 1:
    
      output = "It seems that you are feeling quite " + feelings_list[0] + ". However, do remember that "+ encouragement_list[0] + "! Hope you feel better :)"  

  else:

    feelings = ""    
    for i in range(len(feelings_list)-1):
      feelings += feelings_list[i] + ", "
    feelings += "and " + feelings_list[-1]
    
    encouragement = ""    
    for j in range(len(encouragement_list)-1):
      encouragement += encouragement_list[i] + ", "
    encouragement += "and " + encouragement_list[-1]

    output = "It seems that you are feeling quite " + feelings + ". Please always remember "+ encouragement + "! Hope you feel better :)"

  print()
  print(output)
  print()
