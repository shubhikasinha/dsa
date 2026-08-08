class SegmentTree:
    def __init__(self, s):
        self.n = len(s)
        self.tree_max = [0] * (4 * self.n)
        self.tree_pref = [0] * (4 * self.n)
        self.tree_suff = [0] * (4 * self.n)
        self.tree_lc = [''] * (4 * self.n)
        self.tree_rc = [''] * (4 * self.n)
        self.build(s, 0, 0, self.n - 1)

    def merge(self, node, left_node, right_node, l_len, r_len):
        lc_left = self.tree_lc[left_node]
        rc_left = self.tree_rc[left_node]
        lc_right = self.tree_lc[right_node]
        rc_right = self.tree_rc[right_node]

        self.tree_lc[node] = lc_left
        self.tree_rc[node] = rc_right

        # Default prefix and suffix lengths from children
        pref = self.tree_pref[left_node]
        if pref == l_len and rc_left == lc_right:
            pref += self.tree_pref[right_node]
        self.tree_pref[node] = pref

        suff = self.tree_suff[right_node]
        if suff == r_len and rc_left == lc_right:
            suff += self.tree_suff[left_node]
        self.tree_suff[node] = suff

        # Maximum repeating substring length
        max_val = max(self.tree_max[left_node], self.tree_max[right_node])
        if rc_left == lc_right:
            max_val = max(max_val, self.tree_suff[left_node] + self.tree_pref[right_node])
        
        self.tree_max[node] = max_val

    def build(self, s, node, l, r):
        if l == r:
            self.tree_max[node] = 1
            self.tree_pref[node] = 1
            self.tree_suff[node] = 1
            self.tree_lc[node] = s[l]
            self.tree_rc[node] = s[l]
            return

        mid = (l + r) // 2
        left_node = 2 * node + 1
        right_node = 2 * node + 2

        self.build(s, left_node, l, mid)
        self.build(s, right_node, mid + 1, r)
        self.merge(node, left_node, right_node, mid - l + 1, r - mid)

    def update(self, node, l, r, idx, char):
        if l == r:
            self.tree_lc[node] = char
            self.tree_rc[node] = char
            return

        mid = (l + r) // 2
        left_node = 2 * node + 1
        right_node = 2 * node + 2

        if idx <= mid:
            self.update(left_node, l, mid, idx, char)
        else:
            self.update(right_node, mid + 1, r, idx, char)

        self.merge(node, left_node, right_node, mid - l + 1, r - mid)


class Solution(object):
    def longestRepeating(self, s, queryCharacters, queryIndices):
        """
        :type s: str
        :type queryCharacters: str
        :type queryIndices: List[int]
        :rtype: List[int]
        """
        tree = SegmentTree(s)
        ans = []
        n = len(s)

        for char, idx in zip(queryCharacters, queryIndices):
            tree.update(0, 0, n - 1, idx, char)
            ans.append(tree.tree_max[0])

        return ans