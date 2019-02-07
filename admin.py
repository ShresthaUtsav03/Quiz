




import json,os


def inputInt(prompt):
    while True:
        try:
            temp = int(input(prompt))    
            return temp
        except:
            continue



def inputSomething(prompt):
    global data_list
    question = input(prompt)
    return question
        

def saveChanges(dataList):
    with open('data.txt', 'w') as outfile:
        json.dump(dataList, outfile)
    





print('Welcome to the Admin  Program.')

            

with open('data.txt','r') as data_file:    
    data_text_file = json.load(data_file)
current_ques_list = []
while True:

    data_list = []
    print('Choose [a]dd, [l]ist, [s]earch, [v]iew, [d]elete or [q]uit.')
    choice = input('> ').strip()
    try:
        if(type(choice)!='str'):
            raise Exception
    except Exception:
        if choice == 'a':
            
            
            question = str(inputSomething("Enter the question: ").strip()).lower()
            while True:
                if(question == ""):
                    question =str(inputSomething("Enter the question: ").strip()).lower()
                else:
                    break


            answer = []
            while True:
                x = str(input("Enter a valid answer (enter 'q' when done):").strip()).lower()
                if(x==''):
                    continue
                elif(x!='' and x!='q'):
                    answer.append(x)
                elif(x=='q' and len(answer)!=0):
                    break
                
            temp = inputInt('Enter question difficulty (1-5)')
            while True:
                if(temp < 1 or temp >5):

                    print("Invalid value. Must be an integer between 1 and 5")
                    temp = inputInt('Enter question difficulty (1-5)')
                else:
                    break

            
            diff = temp
        
            final_object = {'question':question,'answer':answer,'diff_level':diff}
            data_list.append(final_object)
            current_ques_list.append(final_object)
            if(os.stat("data.txt").st_size == 0):
                saveChanges(data_list)
            else:
                
           
                for i in data_list:
                    data_text_file.append(i)
                saveChanges(data_text_file)
            
        
        elif choice == 'l':
          
            if(len(current_ques_list)==0):
                print("No questions saved")
            else:
                print("Current Question:")
                for i in range(0,len(current_ques_list)):
                    print('\t',i+1,")",current_ques_list[i]['question'])    



        elif choice == 's':
            
            search_term = inputSomething("Enter a search term: ").strip()
            
            
            for i in range(len(current_ques_list)):
                if search_term in current_ques_list[i]['question']:
                    print("Search results:")
                    print('\t',i+1,')',current_ques_list[i]['question'])
        


        elif choice == 'v':
           
            view_index = inputInt('Question number to view: ')
            
            try:
                req_data = current_ques_list[view_index-1]
                print("Question:")
                print("\t",req_data['question'])
                print("\t","Valid Answers: ",', '.join(req_data['answer']))
                print("\t","Difficulty: ",req_data["diff_level"])
                
            except:
                print("Invalid index number")

            

        elif choice == 'd':
           
            try:
                del_index = int(inputInt('Question number to delete: '))-1
                if(del_index+1>len(current_ques_list)):
                    print("Invalid index number")
                else:
                    del_question = current_ques_list.pop(del_index)
                    
                  
                    for i in range(len(data_text_file)):
                        if(data_text_file[i]['question']==del_question['question']):
                            del data_text_file[i]
                    
                    
                    
                    try:
                       
                        with open('data.txt', 'w') as outfile:
                            json.dump(data_text_file, outfile)
                    
                    except:
                        print("Invalid index number")
            except:
                pass



        elif choice == 'q':
            
            print("GoodBye!")
            break



        else:
           
            print("Invalid choice")
            continue
