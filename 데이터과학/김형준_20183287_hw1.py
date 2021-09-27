class Matrix:
  def __init__(self, data):
    self.data = data

  def __repr__(self):
    return f"Matrix{self.data}"

  def __add__(self, other):
    assert(len(self.data) == len(other.data) and len( self.data[0] ) == len( other.data[0] )), 'Do not match'
    tmp = []
    for n in range(len(self.data)):
      tmp.append([])
    for n in range(len(self.data)):
      for m in range(len(self.data[n])):
        sum_tmp = self.data[n][m] + other.data[n][m]
        tmp[n].append(sum_tmp)
    return Matrix(tmp)

  def __sub__(self, other):
    assert(len(self.data) == len(other.data) and len( self.data[0] ) == len( other.data[0] )), 'Do not match'
    tmp = []
    for n in range(len(self.data)):
      tmp.append([])
    for n in range(len(self.data)):
      for m in range(len(self.data[n])):
        sub_tmp = self.data[n][m] - other.data[n][m]
        tmp[n].append(sub_tmp)
    return Matrix(tmp)

  def __mul__(self, other):
    if type(other) == Matrix:
      assert(len(self.data[0]) == len(other.data)) , 'Do not match'
      answer = []
      for n in range(len(self.data)):
        answer.append([])
      a = self.data
      b = list(zip(*other.data))
      for n in range(len(a)):
        for h in range(len(b)):
          num = 0
          for m in range(len(a[n])):
            x = a[n][m]
            y = b[h][m]
            num += x*y
          
          answer[n].append(num)
      return Matrix(answer)

    else:
      for n in range(len(self.data)):
        for m in range(len(self.data[n])):
          self.data[n][m] = self.data[n][m] * other
      return self

  def __rmul__(self, k):
    for n in range(len(self.data)):
      for m in range(len(self.data[n])):
        self.data[n][m] = self.data[n][m] * k
    return self
