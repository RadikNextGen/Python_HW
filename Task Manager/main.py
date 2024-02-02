from task_manager import *

n = 1
while n:
    print('\n'
          '   Выберите действие:\n'
          '_______________________\n'
          '1 - Посмотреть задачи\n'
          '2 - Добавить задачу\n'
          '3 - Изменить статус\n'
          '4 - Удалить задачу\n'
          '5 - Посмотреть историю\n')
    act = int(input())
    if act == 1:
      ts.task_view()
    elif act == 2:
      ts.add_task()
    elif act == 3:
      ts.task_change()
    elif act == 4:
      ts.task_delete()
    else:
      ts.view_history()
