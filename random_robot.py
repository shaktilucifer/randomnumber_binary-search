import random
def randomgenerate():
    a=random.randint(1,100)
    return a;

def robot(seed,numonmind):
    print numonmind,"hello"
    while True:
        usernumber=seed
                #print usernumber
        if numonmind == usernumber:
            print("you have guessed it right!")
            return numonmind
            break
        else:
            if usernumber > numonmind:
                print("try a little bit lower - too low")
                return 2
            else:
                print("try a little bit higher - too high")
                return 1

randnum=numonmind=randomgenerate()
mid=50
end=100;s=1;
b=robot(mid,randnum)
while True:
    if(b==2):
        end=mid
        mid=(s+end)/2
        b=robot(mid,randnum)
    else:
        if(b==1):
            s=mid
            mid=(s+end)/2
            b=robot(mid,randnum)
        else:
            print "success",b
            break

    
