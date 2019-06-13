# 提示使用者輸入體重
weight = eval(input("請輸入體重(公斤):"))
# 提示使用者輸入身高
height = eval(input("請輸入身高(公分):"))

# 計算BMI
weightInKilograms = weight
heightInMeters = height / 100
bmi = weightInKilograms / (heightInMeters ** 2)
# 顯示結果
print("BMI is", format(bmi, ".2f"))
if bmi < 18.5:
    print("體重不足")
elif bmi < 25:
    print("正常")
elif bmi < 30:
    print("過重")
else:
    print("肥胖")

# 提示使用者輸入運動
user_exercise = input("請輸入運動項目:")
hour = float(input("小時"))

# 計算消耗卡路里

weightInKilograms = weight
heightInMeters = height / 100

exercise = {'hike': 3.5, 'jog': 8.2, 'run': 16.8, 'swim': 6.3, 'yoga': 3, 'basketball': 6, 'badminton': 5.12,
            'go upstairs': 7.96, 'ride a bike': 5}

calories = weightInKilograms * exercise[user_exercise] * hour


# 顯示結果
print("Calories is", format(calories, ".2f"))
if calories < 100:
    print("運動不足")
elif calories > 200:
    print("運動正常")
elif calories > 1000:
    print("運動稍微過量，建議每天均衡運動即可")

