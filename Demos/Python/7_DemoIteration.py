# # for loop
# # Example 1
# fruits = ["Apple", "Banan", "Mango"];
# # for fruit in fruits:
# #     print(fruit);
# for index,fruit in enumerate(fruits):
#     print(f"{index}: {fruit}")
# print(fruits[2]);


#example 2
# total = 0

# for num in range(1,6):
#     total += num
# print(f"Sum :{total}")


# while loop
# count = 10;
# while count <= 5:
#     print(count);
#     count +=1;
# print();
# print(count);

#break statement
# total = 0;
# for num in range (1,11):
#     total += num;
#     if total >= 15:
#         print(f"num: {num}")
#         break;
# print (f"Total: {total}");

#continue statement

# for num in range(1,6):
#     if num == 3:
#         continue;
#     print(num);


#pass statement
for num in range(1,6):
    if (num == 3):
        print("hi");
        pass;
    print(num);