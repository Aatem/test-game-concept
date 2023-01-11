import prompt

def start_game(game):
    print(game.GAME_RULE)
    name = prompt.string('Здесь человек вводит имя ')
    question, current_answer = game.osnova_igri()
    print(f'здесь вопрос из игры {question}')
    user_answer = prompt.string('Здесь человек вводит ответ ')
    if user_answer == str(1): #единица просто для упрощения
        print('ура')
    else:
        print('не ура')
    
    
