"""
git concepts
creating repo in remote
git clone
git status
git add
tracked and untracked
git commit
git push
git pull
dir

"""

if __name__ == '__main__':
    n = int(input().strip())
    if   n % 2 == 0:
        if n >= 2 and n <= 5:
            print("Not Weird")
        elif n >= 6 and n<= 20:
            print ("Weird")
        else: 
            print("Not Weird")  
    else:
        print("Weird")