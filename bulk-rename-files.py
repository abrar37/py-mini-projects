import os

# os.chdir("C:/Users/khawa/Desktop/junks")
# directory = os.listdir("C:/Users/khawa/Desktop/junks")
# i = 1
# for file in directory:
#     print(file)
#     if file.endswith(".jpg"):
#         print(file)
#         os.rename(file, str(i)+".jpg")
#         i += 1

def bulkrename(dir_addr, file_ext):
    # os.chdir(dir_addr)
    directory = os.listdir(dir_addr)
    i = 1
    for file in directory:
        print(file)
        if file.endswith(file_ext):
            print(file)
            os.rename(f"{dir_addr}/{file}",  f"{dir_addr}/{str(i)+file_ext}")
            i += 1
        
bulkrename("C:/Users/khawa/Desktop/junks", ".pdf")