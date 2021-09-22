class Matrix:
  def __init__(self, *data):
    self.data = data

  def __repr__(self):
    return f"Matrix{self.data}"

  def __add__(self, other):
    assert(len(self.data[0]) == len(other.data[0]) and len( self.data[0][0] ) == len( other.data[0][0] )), 'Do not match'
    tmp = []
    for n in range(len(self.data[0])):
      tmp.append([])
    for n in range(len(self.data[0])):
      for m in range(len(self.data[0][n])):
        sum_tmp = self.data[0][n][m] + other.data[0][n][m]
        tmp[n].append(sum_tmp)
    return Matrix(tmp)

  def __sub__(self, other):
    assert(len(self.data[0]) == len(other.data[0]) and len( self.data[0][0] ) == len( other.data[0][0] )), 'Do not match'
    tmp = []
    for n in range(len(self.data[0])):
      tmp.append([])
    for n in range(len(self.data[0])):
      for m in range(len(self.data[0][n])):
        sub_tmp = self.data[0][n][m] - other.data[0][n][m]
        tmp[n].append(sub_tmp)
    return Matrix(tmp)

  def __mul__(self, other):
    if type(other) == Matrix:
      assert(len(self.data[0][0]) == len(other.data[0])) , 'Do not match'
      answer = []
      for n in range(len(self.data[0])):
        answer.append([])
      a = [self.data[0]]
      b = list(zip(*other.data[0]))
      print(a)
      for n in range(len(a[0])):
        for h in range(len(b)):
          num = 0
          for m in range(len(a[0][n])):
            x = a[0][n][m]
            y = b[h][m]
            num += x*y
          print(num)
          answer[n].append(num)
      return Matrix(answer)

    else:
      for n in range(len(self.data[0])):
        for m in range(len(self.data[0][n])):
          self.data[0][n][m] = self.data[0][n][m] * other
      return self

  def __rmul__(self, k):
    for n in range(len(self.data[0])):
      for m in range(len(self.data[0][n])):
        self.data[0][n][m] = self.data[0][n][m] * k
    return self
