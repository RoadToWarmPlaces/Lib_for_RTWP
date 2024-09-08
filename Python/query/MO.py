class Mo:
    """\
    Mo's algorithm
    """ 
    #qryの数だけ与えて構築をしてもらう
    @classmethod
    def build(cls, q, lclose = True, rclose = True, index = 1):
        """全閉区間[l:r]かつ1-index想定"""
        qry = []
        for i in range(q):
            l,r = map(int, input().split())
            #0-indexに
            l -= index
            r -= index
            #半開区間[l:r)に
            l -= lclose^1
            r += rclose
            qry.append((l,r,i))
        
        obj = Mo(qry)
        return obj
                
    def __init__(self, qry):
        self.q = len(qry)
        self.ans = [0]*self.q
        
        #もしqryのindexが無いとき
        if len(qry[0]) < 3:
            self.qry = [(qry[0],qry[1],i) for i in range(self.q)]
        else:
            self.qry = qry 
        
        #平方分割 (なさそうだけど範囲が負の想定もしている)
        minl = min(l for l,r,i in qry)
        maxl = max(l for l,r,i in qry)
        n = maxl - minl
        size = n//isqrt(self.q) + 1
        
        self.qry.sort(key = lambda x : (x[0]//size, x[1]*((x[0]//size)%2*2-1)))
    
    #差分に対して作用させたい関数を渡す
    def answer(self, add_x, del_x):
        nl,nr = 0,0
        tmp = 0
        for l,r,idx in self.qry:
            while nl > l:
                nl -= 1
                tmp = add_x(nl,tmp)
            while nl < l:
                tmp = del_x(nl,tmp)
                nl += 1
            while nr > r:
                nr -= 1
                tmp = del_x(nr,tmp)
            while nr < r:
                tmp = add_x(nr,tmp)
                nr += 1
            self.ans[idx] = tmp
            
        return self.ans