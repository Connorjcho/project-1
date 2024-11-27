# num = [2, 7, 11, 15] target = 9
# num list에서 정확히 2개의 요소의 합이 타겟이 되는지 검사해서 
# 타겟이 된다면 두개의 요소의 인덱스 값을 출력하고
# 타겟이 안되면 안된다고 출력해주세요
num = [2,7,11,15]
target = 9
for i in range(len(num)):
    # i+1 i+2 i+3
    # i+1 i+2
    # i+1
    for j in range(i+1,len(num)):
        addtion = num[i] + num[j]
        if addtion == target:
            print(str(i) + str(j))
            break
        elif addtion != target:
            continue
