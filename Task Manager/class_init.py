from datetime import datetime
from dataclasses import dataclass, field
from typing import List, Optional

status_dic = ["начата", "выполняется", "ревью", "закончена", "отменена"]


@dataclass
class Task:
    task_name: str
    description: str
    status: str
    date: str
    last_change: str
    # date: datetime = datetime.now().strftime("%Y-%m-%d %H:%M")
    # last_change: datetime = field(default_factory=datetime.now)

    def change_status(self, num):
        current_status_index = status_dic.index(self.status)
        if num == 1:
            new_status_index = current_status_index + 1
        elif num == 2:
            new_status_index = current_status_index - 1
        else:
            new_status_index = 4
        if new_status_index > 4:
            print('Задача отменена')
        elif new_status_index == 3 and num == 2:
            print('Задача отменена')
        elif new_status_index < 0:
            print('Недопустимый статус задачи')
        else:
            self.status = status_dic[new_status_index]
            self.last_change = datetime.now().strftime("%Y-%m-%d %H:%M")
            W = (f"name:             {self.task_name}\n"
                 f"description:      {self.description}\n"
                 f"status:           {self.status}\n"
                 f"date:             {self.date}\n"
                 f"last change:      {self.last_change}\n")
            print(W)

    def to_json(self):
        exit = {'name': self.task_name,
                'description': self.description,
                'status': self.status,
                'date': self.date,
                'last change': self.last_change}
        return exit

    def __repr__(self):
        W = (f"name:             {self.task_name}\n"
                f"description:      {self.description}\n"
                f"status:           {self.status}\n"
                f"date:             {self.date}\n"
                f"last change:      {self.last_change}\n")
        return W