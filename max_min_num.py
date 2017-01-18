def find_max_min(x):
  max_num = max(x)  
  min_num = min(x)  

  if max_num == min_num:
      return [len(x)]
  else:
      return [min_num,max_num]
