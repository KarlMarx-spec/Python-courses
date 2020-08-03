try:
        first1 = int(input());
        first2 = int(input());
        second1 = int(input());
        second2 = int(input());
except: 
        print ("Данные введены некорректно");
else:
        if (abs(second1-first1)== abs(second2-first2)):
                print ("YES");
        else: print ("NO");
