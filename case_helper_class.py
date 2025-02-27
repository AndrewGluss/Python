from re import findall
class CaseHelper:
  @staticmethod
  def is_snake(text):
    pattern = r'([A-Z][a-z]{1,})'
    pattern2 = r'([a-z]{1,})'
    match1 = findall(pattern2, text)
    text2 = "_".join(match1)
    if text2 != text:
      return False
    else:
      return True

  @staticmethod
  def is_upper_camel(text):
    pattern = r'([A-Z][a-z]{1,})'
    pattern2 = r'([a-z]{1,})'
    match1 = findall(pattern, text)
    text2 = "".join(match1)
    if text2 != text:
      return False
    else:
      return True

  @staticmethod
  def to_snake(text):
    pattern = r'([A-Z][a-z]{1,})'
    pattern2 = r'([a-z]{1,})'
    match1 = findall(pattern, text)
    return '_'.join([i.lower() for i in match1])


  @staticmethod
  def to_upper_camel(text):
    pattern2 = r'([a-z]{1,})'
    match2 = findall(pattern2, text)
    return ''.join([i.capitalize() for i in match2])


print(CaseHelper.is_snake('beegeek'))
print(CaseHelper.is_snake('bee_geek'))
print(CaseHelper.is_snake('Beegeek'))
print(CaseHelper.is_snake('BeeGeek'))


print(CaseHelper.is_upper_camel('beegeek'))
print(CaseHelper.is_upper_camel('bee_geek'))
print(CaseHelper.is_upper_camel('Beegeek'))
print(CaseHelper.is_upper_camel('BeeGeek'))


print(CaseHelper.to_snake('Beegeek'))
print(CaseHelper.to_snake('BeeGeek'))


print(CaseHelper.to_upper_camel('beegeek'))
print(CaseHelper.to_upper_camel('bee_geek'))