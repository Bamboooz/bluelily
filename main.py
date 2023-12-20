import bluelily as bl

bl.log_actions = True  # set to true if you want to see bluelily logs

repo = bl.Repository("Bamboooz", "os.py")
print(repo.user)
    