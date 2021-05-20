from questions import QUESTIONS


def isAnswerCorrect(question, answer):

    '''
    :param question: question (Type JSON)
    :param answer:   user's choice for the answer (Type INT)
    :return:
        True if the answer is correct
        False if the answer is incorrect
    '''
    if answer == question["answer"]:
        return True
    else:
        return False

    #return True if answer == 2 else False      #remove this

def islfAnswerCorrect(question, answer):

    '''
    :param question: question (Type JSON)
    :param answer:   user's choice for the answer (Type INT)
    :return:
        True if the answer is correct
        False if the answer is incorrect
    '''
    if answer == question["answer"]:
        return True
    else:
        return False

def lifeLine(ques):

    '''
    :param ques: The question for which the lifeline is asked for. (Type JSON)
    :return: delete the key for two incorrect options and return the new ques value. (Type JSON)
    '''
    k=0
    e=0
    j=0
    a=0
    x = ques["answer"]
    for e,k in list(enumerate(ques.keys())):
        if j==2:
            break
        elif str(x) in k or "name" is k:
            continue
        else:
            del ques[k]
            j +=1
    return ques



def kbc():
    '''
        Rules to play KBC:
        * The user will have 15 rounds
        * In each round, user will get a question
        * For each question, there are 4 choices out of which ONLY one is correct.
        * Prompt the user for input of Correct Option number and give feedback about right or wrong.
        * Each correct answer get the user money corresponding to the question and displays the next question.
        * If the user is:
            1. below questions number 5, then the minimum amount rewarded is Rs. 0 (zero)
            2. As he correctly answers question number 5, the minimum reward becomes Rs. 10,000 (First level)
            3. As he correctly answers question number 11, the minimum reward becomes Rs. 3,20,000 (Second Level)
        * If the answer is wrong, then the user will return with the minimum reward.
        * If the user inputs "lifeline" (case insensitive) as input, then hide two incorrect options and
            prompt again for the input of answer.
        * NOTE:
            50-50 lifeline can be used ONLY ONCE.
            There is no option of lifeline for the last question( ques no. 15 ), even if the user has not used it before.
        * If the user inputs "quit" (case insensitive) as input, then user returns with the amount he has won until now,
            instead of the minimum amount.
    '''

    #  Display a welcome message only once to the user at the start of the game.
    #  For each question, display the prize won until now and available life line.
    # For now, the below code works for only one question without LIFE-LINE and QUIT checks

    print(" * * * WELCOME TO KBC * * * ")
    print("Rules for the game:")
    n = 0
    p = 0
    h=0
    while n<16:
        print(f'\tQuestion ',n+1,': ',QUESTIONS[n]["name"] )
        print(f'\t\tOptions:')
        print(f'\t\t\tOption 1: ',QUESTIONS[n]["option1"])
        print(f'\t\t\tOption 2: ',QUESTIONS[n]["option2"])
        print(f'\t\t\tOption 3: ',QUESTIONS[n]["option3"])
        print(f'\t\t\tOption 4: ',QUESTIONS[n]["option4"])
        ans = input('Your choice ( 1-4 ) : ')

        # check for the input validations

        if ans.lower().strip() == "lifeline" and h==0:                  
            q = lifeLine(QUESTIONS[n])
            e=0
            f=0
            print(f'\tQuestion ',n+1,': ',q["name"] )
            print(f'\t\tOptions:')
            for e,t in enumerate(q.keys()):
                if f==2:
                    break
                if e>0:
                    print(f'\t\t\tOption ',e,': ',q[t])
                    f+=1

            answ = input('Your choice ( 1-2 ) : ')

            # check for the input validations

            if islfAnswerCorrect(q, int(answ) ):
                # print the total money won.
                print('\nCorrect !')
                p += q["money"]
                print("Total money won : ",p)
                # See if the user has crossed a level, print that if yes
                if n==4:
                    print("Congratulations! You have crossed the first level.")
                elif n==10:
                    print("Congratulations! You have crossed the second level.")

            else:
                # end the game now.
                # also print the correct answer
                print('\nIncorrect !  \nThe correct answer is option ',q["answer"])
                print("Sorry! This is as far you go. Try again later.")
                if n<4:
                    print("Prize money won: Rs. 0")
                elif n>=4 and n<10:
                    print("Prize money won: Rs. 10,000")
                elif n>=10:
                    print("Prize money won: Rs. 3,20,000")
                break
            h+=1
        elif ans.strip().lower()=="lifeline" and h>0:
            print("*Lifeline not available!*")
            ans = input('Your choice ( 1-4 ) : ')
            if isAnswerCorrect(QUESTIONS[n], int(ans) ):
                # print the total money won.
                print('\nCorrect !')
                p += QUESTIONS[n]["money"]
                print("Total money won : ",p)
                # See if the user has crossed a level, print that if yes
                if n==4:
                    print("Congratulations! You have crossed the first level.")
                elif n==10:
                    print("Congratulations! You have crossed the second level.")

            else:
                # end the game now.
                # also print the correct answer
                print('\nIncorrect !  \nThe correct answer is option ',QUESTIONS[n]["answer"])
                print("Sorry! This is as far you go. Try again later.")
                if n<4:
                    print("Prize money won: Rs. 0")
                elif n>=4 and n<10:
                    print("Prize money won: Rs. 10,000")
                elif n>=10:
                    print("Prize money won: Rs. 3,20,000")
                break
        else:
            if isAnswerCorrect(QUESTIONS[n], int(ans) ):
                # print the total money won.
                print('\nCorrect !')
                p += QUESTIONS[n]["money"]
                print("Total money won : ",p)
                # See if the user has crossed a level, print that if yes
                if n==4:
                    print("Congratulations! You have crossed the first level.")
                elif n==10:
                    print("Congratulations! You have crossed the second level.")

            else:
                # end the game now.
                # also print the correct answer
                print('\nIncorrect !  \nThe correct answer is option ',QUESTIONS[n]["answer"])
                print("Sorry! This is as far you go. Try again later.")
                if n<4:
                    print("Prize money won: Rs. 0")
                elif n>=4 and n<10:
                    print("Prize money won: Rs. 10,000")
                elif n>=10:
                    print("Prize money won: Rs. 3,20,000")
                break
            # print the total money won in the end.
        n+=1
            
      

kbc()
