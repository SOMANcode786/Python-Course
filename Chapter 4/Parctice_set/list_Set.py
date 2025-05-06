# 🔸 Question:
# Aapke paas ek list hai jisme kuch fruits repeat ho rahe hain.
# Aapko:

# List ke total elements count karne hain

# Sirf unique fruits print karne hain (using set)

# Batana hai kitne duplicate elements the

fruits=['banana','apple','orange','kiwi','mango','banana','kiwi','kiwi','kiwi']
count_elements=len(fruits)
unique_fruits=set(fruits)
duplicate_elements=len(fruits)-len(unique_fruits)
print(f"Total elements in the list : {count_elements}")
print(f"Unique fruits in the list : {unique_fruits}")
print(f"Duplicate elements in the list : {duplicate_elements}")