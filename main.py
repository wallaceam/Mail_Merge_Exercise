# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Get names from file & output list of names
with open("./Input/Names/invited_names.txt") as all_names:
    names_list_dirty = all_names.readlines()

# Remove line breaks from names list
names_list_clean = []
for name in names_list_dirty:
    cleaned_name = name.strip()
    names_list_clean.append(cleaned_name)

# Extract template as string
with open("./Input/Letters/starting_letter.txt") as template:
    str_template = template.read()

# Write individual letters
for name in names_list_clean:
    with open(f"./Output/ReadyToSend/{name}_letter.txt", mode="w") as personalized_letter:
        personalized_letter.write(str_template.replace("[name]", name))
