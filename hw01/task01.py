# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других,
# то треугольника с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним,
# равнобедренным или равносторонним, только если треугольник существует .

a = 4
b = 5
c = 12

if a >= b+c or b >= a+c or c >= a+b:
    print("Треугольник не существует")
elif a == b and a == c and c == b:
    print('Треугольник существует')
    print('Треугольник равносторонний')
elif a == b or a == c or c == b:
    print('Треугольник существует')
    print('Треугольник равнобедренный')
elif a != b and a != c and c != b:
    print('Треугольник существует')
    print('Треугольник разносторонний')