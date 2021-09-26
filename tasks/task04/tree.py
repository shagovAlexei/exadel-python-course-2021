# Shagov Aleksei

# run
# python -m pytest tree.py -v

tree = {
    "node1": {
        "node11": {
            "node111": [1, 2, 3],
            "node112": [4, 5]
        },
        "node12": [6]
    },
    "node2": [7, 8, 9]
}

def my_pow(a, b):
    return (pow(a, b))

def test_math_2x2():
    assert my_pow(2, 2) == 4

def test_math_3x3():
    assert my_pow(3, 3) == 27

def test_math_4x4():
    assert my_pow(4, 4) == 256


def test_collect_leaves():
    assert my_pow(4, 4) == 256


def collect_leaves(tree, list_final=[]):
    if (isinstance(tree, dict)):
        for key in tree:
            value = tree[key]
            print(value)
