## Описание
Программа реализует алгоритм RSA для шифрования и дешифрования сообщений. Ключи генерируются с использованием простых чисел.
## Установка и запуск
1. Убедитесь, что у вас установлен Python 3 и выше
2. Склонируйте репозиторий или сохраните файлы `hw.py` и `test_hw.py`.
3. Для запуска шифрования и дешифрования можно использовать такой алгоритм:
   ```bash
   public_key, private_key = generate_keys()
   message = "Hello"
   ciphertext = encrypt(message, public_key)
   decrypted_message = decrypt(ciphertext, private_key)
4. Для запуска тестов выполните команду
    ```bash
    python -m unittest test_hw.py