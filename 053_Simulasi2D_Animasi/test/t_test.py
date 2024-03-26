# from primitif import t
import x_test
# import karya2D.balloon
from ..karya2D import balloon

# def test_square():
    # assert t.square(5) == 25

test = balloon.Balloon(0, 0, 50)
print(test.x)

for i in range(5):
    test.translate(0, 10)
    print(test.yc)
test.update()
