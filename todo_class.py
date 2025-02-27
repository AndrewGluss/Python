class Todo:

    def __init__(self):
        self.things = []

    def add(self, business, priority):
        self.things.append(tuple([business, priority]))

    def get_by_priority(self, n):
        return [i[0] for i in self.things if i[1] == n]

    def get_low_priority(self):
        return [i[0] for i in self.things if i[1] == min(self.things, key=lambda i: i[1])[1]]

    def get_high_priority(self):
        return [i[0] for i in self.things if i[1] == max(self.things, key=lambda i: i[1])[1]]


todo = Todo()

print(todo.things)
print(todo.get_by_priority(1))
print(todo.get_low_priority())
print(todo.get_high_priority())

todo = Todo()

todo.add('Проснуться', 3)
todo.add('Помыться', 2)
todo.add('Поесть', 2)

print(todo.get_by_priority(2))


todo = Todo()

todo.add('Ответить на вопросы', 5)
todo.add('Сделать картинки', 1)
todo.add('Доделать задачи', 4)
todo.add('Дописать конспект', 5)

print(todo.get_low_priority())
print(todo.get_high_priority())
print(todo.get_by_priority(3))