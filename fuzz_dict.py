import pypinyin
import random
#百家姓名后两位
b=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
def pinyin():
    file=open("config.inc.txt","r")
    dicts=[]
    for x in file:
        for i in pypinyin.pinyin(x.replace("\n",""),style=pypinyin.NORMAL):

            dicts=str(i).replace("[","").replace(']',"").replace("'","").replace("'","").replace("\n","")
            
            with open("pinyin.txt","a+") as f:
                f.write(dicts+"\n")
                f.close
#生成姓名拼音拼音后两位是简称 百家姓默认有567 
def word():
    file1=open("pinyin.txt","r")
    file_list=[]
    for xx in file1:
        file_list.append(xx.replace("\n",""))       
    for x in range(0,567):
        row_list=[]
        lists=random.sample(b,2)
        row=str(lists).replace("]","").replace("[","").replace(",","").replace("'","").replace("'","").replace(" ","")
        #print(row)
        for bb in file_list:
            cc=bb+row
            with open("success.txt","a+") as f:
                f.write(cc+"\n")
                f.close
    print("succ")
if __name__ == "__main__":
    #print(pinyin())
    word()
    