f = open('정보.txt', 'r', encoding='utf8')
line = f.readlines()
f.close()

# 이때 경로 작성을 해야 함 - 경로가 없는 경우 현재 경로의 txt 파일을 불러옴

# 데이터의 줄바꿈 표시를 없애기
result = []
for i in line :
    temp = i.replace('\n', '');
    result.append(temp);

print(result)

# 정보.txt의 결과를 :로 구분하여 구성
total = []
for i in result:
    total.append(i.split(':'))

print(total)

# 리스트 내의 리스트 묶음을 해제
# result3 = []
# for i in total:
#     for j in i:
#         result3.append(j)

flat_list = [item for sublist in total for item in sublist]

print(flat_list)