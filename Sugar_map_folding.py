# coding: utf-8

import itertools
import subprocess # コマンド実行用
import random


# 制約条件 2 newsによる局所的な重なり順
# 重なり順生成
def stacking_order(news_list):
    
    M = len(news_list) + 1
    N = len(news_list[0]) + 1
    layer = [] # layer[[a,b,c,d]] a->b->c->d
    flag12 = 0 # (上->下)  if 2->1:flag12=0   elif 1->2:flag12=1
    flag24 = 2 # (上->下)  if 2->4:flag24=0   elif 4->2:flag12=1 initial:2

    for i in range(M-1):
        for j in range(N-1):

            if j == 0: # 最初の列のとき

                if i != 0: # 最初の行でないとき前のflag24からflag12を設定
                    if news_list[i][j] == "n":
                        flag12 = flag24
                    elif news_list[i][j] == "s":
                        flag12 = 1 - flag24
                    elif news_list[i][j] == "w":
                        flag12 = flag24
                    elif news_list[i][j] == "e":
                        flag12 = 1 - flag24                 

                # flag12からflag24を設定
                if news_list[i][j] == "n":
                    flag24 = flag12
                elif news_list[i][j] == "s":
                    flag24 = 1 - flag12
                elif news_list[i][j] == "w":
                    flag24 = 1 - flag12
                elif news_list[i][j] == "e":
                    flag24 = flag12              


            # flag12から層を決定  
            if flag12 == 0:
                if news_list[i][j] == "n":
                    layer.append([M*j+i+2,M*j+i+1,M*(j+1)+i+1,M*(j+1)+i+2])
                    flag12 = 1 - flag12
                elif news_list[i][j] == "s":
                    layer.append([M*(j+1)+i+1,M*(j+1)+i+2,M*j+i+2,M*j+i+1])
                    flag12 = 1 - flag12
                elif news_list[i][j] == "w":
                    layer.append([M*(j+1)+i+2,M*j+i+2,M*j+i+1,M*(j+1)+i+1])
                elif news_list[i][j] == "e":
                    layer.append([M*j+i+2,M*(j+1)+i+2,M*(j+1)+i+1,M*j+i+1])
            else:
                if news_list[i][j] == "n":
                    layer.append([M*(j+1)+i+2,M*(j+1)+i+1,M*j+i+1,M*j+i+2])
                    flag12 = 1 - flag12
                elif news_list[i][j] == "s":
                    layer.append([M*j+i+1,M*j+i+2,M*(j+1)+i+2,M*(j+1)+i+1])
                    flag12 = 1 - flag12
                elif news_list[i][j] == "w":
                    layer.append([M*(j+1)+i+1,M*j+i+1,M*j+i+2,M*(j+1)+i+2])
                elif news_list[i][j] == "e":
                    layer.append([M*j+i+1,M*(j+1)+i+1,M*(j+1)+i+2,M*j+i+2])
              
    return layer

# 引数 1 : 重なり順リスト stack_list
# 引数 2 : ファイルオブジェクト f_obj
# 出力   : CNF条件
# 戻り値 : なし
def stacking_order_cnf(stack_list, f_obj):
    
    # "map_folding.csp"を追記モードでオープンしている
    
    for k in range( len(stack_list) ):
        
        a = stack_list[k][0]
        b = stack_list[k][1]
        c = stack_list[k][2]
        d = stack_list[k][3]
        print("; 制約条件 2.%d " %(k+1), stack_list[k], "の重なり順", file=f_obj)
        
        
        # 地図番号 aが 地図番号 bより上にある
        print("(< m_",a," m_", b, ")", sep="", file=f_obj)
        # 地図番号 bが 地図番号 cより上にある
        print("(< m_",b," m_", c, ")", sep="", file=f_obj)
        # 地図番号 cが 地図番号 dより上にある
        print("(< m_",c," m_", d, ")", sep="", file=f_obj)

        

# 制約条件 3,4,5,6  領域での交差  

