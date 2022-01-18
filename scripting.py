result=""
#with open("/home/sigmoid/ASSIGNMENTS/task2/sig.conf","r") as f:
    #lines = f.readlines()

#COMPONENT
component=["INGESTOR","JOINER","WRANGLER","VALIDATOR"]
counter=1
for i in component:

    print(str(counter)+" "+ i)
    counter+=1
print("select component")
comp_value= int(input("Please select value 1 to 4: "))
print(str(component[comp_value-1])+" selected")
comp_input=component[comp_value-1]

#SCALE
scale=["MID","HIGH","LOW"]
counter=1
for i in scale:

    print(str(counter)+" "+ i)
    counter+=1
print("select scale")
scale_value= int(input("Please select value 1 to 3: "))
print(str(scale[scale_value-1])+" selected")
scale_input=scale[scale_value-1]

#VIEW
view=["AUCTION","BID"]
counter=1
for i in view:

    print(str(counter)+" "+ i)
    counter+=1
print("select view")
view_value= int(input("Please select value 1 to 2: "))
print(str(view[view_value-1])+" selected")
view_input=view[view_value-1]
if view[view_value-1]=="Auction":
    view_input="vdopiasample"
else:
    view_input="vdopiasample-bid"

#COUNT
count=range(1,10)
counter=1
for i in range(1,10):
    print(i)
    counter+=1
print("select count")
count_value= int(input("Please select value 1 to 9: "))
print(str(count[count_value-1])+" selected")

#result=str(view_input)+";"+scale_input+";"+comp_input+";ETL;vdopia-etl="+str(count_value)

#print(result)

with open("/home/sigmoid/ASSIGNMENTS/task2/sig.conf","r") as f:
    lines = f.readlines()
flag=False
for line in lines:
    data=line.split(";")
    if data[2]==comp_input:
        if data[0]==view_input:
            data[1]=scale_input
            data[4]="vdopia-etl="+str(count_value)+"\n"
            flag=True
        #else:
    #else:
    newline=""          #updated line 
    counter=1
    for item in data:
        if counter==5:
            newline=newline+item
        else:
            newline=newline+item+";"
        counter+=1

    result=result+newline
#print(result)
if flag==False:
    print("entered value does not match in sig.conf")
else:
    print("sig.conf updated")


with open("/home/sigmoid/ASSIGNMENTS/task2/sig.conf","w") as f:
    lines = f.writelines(result)
