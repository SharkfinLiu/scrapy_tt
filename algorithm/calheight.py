"""

int rank[maxn],height[maxn];
void calheight(int *r,int *sa,int n)
{
int i,j,k=0;
for(i=1;i<=n;i++) rank[sa[i]]=i;
for(i=0;i<n;height[rank[i++]]=k)
for(k?k--:0,j=sa[rank[i]-1];r[i+k]==r[j+k];k++);
return;
}
"""
src_list = ['a', 'a', 'b', 'a', 'a', 'a', 'a', 'b', 'a','','']
sa = [8, 3, 4, 5, 0, 6, 1, 7, 2]
rank = [0,0,0,0,0,0,0,0,0]
height = [0,0,0,0,0,0,0,0,0]


def calheight(r, sa, n):
    k = 0
    for i in range(n):
        rank[sa[i]] = i
    for i in range(n):
        height[rank[i]] = k

        if k:
            k -= 1
        else:
            pass
        j = sa[rank[i] - 1]
        while True:
            if r[i + k] == r[j + k]:
                k += 1
            else:
                break

if __name__ == '__main__':
    calheight(src_list,sa,len(sa))
    print(height)

"""
aaaaba

aaaba

aaba

aabaaaaba

aba

abaaaaba

ba

baaaaba
"""