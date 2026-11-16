# Awesome Fable 5.2 Games

**64 款游戏 · 51 个游戏仓库 · 3 份社区合集 · 45 款附浏览器试玩链接**

Fable 5.2 上线后，GitHub 上已经出现了一批不像「demo」的作品：能开车抢车被警察追的开放世界、骑马打猎的西部、能联机的港口 FPS、三国志式的 3D 即时战略、甚至单人用 21 句话写完的《帝国时代》替身。

这个仓库把它们整理成一份可检索的清单：**每款都有源码地址、玩法说明和真实技术栈；有在线试玩的附链接，没有试玩页的写清本地运行方式**。技术栈对比与 Prompt 原文各自独立成篇，方便你反推「什么样的提示词能做出这种东西」。

| 文档 | 内容 |
| --- | --- |
| [TECH_STACK.md](TECH_STACK.md) | 51 个仓库的技术栈、构建方式、交付体积、生成成本横向对比 |
| [PROMPTS.md](PROMPTS.md) | 可复现的原始提示词：一句话 FPS、21 句 RTS、三句需求做出三个游戏 |
| [data/games.csv](data/games.csv) | 结构化数据，方便二次加工或做站 |

> **核验说明**：原有 26 款数据抓取于 **2026-11-12**；《潮汐战线》和 5 款游戏于 **2026-11-14** 核验；**2026-11-16** 新增 32 款、23 个仓库，并更新已更名的 Last Return。新增条目的 Fable 5.2 依据来自作者 README 或 About，多模型协作作品在条目中注明；已测试本次新增和更新的 21 个试玩页面均返回 HTTP 200，未实际验证完整游玩流程。Star 数按各条目的抓取日期记录。
> 作品包含开发中游戏、交互体验与多人原型；没有浏览器试玩链接的 19 款，需按条目说明本地运行、构建或下载作者发布包。

## 图例

