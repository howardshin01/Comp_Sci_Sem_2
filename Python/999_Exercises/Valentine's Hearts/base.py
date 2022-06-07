people_list = ["My Girlfriend", "My Mother", "My teacher", "My Grandma"]
comp_list = ["is kind", "is smart", "is lovely", "is pretty", "is beautiful", "is hot"]

import random
num_people = random.randrange(0,len(people_list))
num_comp = random.randrange(0,len(comp_list))

print(people_list[num_people] + " " + comp_list[num_comp])