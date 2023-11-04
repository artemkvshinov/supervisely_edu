import os
real_name = 0
is_name = 0
num_frame = 59
for y in range(num_frame):
    for i in range(num_frame):
        if os.path.isfile(str(real_name)+'.png') == True and os.path.isfile(str(is_name)+'.png') == True:
            real_name += 1
            is_name += 1
            print('1\t'+str(i))

        if os.path.isfile(str(real_name)+'.png') == True and os.path.isfile(str(is_name)+'.png') == False:
            os.rename(str(real_name)+".png",str(is_name)+".png")
            real_name = is_name
            print('2\t'+str(i))
        

        elif os.path.isfile(str(real_name)+'.png') == False :
            real_name += 1
            print('3\t'+str(i))


        