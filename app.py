print("Title of program: Foxy's Encouragement bot")
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
      encouragement_list.append("tomorrow will be a better day and that you can confide in your family or friends")
      counter += 1
    if each_word == "happy":
      feelings_list.append("happy")
      encouragement_list.append("you are doing great! Remember to keep smiling")
      counter += 1
    if each_word == "tired":
      feelings_list.append("tired")
      encouragement_list.append("you are stronger than you think! Do not overwork yourself out as well and have ample rest")
      counter += 1
    if each_word == "depressed":
      feelings_list.append("depressed")
      encouragement_list.append("your family and friends are there for you! Tomorrow will be a better day!")
      counter +=1
    if each_word == "sleepy":
      feelings_list.append("sleepy")
      encouragement_list.append("you can do it! However, do have ample rest and do not burn the midnight oil")
      counter +=1
    if each_word == "angry":
      feelings_list.append("angry")
      encouragement_list.append("we all get angry at times! Take in 10 deep breaths slowly and feel yourself relax. Once you have calmed down, you can think and talk nicely with the person you are angry at")
      counter +=1
    if each_word == "upset":
      feelings_list.append("upset")
      encouragement_list.append("you are doing great! No matter what happens, stay optimistic")
      counter +=1
    if each_word == "disappointed":
      feelings_list.append("disappointed")
      encouragement_list.append("you have tried your best. No matter what the result is, you have done what you could. What you can do now is to work harder and try harder the next time and use this as a learning experience")
      counter +=1
    if each_word == "furious":
      feelings_list.append("furious")
      encouragement_list.append("we all make mistakes! Take a deep breath slowly and feel yourself relex. Once you have calmed down, you can think and talk nicely with the person or problem you are upset with")
      counter +=1
    if each_word == "annoyed":
      feelings_list.append("annoyed")
      encouragement_list.append("we all make mistakes! No matter what happens, calm down and think carefully on your actions")
      counter +=1
    if each_word == "confused":
      feelings_list.append("confused")
      encouragement_list.append("you can ask for help if you are confused")
      counter +=1

  if counter == 0:
    
      output = "Sorry I don't really understand. Please use different words."

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
