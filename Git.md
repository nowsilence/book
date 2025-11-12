``` 
git clone --depth=1
# 将本地子目录推送到远程分支
git subtree push --prefix 本地目录 origin 分支名称

git remote update：更新远程跟踪分支、标签等。
git remote update origin 更新特定仓库
-p 或 --prune：删除那些在远程仓库中已经不存在的本地引用。

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


git pull 拉取代码之后有冲突
解决冲突后
git add file
继续合并
git merge --continue //提交完这一个冲突之后，继续其他冲突,zuoyou

git cherry-pick 后有冲突
解决冲突后
git cherry-pick --continue
git cherry-pick 会导致提交的commit id变更

删除某一条提交记录commit_1，他的前一条记录为commit_0
git rebase -i commit_0
进入编辑模式，把想要删除的记录由pick改为drop
会导致commit_0之后的所有提交记录的commitid变更

切到master分支，
执行git merge branch1，
将branch1的代码合并到master分支。
代码之后有冲突
解决冲突后
git add file
继续合并
git merge --continue //提交完这一个冲突之后，继续其他冲突,zuoyou


将Branch1的代码合并到Branch2分支上
git checkout Branch2
git rebase Branch1
若有冲突，解决冲突后add，执行git rebase --continue

git stash pop [number] -- git stash pop 2
git stash show [numer] -- git stash show 2
type：用于说明 commit 的类型，被指定在 commitlint.config.js 的 type-enum
feat：新功能（feature）
fix：修补bug
docs：文档
style： 格式（不影响代码运行的变动）
refactor：重构（即不是新增功能，也不是修改bug的代码变动）
test：增加测试
chore：构建过程或辅助工具的变动
revert: 回滚到上一个版本
perf:优化

```

