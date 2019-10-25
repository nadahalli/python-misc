import hashlib
import math

class SparseMerkle:
    def next_power_of_2(self, sub_tree_root):
        return int(2 ** math.ceil(math.log2(sub_tree_root + 1)))

    def get_height(self, sub_tree_root):
        return int(math.log2(self.next_power_of_2(sub_tree_root)))

    def is_leaf(self, sub_tree_root, global_height):
        return 2 ** (global_height - 1) <= sub_tree_root < 2 ** (global_height)

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

    def present(self, sub_tree_root, global_height, tree):
        min_range = max_range = sub_tree_root
        for i in range(self.get_height(sub_tree_root), global_height):
            min_range = min_range * 2
            max_range = max_range * 2 + 1

        present_list = []
        offset = 2 ** (global_height - 1)
        for x in sorted(tree.keys()):
            if min_range <= x + offset <= max_range:
                present_list.append(x)
        return present_list
        

    def find_root(self, sub_tree_root, global_height, tree, null_proofs):
        present_list = self.present(sub_tree_root, global_height, tree)
        if (len(present_list) > 0):
            if (self.is_leaf(sub_tree_root, global_height)):
                proof = self.get_hash(sub_tree_root)
                return proof, tree
            else:
                left_root, tree = self.find_root(sub_tree_root * 2,
                                                 global_height,
                                                 tree,
                                                 null_proofs)
                right_root, tree = self.find_root(sub_tree_root * 2 + 1,
                                                  global_height,
                                                  tree,
                                                  null_proofs)
                proof = self.get_concat(left_root, right_root)
                for present_item in present_list:
                    tree[present_item].extend([left_root, right_root])
                return proof, tree
        else:
            proof = null_proofs[
                global_height - self.get_height(sub_tree_root) + 1]
            return proof, tree

if __name__ == '__main__':
    print(get_null_proofs(10))
    

                           
        
    
