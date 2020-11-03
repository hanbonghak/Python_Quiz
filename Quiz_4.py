import copy
import time
H = int(input())
int_triangle = []
for i in range(H):
    input_ = input()
    line = list(map(int, input_.split(' ')))
    assert len(line) == i + 1
    int_triangle.append(line)

print(int_triangle)

def update_triangle(int_triangle, level) :
    for i in range(level) :
        int_triangle[level-1][i] += max(int_triangle[level][i],int_triangle[level][i+1])
    return int_triangle

def main(H, int_triangle) :
    triangle = copy.deepcopy(int_triangle)
    for i in range(H-1,0,-1) :
        update_triangle(triangle,i)
        if i == 0:
            break
        else :
            del(triangle[i])
    return triangle

if __name__ == '__main__' :
    s = time.time()
    result = main(H, int_triangle)
    e = time.time()
    print("수행 시간: {0:3.6f}초".format(e-s))
    print("결과 값: {}".format(result[0][0]))