# 引数 1 : 領域に格納されている折り線リスト c_list
# 引数 2 : 制約条件の数字
# 引数 3 : ファイルオブジェクト f_obj
# 出力   : 交差しない条件
# 戻り値 : なし
def intersction(crease_list, const_num, f_obj):
    
    # "map_folding.csp"を追記モードでオープンしている    

    for element in itertools.combinations(crease_list,2):

        # (a,b)と(c,d)が交差しない条件(節)
        a = element[0][0]
        b = element[0][1]
        c = element[1][0]
        d = element[1][1]
        print("; 制約条件 %d (%d,%d)と(%d,%d)が交差しない条件" %(const_num,a, b, c, d), file=f_obj)
        
        # [ min(a,b) < c < max(a,b) ] <=> [ min(a,b) < d < max(a,b) ]
        print("(iff ", end="", file=f_obj)
        print("(and (< (min m_%d m_%d) m_%d ) (< m_%d (max m_%d m_%d))) " %(a,b,c,c,a,b), end="", file=f_obj)
        print("(and (< (min m_%d m_%d) m_%d ) (< m_%d (max m_%d m_%d)))"  %(a,b,d,d,a,b), end="", file=f_obj)
        print(")", file=f_obj)
        
        
        
# 地図折り問題からCSPファイルを作成
def map_to_csp(news_list):
    
    M = len(news_list) + 1
    N = len(news_list[0]) + 1
    cell_num = M * N
    numbers = range( 1, cell_num+1 )


    # 変数の宣言
    f_obj = open("map_folding.csp", 'w')# 書き込みモードで初期化
    print("; %d × %d 地図折り問題 " %(M,N), news_list, file=f_obj)
    f_obj.close()


    f_obj = open("map_folding.csp", 'a') # 追記モードでオープン
    print("; 変数の宣言", file=f_obj)

    for i in numbers:
        print("(int m_",i," 1 ", cell_num, ")", sep="", file=f_obj)


    # 制約条件 1 セル番号と層が1対1で対応する  
    # (alldifferent m_1 m_2 m_3 m_4 m_5 m_6 )

    print("; 制約条件 1", file=f_obj)
    print("(alldifferent ", sep="", end="", file=f_obj)
    for i in numbers:
        print("m_",i," ", sep="", end="", file=f_obj)
    print(")", file=f_obj)


    # 制約条件 2 newsによる重なり順

    stack_list = stacking_order(news_list) # 重なり順の生成
    stacking_order_cnf(stack_list, f_obj) # CNFの作成


    # 制約条件 3 A領域での交差

    # A領域に格納されている折り線リストの作成
    domainA_list = []

    if M % 2 == 0: # Mが偶数のとき
        i = 1
        while i < cell_num:
            domainA_list.append([i,i+1])
            i = i + 2
    else: # Mが奇数のとき
        i = 1
        while i < cell_num:
            if i % M != 0: # セル番号iが端でないなら
                domainA_list.append([i,i+1])
                i = i + 2
            else: # セル番号iが端
                i = i + 1


    # "map_folding.csp"を追記モードでオープンしている
    intersction(domainA_list, 3, f_obj) # CNFの作成


    # 制約条件 4 B領域での交差

    # B領域に格納されている折り線リストの作成
    domainB_list = []

    i = 1
    while i <= cell_num-M:
        domainB_list.append([i,i+M])
        if i % M != 0: # セル番号iが端でないなら
            i = i + 1
        else: # セル番号iが端
            i = i + M + 1

    # "map_folding.csp"を追記モードでオープンしている
    intersction(domainB_list, 4, f_obj) # CNFの作成


    # 制約条件 5 C領域での交差

    # C領域に格納されている折り線リストの作成
    domainC_list = []

    if M % 2 == 0: # Mが偶数のとき
        i = 2
        while i < cell_num:
            if i % M != 0: # セル番号iが端でないなら
                domainC_list.append([i,i+1])
                i = i + 2
            else: # セル番号iが端
                i = i + 2
    else: # Mが奇数のとき
        i = 2
        while i < cell_num:
            domainC_list.append([i,i+1])
            if (i+1) % M != 0: # セル番号i+1が端でないなら
                i = i + 2
            else: # セル番号i+1が端
                i = i + 3

    # "map_folding.csp"を追記モードでオープンしている
    intersction(domainC_list, 5, f_obj) # CNFの作成



    # 制約条件 6 D領域での交差

    # D領域に格納されている折り線リストの作成
    domainD_list = []

    i = M + 1
    while i <= cell_num-M:
        domainD_list.append([i,i+M])
        if i % M != 0: # セル番号iが端でないなら
            i = i + 1
        else: # セル番号iが端
            i = i + M + 1

    # "map_folding.csp"を追記モードでオープンしている
    intersction(domainD_list, 6, f_obj) # CNFの作成


    # # テスト制約条件 （コメントアウト）
    # ; テスト制約  
    # (not (and (= m_1 6) (= m_2 1) (= m_3 3) (= m_4 2) (= m_5 4) (= m_6 5)))


    # 禁止する解をprohibit_whereに追加

    # "map_folding.csp"を追記モードでオープンしている
    print("; テスト制約", file=f_obj)
    prohibit_where = []
    prohibit_where.append([6, 1, 3, 2, 4, 5])

    for i in range(len(prohibit_where)):
        # print("(not ", end="", file=f_obj)
        # print("(and", end="", file=f_obj)
        for j in range(len(prohibit_where[i])):
            pass
            # print(" (= m_", j+1," ", prohibit_where[i][j],")", sep="", end="", file=f_obj)
        # print(")", end="", file=f_obj)
        # print(")", file=f_obj)

    print("; END", file=f_obj)
    f_obj.close()

    print("%d × %d 地図折り問題 " %(M,N), news_list)
    

