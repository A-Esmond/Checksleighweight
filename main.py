def check_sleigh_weight():
    weight_limit = float(input("Enter the weight limit of the sleigh: "))
    gift_amount = int(input("Enter the amount of gifts: "))
    total_weight = 0
    for i in range(gift_amount):
        total_weight += float(input(f"Enter the weight of gift {i+1}: "))


    if total_weight < weight_limit:
      print('Sleigh is under the weight limit')
    elif total_weight > weight_limit:
      print('Sleigh is over the weight limit')
    else:
      print('Sleigh is at the weight limit')



check_sleigh_weight()