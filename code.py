#testtesttesttest
# 01
def calculate(min, max):
    # 請用你的程式補完這個函式的區塊
    result = 0
    for i in range(min, max+1):
        result += i
    print(result)


calculate(1, 3)  # 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8)  # 你的程式要能夠計算 4+5+6+7+8，最後印出 30


# 02


def avg(data):
    # 請用你的程式補完這個函式的區塊
    salaries = 0
    for staff in data["employees"]:
        salaries += staff["salary"]
        result = salaries/data["count"]
    print(result)


avg({
    "count": 3, "employees": [
        {
            "name": "John",
            "salary": 30000},
        {
            "name": "Bob",
            "salary": 60000},
        {
            "name": "Jenny",
            "salary": 50000}
    ]
})  # 呼叫avg函數


# 03


def maxProduct(nums):
    # 請用你的程式補完這個函式的區塊
    max = nums[0]*nums[1]
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]*nums[j] > max:
                max = nums[i]*nums[j]
    print(max)


maxProduct([5, 20, 2, 6])  # 得到 120 因為 20 和 6 相乘得到最大值
maxProduct([10, -20, 0, 3])  # 得到 30 因為 10 和 3 相乘得到最大值


# 04


def twoSum(nums, target):
    # your code here
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j] == target:
                return [i, j]


result = twoSum([2, 11, 7, 15], 9)
print(result)  # show [0, 2] because nums[0]+nums[2] is 9


# 05
def maxZeros(nums):
    # 請用你的程式補完這個函式的區塊
    max_time = 0
    cur_time = 0
    for i in nums:
        if i == 0:
            cur_time += 1
            max_time = max((cur_time, max_time))
        else:
            cur_time = 0
    print(max_time)


maxZeros([0, 1, 0, 0])  # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0])  # 得到 4
maxZeros([1, 1, 1, 1, 1])  # 得到 0
