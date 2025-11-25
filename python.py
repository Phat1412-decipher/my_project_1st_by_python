import random
mode=input("nhập chế độ ngôn ngữ Vi hoặc En : ").lower()
sum =0
s=0 
Eng =[{"word":"scooter","mean":"xe tay ga"},
      {"word":"bicycle","mean":"xe đạp"},
      {"word":"car","mean":"xe hơi"},
      {"word":"yard","mean":"sân"},
      {"word":"animation","mean":"hoạt hình"},
      {"word":"movie","mean":"phim"},
      {"word":"game","mean":"trò chơi"},
      {"word":"computer","mean":"máy tính"},
      {"word":"century","mean":"thế kỷ"},
      {"word":"history","mean":"lịch sử"}]
Vi=[{"word":"xe tay ga","mean":"scooter"},
    {"word":"xe đạp","mean":"bicycle"},
    {"word":"xe hơi","mean":"car"},
    {"word":"sân","mean":"yard"},
    {"word":"hoạt hình","mean":"animation"},
    {"word":"phim","mean":"movie"},
    {"word":"trò chơi","mean":"game"},
    {"word":"máy tính","mean":"computer"},
    {"word":"thế kỷ","mean":"century"},
    {"word":"lịch sử","mean":"history"}]
if (mode == "vi"):
    per=True
    while (per): 
        
        print(f"câu {s+1}: chữ {Eng[s]["word"]} dịch sang tiếng Việt là gì?")
        # tạo vị trí cho đáp án đúng từ việc cho random từ 1 đến 3 với 1 đến 3 ứng với A B C
        posi=random.randint(1,3)
        ''' 
        tạo 1 list mới ko chứa giá trị của posi  và trong khoảng từ 0 đến 9 để xóa vị trí
        của đáp án đúng trong list Eng và vị trí xuất hiện của đáp án đúng trong 3 vị trí A B C  
        '''
        
        list_posi=list (filter(lambda x:x!=posi and x!=s , range(0,10)))

        for i in range(1,4):
                
            
                
           

            if i==1:
                if posi==1:
                    print ("A. ",Eng[s]["mean"])
                else:
                    # tạo biến a có giá trị random từ list_posi để lấy đáp án sai 
                    a =random.choice(list_posi)
                    print ("A. ",Eng[a]["mean"])
                    list_posi.remove(a)
            if i==2:
                if posi==2:
                    print ("B. ",Eng[s]["mean"])
                else:
                    b=random.choice(list_posi)
                    print ("B. ",Eng[b]["mean"])
                    list_posi.remove(b)
                        
            if i==3:
                if posi==3:
                    print ("C. ",Eng[s]["mean"])
                else:
                    
                    c = random.choice(list_posi)
                    print("C. ", Eng[c]["mean"])
                    list_posi.remove(c)

                         
        ans=input("nhập đáp án của bạn ... ").lower()
        per_ans=0
        if ans=="a":
            per_ans=1
        if ans=="b":
            per_ans=2
        if ans=="c":
            per_ans=3    
        if per_ans==posi:
            print("cũng tạm tạm thôi ")
            s=s+1
            sum=sum + 1
        else:
            print("ôi bạn ơi, mất lượt rồi bạn ơi ")
            s+=1    
        if s+1==11:
            per =False
    print(f"bạn đã hoàn thành bài kiểm tra với {sum} điểm")
if (mode == "en"):
    per=True
    while (per): 
        
        print(f"câu {s+1}: chữ {Vi[s]["word"]} dịch sang tiếng Anh là gì?")
        # tạo vị trí cho đáp án đúng từ việc cho random từ 1 đến 3 với 1 đến 3 ứng với A B C
        posi=random.randint(1,3)
        ''' 
        tạo 1 list mới ko chứa giá trị của posi  và trong khoảng từ 0 đến 9 để xóa vị trí
        của đáp án đúng trong list Eng và vị trí xuất hiện của đáp án đúng trong 3 vị trí A B C  
        '''
        
        list_posi=list (filter(lambda x:x!=posi and x!=s , range(0,10)))

        for i in range(1,4):
                
            
                
           

            if i==1:
                if posi==1:
                    print ("A. ",Vi[s]["mean"])
                else:
                    # tạo biến a có giá trị random từ list_posi
                    a =random.choice(list_posi)
                    print ("A. ",Vi[a]["mean"])
                    list_posi.remove(a)
            if i==2:
                if posi==2:
                    print ("B. ",Vi[s]["mean"])
                else:
                    b=random.choice(list_posi)
                    print ("B. ",Vi[b]["mean"])
                    list_posi.remove(b)
                        
            if i==3:
                if posi==3:
                    print ("C. ",Vi[s]["mean"])
                else:
                    
                    c = random.choice(list_posi)
                    print("C. ", Vi[c]["mean"])
                    list_posi.remove(c)

                         
        ans=input("nhập đáp án của bạn ... ").lower()
        per_ans=0
        if ans=="a":
            per_ans=1
        if ans=="b":
            per_ans=2
        if ans=="c":
            per_ans=3      
        if per_ans==posi:
            print("cũng tạm tạm thôi ")
            s=s+1
            sum=sum + 1
        else:
            print("ôi bạn ơi, mất lượt rồi bạn ơi ")
            s+=1    
        if s+1==11:
            per =False
    print(f"bạn đã hoàn thành bài kiểm tra với {sum} điểm")
