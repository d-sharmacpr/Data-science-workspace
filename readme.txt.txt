To clone the repository in the local system:-
--------------------------------------
>git clone 'rep_url'

to push the data to the github repo:-
-----------------------------------
>git add . ( to select all the files from this currect directory)
>git status ( to check the list of file to that will go the the github rep)
>git commit -m 'your commit msg'  ( file commit with the proper msg)
 or >git commit ( without any msg )
>git push -u origin main/master ( puch the code to the github)

for more information please check the below link:
https://www.datacamp.com/tutorial/git-push-pull

Standard instruction to push the code to github
================================================
create a new repository on the command line:-
------------------------------------------
echo "# dk-test" >> README.md
git init
git add README.md
git commit -m "first commit"  ( m for msg )
git branch -M main ( to switch the branch)
git remote add origin https://github.com/d-sharmacpr/dk-test.git
git push -u origin main

push an existing repository from the command line:-
----------------------------------------
git remote add origin https://github.com/d-sharmacpr/dk-test.git
git branch -M main
git push -u origin main
