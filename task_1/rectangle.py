# Добавьте логирование ошибок и полезной информации.
# Также реализуйте возможность запуска из командной
# строки с передачей параметров.

import logging
import argparse

# Настройка логгера
FORMAT = '{levelname:<8} - {asctime}. В модуле "{name}" ' \
         'в строке {lineno:03d} функция "{funcName}()" ' \
         'в {created} секунд записала сообщение: {msg}'
logging.basicConfig(
    format=FORMAT,
    style='{',
    level=logging.INFO,
    filename='rectangle.log',
    encoding='utf-8'
)
logger = logging.getLogger('rectangle')


class NegativeValueError(ValueError):
    """Исключение, выбрасываемое при установке отрицательных значений ширины или высоты."""
    pass


class Rectangle:
    """
    Класс, представляющий прямоугольник.

    Атрибуты:
    - width (int): ширина прямоугольника
    - height (int): высота прямоугольника

    Методы:
    - perimeter(): вычисляет периметр прямоугольника
    - area(): вычисляет площадь прямоугольника
    - __add__(other): определяет операцию сложения двух прямоугольников
    - __sub__(other): определяет операцию вычитания одного прямоугольника из другого
    - __lt__(other): определяет операцию "меньше" для двух прямоугольников
    - __eq__(other): определяет операцию "равно" для двух прямоугольников
    - __le__(other): определяет операцию "меньше или равно" для двух прямоугольников
    - __str__(): возвращает строковое представление прямоугольника
    - __repr__(): возвращает строковое представление прямоугольника, которое может быть использовано для создания нового объекта
    """

    def __init__(self, width, height=None):
        self.width = width
        self.height = height if height is not None else width

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value < 0:
            logger.error(f"Ошибка установки ширины: {value}")
            raise NegativeValueError(f"Ширина должна быть положительной, а не {value}")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value < 0:
            logger.error(f"Ошибка установки высоты: {value}")
            raise NegativeValueError(f"Высота должна быть положительной, а не {value}")
        self._height = value

    def perimeter(self):
        """
        Вычисляет периметр прямоугольника.

        Возвращает:
        - int: периметр прямоугольника
        """
        return 2 * (self.width + self.height)

    def area(self):
        """
        Вычисляет площадь прямоугольника.

        Возвращает:
        - int: площадь прямоугольника
        """
        return self.width * self.height

    def __add__(self, other):
        """
        Определяет операцию сложения двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - Rectangle: новый прямоугольник, полученный путем сложения двух исходных прямоугольников
        """
        width = self.width + other.width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter // 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        """
        Определяет операцию вычитания одного прямоугольника из другого.

        Аргументы:
        - other (Rectangle): вычитаемый прямоугольник

        Возвращает:
        - Rectangle: новый прямоугольник, полученный путем вычитания вычитаемого прямоугольника из исходного
        """
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self.width - other.width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter // 2 - width
        return Rectangle(width, height)

    def __lt__(self, other):
        """
        Определяет операцию "меньше" для двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - bool: True, если площадь первого прямоугольника меньше площади второго, иначе False
        """
        return self.area() < other.area()

    def __eq__(self, other):
        """
        Определяет операцию "равно" для двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - bool: True, если площади равны, иначе False
        """
        return self.area() == other.area()

    def __le__(self, other):
        """
        Определяет операцию "меньше или равно" для двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - bool: True, если площадь первого прямоугольника меньше или равна площади второго, иначе False
        """
        return self.area() <= other.area()

    def __str__(self):
        """
        Возвращает строковое представление прямоугольника.

        Возвращает:
        - str: строковое представление прямоугольника
        """
        return f"Прямоугольник со сторонами {self.width} и {self.height}"

    def __repr__(self):
        """
        Возвращает строковое представление прямоугольника, которое может быть использовано для создания нового объекта.

        Возвращает:
        - str: строковое представление прямоугольника
        """
        return f"Rectangle({self.width}, {self.height})"


def main():
    parser = argparse.ArgumentParser(description='Работа с прямоугольниками.')
    parser.add_argument('width', type=int, help='Ширина прямоугольника')
    parser.add_argument('height', type=int, nargs='?', default=None, help='Высота прямоугольника (необязательно)')
    args = parser.parse_args()

    try:
        rect = Rectangle(args.width, args.height)
        logger.info(f"Создан прямоугольник: {rect}")
        print(f"Прямоугольник: {rect}")
        print(f"Площадь: {rect.area()}")
        print(f"Периметр: {rect.perimeter()}")
    except NegativeValueError as e:
        logger.error(f"Ошибка создания прямоугольника: {e}")
        print(f"Ошибка: {e}")


# Для запуска скрипта нужно перейти в директорию task_1
#  test OK
#  python rectangle.py 10 5
#  python rectangle.py 10

#  test ERROR
#  python rectangle.py -10 5
#  python rectangle.py 10 -5
#  python rectangle.py -10

if __name__ == '__main__':
    main()
