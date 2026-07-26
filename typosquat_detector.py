import difflib


ls_legit_pkg=(input().split(","))
print(ls_legit_pkg)
userinput=input()
def typosquat(ls_legit_pkg1,userinput1):
  highest_percentage=0.0
  matched_lib=""
  limit=60.0
  suspicious_pkg=[]
  for i in ls_legit_pkg1:
    comparer=difflib.SequenceMatcher(None,i.lower(),userinput1).ratio()
    percentage=comparer*100
    if highest_percentage<percentage:
        highest_percentage=percentage
        matched_lib=i
  if(highest_percentage>=limit) and (highest_percentage!=float(100)):
      suspicious_pkg=userinput1
      print(f"suspicious package alert!! {suspicious_pkg}")
  elif (highest_percentage==float(100)):
      print(f"the package is legitimate!")
  return(highest_percentage,matched_lib)
print(f"the user input matches about {typosquat(ls_legit_pkg,userinput)} ")
   


