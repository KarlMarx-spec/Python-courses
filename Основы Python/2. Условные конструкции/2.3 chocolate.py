try:
        N=int(input());
        M=int(input());
        K=int(input());
except: 
        print ("Данные введены некорректно")
else:
        if ((K % N == 0) and (K // N < M)) or ((K % M == 0) and (K // M < N)):
                print("YES");
        else:
                print("NO");
