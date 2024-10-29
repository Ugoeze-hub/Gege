IT_Company_1 = [5, 9, 16, 21, 27]
IT_Company_2 = [25, 45, 66, 97, 134]
    
    
E_IT_Company_1 = sum(IT_Company_1) / len(IT_Company_1)
E_IT_Company_2 = sum(IT_Company_2) / len(IT_Company_2)

add = 0
for i in range(len(IT_Company_1)):
    add += (IT_Company_1[i] * IT_Company_2[i])
add /= len(IT_Company_1)

Co_Var = add - (E_IT_Company_1 * E_IT_Company_2)
print(Co_Var)
        

