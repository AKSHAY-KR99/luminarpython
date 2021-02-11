#rotation array
#[1,2,3,4,5,6][6,5,4,3,2,1]

def rotation(lst,rot_list):
    new_list=lst[len(lst)//2:]+lst[:len(lst)//2]
    print(new_list)
    if new_list==rot_list:
        print("it is rotoation of given list")
    else:
        print("it is not rotation of given list")
rotation([1,2,3,4,5,6,7,8],[5,6,7,8,1,2,3,4])