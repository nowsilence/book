``` 
# 将本地子目录推送到远程分支
git subtree push --prefix 本地目录 origin 分支名称

#本地添加远程仓库
git remote add 本地仓库名称 远程仓库地址（https://github.com/XXX/XXX.git）

#将分支代码合并到master分支，切换到master分支
git cherry-pick ce3252（提交记录）

#远程分支拉到本地
git checkout -b 本地分支名x origin/远程分支名x

#删除本地分支
git branch -D branchName

#删除远程分支
git push origin :branchName  (origin 后面有空格)

#可以看到fileName相关的commit记录
git log filename

# 可以显示每次提交的diff
git log -p filename


```

