class Sol:
    def sum_of_2_integers(self,a,b):
        while a!=0:
            carry=a&b
            b=a^b
            a=carry<<1
        return b

if __name__ == '__main__':
    p1=Sol()
    print(p1.sum_of_2_integers(64,64))
