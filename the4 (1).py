def construct_forest(defs):
    def term(string):
        no_spaces = string.replace(" ", "")
        split_from_equality = no_spaces.split("=")
        term1 = split_from_equality[0]
        if "+" in split_from_equality[1]:
            term2 = split_from_equality[1].split("+")[0]
            term3 = split_from_equality[1].split("+")[1]
            operator = "+"
        elif "-" in split_from_equality[1]:
            term2 = split_from_equality[1].split("-")[0]
            term3 = split_from_equality[1].split("-")[1]
            operator = "-"
        elif "*" in split_from_equality[1]:
            term2 = split_from_equality[1].split("*")[0]
            term3 = split_from_equality[1].split("*")[1]
            operator = "*"
        elif "^" in split_from_equality[1]:
            term2 = split_from_equality[1].split("^")[0]
            term3 = split_from_equality[1].split("^")[1]
            operator = "^"
        terms_list = [term1, term2, term3, operator]
        return terms_list

    def seperate_trees(defs):
        seperate_trees = []
        for i in defs:
            i_list = term(i)
            tree = [i_list[0], i_list[3], i_list[1], i_list[2]]
            seperate_trees.append(tree)
        return  seperate_trees

    def format_trees(lst):
        for elem in lst:
            elem[0] = elem[0][0]
            elem[2] = [elem[2]]
            elem[3] = [elem[3]]
        return lst

    def link_trees(seperate_tree_list):
        def is_function(term): return len(term) == 4
        count = 0
        while count <= len(seperate_tree_list)+26:
            for i in seperate_tree_list:
                if is_function(i[2][0])==False and is_function(i[3][0])==False:
                    for j in seperate_tree_list:
                        if j[2][0][0]==i[0] and i in seperate_tree_list:
                            j[2] = i
                            seperate_tree_list.remove(i)
                        elif j[3][0][0]==i[0] and i in seperate_tree_list:
                            j[3] = i
                            seperate_tree_list.remove(i)
            count += 1
        return seperate_tree_list

    return link_trees(format_trees(seperate_trees(defs)))