- 🎮 `[Play Online Live Demo]` —— 托管镜像，点开即玩，无需安装（[技术栈速查表](#六技术栈速查表)里的「🎮 试玩」同样可直接点）
- 🖥 作者自建站 / GitHub Pages —— 作者本人托管的版本，通常与源码同步更新
- ⌨️ 暂无浏览器试玩链接 —— 按条目说明起静态服务、构建程序，或使用作者提供的桌面版本
- ⭐ —— Star 数（日期见条目）

## 目录

- [一、开放世界与动作（9 款）](#一开放世界与动作9-款)
- [二、第一人称射击（8 款）](#二第一人称射击8-款)
- [三、视觉效果与探索（14 款）](#三视觉效果与探索14-款)
- [四、体育、竞速与其他（33 款）](#四体育竞速与其他33-款)
- [五、值得收藏的社区合集](#五值得收藏的社区合集)
- [六、技术栈速查表](#六技术栈速查表)
- [七、这些游戏是怎么被写出来的](#七这些游戏是怎么被写出来的)
- [附录：站上还有这 11 款](#附录站上还有这-11-款)

---

## 一、开放世界与动作（9 款）

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

**07 · The Long Climb** — 开放世界叙事 · [源码](https://github.com/HILAYTRIVEDI/thirty-days) ⭐ 1（2026-11-16）
围绕 NVIDIA 创业历程展开的三时期 3D 叙事游戏，包含经营抉择、对话和芯片布线小游戏；剧情为游戏演绎。
`three.js` · 无构建 · ⌨️ 暂无浏览器试玩链接，运行 `python3 -m http.server 8137` 后打开 <http://localhost:8137> · 作者说明使用 Fable 5.2

**08 · The Boondocks: The Woodcrest Files** — 2D 动作 · [源码](https://github.com/Achraf921/boondocks) ⭐ 0（2026-11-16）
非官方同人清版动作游戏，以街区为据点推进五个任务；支持连招、格挡、弹反与手柄。
`原生 JavaScript` · 无构建 · ⌨️ 暂无浏览器试玩链接，打开 `index.html`；或运行 `python3 -m http.server 8765` · 作者说明使用 Fable 5.2

**09 · Duel Knights** — 3D 动作 · [源码](https://github.com/bitofastickler/duel-knights) ⭐ 0（2026-11-16）
在庭院或山顶回廊里进行三局制骑士决斗，选择角色、武器和对手，通过闪避、佯攻与弹反获胜。
`three.js` · 无构建 · [在线试玩](https://bitofastickler.github.io/duel-knights/) · 源自 Fable 5.2 的 Ashen Crown，后续扩展见作者 Origin 说明

## 二、第一人称射击（8 款）

**10 · Saltline** — 3D 港口 FPS · [源码](https://github.com/realcodebear/saltline-fable-5.2) ⭐ 230
整条链路的起点：Anthropic 的 Felix Rieseberg 一句提示词、无人干预 8 小时跑出来的雨夜集装箱码头，切断三个中继站，躲开机群「Gulls」和机械狗「Hounds」。
`three.js` 内联 · **单文件 1.4 MB** · 模型、音效、贴图全部代码生成 · [Play Online Live Demo](https://fable52.games/play/saltline-fable-5-2-fps) · [作者站](https://realcodebear.github.io/saltline-fable-5.2/)

**11 · 盐线行动 Online** — 港口 FPS 联机版 · [源码](https://github.com/wenzhengshi/fable5-2-salt-online) ⭐ 16
在 Saltline 基础上扩出多人对战：5 秒复活、房间大厅、本地排行榜落盘，无数据库，单机 `node server.js` 就能开局。
`Node.js + Express + WebSocket + three.js` · 前后端同一仓库 · [Play Online Live Demo](https://fable52.games/play/saltline-online)

**12 · SUBLEVEL 07** — 科幻地下变电站 FPS · [源码](https://github.com/wquguru/fable52-fps-repro) ⭐ 78
中文社区里最能「抄作业」的一份：一句提示词、73 轮无人干预、41 分钟，产出 **131 KB 单文件**，潮湿地面实时反射、红点卡宾枪、三波悬浮无人机、18 个合成音效，AI 自己写脚本打通关验证零报错。仓库同时公开提示词原文与逐轮 token 账单。
`单文件 HTML` · 体积极小但含后处理 · [Play Online Live Demo](https://fable52.games/play/sublevel-07-fps-repro) · [作者站](https://wquguru.github.io/fable52-fps-repro/)

**13 · BLAMELESS** — 程序员主题 FPS · [源码](https://github.com/Petyok/blameless) ⭐ 0
凌晨 3:07 告警响了：你 `kubectl exec` 进生产环境，用 `kill -9`、`grep -r`、`rm -rf` 当武器，清掉十个故障、四台主机、一个根因。没有弹药，只有限流（打太久返回 429），血量就是错误预算，死后写复盘。
`three.js` + npm 构建 · Python 标准库排行榜服务 · 确定性模拟可在 Node 里跑端测 · [Play Online Live Demo](https://fable52.games/play/blameless) · [作者站](https://blameless.petruha.ge/)

**14 · Dustline Outpost** — 时间循环 FPS · [源码](https://github.com/systemsluke/fable5.2game) ⭐ 1
每道闪电把世界倒回 70 秒，你上一轮的自己被留下成一个半透明「回声」，按原样重放每一枪。三个中继站相距太远，只能靠不同轮次的自己配合占领——一共六次机会。
`three.js r128` · 无构建 · 回声按 20 Hz 记录并从**当前**世界重发射线 · Poly Haven CC0 扫描素材 · ⌨️ 暂无在线版本，需静态服务且首屏拉 41 MB 资源

**15 · Last Return（原 No Return）** — LiDAR 点云恐怖游戏 · [源码](https://github.com/StefanKnol/Last-Return) ⭐ 1（2026-11-16）
在全黑的地下泵房里寻找三卷测绘资料；手持扫描仪照出的点云会留在原地，停下扫描就看不见周围的东西。
`WebGL 2 + JavaScript` · [在线试玩](https://last-return.sknol.com/) · 源码已拆分，`npm run build` 生成单文件 `index.html`；原仓库地址已重定向至此

**16 · Riftline** — 3D 第一人称英雄射击 · [源码](https://github.com/wongh26/claude_fps) ⭐ 0
用 Vesper 的双枪、瞬移和回溯技能打机器人或与朋友联机对决；支持 PeerJS 点对点联机。
`three.js r160 + PeerJS` · 无构建 · ⌨️ 暂无在线版本，运行 `python3 -m http.server 8000` 后打开本地地址

**17 · Graveyard Shift** — FPS · [源码](https://github.com/ethanplusai/zombies) ⭐ 9（2026-11-16）
在路边餐馆与加油站抵御逐轮增强的僵尸，修窗、搜刮、购买武器并恢复供电；支持桌面与触屏。
`three.js / WebGL 2` · esbuild · [在线试玩](https://zombies.ethanplus.ai) · 作者说明使用 Fable 5.2

## 三、视觉效果与探索（14 款）

**18 · Tidebell 潮钟** — 3D 水下探索 · [源码](https://github.com/hahaliu1029/fable5.2demo) ⭐ 0
驾驶小潜水器从阳光照透的珊瑚礁一路下潜到深渊，唤醒七口沉睡的潮钟。48 个模型全部由 Blender 里的 Python 脚本生成，手写水下光照：红色最先随深度消失，开灯才把颜色找回来。
`three.js r170` · 单文件 `index.html` · 18,000 个海底实例，鱼群动画跑在顶点着色器里 · [Play Online Live Demo](https://fable52.games/play/tidebell)

**19 · MOTHLIGHT // Vesper-9** — 赛博朋克城市驾驶 · [源码](https://github.com/hahaliu1029/fable5.2demo) ⭐ 0
雨夜霓虹城里穿 12 道光门，手刹漂移、加速带、单轨列车与全息飞蛾；9×9 街区 694 栋楼一次实例化绘制，窗户画出带纵深的房间。
`three.js r170` · 单文件 · 湿街道镜面反射与实时环境贴图 · [Play Online Live Demo](https://fable52.games/play/mothlight)

**20 · 青云宗 · 御剑采灵** — 3D 仙侠 · [源码](https://github.com/hahaliu1029/fable5.2demo) ⭐ 0
第三人称御剑飞行，在体积云海、浮岩和真实反射的湖面之间收集 20 颗灵气，点亮山门牌匾后穿门通关；水墨标题、飞剑光带、解锁金光柱。
`three.js r170` · 单文件 · 支持触屏；自驾驶脚本可完整通关并录回放 · [Play Online Live Demo](https://fable52.games/play/qingyun-sword-flight)

**21 · MISREMEMBER** — 第一人称心理恐怖 · [源码](https://github.com/hahaliu1029/fable5.2demo) ⭐ 0
有什么东西按你的记忆重建了童年的家，而记忆并不可靠：你盯着的东西永远不变，变化只发生在你身后。房间靠门洞模板遮罩拼接，同一扇门下次打开可能通向别处。
`three.js` · 单文件 · 变化排队等离开视野才落地；贴图由 Codex 生成（仓库只放 WebP）· [Play Online Live Demo](https://fable52.games/play/misremember)

**22 · Hanford Reach** — 小镇探索与定居点建设 · [源码](https://github.com/chzbloom123/settlement-bluff-fable5.2) ⭐ 0
哥伦比亚河畔小镇废墟上的慢节奏建造游戏，第一人称与第三人称随时切换，带质量档位、性能报表和一键渲染 14 个固定机位的对比截图脚本。
`three.js + Vite` · Vercel 自动部署，每个 PR 有独立预览 · [Play Online Live Demo](https://fable52.games/play/hanford-reach) · [作者站](https://settlement-bluff-fable52.vercel.app)

**23 · Boring Game** — 湾区体素世界 · [源码](https://github.com/jakozaur/sf_bay_area_transit_fable_5_2_game) ⭐ 0
用真实地图数据重建旧金山湾区体素地形，规划线路、挖隧道、建车站，把列车开到作者公司楼下。15 条提示词、15 小时、66,000 行、约 $700。
`TypeScript + Vite` · typecheck + Biome + Vitest + 基准测试 · [Play Online Live Demo](https://fable52.games/play/boring-game-sf-bay-transit) · [作者站](https://jakozaur.github.io/sf_bay_area_transit_fable_5_2_game/)

**24 · SHUTTERPINE** — 叙事恐怖 · [源码](https://github.com/DQuanBui/shutterpine) ⭐ 0（2026-11-16）
沿失踪摄影师的山林足迹寻找线索，复拍旧照片；相机能看见并阻止追踪者，山顶选择通向两个结局。
`three.js` · Vite · [在线试玩](https://dquanbui.github.io/shutterpine/) · 作者说明使用 Fable 5.2

**25 · Power the Spire** — 3D 收集探索 · [源码](https://github.com/cdurgun/claude-fable-3d-world) ⭐ 0（2026-11-16）
在程序化漂浮岛城市里驾车收集八颗能量球，点亮中央尖塔；与同仓库的自动镜头场景共享世界。
`three.js 0.187` · 无构建 · ⌨️ 暂无浏览器试玩链接，运行 `npm install && npm start` 后打开 <http://127.0.0.1:4173/game/index.html> · 作者说明使用 Fable 5.2

**26 · Tropical Island** — 海岛探索 · [源码](https://github.com/Tarzno/tropical_island) ⭐ 0（2026-11-16）
在塞舌尔风格海岛步行、游泳、潜水和拍照，观察植物、动物、日月与潮汐；没有战斗目标。
`Godot 4.7.2` · Godot · ⌨️ 暂无浏览器试玩链接，用 Godot 4.7.2 打开项目后运行；[macOS 构建](https://github.com/Tarzno/tropical_island/releases) · Opus 5.5 初始实现，Fable 5.2 进行后续实质扩展

**27 · CASCADE** — 自然灾害体验 · [源码](https://github.com/Prokopiy8247/Fable5-2-Natural-Disasters) ⭐ 1（2026-11-16）
第一人称观测火山喷发、山体坍塌与海啸的自然灾害体验。作者提供约 11 分钟的流程与可切换的自动镜头模式。
`Unity HDRP` · Unity 6000.6.0f1 · ⌨️ 暂无浏览器试玩链接，拉取 Git LFS 文件后运行 `START_HERE.bat`；或 `games/01-cascade/PLAY.bat` · 作者说明使用 Fable 5.2

**28 · MESOCYCLONE** — 自然灾害体验 · [源码](https://github.com/Prokopiy8247/Fable5-2-Natural-Disasters) ⭐ 1（2026-11-16）
第一人称观测超级单体雷暴、冰雹与龙卷风的自然灾害体验。作者提供约 11 分钟的流程与可切换的自动镜头模式。
`Unity HDRP` · Unity 6000.6.0f1 · ⌨️ 暂无浏览器试玩链接，拉取 Git LFS 文件后运行 `START_HERE.bat`；或 `games/02-mesocyclone/PLAY.bat` · 作者说明使用 Fable 5.2

**29 · ZERO** — 自然灾害体验 · [源码](https://github.com/Prokopiy8247/Fable5-2-Natural-Disasters) ⭐ 1（2026-11-16）
第一人称观测小行星撞击与冲击波的自然灾害体验。作者提供约 11 分钟的流程与可切换的自动镜头模式。
`Unity URP` · Unity 6000.6.0f1 · ⌨️ 暂无浏览器试玩链接，拉取 Git LFS 文件后运行 `START_HERE.bat`；或 `games/03-zero/PLAY.bat` · 作者说明使用 Fable 5.2

**30 · OUT OF REACH** — 太空生存 · [源码](https://github.com/alex-slovakia/out-of-reach) ⭐ 1（2026-11-16）
为 NASA Space Apps 制作的第一人称太空生存游戏，先设计任务，再管理飞船资源并应对零重力环境。
`Unity URP` · Unity 6000.3.28f1 · ⌨️ 暂无浏览器试玩链接，拉取 Git LFS 文件后用 Unity 6000.3.28f1 打开 `Assets/_OutOfReach/Scenes/Bootstrap.unity`；[Windows 成品](https://github.com/alex-slovakia/out-of-reach/releases/tag/spaceapps-2026-final) · 作者披露 Fable 5.2、Opus / Sonnet 5.5 与 Codex 协作

**31 · うしろのハニワ** — 第一人称解谜 · [源码](https://github.com/shioa2006-game/ONE_PROMPT_WORLDS) ⭐ 0（2026-11-16）
在古坟石室逐格移动，用视线控制背后靠近的埴轮，把它们引到对应台座；支持撤销。
`原生 JavaScript` · 无构建 · [在线试玩](https://shioa2006-game.github.io/ONE_PROMPT_WORLDS/game6/index.html) · ONE PROMPT WORLDS 第 1–8 作，作者标注为 Fable 5.2

## 四、体育、竞速与其他（33 款）

**32 · Soccer 3D** — 7 人制 3D 足球 · [源码](https://github.com/ShaunPrice/soccer-3d) ⭐ 0
有裁判、越位、红黄牌、点球与人墙、伤停补时和平局点球大战；阵型/心态/逼抢三档战术，体力、受伤、三个换人名额，进球慢镜回放，八级难度。
`单文件 HTML` · PWA 可装到手机主屏、离线可玩 · 音效与解说由 ElevenLabs 生成 · [Play Online Live Demo](https://fable52.games/play/pocket-soccer-3d) · [作者站](https://shaunprice.github.io/soccer-3d/)

**33 · TukTuk** — 埃及街头驾驶 · [源码](https://github.com/basemazab/tuktuk) ⭐ 0
在挤满小巴、出租和西瓜车的开罗街道里钻缝拉客，收车费、躲路障。所有形状、材质、音效都由代码生成，仓库里没有一张图片、一个音频文件。
`three.js` · `game.js` + `index.html` 两个文件 · [Play Online Live Demo](https://fable52.games/play/tuktuk) · [作者站](https://basemazab.github.io/tuktuk/)

**34 · Emberdeep** — 浏览器冒险 · [源码](https://github.com/DNDNoob/EmberDeep) ⭐ 0
火把在烧，往下走。单文件地牢下潜，约 100 KB。
`单文件 HTML` · [Play Online Live Demo](https://fable52.games/play/emberdeep) · [作者站](https://dndnoob.github.io/EmberDeep/)

**35 · Daedalus** — 古希腊神话解谜 · [源码](https://github.com/S77FFY/daedalus) ⭐ 1
以代达罗斯迷宫为题的谜题游戏，121 KB 单文件。
`单文件 HTML` · [Play Online Live Demo](https://fable52.games/play/daedalus) · [作者站](https://s77ffy.github.io/daedalus/)

**36 · Sternenjäger** — 科幻太空射击 · [源码](https://github.com/oldzitterhand/sternenjaeger) ⭐ 0
12 个星区、3 场 Boss 战，飞船自动开火，玩家只管飞位与 EMP；手机、键盘、手柄三种操作都支持。
`单文件 HTML` · 无构建无服务 · [Play Online Live Demo](https://fable52.games/play/sternenjaeger) · [作者站](https://oldzitterhand.github.io/sternenjaeger/)

**37 · Shuttle Strike** — 第一人称羽毛球 · [源码](https://github.com/fedifianto/shuttlestrike) ⭐ 0
用摄像头追踪手部：握拳即握拍，挥快球杀球，拍面高低决定挑高或吊球；张开手掌停住是暂停。没摄像头可切鼠标模式。
`单文件 HTML` + CDN 手部追踪 · 需 HTTPS 或 localhost 才能开摄像头 · [Play Online Live Demo](https://fable52.games/play/shuttle-strike) · [作者站](https://fedifianto.github.io/shuttlestrike/)

**38 · NEON RUNNER** — 赛博朋克 2D 跑酷 · [源码](https://github.com/Ilias-AK/NewGameFromFable5.2) ⭐ 0
霓虹城市无尽跑酷，障碍按「与玩家相遇的时间」生成，因此难度提升不会压缩反应窗口；三档难度、护盾与磁铁道具、每 500 米记速、Top-5 本地存档。
`单文件 HTML` · Canvas 2D + Web Audio + LocalStorage，零外部资源 · ⌨️ 暂无在线版本，双击 `index.html` 即可

**39 · Becario del Universo** — 宇宙主题小游戏 · [源码](https://github.com/masugus/fable5.2-5min-game) ⭐ 0
「宇宙最新实习生」的琐碎任务合集，桌面与手机同一份代码，5 分钟能玩完一局，最高分存在浏览器里。
`单文件 HTML` · [Play Online Live Demo](https://fable52.games/play/becario-del-universo) · [作者站](https://masugus.github.io/fable5.2-5min-game/)

**40 · Harvest Standoff** — 农场 5v5 团队竞技 · [源码](https://github.com/andreteow/farm-ca) ⭐ 0
动物对农场工人，回合制 5v5，有商店、金币、中场与「臭南瓜」；十名角色全部由 Blender 脚本雕刻生成，语音与配乐由脚本批量产出。
`three.js` + 自写 `build.mjs` · 有 AI 自动对战测试与地图公平性统计 · [Play Online Live Demo](https://fable52.games/play/harvest-standoff) · [作者站](https://harvest-standoff.vercel.app)

**41 · 潮汐战线（Tidemark）** — 《高级战争》式回合制战棋 · [源码](https://github.com/CocoSgt/dsh-game-tidemark) ⭐ 12（2026-11-14）
陆海空 33 个兵种、29 位指挥官和 27 关战役；纯前端、多文件 HTML/JavaScript，无需构建，支持本地打开游玩。
`HTML Canvas + JavaScript` · [在线试玩](https://dsh-game-store.com/games/tidemark/) · [游戏手册](https://dsh-game-store.com/games/tidemark/manual/)

**42 · The County** — 土豆农场经营策略 · [源码](https://github.com/TheMizeGuy/fable-5.2-potatobench) ⭐ 1（2026-11-14）
从六块田和一名农夫起步，安排种植、收获、雇工、扩地和订单；作物长在地下，得等收成时才知道结果。
`TypeScript + three.js + Vite` · [Play Online Live Demo](https://themizeguy.github.io/fable-5.2-potatobench/)

**43 · MAKINAMON · Versión Pulso** — Game Boy Color 风格像素怪物 RPG · [源码](https://github.com/gavilanbe/makinamon-pulso) ⭐ 0（2026-11-14）
在 10 个章节里收集并培养 50 种机器生物，挑战 6 名中央设施首领；50 种攻击各有动画与音效。
`Canvas 2D + JavaScript` · [Play Online Live Demo](https://gavilanbe.github.io/makinamon-pulso/)

**44 · SUPERFORGE GT** — SNES 赛车生涯游戏 · [源码](https://github.com/jreinach-alt/sf-gt) ⭐ 0（2026-11-14）
买车、跑 12 场赛事、用奖金改装；8 台车、6 条 Mode 7 赛道和 9 名对手，最终构建为 4 MB SNES ROM。
`65C816 Assembly + Python` · 按 README 在 Linux 上构建，再用 SNES 模拟器运行

**45 · FableFlight** — 飞行模拟 · [源码](https://github.com/Rolandjg/fableflight) ⭐ 213（2026-11-16）
Rust 编写的开放世界飞行模拟器，提供实时天气、真实空中交通、燃油与配重、无线电导航和可绑定的飞行外设。
`wgpu + egui` · Cargo · ⌨️ 暂无浏览器试玩链接，安装 Rust 后运行 `cargo run --release` · 作者披露由 Fable 5.2 与 Opus 5.5 协作制作

**46 · Liquid Labyrinth** — 物理解谜 · [源码](https://github.com/tuki0918/maze-exit) ⭐ 0（2026-11-16）
旋转 3D 迷宫，让液体在重力作用下流向出口；可通过带种子参数的 URL 分享同一迷宫。
`three.js 0.187` · Vite + TypeScript · [在线试玩](https://maze.bbbit.cc) · 仓库 About 标注为 Fable 5.2 sample game

**47 · Mini RPG** — RPG · [源码](https://github.com/ertertwert/Mini-RPG) ⭐ 0（2026-11-16）
浏览器角色扮演游戏，支持为战斗、地牢和高塔等主题替换配乐；音乐来源见作者 README。
`原生 JavaScript` · 无构建 · [在线试玩](https://ertertwert.com/MiniRPG.html) · 作者说明使用 Fable 5.2

**48 · Rufus Crush** — 三消 · [源码](https://github.com/bhoult/phone-games) ⭐ 0（2026-11-16）
围绕黑色拉布拉多 Rufus 日常生活的三消游戏，含 36 关、三档难度和特殊棋子；首次加载后可离线。
`macroquad / WebGL` · Rust → WebAssembly · [在线试玩](https://bhoult.github.io/phone-games/rufus-crush/) · 作者说明使用 Fable 5.2

**49 · ぽん、と森は灯る** — 物理探索 · [源码](https://github.com/shioa2006-game/ONE_PROMPT_WORLDS) ⭐ 0（2026-11-16）
弹射孢子长出蘑菇，把新蘑菇作为下一座发射台，逐步照亮森林并抵达深处大树。
`原生 JavaScript` · 无构建 · [在线试玩](https://shioa2006-game.github.io/ONE_PROMPT_WORLDS/game/index.html) · ONE PROMPT WORLDS 第 1–8 作，作者标注为 Fable 5.2

**50 · ひとつぶ庭園** — 粒子解谜 · [源码](https://github.com/shioa2006-game/ONE_PROMPT_WORLDS) ⭐ 0（2026-11-16）
把砂、水、种子与火种倒进瓶子，利用粒子相互反应培育小小的夜间花园。
`原生 JavaScript` · 无构建 · [在线试玩](https://shioa2006-game.github.io/ONE_PROMPT_WORLDS/game2/index.html) · ONE PROMPT WORLDS 第 1–8 作，作者标注为 Fable 5.2

**51 · EMBERDEEP ― 燈守りの坑道** — 动作 RPG · [源码](https://github.com/shioa2006-game/ONE_PROMPT_WORLDS) ⭐ 0（2026-11-16）
提灯深入矿道，点燃火盆、与暗影战斗，逐区驱散黑暗并抵达最深处炉心。
`原生 JavaScript` · 无构建 · [在线试玩](https://shioa2006-game.github.io/ONE_PROMPT_WORLDS/game3/index.html) · ONE PROMPT WORLDS 第 1–8 作，作者标注为 Fable 5.2

**52 · LUMEN REEL ― まわる灯台と三つの海路** — 转轮解谜 · [源码](https://github.com/shioa2006-game/ONE_PROMPT_WORLDS) ⭐ 0（2026-11-16）
转动灯塔卷轴为航路送光，重组卷轴零件，越过五个夜晚把迷航船只送回港口。
`原生 JavaScript` · 无构建 · [在线试玩](https://shioa2006-game.github.io/ONE_PROMPT_WORLDS/game4/index.html) · ONE PROMPT WORLDS 第 1–8 作，作者标注为 Fable 5.2

**53 · REEL DELVE ― まわる迷宮と三人の旅** — 地牢解谜 · [源码](https://github.com/shioa2006-game/ONE_PROMPT_WORLDS) ⭐ 0（2026-11-16）
选择时机停下卷轴，三行符号构成三位冒险者的通路，逐步探索十二层地下迷宫。
`原生 JavaScript` · 无构建 · [在线试玩](https://shioa2006-game.github.io/ONE_PROMPT_WORLDS/game5/index.html) · ONE PROMPT WORLDS 第 1–8 作，作者标注为 Fable 5.2

**54 · 切りもどし ― 鋏と春の小さな鉢** — 盆栽解谜 · [源码](https://github.com/shioa2006-game/ONE_PROMPT_WORLDS) ⭐ 0（2026-11-16）
修剪枝条并让春天催生新芽，以分枝规则控制盆栽形状并使花朵开放。
`原生 JavaScript` · 无构建 · [在线试玩](https://shioa2006-game.github.io/ONE_PROMPT_WORLDS/game7/index.html) · ONE PROMPT WORLDS 第 1–8 作，作者标注为 Fable 5.2

**55 · ひつじが いっぴき ― 牧羊犬コロの一日** — 牧羊动作 · [源码](https://github.com/shioa2006-game/ONE_PROMPT_WORLDS) ⭐ 0（2026-11-16）
操纵牧羊犬把羊群送进小屋，利用步行聚拢、奔跑驱散的差异走过九座牧场。
`原生 JavaScript` · 无构建 · [在线试玩](https://shioa2006-game.github.io/ONE_PROMPT_WORLDS/game8/index.html) · ONE PROMPT WORLDS 第 1–8 作，作者标注为 Fable 5.2

**56 · MAPLE RUN** — 3D 跑酷 · [源码](https://github.com/nanha0130/maple-run-fable) ⭐ 0（2026-11-16）
在红叶季乡间铁路上三轨奔跑，躲避火车与障碍、收集金叶；支持键盘与触屏，需要 WebGPU。
`PlayCanvas + Splat Engine / WebGPU` · Vite · [在线试玩](https://maple-run-fable.vercel.app) · 作者说明使用 Fable 5.2

**57 · Escape the Fable** — 密室解谜 · [源码](https://github.com/ai-gamez-r-funz/escape-the-fable) ⭐ 0（2026-11-16）
生成可解的二十世纪风格密室，使用钥匙、密码盘和家具暗格逃脱；内置关卡工作坊与链接分享。
`three.js` · 无构建 · ⌨️ 暂无浏览器试玩链接，运行 `npm start` 后打开 <http://localhost:8080> · 作者说明使用 Fable 5.2

**58 · Circular Tic Tac Toe** — 棋盘 · [源码](https://github.com/muhammad-sayed-mahdy/circular-tic-tac-toe-web) ⭐ 0（2026-11-16）
在四环八辐的环形棋盘上连成四子，支持双人、不同难度 AI、提示、撤销与主题切换。
`SVG + JavaScript` · 无构建 · [在线试玩](https://muhammad-sayed-mahdy.github.io/circular-tic-tac-toe-web/) · 作者说明使用 Fable 5.2

**59 · EarthFM · Listening Game** — 听音辨识 · [源码](https://github.com/Aarosunn/SpaceApps) ⭐ 0（2026-11-16）
NASA 地球数据音乐化项目中的四轮听音小游戏，依据声化数据作答；游戏入口位于 /play。
`Next.js + React + Tone.js` · Next.js · [在线试玩](https://earthfm.vercel.app/play) · 作者 AI use 披露 Fable 5.2 与其他 Claude 模型协作

**60 · T-Minus** — 多人任务规划 · [源码](https://github.com/XDracam/spaceappschallenge2026) ⭐ 0（2026-11-16）
玩家分别操作任务规划、采购、科学和通信工位，协作完成气象卫星或火星轨道器加着陆器任务。
`Preact + PeerJS / WebRTC` · Vite + TypeScript · [在线试玩](https://missioncontrol.dractec.com/) · 作者披露 Fable 5.2、Opus 5.5 与 Sonnet 5.5 协作

**61 · Jester** — 摄像头派对 · [源码](https://github.com/aaron-sulbaran/jester) ⭐ 0（2026-11-16）
玩家用摄像头模仿短片里不同角色的动作，浏览器姿态模型计分并把玩家剪影合成到片段中；推荐桌面 Chrome / Edge。
`MediaPipe + three.js` · Vite + TypeScript（Make） · [在线试玩](https://jester-pi.vercel.app) · 作者披露 Fable 5.2、Opus 5.5 与 Sonnet 5.5 协作

**62 · Retro Sisters** — 2D 平台跳跃 · [源码](https://github.com/rob0511-777/Retro-Sisters) ⭐ 0（2026-11-16）
C64 风格原创平台跳跃游戏，使用程序化像素美术与 SID 风格音乐；Fable 5.2 负责画面改造。
`Canvas + SID 音频` · 无构建 · ⌨️ 暂无浏览器试玩链接，打开 `index.html`；或运行 `python3 -m http.server 8000` · 多模型协作；Fable 5.2 负责像素美术、动画与视差背景

**63 · Rawza Ring** — 3D 竞速 · [源码](https://github.com/Hashmatullahzaher/mazar-rawza-race) ⭐ 0（2026-11-16）
围绕马扎里沙里夫圣陵附近真实街道进行赛车，支持漂移、检查点与触屏；手机界面等功能由作者后续补充。
`three.js` · 无构建 · [在线试玩](https://hashmatullahzaher.github.io/mazar-rawza-race/) · 作者说明使用 Fable 5.2

**64 · Gifts for the Tall One** — 猫咪收集探索 · [源码](https://github.com/eyeb0l/catslop) ⭐ 0（2026-11-16）
扮演小岛上的猫，潜行捕猎并带回家换零食，购买装备、毛色和帽子；同仓库其他模型的运行不计入本条。
`three.js` · 无构建 · ⌨️ 暂无浏览器试玩链接，运行 `npm run serve` 后打开 `/runs/claude-fable-5-2/` · README 与 runs/claude-fable-5-2/NOTES.md 标明模型；这是作者的演示运行

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
| The Long Climb | three.js | 无构建 | 多文件静态站点 | ⌨️ |
| The Boondocks: The Woodcrest Files | 原生 JavaScript | 无构建 | 多文件静态站点 | ⌨️ |
| Duel Knights | three.js | 无构建 | 多文件静态站点 | [🎮 试玩](https://bitofastickler.github.io/duel-knights/) |
| Saltline | three.js | 无 | 单文件 1.4 MB | [🎮 试玩](https://fable52.games/play/saltline-fable-5-2-fps) |
| 盐线行动 Online | three.js + WS | npm 打包 | Node 服务 | [🎮 试玩](https://fable52.games/play/saltline-online) |
| SUBLEVEL 07 | three.js | 无 | 单文件 131 KB | [🎮 试玩](https://fable52.games/play/sublevel-07-fps-repro) |
| BLAMELESS | three.js | npm 构建 | 站点 + Python 榜单 | [🎮 试玩](https://fable52.games/play/blameless) |
| Dustline Outpost | three.js r128 | 无 | HTML + game.js + assets | ⌨️ |
| Last Return（原 No Return） | WebGL 2 | Node.js 自写构建 | 单文件 index.html | [🎮 试玩](https://last-return.sknol.com/) |
| Riftline | three.js r160 + PeerJS | 无构建 | 多文件静态站点 | ⌨️ |
| Graveyard Shift | three.js / WebGL 2 | esbuild | 单文件 dist/index.html；可选 Worker + D1 | [🎮 试玩](https://zombies.ethanplus.ai) |
| Tidebell 潮钟 | three.js r170 | 无 | 单文件 | [🎮 试玩](https://fable52.games/play/tidebell) |
| MOTHLIGHT | three.js r170 | 无 | 单文件 | [🎮 试玩](https://fable52.games/play/mothlight) |
| 青云宗 · 御剑采灵 | three.js r170 | 无 | 单文件 | [🎮 试玩](https://fable52.games/play/qingyun-sword-flight) |
| MISREMEMBER | three.js r170 | 无 | 单文件 | [🎮 试玩](https://fable52.games/play/misremember) |
| Hanford Reach | three.js | Vite | 站点（Vercel） | [🎮 试玩](https://fable52.games/play/hanford-reach) |
| Boring Game | three.js | Vite + tsc | TypeScript 站点 | [🎮 试玩](https://fable52.games/play/boring-game-sf-bay-transit) |
| SHUTTERPINE | three.js | Vite | 浏览器站点 dist/ | [🎮 试玩](https://dquanbui.github.io/shutterpine/) |
| Power the Spire | three.js 0.187 | 无构建 | 多文件静态站点 | ⌨️ |
| Tropical Island | Godot 4.7.2 | Godot | macOS 应用 / Godot 源码项目 | ⌨️ |
| CASCADE | Unity HDRP | Unity 6000.6.0f1 | Windows 构建 + Unity 源码（Git LFS） | ⌨️ |
| MESOCYCLONE | Unity HDRP | Unity 6000.6.0f1 | Windows 构建 + Unity 源码（Git LFS） | ⌨️ |
| ZERO | Unity URP | Unity 6000.6.0f1 | Windows 构建 + Unity 源码（Git LFS） | ⌨️ |
| OUT OF REACH | Unity URP | Unity 6000.3.28f1 | Windows 程序 / Unity 源码项目 | ⌨️ |
| うしろのハニワ | 原生 JavaScript | 无构建 | 多文件静态站点 | [🎮 试玩](https://shioa2006-game.github.io/ONE_PROMPT_WORLDS/game6/index.html) |
| Soccer 3D | 自绘 + three.js | 无 | 单文件 + PWA | [🎮 试玩](https://fable52.games/play/pocket-soccer-3d) |
| TukTuk | three.js | 无 | 单文件 | [🎮 试玩](https://fable52.games/play/tuktuk) |
| Emberdeep | 原生 | 无 | 单文件 | [🎮 试玩](https://fable52.games/play/emberdeep) |
| Daedalus | 原生 | 无 | 单文件 121 KB | [🎮 试玩](https://fable52.games/play/daedalus) |
| Sternenjäger | 原生 | 无 | 单文件 | [🎮 试玩](https://fable52.games/play/sternenjaeger) |
| Shuttle Strike | three.js + 手部追踪 | 无 | 单文件 + CDN | [🎮 试玩](https://fable52.games/play/shuttle-strike) |
| NEON RUNNER | Canvas 2D | 无 | 单文件 | ⌨️ |
| Becario del Universo | 原生 | 无 | 单文件 | [🎮 试玩](https://fable52.games/play/becario-del-universo) |
| Harvest Standoff | three.js | 自写 build.mjs | dist 目录 | [🎮 试玩](https://fable52.games/play/harvest-standoff) |
| 潮汐战线（Tidemark） | HTML Canvas | 无构建 | 多文件 HTML + JavaScript | [🎮 试玩](https://dsh-game-store.com/games/tidemark/) |
| The County | three.js + Vite | Vite + TypeScript | 浏览器站点 | [🎮 试玩](https://themizeguy.github.io/fable-5.2-potatobench/) |
| MAKINAMON | Canvas 2D | 无构建 | 多文件 HTML + JavaScript | [🎮 试玩](https://gavilanbe.github.io/makinamon-pulso/) |
| SUPERFORGE GT | SNES Mode 7 | Make + ca65/ld65 | 4 MB `.sfc` ROM | ⌨️ |
| FableFlight | wgpu + egui | Cargo | Rust 原生桌面程序 | ⌨️ |
| Liquid Labyrinth | three.js 0.187 | Vite + TypeScript | 浏览器站点 dist/ | [🎮 试玩](https://maze.bbbit.cc) |
| Mini RPG | 原生 JavaScript | 无构建 | 多文件静态站点 | [🎮 试玩](https://ertertwert.com/MiniRPG.html) |
| Rufus Crush | macroquad / WebGL | Rust → WebAssembly | 静态 WASM 站点；另有 Android WebView 构建 | [🎮 试玩](https://bhoult.github.io/phone-games/rufus-crush/) |
| ぽん、と森は灯る | 原生 JavaScript | 无构建 | 多文件静态站点 | [🎮 试玩](https://shioa2006-game.github.io/ONE_PROMPT_WORLDS/game/index.html) |
| ひとつぶ庭園 | 原生 JavaScript | 无构建 | 多文件静态站点 | [🎮 试玩](https://shioa2006-game.github.io/ONE_PROMPT_WORLDS/game2/index.html) |
| EMBERDEEP ― 燈守りの坑道 | 原生 JavaScript | 无构建 | 多文件静态站点 | [🎮 试玩](https://shioa2006-game.github.io/ONE_PROMPT_WORLDS/game3/index.html) |
| LUMEN REEL ― まわる灯台と三つの海路 | 原生 JavaScript | 无构建 | 多文件静态站点 | [🎮 试玩](https://shioa2006-game.github.io/ONE_PROMPT_WORLDS/game4/index.html) |
| REEL DELVE ― まわる迷宮と三人の旅 | 原生 JavaScript | 无构建 | 多文件静态站点 | [🎮 试玩](https://shioa2006-game.github.io/ONE_PROMPT_WORLDS/game5/index.html) |
| 切りもどし ― 鋏と春の小さな鉢 | 原生 JavaScript | 无构建 | 多文件静态站点 | [🎮 试玩](https://shioa2006-game.github.io/ONE_PROMPT_WORLDS/game7/index.html) |
| ひつじが いっぴき ― 牧羊犬コロの一日 | 原生 JavaScript | 无构建 | 多文件静态站点 | [🎮 试玩](https://shioa2006-game.github.io/ONE_PROMPT_WORLDS/game8/index.html) |
| MAPLE RUN | PlayCanvas + Splat Engine / WebGPU | Vite | 浏览器站点 dist/ | [🎮 试玩](https://maple-run-fable.vercel.app) |
| Escape the Fable | three.js | 无构建 | 多文件静态站点 | ⌨️ |
| Circular Tic Tac Toe | SVG + JavaScript | 无构建 | 多文件静态站点 | [🎮 试玩](https://muhammad-sayed-mahdy.github.io/circular-tic-tac-toe-web/) |
| EarthFM · Listening Game | Next.js + React + Tone.js | Next.js | Web 应用 | [🎮 试玩](https://earthfm.vercel.app/play) |
| T-Minus | Preact + PeerJS / WebRTC | Vite + TypeScript | 浏览器站点 game/ | [🎮 试玩](https://missioncontrol.dractec.com/) |
| Jester | MediaPipe + three.js | Vite + TypeScript（Make） | 浏览器站点 app/dist | [🎮 试玩](https://jester-pi.vercel.app) |
| Retro Sisters | Canvas + SID 音频 | 无构建 | 多文件静态站点 | ⌨️ |
| Rawza Ring | three.js | 无构建 | 多文件静态站点 | [🎮 试玩](https://hashmatullahzaher.github.io/mazar-rawza-race/) |
| Gifts for the Tall One | three.js | 无构建 | 多文件静态站点 | ⌨️ |

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
- 部分作品借鉴既有游戏玩法，也有明确标注的同人作品；素材、角色与第三方资源的使用范围以作者 README 和许可证为准。
- 部分作品仍在开发中，完成度差异很大；「在线可玩」只代表能打开，不代表完成度。
- 原有条目快照为 2026-11-12、2026-11-14；本次新增 32 款与 Last Return 更新记录于 2026-11-16，Star 数与在线状态会随时间变化。

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
