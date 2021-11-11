from numpy import  *

'''
The implement of Forward Algorithm
'''

class HMM:
    def __init__(self):
        self.A = array([(0.5, 0.2, 0.3), (0.3, 0.5, 0.2), (0.2, 0.3, 0.5)]) #盒子1 盒子2 盒子3
        self.B = array([(0.5, 0.5), (0.4, 0.6), (0.7, 0.3)])
        self.pi = array([(0.2),(0.4),(0.4)])
        self.o = [0, 1, 0] #小球 红-白-红
        self.t = len(self.o) #观测序列长度
        self.m = len(self.A) #状态集合个数
        self.n = len(self.B[0])

    def forward(self):
        # 矩阵大小由行数为观测序列，列数为状态个数
        self.x = array(zeros((self.t, self.m)))
        for i in range(self.m):
            self.x[0][i] = self.pi[i] * self.B[i][0]

        for j in range(1, self.t):
            for i in range(self.m):
                temp = 0
                for k in range(self.m):
                    #self.A[k][i] = (0->0),(1->0),(2->0)
                    temp = temp + self.A[k][i] * self.x[j-1][k] * self.B[i][self.o[j]]
                self.x[j][i] = temp

        result = 0
        for i in range(self.m):
            result += self.x[self.t-1][i]

        print(u"前向概率矩阵及当前观测序列概率如下：")
        print(self.x)
        print(result)

    def backward(self):
        #t时刻状态为qi, 从t+1到T观测为ot+1,ot+2,oT的概率用矩阵y表示
        #则矩阵大小的行数为观测序列书，列数为状态个数
        self.y = array(zeros((self.t, self.m)))
        for i in range(self.m):
            self.y[self.t-1][i] = 1
        j = self.t-2
        while(j >= 0):
            for i in range(self.m):
                for k in range(self.m):
                    self.y[j][i] += self.y[j+1][k] * self.A[i][k] * self.B[k][self.o[j+1]]
            j = j-1
        result = 0
        for i in range(self.m):
            result += self.pi[i] * self.B[i][self.o[0]]*self.y[0][i]
        print(u'后向矩阵以及当前观测序列概率如下')
        print(self.y)
        print(result)



if __name__  == '__main__':
    test = HMM()
    test.forward()
    test.backward()

