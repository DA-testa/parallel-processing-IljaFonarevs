# python3

def parallel_processing(n, m, data):
    output = []
    thread_arr = [0]*n
    for i in range(int(m)):
        min_arr = min(thread_arr)
        index = thread_arr.index(min_arr)
        output.append((index, min_arr))
        thread_arr[index] += data[i]

    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    Linefirst = input().split()
    n = int(Linefirst[0]) 
    m = int(Linefirst[1])
    
    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = list(map(int,input().split(" ")))

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for i,j in result:
        print(i, j)



if __name__ == "__main__":
    main()
