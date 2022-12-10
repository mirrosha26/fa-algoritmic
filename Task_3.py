'''
### класс Ведомость, имеющий атрибут класса: 
  *** список_дисциплин (значением является список с названиями дисциплин); 
  *** дисциплина (при задании значения проверять наличие дисциплины в атрибуте список_дисциплин), 
  *** группа;
### Методы: 
  *** put – добавляет в ведомость информацию об оценке студента (фамилия, оценка – параметры метода).
    Для хранения данных внутри класса используйте словарь, в котором ключом является фамилия студента. 
    Возможные оценки – «отлично», «хорошо», «удовл.», «неудовл.», «н/я»; 
  *** get – возвращает оценку, полученную студентом (фамилия студента – параметр метода); 
  *** change – изменяет оценку, полученную студентом (фамилия студента и новая оценка – параметры метода);
  *** del – удаляет информацию о студенте из ведомости (фамилия студента – параметр метода); 
  *** result – возвращает кортеж из 5 чисел (количество каждого вида оценок в ведомости); 
  *** __init__ – конструктор;
  *** __str__ – возвращает строку, содержащую заголовки (название экзамена, группа) и результаты экзамена в виде таблицы; 
  *** count – возвращает количество студентов в ведомости; 
  *** names – возвращает список фамилий, имеющихся в ведомости. 
Продемонстрируйте работу с классами, создав необходимые объекты и вызвав все их методы.
'''
# pip install tabulate
from tabulate import tabulate
from collections import Counter

class Statement:
  EVAL_OPTIONS = ['отлично', 'хорошо', 'удовл.', 'неудовл.', 'н/я' ]
  disciplines = ['Биология','Информатика','Физика','Русский']

  def __init__(self, discipline, group):
    if discipline in self.disciplines:
      self.discipline = discipline
      self.evaluations = {}
      self.group = group
      print('Отлично, ведомость создана!') 
    else:
      print('Дисциплины нет в списке, ведомость не создана') 

  def __str__(self):
    table = tabulate(self.evaluations.items(), headers=['Студент', 'Оценка'])
    return f'{table}'

  def put(self, surname, evaluation):
    if evaluation not in self.EVAL_OPTIONS:
      print("Оценка введена неверно")
      raise Exception("Оценка введена неверно")

    if self.evaluations.get(surname) != None:
      raise Exception("Оценка уже есть")

    self.evaluations[surname] = evaluation
    print(f'Оценка добавлена: {surname} [{evaluation}]')
    return True
    

  def get(self, surname):
    return self.evaluations.get(surname)

  def change(self, surname, evaluation):
    if evaluation in self.EVAL_OPTIONS:
      if surname in self.evaluations:
        self.evaluations[surname] = evaluation
        print(f'Оценка обновлена: {surname} [{evaluation}]')
      else:
        print('Студента нет в списке')
    else:
      print("Оценка введена неверно")

  def delete(self, surname):
    if surname in self.evaluations:
      del self.evaluations[surname]
      print(f'{surname} удален')
    else: 
      print('Студент не найден!')

  def result(self):
    typle = ()
    list_count = self.evaluations.values()
    for eval_op in Statement.EVAL_OPTIONS:
      count = 0 
      for i in list_count:
        if i == eval_op:
          count += 1
      typle += (count,)
    return typle

  def count(self):
    return len(self.evaluations)

  def names(self):
    return list(self.evaluations.keys())



print("Создаем две ведомости : ")
bio = Statement('Биология', 'B21-2')
info = Statement('Русский', 'ИТ21-2')
print("-------")
print("put: добовляем оценки студентов")
print("-------")
bio.put('Оливиков','хорошо')
bio.put('Ром','отлично')
bio.put('Иванов','хорошо')
bio.put('Толмачев','неудовл.')
bio.put("Гузов", 'н/я')
print("-------")
info.put('Си','хорошо')
info.put('Ким','отлично')
info.put('Ли','хорошо')
info.put('Ян','неудовл.')
info.put("Чан", 'н/я')
info.put("Ван", 'н/я')
print("-------")
print("get – получаем оценки нескольких студентов из группы B21-2")
print(f"Иванов: { bio.get('Иванов') }")
bio.change('Иванов','н/я')
print(f"Иванов: { bio.get('Иванов') }")
print("-------") 
print("delete, удалим информацию некторых студентов (я не использовал del, так как он магический)")
bio.delete('Иванов')
print(f"Иванов: { bio.get('Иванов') }")

print("-------") 
print("Result") 
print(bio.result())
print("-------") 
print("count – возвращает количество студентов в ведомости")
print(bio.count())
print("-------") 
print("names – возвращает список фамилий, имеющихся в ведомости")
print(bio.names())
print("-------") 
print("__str__")
print(bio)
print("---")