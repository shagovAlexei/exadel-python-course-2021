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
    return pow(a, b)

def test_math_pow_2x2():
    assert my_pow(2, 2) == 4

def test_math_pow_3x3():
    assert my_pow(3, 3) == 27

def test_math_pow_4x4():
    assert my_pow(4, 4) == 256

def test_math_pow_5x3():
    assert my_pow(5, 3) == 125

def test_with_dict_of_dicts():
    assert collect_leaves(tree) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

def test_with_list():
    assert collect_leaves([1, 2, 3]) == [1, 2, 3]

def collect_leaves(tree, list_final=[]):
    if (isinstance(tree, dict)):
        for key in tree:
            value = tree[key]
            # print(value)
            if (isinstance(value, dict)):
                collect_leaves(value)
            elif (isinstance(value, list)):
                for list_item in value:
                    list_final.append(list_item)
                    # print(list_item)
            else:
                print(f"{value} is non list or dict")
    elif (isinstance(tree, list)):
        return(tree)
    else:
        list_final = []
        list_final.append(tree)

    return(list_final)

# collect_leaves(tree)
