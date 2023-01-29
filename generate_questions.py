import csv
import pymysql
import bag_of_words
import noun_extractor
import original_tasks


def generate_tasks(task_ids):
    '''This method generates personalised tasks for the list of task_ids provided. Task_id is tskl_tsk_id column in task_localization table'''

    #Retrieve the tasks from tsk_localization based on the tskl_tskl_id provided
    tasks_list = original_tasks.original_tasks(task_ids)
    #print("Tasks are : ", tasks_list)
    personalised_tasks = []
    for task in tasks_list:
        #For each tasks get the proper nouns. Proper nouns is a set to avoid duplicate values
        proper_nouns = get_proper_nouns(task)
        print("Proper_nouns are", proper_nouns)

        #Extract bag_of_words for each task
        bag_of_words_list = get_bag_of_words(task.get("task_id"))
        #print("bag of words are ", bag_of_words_list)

        personalised_tasks += replace_and_generate_questions(task, proper_nouns, bag_of_words_list)
    insert_into_database(personalised_tasks)

def get_proper_nouns(task):
    proper_nouns = []
    nouns = noun_extractor.noun_extractor(task.get("task_title"))
    nouns += noun_extractor.noun_extractor(task.get("task_description"))
    for noun in nouns:
        if noun not in proper_nouns:
            proper_nouns.append(noun)
    return proper_nouns

def get_bag_of_words(task_id):
    bag_of_words_list = bag_of_words.get_bag_of_words_from_db(task_id)
    return bag_of_words_list

def  replace_and_generate_questions(task, proper_nouns, bag_of_words):
    '''This method replaces the proper nouns in the original questions with the bag of words'''
    personalised_tasks = []

    for bag_of_word in bag_of_words:
        words = bag_of_word.get("bow").split(",")
        print("Words are: ", words)
        task_title = task.get("task_title")
        task_description = task.get("task_description")
        for noun in proper_nouns:
            if noun in task.get("task_title"):
                task_title = task_title.replace(
                    noun, words[proper_nouns.index(noun)])
            if noun in task.get("task_description"):
                task_description = task_description.replace(
                    noun, words[proper_nouns.index(noun)])
        personalised_tasks.append(
            {
                "task_id":task.get("task_id"),
                "bow_id": bag_of_word.get("bow_id"),
                "task_title": task_title, 
                "task_description": task_description
                
            }
            )

    print("Personalised tasks are: ", personalised_tasks)
    return personalised_tasks


def insert_into_database(new_tasks):
    '''This method inserts the generated personalized questions into database'''

    vals = [list(task.values()) for task in new_tasks]

    with open("out.csv", "w") as f:
        wr = csv.writer(f)
        wr.writerow(["task_id","bow_id","task title", "task_description"])
        wr.writerows(vals)

    #database connection
    connection = pymysql.connect(host="localhost", user="root", passwd="", database="dbse_project")

    cursor = connection.cursor()
    cursor.executemany("insert into tasks (tskgl_tskg_id, bow_id, task_title, task_desc ) values (%s, %s, %s, %s)", vals)

    #commiting the connection then closing it.
    connection.commit()
    connection.close()  

generate_tasks([487, 482])