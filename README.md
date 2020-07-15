# vx-mp-server
微信公众号 “就叫旻天吧” 后端接口

# 使用场景
网络文章千千万，但是自己总结的还是更香一点。

但是学习笔记总是忘记回顾，有时突然想起某个问题还要打开有道手动查找。

所以做了这个公众号后台，可以在公众号输入栏文字或语音的输入“给我一片关于***的文章”，
利用 Python 的 fuzzywuzzy 库，选择关联度最高的一片知乎文章推送给自己。

如果文章中有打入 <问> *** <问> <答> *** <答> 的标识包裹起来，
还可以使用 “给我一道 *** 的问题” 返回自己 <问> *** <问> 中的内容，
再次使用 “答案” 就会把 <答> *** <答> 的内容返回了。

目前自己需要的场景就这些，有兴趣的朋友可以给我提提意见，希望我们共同进步。
