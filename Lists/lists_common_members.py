def common_members(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    
    if len(set1 & set2) > 0:
     return True
    else:
      return False
def main():
    common_members()