import hashlib
import math

class SparseMerkle:
    def next_power_of_2(self, sub_tree_root):
        return int(2 ** math.ceil(math.log2(sub_tree_root + 1)))

    def get_height(self, sub_tree_root):
        return math.log2(self.next_power_of_2(sub_tree_root))

    def find_common_ancestor(self, x, y):
        if x < 1 or y < 1:
            raise ValueError("Paramters must be greater than Zero")
        if x == y:
            return x
        lower = min(x, y)
        lower_height = self.get_height(lower)
        
        higher = max(x, y)
        higher_height = self.get_height(higher)
        
        while (lower_height != higher_height):
            higher = higher/2
            higher_height = self.get_height(higher)
            
        while(lower != higher):
            lower = int(lower/2)
            higher = int(higher/2)
                
        return lower

    def get_hash(self, x):
        return hashlib.sha256(x.encode('utf-8')).hexdigest()[54:]

    def get_concat(self, x, y):
        return self.get_hash(x + '-' + y)

    def get_null_proofs(self, size):
        null_proofs = {0: self.get_hash('0')}
        for i in range(size):
            null_proofs[i + 1] = self.get_concat(null_proofs[i],
                                                 null_proofs[i])
        return null_proofs

    def attach_null_proofs_till(self, index, sub_tree_root, null_proofs):
        null_proof_index = 0
        non_null_proof = get_hash('1')
        while (index != sub_tree_root):
            if (index % 2 == 0):
                non_null_proof = self.get_concat(non_null_proof,
                                                 null_proofs[null_proof_index])
            else:
                non_null_proof = self.get_concat(null_proofs[null_proof_index],
                                                 non_null_proof)
            null_proof_index += 1
            index = int(index/2)
        return non_null_proof


    def find_root(self, tree, null_proofs):
        keys = sorted(tree.keys())
        
        prev_subtree_root = 1
        for key in keys:
            pass

if __name__ == '__main__':
    print(get_null_proofs(10))
    

                           
        
    
