list= ["Apple", "Pear", "Orange"]
list_str = str(list)
fruits = eval(list_str)
print(fruits)
print(type(fruits))
print(fruits[0])

def make_pie(index):
  try:
    fruit = fruits[index]
  except IndexError:
    print("Fruit Pie")
  else:
    print(fruit + "pie")

make_pie(4)


print("KEY ERROR TESTS\n")

facebook_posts = [
    {'Likes': 21, 'Comments': 2}, 
    {'Likes': 13, 'Comments': 2, 'Shares': 1}, 
    {'Likes': 33, 'Comments': 8, 'Shares': 3}, 
    {'Comments': 4, 'Shares': 2}, 
    {'Comments': 1, 'Shares': 1}, 
    {'Likes': 19, 'Comments': 3}
]
facebook_posts = str(facebook_posts)

# eval() function will create a list of dictionaries using the input
facebook_posts = eval(facebook_posts)
print(facebook_posts)
print(type(facebook_posts))

total_likes = 0
# TODO: Catch the KeyError exception
for post in facebook_posts:
  print(post.items())
  print(type(post))
  try:
    total_likes = total_likes + post['Likes']
  except KeyError:
    pass


print(total_likes)
