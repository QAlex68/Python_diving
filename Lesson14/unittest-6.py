# ➢ Метод tearDown
# Метод tearDown будет вызван после успешного выполнения метода setUp и в случае
# если тест отработал успешно, и если он провалился.
import unittest


class TestSample(unittest.TestCase):
    def setUp(self) -> None:
        with open('top_secret.txt', 'w', encoding='utf-8') as f:
            for i in range(10):
                f.write(f'{i:05}\n')

    def test_line(self):
        with open('top_secret.txt', 'r', encoding='utf-8') as f:
            for i, line in enumerate(f, start=1):
                pass
        self.assertEqual(i, 10)

    def test_first(self):
        with open('top_secret.txt', 'r', encoding='utf-8') as f:
            first = f.read(5)
            self.assertEqual(first, '00000')

    def tearDown(self) -> None:
        from pathlib import Path
        Path('top_secret.txt').unlink()


if __name__ == '__main__':
    unittest.main()
# В примере метод setUp создаёт перед каждым тестом файл со строками чисел. Два
# теста работают с этим файлом. И после каждого происходит удаление файла из
# tearDown метода.
# Даже если провалить тест, файл будет удалён.

# Перечень доступных утверждений assert
# В списке ниже приведены доступные в unittest утверждения и пояснения о том что
# именно они проверяют.
# ● assertEqual(a, b) - a == b
# ● assertNotEqual(a, b) - a != b
# ● assertTrue(x) - bool(x) is True
# ● assertFalse(x) - bool(x) is False
# ● assertIs(a, b) - a is b
# ● assertIsNot(a, b) - a is not b
# ● assertIsNone(x) - x is None
# ● assertIsNotNone(x) - x is not None
# ● assertIn(a, b) - a in b
# ● assertNotIn(a, b) - a not in b
# ● assertIsInstance(a, b) - isinstance(a, b)
# ● assertNotIsInstance(a, b) - not isinstance(a, b)
# ● assertRaises(exc, fun, *args, **kwds) - функция fun(*args, **kwds) поднимает
# исключение exc
# ● assertRaisesRegex(exc, r, fun, *args, **kwds) - функция fun(*args, **kwds)
# поднимает исключение exc и сообщение совпадает с регулярным
# выражением r
# ● assertWarns(warn, fun, *args, **kwds) - функция fun(*args, **kwds) поднимает
# предупреждение warn
# ● assertWarnsRegex(warn, r, fun, *args, **kwds) - функция fun(*args, **kwds)
# поднимает предупреждение warn и сообщение совпадает с регулярным
# выражением r
# ● assertLogs(logger, level) - блок with записывает логи в logger с уровнем level
# 20
# ● assertNoLogs(logger, level) - блок with не записывает логи в logger с уровнем
# level
# ● assertAlmostEqual(a, b) - round(a-b, 7) == 0
# ● assertNotAlmostEqual(a, b) - round(a-b, 7) != 0
# ● assertGreater(a, b) - a > b
# ● assertGreaterEqual(a, b) - a >= b
# ● assertLess(a, b) - a < b
# ● assertLessEqual(a, b) - a <= b
# ● assertRegex(s, r) - r.search(s)
# ● assertNotRegex(s, r) - not r.search(s)
# ● assertCountEqual(a, b) - a и b содержат одни и те же элементы в одинаковом
# количестве независимо от их порядка в коллекциях
# Как вы видите перечень допустимых проверок достаточно обширный, чтобы
# удовлетворить практически любые запросы по написанию тестов
