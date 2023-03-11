
for k in range(2,21):
    
    table=''
    for j in range(1,11):
        table +=f"{k} *{j}={k*j}\n"
    with open(f'tables/{k}.txt','w') as f:
        f.write(table)
        
    

            