import time

PI =     3.1415926
ROOT_2 = 1.4142135
ROOT_6 = 2.4494897

#a÷bの余り
def rem(a,b):
    div = int(a/b)
    return a-b*div

def sin(a):
    if rem(a,2*PI)<PI:
        a = rem(a, 2 * PI)
        value = a - (a**3)/6 + (a**5)/120
    else:
        a = rem(a,2*PI) -PI
        value = a - (a**3)/6 + (a**5)/120

    return value

def cos(a):
    if rem(a,2*PI)<PI:
        a = rem(a,2*PI)
        value = 1 - (a**2)/2 + (a**4)/24
    else:
        a = rem(a,2*PI)-PI
        value = 1 - (a ** 2) / 2 + (a ** 4) / 24

    return value

def main():
    width = 20
    length = 50
    picture = [[0 for j in range(width)] for i in range(length)]
    R = 20
    r = 5
    alpha = 0.01
    beta = 0.01

    t = 0
    while t < 300:
        #三次元での図形
        proj_x = ((R+r)/2 + ((R-r)/2)*(cos(alpha*t))*cos(beta*t))
        proj_y = ((R+r)/2 + ((R-r)/2)*(cos(alpha*t))*sin(beta*t))
        #z = ((R-r)/2)*sin(alpha*t)

        #二次元に投影する
        #proj_x = -x*ROOT_2/2 + y*ROOT_2/2
        #proj_y = (-x*ROOT_6/6 + -y*ROOT_6/6 + z*ROOT_6/3 +10)/10

        #整数にキャストしてpictureに描画する
        int_x = int(proj_x)
        int_y = int(proj_y)
        if int_x<length and int_y<width:
            if picture[int_x][int_y] == 0:
                picture[int_x][int_y] += 1


        for i in range(len(picture)):
            for j in range(len(picture[i])):
                print(picture[i][j], end="")
            print("")


        t+=1
        time.sleep(0.01)

if __name__ == "__main__":
    main()



