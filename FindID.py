def solution(x, y):

    # ID at position (x,1) is the sum of all numbers from 1 to x
    val_x = (x * (x + 1)) >> 1
    id = val_x # if y == 1

    if y > 1:

        # ID at position (x,2) is ID(x,0) + x
        id += x
        temp = x

        # if y >= 3, ID(x,y) = ID(x,2) + sum(x+1 to x+n) where
        # n = (y-1) - 2
        for y_in in range(2, y):
            temp += 1
            id += temp

    return str(id)

if __name__ == "__main__":

        #4 | 7
        #3 | 4  8
        #2 | 2  5  9
        #1 | 1  3  6  10
        #  -----------
        #   #1 #2 #3 #4
        print(solution(1, 1))
        print(solution(3, 2))
        print(solution(5, 10))
        print(solution(2, 3))
        print(solution(2, 2))
        print(solution(5, 5))
        print(solution(1, 100000))