event=["hs-access","demo-clg"]

questions={
    101 : "Father Education Level", 
    201 : "Mother Education Level",
    301 : "City of Upbringing"
    }
    
options={
    101 : ["10 or Below","12 or Below","Graduate or Below","PG or Below"],
    201 : ["10 or Below","12 or Below","Graduate or Below","PG or Below"],
    301 : ["metro", "Tier 1", "Tier 2"] 
    }

marks={
    101 : [1.6, 2.4, 3.2, 4],
    201 : [1.6, 2.4, 3.2, 4],
    301 : [4, 3.2, 2.4]
}

responses=dict()


def calculate_result():
    total = 0
    for i in responses:
        total += responses[i]
    return total


# questions ; options;  responses; eventname ; date ; makrs ; name ; phone no; email

# def save(eventname):
#     file=open(eventname,)


def main():
    for i in questions:
        # print(type(i))
        print(questions[i])
        for y in range(len(options[i])):
            print("   ",y,":", options[i][y])
        
        response = int(input("enter choice (in int): "))
        responses[i]=marks[i][response]
    print(responses)
    print(calculate_result())


if __name__ == '__main__':
    main()