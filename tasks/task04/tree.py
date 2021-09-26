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

collections_leaves(tree) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

collections_leaves([1, 2, 3]) == [1, 2, 3]
