from bs4 import BeautifulSoup
import pymysql
import re

def original_tasks(task_ids):
    connection = pymysql.connect(host="localhost", user="root", passwd="", database="sqlvali_data")
    cursor = connection.cursor()
    query = "select tskl_tsk_id, tskl_title, tskl_description from task_localization where tskl_tsk_id in  {}  and tskl_lang = 'en'".format(tuple(task_ids))
    cursor.execute(query)
    rows = cursor.fetchall()
    connection.close()

    tasks = []
    for row in rows:
        task = {
                "task_id" : row[0],
                "task_title" : parse_html_script(row[1]),
                "task_description" : parse_html_script(row[2])
                }
        tasks.append(task)
    return tasks

def parse_html_script(text):
    print("text is: ", text)
    soup = BeautifulSoup(str(text), features="html.parser")
     # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()  # rip it out
    result = soup.get_text()
    print("result is: ", result)
    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in result.splitlines())
    print("lines are :", lines)
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    print("chunks are ", chunks)
    # drop blank lines
    result = '\n'.join(chunk for chunk in chunks if chunk)
    a1 = re.sub(r'[^\w\s\r]', ' ', result)
    x = a1.replace('rn', ' ')
    x = x.replace('tttt', ' ')
    x = x.replace('\xa0', ' ')
    x = x.replace('\n', ' ')
    print("x is: ", x)
    return x