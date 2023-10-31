fat = int(input())
protein = int(input())
carbs = int(input())
calories = int(input())
water = int(input())

fat_grams = calories * fat / 100 / 9
protein_grams = calories * protein / 100 / 4
carbs_grams = calories * carbs / 100 / 4
total_grams = fat_grams + protein_grams + carbs_grams
calories_per_gram = calories / total_grams
calories_per_gram_with_water = calories_per_gram * (100 - water) / 100
print(f"{calories_per_gram_with_water:.4f}")