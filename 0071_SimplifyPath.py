class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        l, l_ = [i for i in path.split('/') if i and i != '.'], []
        for i in l:
            if i != '..':
                l_.append(i)
            elif l_:
                l_.pop()
        return '/' + '/'.join(l_)