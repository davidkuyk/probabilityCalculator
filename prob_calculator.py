import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.contents = []
    # red=3,blue=2
    ballDict = {**kwargs}
    for key, value in ballDict.items():
      # put each key, list "value" number of times in the contents list
      for i in range(0, value):
        self.contents.append(key)
  
  def draw(self, num):
    contents = self.contents
    
    if num >= len(contents):
      return contents
    
    selection = []

    for i in range(num):
      index = random.randrange(len(contents))
      ball = contents[index]
      selection.append(ball)
      contents = contents[0:index] + contents[index + 1:] 
    # removes drawn ball from contents
    self.contents = contents
    return selection

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  count = 0
  for i in range(num_experiments):
    tempHat = copy.copy(hat)
    experiment_selection = tempHat.draw(num_balls_drawn)
    gotEm = True
    for key in expected_balls.keys():
      if experiment_selection.count(key) < expected_balls[key]:
        gotEm = False
        break
    if gotEm:
      count += 1
  # calculate probability
  return count / num_experiments