from class_init import *
import sys
import json


@dataclass
class History:
    name: str
    date: str
    action: str

    def to_json(self):
        H = {'name': self.name,
                'date': self.date,
                'action': self.action}
        return H

    def __repr__(self):
        return (f"date       {self.date}\n"
                f"movement   {self.action}\n")


@dataclass
class Task_Manager:
    slovar_zadach = []
    slovar_poiska = []
    try:
        with open('data/tasks.json', 'r') as file:
            f = json.load(file)
        for task in f.keys():
            name = f[task]["name"]
            description = f[task]["description"]
            status = f[task]["status"]
            date = f[task]["date"]
            last_change = f[task]["last change"]
            slovar_zadach.append(Task(name, description, status, date, last_change))
    except Exception:
        pass

    try:
        with open('data/history.json', 'r') as file:
            k = json.load(file)
        for task in k.keys():
            name = k[task]["name"]
            date = k[task]["date"]
            action = k[task]["action"]
            slovar_poiska.append(Task(name, date, action))
    except Exception:
        pass

    def add_task(self):
        name = input("name ")
        description = input("description ")
        status = input("status ")
        date: datetime = datetime.now().strftime("%Y-%m-%d %H:%M")
        last_change: datetime = date
        self.slovar_zadach.append(Task(name, description, status, date, last_change))
        to_json = {}
        for i in self.slovar_zadach:
            to_json[i.task_name] = i.to_json()
        # print(to\_json)
        with open('data/tasks.json', 'w') as file:
            json.dump(to_json, file, indent=2)
        self.slovar_poiska.append(History(name, datetime.now().strftime("%Y-%m-%d %H:%M"), "Task addendum"))
        to_json = {}
        for i in self.slovar_poiska:
            to_json[i.name] = i.to_json()
        # print(to\_json)
        with open('data/history.json', 'w') as file:
            json.dump(to_json, file, indent=2)

    def task_view(self):
        for task in self.slovar_zadach:
            print(task)
        self.slovar_poiska.append(History("all tasks", datetime.now().strftime("%Y-%m-%d %H:%M"), "Task search"))
        to_json = {}
        for i in self.slovar_poiska:
            to_json[i.name] = i.to_json()
        # print(to\_json)
        with open('data/history.json', 'w') as file:
            json.dump(to_json, file, indent=2)

    def task_delete(self, name):
        #print(self.slovar_zadach)
        for i in self.slovar_zadach:
            if i.task_name == name:
                self.slovar_zadach.remove(i)
                self.slovar_poiska.append(History(i.task_name, datetime.now().strftime("%Y-%m-%d %H:%M"), "Task delete"))
                break
        to_json = {}
        for i in self.slovar_zadach:
            to_json[i.task_name] = i.to_json()
        # print(to\_json)
        with open('data/tasks.json', 'w') as file:
            json.dump(to_json, file, indent=2)
        to_json = {}
        for i in self.slovar_poiska:
            to_json[i.name] = i.to_json()
        # print(to\_json)
        with open('data/history.json', 'w') as file:
            json.dump(to_json, file, indent=2)

    def task_change(self):
        print('Введите имя задачи, статус которой хотите изменить:')
        name = input()
        print('Как вы хотите изменить статус программы?'
              '________________________________________'
              '          1 - повысить статус'
              '          2 - понизить статус'
              '          3 - отменить задачу')
        num = int(input())
        for i in self.slovar_zadach:
            if i.task_name == name:
                while num != 1 and num != 2 and num != 3:
                    print('Как вы хотите изменить статус программы?\n'
                          '________________________________________\n'
                          '          1 - повысить статус\n'
                          '          2 - понизить статус\n'
                          '          3 - отменить задачу\n')
                    num = int(input())
                    if num != 1 and num != 2 and num != 3:
                        print("Пожалуйста, введите корректное значение:\n")
                self.slovar_zadach[self.slovar_zadach.index(i)].change_status(num)

                self.slovar_poiska.append(History(i.task_name, datetime.now().strftime("%Y-%m-%d %H:%M"), "Task change"))
                break
        to_json = {}
        for i in self.slovar_zadach:
            to_json[i.task_name] = i.to_json()
        # print(to\_json)
        with open('data/tasks.json', 'w') as file:
            json.dump(to_json, file, indent=2)


    def view_history(self):
        #print(self.slovar_poiska)
        for i in self.slovar_poiska:
            print(i)

ts = Task_Manager()