def main():

    file= open('num_list.txt','w')
for num in range(1,101):
        file.write(str(num))
        file.close()

main()
