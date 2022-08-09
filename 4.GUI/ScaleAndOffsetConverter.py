class ScaleAndOffsetConverter:
  def __init__(self, units_from, units_to, factor, offset):
    ScaleConverter.__init__(self, units_from, units_to, factor)
    self.offset = offset

  def convert(self, value):
    return value * self.factor + self.offset