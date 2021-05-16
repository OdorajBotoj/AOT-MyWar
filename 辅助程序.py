# -*- coding:utf-8 -*-
print("Arduino音乐创建辅助程序")
print("----------")
print("输入示例:h 3 500")
print("[低(l)中(m)高(h)音] [音符(1~7)] [延时(ms)]")
print("----------")
try:
    f=open("output.txt", "a", encoding="utf-8")
    while True:
        aDict={"l":"3","m":"4","h":"5"}
        bDict={"1":"C","2":"D","3":"E","4":"F","5":"G","6":"A","7":"B","4+":"FS","1+":"CS","5+":"GS"}
        inp=input("<<<")
        if inp == "st":
            print(">>>"+str(inp))
            oup=str("  st1ms();")
            print(">>>"+oup)
        else:
            inp=inp.split()
            print(">>>"+str(inp))
            oup=str("  play(NOTE_{}{},{});".format(bDict.get(inp[1]),aDict.get(inp[0]),inp[2]))
            print(">>>"+oup)
        f.write(oup+"\n")
except:
    print("###ERROR")
finally:
    f.close()