# バイトコードを文字列に変換
def conv_hbase_str(bytecode):
    return eval("{}".format(bytecode)).decode()    
    
    
# Sugarの実行
# 引数   : news_list
# 戻り値 : [error], [unfoldable], foldable 解のリスト
def fold_check(news_list):
    
    map_to_csp(news_list) # cspファイルの作成
    
    # コマンド入力
    try:
        byteOut = subprocess.check_output('sugar map_folding.csp', shell=True)
        output = conv_hbase_str(byteOut)
    except:
        print ("Error.")
        return ['Error']
    
    if output.split()[1] == 'SATISFIABLE':
        print(output)
        return output.split()[4::3]
    else:
        print(output)
        return ['unfoldable']



def random_news_list(M, N):
    
    news_element = ["n", "e", "w", "s"]
    es_element = ["e","s"]
    nw_element = ["n","w"]

    news_list =  []

    # 1行目のnewsをランダムに決定
    news_list.append(random.choices(news_element, k=N-1))

    # 2行目以降のnewsを決定
    for i in range(1, M-1):

        # add_listを"0"で初期化
        add_list = ["0" for k in range(N-1)]

        # 1列目の値をnews_elementから, ランダムに決定
        add_list[0] = random.choices(news_element, k=1)[0]

        # 2列目以降の値を決定
        for j in range(1,N-1):
            # flagの計算 
            # True: same-> "e","s"  
            # False: different-> "n","w"
            if news_list[i-1][j-1] == "n" or news_list[i-1][j-1] == "w":
                flag = True
            else:
                flag = False

            if add_list[j-1] == "n" or add_list[j-1] == "e":
                flag = not(flag)

            if news_list[i-1][j] == "w" or news_list[i-1][j] == "s":
                flag = not(flag)

            # flagからnewsの決定
            if flag:
                add_list[j] = random.choice(es_element)[0]
            else:
                add_list[j] = random.choices(nw_element)[0]

        #news_listに追加
        news_list.append(add_list[:])


    return(news_list[:])


def main():
    M = 2
    N = 5

    news_list = random_news_list(M, N)
    # news_list = [['n', 'e', 'w', 'n']]
    fold_check(news_list)
    
if __name__ == '__main__':
    main()
