## Tasks to be implemented (as there wasn´t any implementation especify, it just pass)
def task1():
  pass
def task2():
  pass
def task3():
  pass
def task4():
  pass
def task5():
  pass
def task6():
  pass
# Creation and run of the DAG
with DAG("my_dag", start_date =datetime(2022,1,1),schedule_interval="@daily",catchup=False) as dag:
  task1 = PythonOperator(task_id="task1", python_callable=task1)

  with TaskGroup("section_1", tooltip="Tasks for section_1") as section_1:
    task2 = PythonOperator( task_id="task2", python_callable=task2 )
    task3 = PythonOperator(task_id="task3",python_callable=task3)
  
  with TaskGroup("section_2", tooltip="Tasks for section_2") as section_2:
      task4 = PythonOperator(task_id="task4", python_callable=task4)
      task5 = PythonOperator(task_id="task5",python_callable=task5)
      task6 = PythonOperator(task_id="task6", python_callable=task6)
  

  task1 >> section_1 >> section_2 