pass  # 输出60行时候数据出问题
# with open("ip.txt", "w+", encoding="utf8") as f:
#     for i in range(1, 61):
#         f.write(f"这是第{i}行数据\n")
#     f.seek(0)
#     content = f.readlines()
#     print(content)
#     f.seek(0)
#     for n in range(0, len(content)):
#         content[n] = content[n].strip()
#         if (n + 1) % 20 == 0:
#             content[n] = "哈哈哈哈"
#     print(content)
#     for k in content:
#         f.write(k+"\n")

# with open("ip.txt", "w+", encoding="utf8") as f:
#     for i in range(1, 61):
#         f.write(f"这是第{i}行数据\n")
#     f.seek(0)
#     content = f.readlines()
#     # print(content)
#     f.seek(0)
#     for n in range(0, len(content)):
#         # content[n] = content[n].strip()
#         if (n + 1) % 20 == 0:
#             content[n] = "哈哈哈哈\n"
#     print(content)
#     f.writelines(content)

