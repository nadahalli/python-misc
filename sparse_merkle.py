import hashlib
import math

class SparseMerkle:
    def __init__(self, global_height, get_hash = None):
        self.global_height = global_height
        if get_hash:
            self.get_hash = get_hash
        self.null_proofs = self.get_null_proofs(global_height)
        self.tree = {}


    def add_elem(self, x):
        self.tree[x] = []


    def add_elems(self, many):
        for x in many:
            self.add_elem(x)


    def remove_elem(self, x):
        del self.tree[x]
        

    def remove_all(self):
        for key in list(self.tree.keys()):
            del self.tree[key]
            
        
    def get_tree(self):
        return self.tree

    
    def next_power_of_2(self, sub_tree_root):
        return int(2 ** math.ceil(math.log2(sub_tree_root + 1)))
    

    def get_height(self, sub_tree_root):
        return int(math.log2(self.next_power_of_2(sub_tree_root)))
    

    def is_leaf(self, sub_tree_root):
        return 2 ** (self.global_height - 1) <= sub_tree_root < 2 ** (self.global_height)
    

    def get_hash(self, x):
        return hashlib.sha256(x.encode('utf-8')).hexdigest()[54:]
    

    def get_concat(self, x, y):
        return self.get_hash(x + '-' + y)
    

    def get_null_proofs(self, size):
        null_proofs = {1: self.get_hash('0')}
        for i in range(1, size):
            null_proofs[i + 1] = self.get_concat(null_proofs[i],
                                                 null_proofs[i])
        return null_proofs
    

    def present(self, sub_tree_root):
        min_range = max_range = sub_tree_root
        for i in range(self.get_height(sub_tree_root), self.global_height):
            min_range = min_range * 2
            max_range = max_range * 2 + 1

        present_list = []
        offset = 2 ** (self.global_height - 1)
        for x in sorted(self.tree.keys()):
            if min_range <= x + offset <= max_range:
                present_list.append(x)
        return present_list
        

    def find_root_internal(self, sub_tree_root):
        present_list = self.present(sub_tree_root)
        if (len(present_list) > 0):
            if (self.is_leaf(sub_tree_root)):
                root = self.get_hash(sub_tree_root)
                self.tree[present_list[0]].append(root)
                if (sub_tree_root % 2 == 0):
                    self.tree[present_list[0]].insert(0, '(')
                else:
                    self.tree[present_list[0]].append(')')
                return root, present_list
            else:
                left_root, left_list = self.find_root_internal(sub_tree_root * 2)
                right_root, right_list = self.find_root_internal(sub_tree_root * 2 + 1)

                root = self.get_concat(left_root, right_root)
                for present_item in present_list:
                    if present_item in left_list:
                        self.tree[present_item].append(right_root)
                        self.tree[present_item].append(')')
                    elif present_item in right_list:
                        self.tree[present_item].insert(0, left_root)
                        self.tree[present_item].insert(0, '(')
                    else:
                        assert(False)
                return root, present_list
        else:
            return self.null_proofs[
                self.global_height - self.get_height(sub_tree_root) + 1], present_list


    def find_root(self):
        for key in self.tree.keys():
            self.tree[key].clear()

        return self.find_root_internal(1)[0]


    def get_inclusion_proof(self, ):
        pass


if __name__ == '__main__':
    pass
    

                           
        
    
