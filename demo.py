import csv #调用数据保存文件
import pandas as pd #用于数据输出


def DF2Excel(data_path, data_list, sheet_name_list):
    '''将多个dataframe 保存到同一个excel 的不同sheet 上
    参数：
    data_path：str
        需要保存的文件地址及文件名
    data_list：list
        需要保存到excel的dataframe
    sheet_name_list：list
        sheet name 每个sheet 的名称
    '''

    write = pd.ExcelWriter(data_path)
    for da, sh_name in zip(data_list, sheet_name_list):
        da.to_excel(write, sheet_name=sh_name, index=False)

    # 必须运行write.save()，不然不能输出到本地
    write._save()


# ---------- 调用函数 ------------------

# 需要保存的文件地址及文件名
data_path = 'test2.xlsx'
# 要保存的每个sheet 名称
sheet_name_list = ['sheet_name_0', 'sheet_name_1', 'sheet_name_2', 'sheet_name_3', 'sheet_name_4']
# dataframe list
list1 = [1, 2]
list2 = [3, 4]
list = []
list.append(["1", "100"])
list.append(list1)
list.append(list2)
print(list)
test1 = pd.DataFrame(list)  #
data_list = [test1, test1, test1, test1, test1]
# 调用函数
DF2Excel(data_path, data_list, sheet_name_list)

# def a():
#     writer = pd.ExcelWriter('test2.xlsx')
   # 多次调整以后发现只能是将不同DataFrame输入到不同sheet，即数据先要转化为DataFrame形式才可以
#     L_list=[0, 2]
#     list3=[5,6]
#     list4=[7,8]
#     L_list.append(list3)
#     L_list.append(list4)
#     test2=pd.DataFrame(L_list)
#     test1.to_excel(writer,sheet_name='one',index=False)#此处index=false是去掉excel表中默认生成的第一列数据
#     test2.to_excel(writer,sheet_name='two',index=False)
#     writer._save()
#     writer.close()