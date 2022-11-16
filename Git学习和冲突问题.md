# GIT学习问题

## 学习内容的目录
1. [本地仓库的创建](#1)
2. [上传远程仓库](#2)
3. [获取远程仓库最新版本](#3)
4. [冲突问题](#4)
5. [解决冲突问题时遇到的情况](#5)

## 学习内容
<p id="1"></p>

### 一、本地仓库的创建
1. 在创建一个新的本地仓库
使用**git init**在工作区创建一个`.git`文件，实现本地仓库的创建。

2. 从github上克隆一个仓库
使用**git clone**存储库的地址，将github上的库下载到本地。

<p id="2"></p>

### 二、上传远程仓库
1. 添加文件git add
2. 添加注释git commit
3. 关联github仓库
4. 上传代码`git push -u origin master`
>如果再次上传的仓库是已关联的仓库，可以直接跳过第三步。
>指定origin为默认主机后再次上传代码直接git push就可以了

<p id="3"></p>

### 三、获取远程仓库最新版本
1. **git fetch** 
从远程仓库获得最新版本到本地，不会自动merge。
```
git fetch origin master:tmp  
git diff tmp  
git merge tmp
```
2. **git pull**
从远程仓库获得最新版本并merge到本地。
```
git pull origin master
```
>不管用fetch还是pull，做之前都要在本地仓库做一次git commit，确保，本地仓库和工作目录及缓存一致

<p id="4"></p>

### 四、冲突问题
问题：github上新建一个文件，将文件拉到本地，在github和本地做不同修改，上传本地文件到github上，发生冲突。
>这个问题是因为远程库与本地库不一致造成的

![冲突问题1](https://raw.githubusercontent.com/Zqxg/Tasks/main/%E5%86%B2%E7%AA%81%E9%97%AE%E9%A2%98%E8%A7%A3%E5%86%B3%E5%9B%BE%E7%89%87/%E5%86%B2%E7%AA%81%E9%97%AE%E9%A2%981.png)
1. 使用git status 查看冲突
![冲突问题解决2](https://raw.githubusercontent.com/Zqxg/Tasks/main/%E5%86%B2%E7%AA%81%E9%97%AE%E9%A2%98%E8%A7%A3%E5%86%B3%E5%9B%BE%E7%89%87/%E5%86%B2%E7%AA%81%E9%97%AE%E9%A2%98%E8%A7%A3%E5%86%B32.png)

```
您的分支比“origin/main”领先1次提交。
（使用“git-push”发布本地提交）
```
发现是因为我们远程库与本地库不一致

2. 根据git status 的提示，我先将远程库上的文件拉下来
![冲突问题解决3](https://raw.githubusercontent.com/Zqxg/Tasks/main/%E5%86%B2%E7%AA%81%E9%97%AE%E9%A2%98%E8%A7%A3%E5%86%B3%E5%9B%BE%E7%89%87/%E5%86%B2%E7%AA%81%E9%97%AE%E9%A2%98%E8%A7%A3%E5%86%B33.png)

3. 然后使用git diff对比本地库和远程库有什么不一样的地方
![冲突问题解决4.png (751×280) (raw.githubusercontent.com)](https://raw.githubusercontent.com/Zqxg/Tasks/main/%E5%86%B2%E7%AA%81%E9%97%AE%E9%A2%98%E8%A7%A3%E5%86%B3%E5%9B%BE%E7%89%87/%E5%86%B2%E7%AA%81%E9%97%AE%E9%A2%98%E8%A7%A3%E5%86%B34.png)

4.可以看到本地和github上，都增加了一段文字。我手动打开这个文件，然后对里面的文字进行修改，保存。
![冲突问题解决5.png (544×388) (raw.githubusercontent.com)](https://raw.githubusercontent.com/Zqxg/Tasks/main/%E5%86%B2%E7%AA%81%E9%97%AE%E9%A2%98%E8%A7%A3%E5%86%B3%E5%9B%BE%E7%89%87/%E5%86%B2%E7%AA%81%E9%97%AE%E9%A2%98%E8%A7%A3%E5%86%B35.png)
5. 再次提交文件,提交成功！
![冲突问题解决6.png (853×367) (raw.githubusercontent.com)](https://raw.githubusercontent.com/Zqxg/Tasks/main/%E5%86%B2%E7%AA%81%E9%97%AE%E9%A2%98%E8%A7%A3%E5%86%B3%E5%9B%BE%E7%89%87/%E5%86%B2%E7%AA%81%E9%97%AE%E9%A2%98%E8%A7%A3%E5%86%B36.png)

<p id="5"></p>

### 五、解决冲突问题时遇到的情况

1. 一开始我想将远程库更新合并到本地库
`git pull --rebase origin main`
>先取消commit记录，并且把它们临时保存为补丁(patch)(这些补丁放到".git/rebase"目录中)，之后同步远程库到本地，最后合并补丁到本地库之中

2. 再使用git push提交文件
出现别的问题：第二次提交的时候后面的分支出现了(master|REBASE 1/2)

3. 使用git status检查冲突
（具体什么忘了截图了，下图是找的浏览器翻译记录）
![冲突问题截图.png (1462×577) (raw.githubusercontent.com)](https://raw.githubusercontent.com/Zqxg/Tasks/main/%E5%86%B2%E7%AA%81%E9%97%AE%E9%A2%98%E8%A7%A3%E5%86%B3%E5%9B%BE%E7%89%87/%E5%86%B2%E7%AA%81%E9%97%AE%E9%A2%98%E6%88%AA%E5%9B%BE.png)
4. 我记得好像后来是使用 git rebase--edit todo,然后出现了一个界面好像，反正倒腾半天，还是不行。
5. 最后实在不行了，我把本地库删掉，将github上的冲突问题.md文件手动复原，重新git clone了我的仓库。然后重新修改github和本地文件，再次上传，然后解决冲突（标题四）
>前前后后，断断续续的搞了两天的时间。通过解决这次的冲突问题，让我对git的学习有了一个更深的印象。
## 参考资料
1. [git将远程仓库最新版本拉到本地仓库](http://t.zoukankan.com/litifeng-p-5702607.html)
2. [(25条消息) Git系列三：本地仓库的创建：git init、git clone_小蜗牛冲鸭~的博客-CSDN博客_git init 本地](https://blog.csdn.net/qq_34761779/article/details/126572648)
3. [(25条消息) git push origin master和git push有什么区别_z蓝莲花z的博客-CSDN博客_git push origin master](https://blog.csdn.net/fucong920618717/article/details/89373001)
4. [(25条消息) git push错误failed to push some refs to的解决_考拉-Koala的博客-CSDN博客](https://blog.csdn.net/UUUUUnnn/article/details/125945902)
5. [(25条消息) 【Git】git stash 和 git stash pop_想上天的小鱼的博客-CSDN博客_git pop stash](https://blog.csdn.net/weixin_38629529/article/details/120240362)
6. [git冲突解决问题---多人修改同一文件 - 睁yan-ii - 博客园 (cnblogs.com)](https://www.cnblogs.com/zhangshijiezsj/p/16198903.html)