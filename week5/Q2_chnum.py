#2021041075 이주현
import operator

#전역 변수
st='''내가 그의 이름을 불러주기 전에는 그는 다만 하나의 몸짓에 지나지 않았다.
내가 그의 이름을 불러주었을 떄, 그는 내게로 와 꽃이 되었다.
내가 그의 이름을 불러준 것처럼 나의 이 빛깔과 향기에 알맞는 누가 나의 이름을 불러다오.
그에게로 가서 나도 그의 꽃이 되고 싶다.
우리들은 모두 무엇이 되고 싶다.
나는 너에게 너는 나에게 잊혀지지 않는 하나의 눈짓이 되고 싶다.'''
Dic={}
List=[]

#메인 코드
if __name__ == "__main__" :
    print("원문\n",st);
    
    for i in range(0,len(st)) :
        if 'ㄱ' <= st[i] and st[i]<='힣' :
            if st[i] in Dic:
                Dic[st[i]]+=1
            else:
                Dic[st[i]]=1
            
    List=sorted(Dic.items(),key=operator.itemgetter(1),reverse=True)
        
    print("------------------")
    print("문자\t빈도수")
    print("------------------")
    for i in range(0,len(List)):
        print(List[i][0],'\t',List[i][1])