#str.join[list]
#stack use reculsive function or deque and list
#enumerate
#using deque, -> without inverse
#end of print, end =''! is essential
#f"{}" format is not capitable with this version 
#!!format!!
def main():
    length = int(8)
    datas = "12421421"

    inv_result = []
    for index in range(length):
        if index % 3 == 0:
            inv_result.append(',')
            inv_result.append(str(datas[index]))
        else:
            inv_result.append(str(datas[index]))

    result = inv_result[::-1]

    #first comma delete

    result.pop()

    a = ''.join(result)
    b = format(int(datas),",")
    print(a)
    print(b)
    print(a == b)


if __name__ == "__main__":
    main()