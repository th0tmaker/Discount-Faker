user_text_list = []
final_list = []


def text2list(txt, typ, formatted_txt):
    # take user text and split every time there's a new line
    split_text = txt.split('\n')
    # if user type selected is 'n' for number
    if typ == "n":
        # iterate over split_text variable and get both index (i) and item
        for i, item in enumerate(split_text):
            # append the index and item to a list using f-string formation
            formatted_txt.append(f"{i + 1}. {item}")
    # if user type selected is 'b' for bullet
    elif typ == "b":
        # iterate over split_text variable and get item
        for item in split_text:
            # append item to a list using f-string formation
            formatted_txt.append(f"• {item}")


# ask user for text inputs they wish to format
while True:
    text_input = str(input("Choose text to display: "))
    if text_input == "":
        break
    user_text_list.append(text_input)

# ask user for format type input
while True:
    type_input = str(input("Choose how you want your text displayed. "
                           "Input 'n' for number or 'b' for bullet points: ").lower())
    if type_input in ["n", "b"]:
        break

# takes all string elements separated by '\n' in user_text_list and joins them together
text = '\n'.join(user_text_list)
text2list(text, type_input, final_list)

# print list items each in seperate row
for items in final_list:
    print(items)
