class TextProcessor(object):

    #приватний метод, який перевіряє символ на рівність зі занками пунктуації та повертає True/False,
    def __is_punktiantian (self, znak):
       return znak == "," or znak == "." or znak == ";" or znak == ":" or znak == "!" or znak == "?"

    # публічний метод, який видалить всі знаки пунктіації з рядка який передається йому аргументом
    def get_clean_string (self, text):
        s = ""
        for i in text:
            if self.__is_punktiantian(i) == False:                  # додаємо негативну перевірку
                s += i
        return s

#створюємо екземпляр (об'єкт):
#p = TextProcessor()
#використовуємо на екзкмплярі прописану функцію:
#print(p.get_clean_string("qwe.r!t.y"))


class TextLoader:
    def __init__(self):
        self.__text_processor = TextProcessor()
        self.__clean_string = ""

    # публічний метод, який викликає метод класу TextProcessor.get_clean_string (12334543),
    # через свій атрибут__text_processor,
    # та записує значення в __clean_string.
    def set_clean_text(self, x):
        self.__clean_string = self.__text_processor.get_clean_string(x)

# Створюємо додатковий property для __clean_string,
# який буде виводити повідомлення в консоль про те, що виводиться вже очищений текст.
    @property
    def clean_string(self):
        return self.__clean_string



class DataInterface:
    def __init__(self):
        self._w = TextLoader()
    def process_text (self, n):
        for i in n:
            self._w.set_clean_text(i)
            print(self._w.clean_string)


l = DataInterface()
l.process_text(["4676.h8;!78jk,", "ythg,h:h"])
