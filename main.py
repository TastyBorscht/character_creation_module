from random import randint

# from graphic_arts.start_game_banner import run_screensaver

DEFAULT_ATTACK: int = 5 # Константа содержащая базовое значение атаки.
DEFAULT_DEFENCE: int = 10  # Константа содержащая базовое значение защиты.
DEFAULT_STAMINA: int = 80  # Константа содержащая базовое значение выносливаости.


class Character:
    """
    Базовый класс с общими методами для всех классов.
    Принимает на вход имя персонажа.
    """

    RANGE_VALUE_ATTACK: tuple[int, int] = (1, 3)  # Константа для диапазона очков урона.
    RANGE_VALUE_DEFENCE: tuple[int, int] = (1,5)  # Константа для диапазона очкков защиты.
    SPECIAL_SKILL: str = 'Удача'  # Константа с названием специального навыка.
    SPECIAL_BUFF: int = 15  # Константа со значением бонусного урона класса.
    BRIEF_DESC_CHAR_CLASS: str = 'отважный любитель приключений'  # Константа содержащая краткое описание класса.


    def __init__(self, name: str):
        self.name = name

    def attack(self) -> str:
        """
        Метод для подсчета урона от атаки.
        Возвращает строку с результатом атаки.
        """
        value_attack: int = DEFAULT_ATTACK + randint(*self.RANGE_VALUE_ATTACK)
        return f'{self.name} нанёс противнику урон, равный {value_attack}'

    def defence(self) -> str:
        """
        Метод класса для подсчета предотвращенного урона.
        Возвращает строку с результатом защиты.
        """
        value_defence: int = DEFAULT_DEFENCE + randint(*self.RANGE_VALUE_DEFENCE)
        return f'{self.name} блокировал {value_defence} ед. урона.'


    def special(self) -> str:
        """
        Метод класса описывающий применение специального умения персонажа.
        Возвращает строку с результатом применения умения.
        """
        return (f'{self.name} применил специальное умение '
                f'"{self.SPECIAL_SKILL} {self.SPECIAL_BUFF}".')

    def __str__(self) -> str:
        """Метод класса возвращающий строку с описанием класса."""
        return f'{self.__class__.__name__} - {self.BRIEF_DESC_CHAR_CLASS}.'


class Warrior(Character):
    """Класс 'Воин' наследующий от класса Character."""
    BRIEF_DESC_CHAR_CLASS = (' дерзкий воин ближнего боя. '
                             'Сильный, выносливый и отважный')
    RANGE_VALUE_ATTACK = (3, 5)
    RANGE_VALUE_DEFENCE = (5, 10)
    SPECIAL_BUFF = DEFAULT_STAMINA + 25
    SPECIAL_SKILL = 'Выносливость'


class Mage(Character):
    """Класс 'Маг' наследующий от класса Character."""
    BRIEF_DESC_CHAR_CLASS = (' находчивый воин дальнего боя. '
                             'Обладает высоким интеллектом')
    RANGE_VALUE_ATTACK = (5, 10)
    RANGE_VALUE_DEFENCE = (-2, 2)
    SPECIAL_BUFF = DEFAULT_ATTACK + 40
    SPECIAL_SKILL = 'Атака'


class Healer(Character):
    """Класс 'Целитель' наследующий от класса Character."""
    BRIEF_DESC_CHAR_CLASS = (' могущественный заклинатель. '
                             'Черпает силы из природы, веры и духов')
    RANGE_VALUE_ATTACK = (-3, -1)
    RANGE_VALUE_DEFENCE = (2, 5)
    SPECIAL_BUFF = DEFAULT_DEFENCE + 30
    SPECIAL_SKILL = 'Защита'

# def attack(char_name: str, char_class: str) -> str:
#     """Вычисляет мощь вашей атаки."""
#     if char_class == 'warrior':
#         return (f'{char_name} нанёс урон '
#                 f'противнику равный {5 + randint(3, 5)}')
#     if char_class == 'mage':
#         return (f'{char_name} нанёс урон '
#                 f'противнику равный {5 + randint(5, 10)}')
#     if char_class == 'healer':
#         return (f'{char_name} нанёс урон '
#                 f'противнику равный {5 + randint(-3, -1)}')
#     return True
#
#
# def defence(char_name: str, char_class: str) -> str:
#     """Вычисляет крепость вашей обороны."""
#     if char_class == 'warrior':
#         return f'{char_name} блокировал {10 + randint(5, 10)} урона'
#     if char_class == 'mage':
#         return f'{char_name} блокировал {10 + randint(-2, 2)} урона'
#     if char_class == 'healer':
#         return f'{char_name} блокировал {10 + randint(2, 5)} урона'
#     return True
#
#
# def special(char_name: str, char_class: str) -> str:
#     """Вычисляет результат спец действия класса."""
#     if char_class == 'warrior':
#         return (f'{char_name} применил специальное умение '
#                 f'«Выносливость {80 + 25}»')
#     if char_class == 'mage':
#         return (f'{char_name} применил специальное умение '
#                 f'«Атака {5 + 40}»')
#     if char_class == 'healer':
#         return (f'{char_name} применил специальное умение '
#                 f'«Защита {10 + 30}»')
#     return True


def start_training(character):
    """
    Принимает на вход имя и класс персонажа.
    Возвращает сообщения о результатах цикла тренировки персонажа.
    """
    commands = {  # Словарь сопоставления введенных команд и методов класса.
        'attack' : character.attack,
        'defence' : character.defence,
        'special' : character.special,
    }
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack — чтобы атаковать противника, '
          'defence — чтобы блокировать атаку противника или '
          'special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd = None
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd in commands:
            print(commands[cmd])
    return 'Тренировка окончена.'


def choice_char_class(char_name: str) -> Character:
    """
    Возвращает строку с выбранным
    классом персонажа.
    """
    game_classes = {  # Словарь, в котором соотносится ввод пользователя и класс персонажа.
        'warrior': Warrior,
        'mage': Mage,
        'healer': Healer,
    }

    approve_choice: str = None  #  Переменная, в которую будет сохранятся строка с именем введенным пользователем.

    while approve_choice != 'y':
        selected_class: str = input('Введи название персонажа, '
                               'за которого хочешь играть: Воитель — warrior, '
                               'Маг — mage, Лекарь — healer: ')
        char_class: Character = game_classes[selected_class](char_name)
        print(char_class)
        approve_choice: str = input('Нажми (Y), чтобы подтвердить выбор, '
                               'или любую другую кнопку, '
                               'чтобы выбрать другого персонажа ').lower()
    return char_class


# if __name__ == '__main__':
#     run_screensaver()
#     print('Приветствую тебя, искатель приключений!')
#     print('Прежде чем начать игру...')
#     char_name: str = input('...назови себя: ')
#     print(f'Здравствуй, {char_name}! '
#           'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
#     print('Ты можешь выбрать один из трёх путей силы:')
#     print('Воитель, Маг, Лекарь')
#     char_class: str = choice_char_class()
#     print(start_training(char_name, char_class))
