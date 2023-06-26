class UserInterface:
  def wait_user_answer(self):
      print(" Ввод пользовательских данных ". center(50, "="))
      print("Действие со статьями:")
      print("1 - создание статьи\n"
            "2 - просмотр статьи\n"
            "3 - просмотр определенной статьи\n"
            "4 - удаление статьи\n"
            "q - выход из программы")
      user_answer = input("Выбрите вариант действия: ")
      print("=" * 50)
      return user_answer

  def add_user_article(self):
      dict_article = {
          "название": None,
          "автор": None,
          "количество страниц": None,
          "описание": None
      }
      print(" Создание статьи ". center(50, "="))
      for key in dict_article:
          dict_article[key] = input(f"Введите {key}статьи: ")
      print("=" * 50)
      return dict_article