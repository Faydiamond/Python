import numpy as np
heroes = ["Capitana Marvel","Thor","Capitan America","Irom Mayden","Spiderman"]
print(len(heroes))

heroes_random = [heroes[np.random.randint(low=0,high=len(heroes))] for i in range(len(heroes)) ]
print(heroes_random)





