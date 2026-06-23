first_list = input().split(", ")
second_list = input().split(", ")

result = list(
    filter(
        lambda first_word: any(
            first_word in second_word
            for second_word in second_list
        ),
        first_list
    )
)
print(result)