#Step 5

import random

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
#Delete this line: word_list = ["ardvark", "baboon", "camel"]
from hangman_words import word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
from hangman_art import logo
print(logo)
print("Adivinhe o livro da bíblia.")
print("A primeira letra do nome do livro é maiúscula.")
print("Colocamos números a frente dos livros com nomes repetidos.")

#Testing code
# print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Adivinhe uma letra: ")
    
    

    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    repetida = []
    if guess not in repetida:
        repetida.append(guess)
    elif guess in repetida:
      print("Esta letra já foi.")
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
            print("Você acertou")

    #Check if user is wrong.
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        lives -= 1
        print("Você perdeu uma vida")
        if lives == 1:
          if chosen_word == "Genesis" or chosen_word == "Exodo" or chosen_word == "Levítico" or chosen_word == "Deuteronomio" or chosen_word == "Numeros":
              print("DICA: livro de Moisés.")
          elif chosen_word == "Josue":
              print("DICA: Esforça-te")
          elif chosen_word == "Juizes":
              print("DICA: julgamentos")
          elif chosen_word == "Rute":
              print("DICA: Eu fico")
          elif chosen_word == "1Samuel" or chosen_word == "2Samuel" or chosen_word == "Isaias" or chosen_word == "Jeremias" or chosen_word == "Ezequiel" or chosen_word == "Oseias" or chosen_word == "Joel" or chosen_word == "Amos" or chosen_word == "Obdias" or chosen_word == "Jonas" or chosen_word == "Miqueias" or chosen_word == "Naum" or chosen_word == "Habacuque" or chosen_word == "Sofonias" or chosen_word == "Ageu" or chosen_word == "Zacarias" or chosen_word == "Malaquias":
              print("DICA: Profeta")
          elif chosen_word == "1Reis" or chosen_word == "2Reis" or chosen_word == "1Cronicas" or chosen_word == "2Cronicas":
              print("DICA: História")
          elif chosen_word == "Neemias" or chosen_word == "Esdras":
              print("DICA: Reconstrução")
          elif chosen_word == "Ester" or chosen_word == "Jo":
              print("DICA: Exaltação")
          elif chosen_word == "Salmos":
              print("DICA: Hinario")
          elif chosen_word == "Proverbios" or chosen_word == "Eclesiastes" or chosen_word == "Cantares":
              print("DICA: Salomão")
          elif chosen_word == "Daniel":
              print("DICA: Homem mui desejado")
          elif chosen_word == "Mateus" or chosen_word == "Lucas" or chosen_word == "Marcos" or chosen_word == "Atos":
              print("DICA: Evangelho")
          elif chosen_word == "Apocalipse":
              print ("DICA: Visão")
          elif chosen_word == "Lamentacoes":
              print("DICA: Reclamações")
          else:
              print("DICA: Cartas")
        if lives == 0:
            end_of_game = True
            print("Você perdeu.")
            print(f"Resposta: {chosen_word}")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("Você ganhou.")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    from hangman_art import stages
    print(stages[lives])