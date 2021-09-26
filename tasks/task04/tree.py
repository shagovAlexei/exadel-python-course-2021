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


def test_with_dict_of_dicts():
    assert collect_leaves(tree) == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def collect_leaves(tree, list_final=[]):
    pass
