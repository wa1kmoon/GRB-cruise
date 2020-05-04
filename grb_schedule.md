## 值班安排

- 12.23~12.29   刘行    属于
- 12.30~01.05   余邦耀  不属于
- 01.06~01.12   朱子佩  属于
- 01.13~01.19   朱子佩  不属于
- 01.20~01.26   刘行    属于
- 01.27~02.02   徐栋    不属于
- 02.03~02.09   朱子佩  属于
- 02.10~02.16   徐栋    不属于
- 02.17~02.23   刘行    属于
- 02.24~03.01   朱子佩  不属于
- 03.02~03.08   徐栋    属于
- 03.09~03.15   刘行    不属于
- 03.16~03.22   朱子佩  属于
- 03.23~03.29   徐栋    不属于
- 03.30~04.05   刘行    属于
- 04.06~04.12   朱子佩  不属于
- 04.13~04.19   朱子佩  属于
- 04.20~04.26   徐栋    不属于
- 04.27~05.03   付韶宇  属于
- 05.04~05.10   朱子佩  不属于 #替刘行
- 05.11~05.17   刘行    属于  #还朱子佩

## 参考资料

- [南山天气]    /   [NEXT数据]
- [兴隆216时间分配] /   [兴隆天气]
- [UKIRT]    /    [仪器安排]  /   [曝光时间]  /   [UKIRT天气]
- [NOT] /   [schedule]  /   [NOT_weather]   /   [duty_shift]

[schedule]:http://www.not.iac.es/observing/schedules/
[NOT]:http://www.not.iac.es/
[NOT_weather]:http://www.not.iac.es/weather/
[duty_shift]:https://notendur.hi.is/~pja/NOT/schedule.txt

[南山天气]:http://www.xjltp.com/xo/cn/xmqx.htm
[NEXT数据]:http://psp.china-vo.org/next/

[兴隆216时间分配]:2019-2020_216m_time.pdf
[兴隆天气]:http://www.xinglong-naoc.org/weather/yuntu.jhtml

[UKIRT]:http://www.ukirt.hawaii.edu/
[仪器安排]:http://www.ukirt.hawaii.edu/schedule/semesters/
[曝光时间]:http://www.ukirt.hawaii.edu/cgi-bin/ITC/itc.pl
[UKIRT天气]:http://www.eao.hawaii.edu/weather/camera/ukirt/

## GRB值班注意事项

- 值班交接时间：每周一上午10点
- 值班者在微信群自行交接给下一名值班者，若未交接，则由该值班者继续负责
- 值班期间发生的伽玛暴，由该周值班者负责之后的观测与数据处理（包括非值班周该暴的观测与处理）
- 可以在群里询问确定是否观测与观测方案
- 值班者需要将当周发生的伽玛暴记录在[grb_total]文件中
    - 主要是记录swift暴以及其他指定观测的目标
    - 文件路径:</var/www/html/grb/grb_total.md>
    - 若伽玛暴未观测，则记录为未观测并说明原因，例如高度低，下雨等
    - 若伽玛暴观测，则记录并给出星等，记录gcn等信息
- 不明白的事情及时询问
- 采用Markdown书写，建议Chrome或者Firefox安装Markdown插件方便浏览
    -   [Firefox]
    -   [Chrome]
[grb_total]:http://10.36.0.26/grb/grb_total.md    
[Firefox]:https://addons.mozilla.org/en-US/firefox/addon/markdown-viewer-chrome/
[chrome]:https://chrome.google.com/webstore/detail/markdown-preview-plus/febilkbfcbhebfnokafefeacimjdckgl

## 引力波值班注意事项

- 原则
    - 最需要关注
        - 双中子星合并以及黑洞中子星合并
        - 距离在100Mpc以内的事件
    - 优先观测当天最新的引力波事件
        - 如果是隔日的远距离事件，则放弃观测
        - 如果是当天的远距离事件（如大于1Gpc），可放弃观测
        - `注意`如果是当天第一次发布的历史事件，若满足以下条件，仍然观测
            - 3天以内的事件
            - 距离在100Mpc以内的事件
            - 如，2020年1月7日，第一次发布S200105e事件，如果距离大于100Mpc则不观测，反之则观测
        - 如果同一个引力波在未观测前有更新，则使用更新的列表
    - 候选体观测
        - 如果GCN报道候选体，可安排跟踪望远镜跟踪观测
            - 注意：如果有多个邻近候选体，可选择使用巡天望远镜同时覆盖
        - 如果GCN报道其他仪器误差天区，如IceCube，HAWC等，可安排巡天望远镜搜寻
    - 撤回：如果ligo在随后发布的GCN中声明此次事件是假事件，则停止观测
        - 引力波邮件中有一个参数`Terrestrial`，这代表地面事件的概率，可以理解为假事件概率
            - 如果这个概率较高（比如高于0.3），则可以等待ligo的GCN再决定是否观测
- 目前使用的望远镜
    - 兴隆施密特
        - 巡天望远镜
        - 视场1.5x1.5平方度
        - 列表上传方式：自动同步
        - 通知方式：电话与微信通知
            - 白天的事件则微信通知
            - 夜间紧急事件则打电话
        - 值班人员
            - 滕晓明（白天）：15133840769
            - 关向楠（夜间）：15233248792
            - 刘鹏飞（夜间）：18031400574
    - 南山1m
        - 巡天望远镜
        - 视场1.3x1.3平方度
        - 列表上传方式：邮件上传
            - <optics_staff@xao.ac.cn>
        - 通知方式：电话与微信通知
            - 09915935835
    - NEXT
        - 巡星系与后随观测望远镜
        - 视场20x20角秒
        - 列表上传方式：自动上传
        - 通知方式：QQ与电话
    - 兴隆2.16m
        - 后随观测望远镜
        - 视场10x10角分
        - 通知方式：电话与微信
            - 18631449481
- 值班安排
    - 目前与GRB值班安排一致
- 其他
    - 任何疑问随时联系及时解决
