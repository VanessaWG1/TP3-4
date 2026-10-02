from utils import display_expression_tree_from_dict
import noeud


arbre = {
0: ('exp', [1]),
1: ('+', [2, 3]),
2: ('2', []),
3: ('y', [])
}

display_expression_tree_from_dict(arbre)
