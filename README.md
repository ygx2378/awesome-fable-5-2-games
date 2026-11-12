# Awesome Fable 5.2 Games

**26 款游戏 · 22 个游戏仓库 · 3 份社区合集 · 21 款可直接在浏览器里点开就玩**

Fable 5.2 上线三天，GitHub 上已经出现了一批不像「demo」的作品：能开车抢车被警察追的开放世界、骑马打猎的西部、能联机的港口 FPS、三国志式的 3D 即时战略、甚至单人用 21 句话写完的《帝国时代》替身。

这个仓库把它们整理成一份可检索的清单：**每款都有源码地址、一句玩法说明、真实技术栈，以及能直接玩的在线地址**。技术栈对比与 Prompt 原文各自独立成篇，方便你反推「什么样的提示词能做出这种东西」。

| 文档 | 内容 |
| --- | --- |
| [TECH_STACK.md](TECH_STACK.md) | 22 个仓库的技术栈、构建方式、交付体积、生成成本横向对比 |
| [PROMPTS.md](PROMPTS.md) | 可复现的原始提示词：一句话 FPS、21 句 RTS、三句需求做出三个游戏 |
| [data/games.csv](data/games.csv) | 结构化数据，方便二次加工或做站 |

> **核验说明**：数据抓取于 **2026-11-12**。22 个游戏仓库、3 个合集仓库逐一调用 GitHub API 确认存在；所有在线试玩链接逐一发起请求确认可访问（HTTP 200）。Star 数为抓取当日快照。
> 部分作品仍在开发中，完成度差异很大；标注「暂无在线版本」的 5 款需要本地起服务才能玩。

## 图例

