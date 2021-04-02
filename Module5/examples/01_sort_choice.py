from random import randint

# Алгоритм:
# 1. Найти наименьшее значение в списке.
# 2. Записать его в начало списка, а первый элемент - на место, где раньше стоял наименьший.
# 3. Снова найти наименьший элемент в списке. При этом в поиске не участвует первый элемент.
# 4. Второй минимум поместить на второе место списка. Второй элемент при этом перемещается на освободившееся место.
# 5. Продолжать выполнять поиск и обмен, пока не будет достигнут конец списка.

nums = [5, 2, -1, 8, 4, -4, 7]
print("before sort = ", nums)
i = 0
while i < len(nums) - 1:
    m = i
    j = i + 1
    while j < len(nums):
        if nums[j] < nums[m]:
            m = j
        j += 1
    nums[i], nums[m] = nums[m], nums[i]
    i += 1
print("after sort = ", nums)
