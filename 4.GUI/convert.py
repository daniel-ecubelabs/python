#부모 클래스
class ScaleConverter:
  def __init__(self, units_from, units_to, factor):
    self.units_from = units_from
    self.units_to = units_to
    self.factor = factor

  def description(self):
    return 'Convert ' + self.units_from + ' to ' + self.units_to

  def convert(self, value):
    return value * self.factor

#ScaleConverter클래스 상속받은 자식 클래스 
class ScaleAndOffsetConvert:
  def __init__(self, units_from, units_to, factor, offset):
    ScaleConverter.__init__(self, units_from, units_to, factor)
    self.offset = offset

  def convert(self, value):
    return value * self.factor + self.offset
    
#실행     
c1 = ScaleConverter('inches', 'mm', 25)
print(c1.description())
print('converting 2 inches')
print(str(c1.convert(2)) + c1.units_to)
