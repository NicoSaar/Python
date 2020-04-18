print("Today's date?")
today = input()

print("Breakfast calories?")
bf_calories = int(input())

print("Lunch calories?")
lunch_calories = int(input())

print("Dinner calories?")
dinner_calories = int(input())

total = bf_calories + lunch_calories + dinner_calories
print("Calorie content for " + today + ": " + str(total))