- 🎮 `[Play Online Live Demo]` —— 托管镜像，点开即玩，无需安装（[技术栈速查表](#六技术栈速查表)里的「🎮 试玩」同样可直接点）
- 🖥 作者自建站 / GitHub Pages —— 作者本人托管的版本，通常与源码同步更新
- ⌨️ 暂无在线版本 —— 仓库里没有部署，需 clone 后本地起静态服务
- ⭐ —— Star 数（2026-11-12）

## 目录

- [一、开放世界与 3D 动作（6 款）](#一开放世界与-3d-动作6-款)
- [二、第一人称射击（5 款）](#二第一人称射击5-款)
- [三、视觉效果与探索（6 款）](#三视觉效果与探索6-款)
- [四、体育、竞速与其他（9 款）](#四体育竞速与其他9-款)
- [五、值得收藏的社区合集](#五值得收藏的社区合集)
- [六、技术栈速查表](#六技术栈速查表)
- [七、这些游戏是怎么被写出来的](#七这些游戏是怎么被写出来的)
- [附录：站上还有这 11 款](#附录站上还有这-11-款)

---

## 一、开放世界与 3D 动作（6 款）

**01 · FOG CITY** — GTA 风格开放世界 · [源码](https://github.com/Rikinshah787/Game-Fable-5.2) ⭐ 0
旧金山风格小城，7×7 街区带坡道和跨海大桥；有红绿灯车流、会躲子弹逃跑的行人、可劫持的车辆，五星通缉时警车追上来、警察下车开火，甩掉视线通缉才会清零。
`three.js` · 无构建 · 12 个 ES module 分工（城市 / 车辆 / 警察 AI / 后处理） · ⌨️ 暂无在线版本，`npm start` 后开 <http://localhost:8765>

**02 · Dustfall** — 西部开放世界 · [源码](https://github.com/webKing021/dustfall) ⭐ 2
驯服野马、骑马打猎钓鱼、在酒馆打黑杰克，六个章节的主线加赏金追捕；犯罪需要目击者，赏金会招来追兵团，荣誉值影响物价和结局。
`three.js 0.187 + Vite 8` · 昼夜与暴雨沙尘 · [Play Online Live Demo](https://fable52.games/play/dustfall) · [作者站](https://dustfalls.netlify.app/)

**03 · Bayhaven** — 犯罪题材开放世界，AI 逐次提交 · [源码](https://github.com/fablestar/bayhaven) ⭐ 0
不是「AI 辅助」，而是每行代码、每个 commit 都由 Fable 5.2 在公开直播里写完；仓库里除了 `src/`，还有它自己维护的 `ROADMAP.md`、`BUGS.md` 和每个模块的接口契约。
`three.js` · 模块注册表 · 每次提交都跑 headless Chromium 检查 · [Play Online Live Demo](https://fable52.games/play/bayhaven) · [直播回放](https://fablestar.games/watch.html)

**04 · Aquila** — 古罗马开放世界 · [源码](https://github.com/GavinLOrio/Fable-5.2-random-game) ⭐ 0
扮演凯撒第十三军团的信使，从卢比孔河走到三月十五日；地图用真实海岸线生成，103 个地点按真实坐标摆放，八章主线、十个支线、28 个据点、18 处沉船可潜水。
`three.js + esbuild` · 单文件 `rome/index.html` · 潜行 / 爬墙 / 方阵战斗 / 划桨船 · ⌨️ 暂无在线版本，`node tools/build.mjs rome` 后打开

**05 · Dawnward** — 3D 奇幻开放世界 · [源码](https://github.com/GavinLOrio/Fable-5.2-random-game) ⭐ 0
永夜之岛，穿越六大区域点亮六座古灯塔，升级拿祝福，最后在「王冠」迎战 Umbra Titan。提灯自动攻击，玩的是走位与冲刺的取舍。
`three.js + esbuild` · 单文件 `index.html`，离线可玩、自动存档 · 支持手机触屏 · ⌨️ 暂无在线版本

**06 · Ironvale** — 《帝国时代》风格 RTS · [源码](https://github.com/SharpWizard/ironvale) ⭐ 0
采集、建城、三个时代升级、科技树、编队热键、战争迷雾、AI 对手会投降；五个原创国度各有独特兵种与建筑，还有三部原创战役。
`three.js r128`（内置 `lib/` 并带 CDN 兜底）· 21 句大白话写成 · 另附 5.8 MB 单文件 `Ironvale.exe` · [Play Online Live Demo](https://fable52.games/play/ironvale) · [作者站](https://sharpwizard.github.io/ironvale/) · [完整提示词](https://github.com/SharpWizard/ironvale/blob/main/PROMPTS.md)

## 二、第一人称射击（5 款）

**07 · Saltline** — 3D 港口 FPS · [源码](https://github.com/realcodebear/saltline-fable-5.2) ⭐ 230
整条链路的起点：Anthropic 的 Felix Rieseberg 一句提示词、无人干预 8 小时跑出来的雨夜集装箱码头，切断三个中继站，躲开机群「Gulls」和机械狗「Hounds」。
`three.js` 内联 · **单文件 1.4 MB** · 模型、音效、贴图全部代码生成 · [Play Online Live Demo](https://fable52.games/play/saltline-fable-5-2-fps) · [作者站](https://realcodebear.github.io/saltline-fable-5.2/)

**08 · 盐线行动 Online** — 港口 FPS 联机版 · [源码](https://github.com/wenzhengshi/fable5-2-salt-online) ⭐ 16
在 Saltline 基础上扩出多人对战：5 秒复活、房间大厅、本地排行榜落盘，无数据库，单机 `node server.js` 就能开局。
`Node.js + Express + WebSocket + three.js` · 前后端同一仓库 · [Play Online Live Demo](https://fable52.games/play/saltline-online)

**09 · SUBLEVEL 07** — 科幻地下变电站 FPS · [源码](https://github.com/wquguru/fable52-fps-repro) ⭐ 78
中文社区里最能「抄作业」的一份：一句提示词、73 轮无人干预、41 分钟，产出 **131 KB 单文件**，潮湿地面实时反射、红点卡宾枪、三波悬浮无人机、18 个合成音效，AI 自己写脚本打通关验证零报错。仓库同时公开提示词原文与逐轮 token 账单。
`单文件 HTML` · 体积极小但含后处理 · [Play Online Live Demo](https://fable52.games/play/sublevel-07-fps-repro) · [作者站](https://wquguru.github.io/fable52-fps-repro/)

**10 · BLAMELESS** — 程序员主题 FPS · [源码](https://github.com/Petyok/blameless) ⭐ 0
凌晨 3:07 告警响了：你 `kubectl exec` 进生产环境，用 `kill -9`、`grep -r`、`rm -rf` 当武器，清掉十个故障、四台主机、一个根因。没有弹药，只有限流（打太久返回 429），血量就是错误预算，死后写复盘。
`three.js` + npm 构建 · Python 标准库排行榜服务 · 确定性模拟可在 Node 里跑端测 · [Play Online Live Demo](https://fable52.games/play/blameless) · [作者站](https://blameless.petruha.ge/)

**11 · Dustline Outpost** — 时间循环 FPS · [源码](https://github.com/systemsluke/fable5.2game) ⭐ 1
每道闪电把世界倒回 70 秒，你上一轮的自己被留下成一个半透明「回声」，按原样重放每一枪。三个中继站相距太远，只能靠不同轮次的自己配合占领——一共六次机会。
`three.js r128` · 无构建 · 回声按 20 Hz 记录并从**当前**世界重发射线 · Poly Haven CC0 扫描素材 · ⌨️ 暂无在线版本，需静态服务且首屏拉 41 MB 资源

## 三、视觉效果与探索（6 款）

**12 · Tidebell 潮钟** — 3D 水下探索 · [源码](https://github.com/hahaliu1029/fable5.2demo) ⭐ 0
驾驶小潜水器从阳光照透的珊瑚礁一路下潜到深渊，唤醒七口沉睡的潮钟。48 个模型全部由 Blender 里的 Python 脚本生成，手写水下光照：红色最先随深度消失，开灯才把颜色找回来。
`three.js r170` · 单文件 `index.html` · 18,000 个海底实例，鱼群动画跑在顶点着色器里 · [Play Online Live Demo](https://fable52.games/play/tidebell)

**13 · MOTHLIGHT // Vesper-9** — 赛博朋克城市驾驶 · [源码](https://github.com/hahaliu1029/fable5.2demo) ⭐ 0
雨夜霓虹城里穿 12 道光门，手刹漂移、加速带、单轨列车与全息飞蛾；9×9 街区 694 栋楼一次实例化绘制，窗户画出带纵深的房间。
`three.js r170` · 单文件 · 湿街道镜面反射与实时环境贴图 · [Play Online Live Demo](https://fable52.games/play/mothlight)

**14 · 青云宗 · 御剑采灵** — 3D 仙侠 · [源码](https://github.com/hahaliu1029/fable5.2demo) ⭐ 0
第三人称御剑飞行，在体积云海、浮岩和真实反射的湖面之间收集 20 颗灵气，点亮山门牌匾后穿门通关；水墨标题、飞剑光带、解锁金光柱。
`three.js r170` · 单文件 · 支持触屏；自驾驶脚本可完整通关并录回放 · [Play Online Live Demo](https://fable52.games/play/qingyun-sword-flight)

**15 · MISREMEMBER** — 第一人称心理恐怖 · [源码](https://github.com/hahaliu1029/fable5.2demo) ⭐ 0
有什么东西按你的记忆重建了童年的家，而记忆并不可靠：你盯着的东西永远不变，变化只发生在你身后。房间靠门洞模板遮罩拼接，同一扇门下次打开可能通向别处。
`three.js` · 单文件 · 变化排队等离开视野才落地；贴图由 Codex 生成（仓库只放 WebP）· [Play Online Live Demo](https://fable52.games/play/misremember)

**16 · Hanford Reach** — 小镇探索与定居点建设 · [源码](https://github.com/chzbloom123/settlement-bluff-fable5.2) ⭐ 0
哥伦比亚河畔小镇废墟上的慢节奏建造游戏，第一人称与第三人称随时切换，带质量档位、性能报表和一键渲染 14 个固定机位的对比截图脚本。
`three.js + Vite` · Vercel 自动部署，每个 PR 有独立预览 · [Play Online Live Demo](https://fable52.games/play/hanford-reach) · [作者站](https://settlement-bluff-fable52.vercel.app)

**17 · Boring Game** — 湾区体素世界 · [源码](https://github.com/jakozaur/sf_bay_area_transit_fable_5_2_game) ⭐ 0
用真实地图数据重建旧金山湾区体素地形，规划线路、挖隧道、建车站，把列车开到作者公司楼下。15 条提示词、15 小时、66,000 行、约 $700。
`TypeScript + Vite` · typecheck + Biome + Vitest + 基准测试 · [Play Online Live Demo](https://fable52.games/play/boring-game-sf-bay-transit) · [作者站](https://jakozaur.github.io/sf_bay_area_transit_fable_5_2_game/)

## 四、体育、竞速与其他（9 款）

**18 · Soccer 3D** — 7 人制 3D 足球 · [源码](https://github.com/ShaunPrice/soccer-3d) ⭐ 0
有裁判、越位、红黄牌、点球与人墙、伤停补时和平局点球大战；阵型/心态/逼抢三档战术，体力、受伤、三个换人名额，进球慢镜回放，八级难度。
`单文件 HTML` · PWA 可装到手机主屏、离线可玩 · 音效与解说由 ElevenLabs 生成 · [Play Online Live Demo](https://fable52.games/play/pocket-soccer-3d) · [作者站](https://shaunprice.github.io/soccer-3d/)

**19 · TukTuk** — 埃及街头驾驶 · [源码](https://github.com/basemazab/tuktuk) ⭐ 0
在挤满小巴、出租和西瓜车的开罗街道里钻缝拉客，收车费、躲路障。所有形状、材质、音效都由代码生成，仓库里没有一张图片、一个音频文件。
`three.js` · `game.js` + `index.html` 两个文件 · [Play Online Live Demo](https://fable52.games/play/tuktuk) · [作者站](https://basemazab.github.io/tuktuk/)

**20 · Emberdeep** — 浏览器冒险 · [源码](https://github.com/DNDNoob/EmberDeep) ⭐ 0
火把在烧，往下走。单文件地牢下潜，约 100 KB。
`单文件 HTML` · [Play Online Live Demo](https://fable52.games/play/emberdeep) · [作者站](https://dndnoob.github.io/EmberDeep/)

**21 · Daedalus** — 古希腊神话解谜 · [源码](https://github.com/S77FFY/daedalus) ⭐ 1
以代达罗斯迷宫为题的谜题游戏，121 KB 单文件。
`单文件 HTML` · [Play Online Live Demo](https://fable52.games/play/daedalus) · [作者站](https://s77ffy.github.io/daedalus/)

**22 · Sternenjäger** — 科幻太空射击 · [源码](https://github.com/oldzitterhand/sternenjaeger) ⭐ 0
12 个星区、3 场 Boss 战，飞船自动开火，玩家只管飞位与 EMP；手机、键盘、手柄三种操作都支持。
`单文件 HTML` · 无构建无服务 · [Play Online Live Demo](https://fable52.games/play/sternenjaeger) · [作者站](https://oldzitterhand.github.io/sternenjaeger/)

**23 · Shuttle Strike** — 第一人称羽毛球 · [源码](https://github.com/fedifianto/shuttlestrike) ⭐ 0
用摄像头追踪手部：握拳即握拍，挥快球杀球，拍面高低决定挑高或吊球；张开手掌停住是暂停。没摄像头可切鼠标模式。
`单文件 HTML` + CDN 手部追踪 · 需 HTTPS 或 localhost 才能开摄像头 · [Play Online Live Demo](https://fable52.games/play/shuttle-strike) · [作者站](https://fedifianto.github.io/shuttlestrike/)

**24 · NEON RUNNER** — 赛博朋克 2D 跑酷 · [源码](https://github.com/Ilias-AK/NewGameFromFable5.2) ⭐ 0
霓虹城市无尽跑酷，障碍按「与玩家相遇的时间」生成，因此难度提升不会压缩反应窗口；三档难度、护盾与磁铁道具、每 500 米记速、Top-5 本地存档。
`单文件 HTML` · Canvas 2D + Web Audio + LocalStorage，零外部资源 · ⌨️ 暂无在线版本，双击 `index.html` 即可

**25 · Becario del Universo** — 宇宙主题小游戏 · [源码](https://github.com/masugus/fable5.2-5min-game) ⭐ 0
「宇宙最新实习生」的琐碎任务合集，桌面与手机同一份代码，5 分钟能玩完一局，最高分存在浏览器里。
`单文件 HTML` · [Play Online Live Demo](https://fable52.games/play/becario-del-universo) · [作者站](https://masugus.github.io/fable5.2-5min-game/)

**26 · Harvest Standoff** — 农场 5v5 团队竞技 · [源码](https://github.com/andreteow/farm-ca) ⭐ 0
动物对农场工人，回合制 5v5，有商店、金币、中场与「臭南瓜」；十名角色全部由 Blender 脚本雕刻生成，语音与配乐由脚本批量产出。
`three.js` + 自写 `build.mjs` · 有 AI 自动对战测试与地图公平性统计 · [Play Online Live Demo](https://fable52.games/play/harvest-standoff) · [作者站](https://harvest-standoff.vercel.app)

---

## 五、值得收藏的社区合集

**Fable 5.2 视频与游戏案例合集** — [sandbase-lab/awesome-fable-5-2](https://github.com/sandbase-lab/awesome-fable-5-2) ⭐ 0
Three.js 场景、Canvas 动画、动效片段 + 提示词指南与模型对比，每天从 SandBase Lab 同步。

**22 款 Fable 游戏精选** — [ummydev/awesome-claude-fable-games](https://github.com/ummydev/awesome-claude-fable-games) ⭐ 3
带试玩链接、游戏截图、提示词和作者署名，每款在 vibegamer.io 上也有镜像。

**76 个 HTML 作品与完整提示词** — [MiaAI-Lab/Claude-Fable-5.2-HTML-Files](https://github.com/MiaAI-Lab/Claude-Fable-5.2-HTML-Files) ⭐ 109
76 个视觉小作品，每个都附截图和原始提示词，适合当「提示词语料库」翻。

## 六、技术栈速查表

表中的 🎮 可以直接点开玩；⌨️ 表示无在线版本，需按上方条目的说明在本地运行。

| 游戏 | 渲染 / 引擎 | 构建方式 | 交付形态 | 在线试玩 |
| --- | --- | --- | --- | :---: |
| FOG CITY | three.js | 无构建 | 多文件 ES module | ⌨️ |
| Dustfall | three.js 0.187 | Vite 8 | 站点 | [🎮 试玩](https://fable52.games/play/dustfall) |
| Bayhaven | three.js | Vite | 模块化站点 | [🎮 试玩](https://fable52.games/play/bayhaven) |
| Aquila | three.js | esbuild | 单文件 877 KB | ⌨️ |
| Dawnward | three.js | esbuild | 单文件 678 KB | ⌨️ |
| Ironvale | three.js r128 | 手写 HTML + 本地 lib | 单 HTML + 模型目录 + exe | [🎮 试玩](https://fable52.games/play/ironvale) |
| Saltline | three.js | 无 | 单文件 1.4 MB | [🎮 试玩](https://fable52.games/play/saltline-fable-5-2-fps) |
| 盐线行动 Online | three.js + WS | npm 打包 | Node 服务 | [🎮 试玩](https://fable52.games/play/saltline-online) |
| SUBLEVEL 07 | three.js | 无 | 单文件 131 KB | [🎮 试玩](https://fable52.games/play/sublevel-07-fps-repro) |
| BLAMELESS | three.js | npm 构建 | 站点 + Python 榜单 | [🎮 试玩](https://fable52.games/play/blameless) |
| Dustline Outpost | three.js r128 | 无 | HTML + game.js + assets | ⌨️ |
| Tidebell 潮钟 | three.js r170 | 无 | 单文件 | [🎮 试玩](https://fable52.games/play/tidebell) |
| MOTHLIGHT | three.js r170 | 无 | 单文件 | [🎮 试玩](https://fable52.games/play/mothlight) |
| 青云宗 · 御剑采灵 | three.js r170 | 无 | 单文件 | [🎮 试玩](https://fable52.games/play/qingyun-sword-flight) |
| MISREMEMBER | three.js r170 | 无 | 单文件 | [🎮 试玩](https://fable52.games/play/misremember) |
| Hanford Reach | three.js | Vite | 站点（Vercel） | [🎮 试玩](https://fable52.games/play/hanford-reach) |
| Boring Game | three.js | Vite + tsc | TypeScript 站点 | [🎮 试玩](https://fable52.games/play/boring-game-sf-bay-transit) |
| Soccer 3D | 自绘 + three.js | 无 | 单文件 + PWA | [🎮 试玩](https://fable52.games/play/pocket-soccer-3d) |
| TukTuk | three.js | 无 | 单文件 | [🎮 试玩](https://fable52.games/play/tuktuk) |
| Emberdeep | 原生 | 无 | 单文件 | [🎮 试玩](https://fable52.games/play/emberdeep) |
| Daedalus | 原生 | 无 | 单文件 121 KB | [🎮 试玩](https://fable52.games/play/daedalus) |
| Sternenjäger | 原生 | 无 | 单文件 | [🎮 试玩](https://fable52.games/play/sternenjaeger) |
| Shuttle Strike | three.js + 手部追踪 | 无 | 单文件 + CDN | [🎮 试玩](https://fable52.games/play/shuttle-strike) |
| NEON RUNNER | Canvas 2D | 无 | 单文件 | ⌨️ |
| Becario del Universo | 原生 | 无 | 单文件 | [🎮 试玩](https://fable52.games/play/becario-del-universo) |
| Harvest Standoff | three.js | 自写 build.mjs | dist 目录 | [🎮 试玩](https://fable52.games/play/harvest-standoff) |

完整的体积、依赖、素材来源、生成成本对照见 **[TECH_STACK.md](TECH_STACK.md)**。

## 七、这些游戏是怎么被写出来的

三个数字最能说明问题：

| 作品 | 输入 | 产出 | 折算成本 |
| --- | --- | --- | --- |
| Saltline | 1 句提示词，8 小时无人干预 | 完整 FPS，1.4 MB 单文件 | 约 $550（445M 输入 / 2.7M 输出 token） |
| SUBLEVEL 07 | 1 句提示词，73 轮，41 分钟 | 131 KB 单文件 FPS，含自动通关验证 | $15.96 |
| Boring Game | 15 条提示词，15 小时 | 66,000 行 TypeScript | 约 $700 |
| Ironvale | 21 句大白话 | 带科技树、五国、三部战役的 RTS | — |
| Tidebell 等四款 | 3 句需求 | 4 个可玩的 3D 游戏 + 一支宣传片 | — |

**可复现的提示词原文在 [PROMPTS.md](PROMPTS.md)**，包括那句被反复复刻的 `Build me a FPS. Insanely detailed quality pls...`、Ironvale 的 21 句迭代清单、以及 Tidebell 作者的三句需求。

## 参与贡献

发现漏掉的 Fable 5.2 作品？欢迎提 PR，只需按现有格式补充一行，或直接改 [`data/games.csv`](data/games.csv)：

- 必须是**能跑起来**的作品（在线可玩，或仓库里有明确启动方式）
- 必须给出**源码仓库**，不接受只有视频的条目
- 试玩链接请实测可访问，并在 PR 里说明抓取日期

## 说明

- 本仓库只做索引，不托管任何游戏代码，版权归各作者所有，请遵守各仓库的 LICENSE。
- 不少作品借鉴了 3A 游戏的玩法，但都是原创世界与原创命名，未使用原作素材；引用真实品牌或模型的项目已在各自 README 注明。
- 部分作品仍在开发中，完成度差异很大；「在线可玩」只代表能打开，不代表完成度。
- Star 数与可访问性为 2026-11-12 快照，会随时间变化。

## 附录：站上还有这 11 款

以下作品在试玩站上可以玩，但不在最初流传的那份 26 款清单里，一并列出：

| 作品 | 一句话 | 试玩 |
| --- | --- | --- |
| Evensong | 沉没大教堂里的一场决斗，浏览器里的魂类 demo | [Play](https://fable52.games/play/evensong) |
| What the Water Keeps | 提灯小船穿过一串截然不同的水域 | [Play](https://fable52.games/play/what-the-water-keeps) |
| 黑神话：悟空 · 虎先锋 | 同人 Boss 战，复刻虎先锋 | [Play](https://fable52.games/play/wukong-tiger-vanguard) |
| 雾锁山门 | 云海山门 3D 动作 demo | [Play](https://fable52.games/play/wusuo-shanmen) |
| 海克斯大乱斗 | 冰封大桥上的同人 ARAM 竞技场 | [Play](https://fable52.games/play/hextech-aram) |
| 运输船 3D | 经典地图团队死斗的浏览器复刻 | [Play](https://fable52.games/play/transport-ship-3d) |
| BREACH · 运输船联机大厅 | 运输船地图的多人联机大厅 | [Play](https://fable52.games/play/breach-transport-ship-online) |
| 几猫 CS | Saltline 的中文本地化改版 | [Play](https://fable52.games/play/jimao-cs) |
| 飞车 3D | 带漂移蓄力、氮气与道具赛的卡丁车 | [Play](https://fable52.games/play/feiche-3d) |
| 鹈鹕骑单车 | 戴头盔的鹈鹕沿海岸骑复古单车 | [Play](https://fable52.games/play/pelican-on-a-bike) |
| 暖光玩具房 · V25 | 温馨玩具房里的跑跳搬运平台 demo | [Play](https://fable52.games/play/warm-toy-room-v25) |

---

MIT License · 索引内容可自由转载，请保留各作品作者署名。
