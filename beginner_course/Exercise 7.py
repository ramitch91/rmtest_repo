d = {"Sam": 7, "rolls": ["rock", "paper", "scissors"], "done": True}

# Should output 7
print(d["Sam"])

# Should output ['rock', 'paper', 'scissors']
print(d["rolls"])

# Should output None
print(d.get("Sarah"))

# Should output -1
print(d.get("Jeff", -1))

#  Should output True
print(d["done"])
