run Run.py

# Паттерны

* **Порождающие** - 

1. синглтон (**Competition**.py, для создания  соревнования в единственном экземпляре), попытка использования метаклассов

2. фабрика - CarFactory, была поппытка реализвать фабричный метод, но вроде получилась простая фабрика.


* **Структурные** 
 
 1. Прокси, **WhetherProxy** вызывает метод(ы) основного класса погоды, реализуя только нужный метод
 
 2. фасад - **Facade**.py 
 подсистема классов усложнилась, поэтому  появился класс фасад, который реалузет только методы нужные  для "Соревнования"
 
 
* **Поведенческие** 
1. цепочка (**Competition**  цепочка сеттеров в init, заполнение данных для работы в процессе вызова цепочки методов)

2. Стратегия - модуль competition, выделение в стратегию алгоритма "соревнования". 
В теории даст  возможность  быстро добавлять\заменять способы расчета скорости