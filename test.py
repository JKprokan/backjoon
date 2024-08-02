#3. 임의의 길이의 단어들을 인자로 받아 딕셔너리에 알파벳에 따라 
# 저장하는 함수를 작성하려고 한다.
#  이 함수는 sort_dic() 이다. 즉, A 로 시작하는 단어들은
#  A 딕셔너리 아래에,
# B 로 시작되는 단어들을 B 라는 key 값 아래 저장할 것이다. 
# 예를 들어, 'ate' 이라는 단어를 받았다하자.
# 여기서 첫 알파벳은 'a' 이니, 딕셔너리에 {'A': ['ate']} 
# 이렇게 저장할 수 있을 것이다. 
# 각 딕셔너리는 초기에 비어있는 리스트[]를 갖고, 첫 알파벳에 따라 
# 순차적으로 리스트에 더해진다. 
# 예를 들어, sort_dic('ate', 'apple', 'bad', 'dad') 를 입력하면, 
# 딕셔너리 {'A':['ate', 'apple'], 'B': ['bad], 'D': ['dad']} 를 반환한다. 
# 이 함수의 인자는 길이가 정해져있지 않음을 유의하자. 
# key 가 되는 알파벳은 대문자로 한다.
#다음의 단어들을 넣어서, 아래와 같이 출력되는지 확인하라. --> 
# 'apple', 'test', 'bird', 'car', 'change', 'time', 'arange'
# apple arange bird car change test time
def sort_dic(*word):
    word = list(word) #word 리스트화
    word.sort() #word를 알파벳순으로
    dic = {} 
    alpha = [] #맨앞 알파벳들의 리스트

    for i in range(0,len(word)):
        a = []
        alpha.append(word[i][0]) #맨앞 앞파벳들의 리스트
        a.append(word[i]) #a리스트에 word의 리스트에 있는 순서대로 1개를 넣는다
        A = word[i][0].upper()

        if alpha.count(word[i][0]) == 1: #만약 앞글자가 혼자 딱 1개 있으면 그걸 dic에 넣는다
            dic[A] = a

        for j in range(i+1,len(word)):
            if word[i][0] == word[j][0]: #앞글자가 같은게 있으면 같은 리스트로 a에 넣는다
                
                a.append(word[j])
                dic[A] = a
    
    s = str(dic)
    for z in range(len(s)+1):
        if s[z] == "]":
            s = s[:z+1] + "\n" + s[z+2:]
    
    print(s)
sort_dic('apple', 'test', 'bird', 'car', 'change', 'time', 'arange')