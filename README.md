# Claude Fable 5.2 / GPT-6.2 Astra / Gemini 4 / GLM-5.4 游戏合集

**189 款游戏与交互作品 · 116 个游戏仓库 · 4 份社区合集 · 128 款附浏览器试玩链接 · 附录另有 23 款补充作品**

Claude Fable 5.2、GPT-6.2 Astra、Gemini 4 Carbon、Gemini 4 Neon 与 GLM-5.4 带来的游戏作品，已经从小型 demo 延伸到开放世界、3D 竞速、第一人称恐怖与多人格斗。

这个仓库把它们整理成一份可检索的清单：**每款都有源码地址、玩法说明、模型归属和真实技术栈；有在线试玩的附链接，没有试玩页的写清本地运行方式**。多模型协作和同一仓库里的不同模型版本分开标注，方便比较不同模型做出的作品。

按作者披露的模型归属分：**111 款由 Claude Fable 5.2 独立完成，41 款由 GPT-6.2 Astra 独立完成，4 款是 Claude Opus 5.5 的同款对照版本，Gemini 4 Carbon 独立作品 2 款、Gemini 4 Neon 独立作品 12 款、GLM-5.4 独立作品 2 款，另有 17 款多模型协作**。同一仓库、同一提示词下的不同模型版本分别列出；版本未注明的 GPT-6 Astra 不计入 GPT-6.2 Astra。

同款对照现在有了一条完整的对照链：Model Arena 的屋顶跑酷有 Fable 5.2、Astra、Opus 5.5、Sol 四个实现，Mall Action 有 Fable、Astra、Opus 三个分支，Lantern Drift 是 Fable 与 Astra 各跑一轮。编号相邻，可以直接比较各家模型在同一任务上的完成度和耗时。

| 文档 | 内容 |
| --- | --- |
| [TECH_STACK.md](TECH_STACK.md) | 116 个仓库的技术栈、模型归属、构建方式、交付体积、生成成本横向对比 |
| [PROMPTS.md](PROMPTS.md) | 可复现的原始提示词：一句话 FPS、21 句 RTS、三句需求做出三个游戏 |
| [GAME_DEV_SKILLS.md](GAME_DEV_SKILLS.md) | 12 个游戏制作 Skill：对应作品、试玩入口与公开情况 |
| [data/games.csv](data/games.csv) | 含模型归属的结构化数据，方便二次加工或做站 |

> **核验说明**：原有 26 款数据抓取于 **2026-11-12**；《潮汐战线》和 5 款游戏于 **2026-11-14** 核验；**2026-11-16** 新增 32 款、23 个仓库，并更新已更名的 Last Return；**2026-11-17** 新增 21 款、9 个仓库，其中《回声游戏厅》同一仓库含 13 款；**2026-11-18** 新增 3 款、2 个仓库：《柑仔的晚霞航空信》（Claude Fable 5.2 版）、《夕阳邮航》（GPT-6.2 Astra 版）和《Santa Express: Chimney Panic!》（GPT-6.2 Astra）。前两款共用一个仓库，但模型版本分别列出。模型归属依据作者 README 或项目说明；协作模型按披露记录，不推测未说明的模型。两个托管页面均返回 HTTP 200，未实际验证完整游玩流程。**2026-11-19** 新增 19 款、10 个新仓库：Claude Fable 5.2 新作 11 款（6 款单模型、5 款与 Claude Opus 5.5 协作），GPT-6.2 Astra 新作 8 款；同一仓库内的模型对照版本分别记录。原自然灾害项目仓库已不可访问，三款既有作品的源码链接改为目前可访问的同名项目仓库。新增的 7 条浏览器试玩记录对应 6 个网址均返回 HTTP 200，仅核验可访问性，未逐款验证完整流程。Star 数按各条目的抓取日期记录。
> **2026-11-20** 新增 15 款、11 个新仓库：Claude Fable 5.2 单模型作品 3 款、GPT-6.2 Astra 作品 11 款，以及 1 款包含 Fable 5.2 与多模型协作的作品。10 条试玩链接返回 HTTP 200；另 5 款按作者文档在本地或指定硬件运行。GPT-6.2 Astra 与未注明 6.2 的旧版 GPT-6 Astra 分开处理。
> **2026-11-21** 新增 6 款、6 个新仓库：Claude Fable 5.2 独立作品 1 款、Fable 与 Opus 5.5 协作 1 款、Gemini 4 Carbon 独立作品 1 款、Carbon 与未注明版本的 GPT-6 Astra 协作 1 款、Gemini 4 Neon 独立作品 2 款；本轮未发现符合明确版本要求的新 GPT-6.2 Astra 游戏。4 个浏览器试玩链接返回 HTTP 200，未逐款验证完整流程；《After the Tide》按 README 的本地服务方式运行，《Street Trash: Dezombifier》提供桌面与 Android 下载。Kurogane III 的模型设置与生成日志尚未公开，项目 README 也说明它不是官方或独立验证的基准。
> **2026-11-21 补录（含更正）**：附录新增《重庆（试玩版）》一款——浏览器里的重庆观光 demo，来自 Gary 的深海 AI 视频实验室独立站点（lab.ytdeepsea.com，非 aiarcade 镜像）。作者 Gary 曹淦（@GaryAIytb）在[发布推文](https://x.com/GaryAIytb/status/2123331645046714382)中明确说明：这是 **Claude Fable 5.2** 的作品，25 亿 token、187 轮修改、5 天，AI 自己写 Python 指挥 Blender 逐栋建模，作者一行代码没写、只发了 23 条消息。素材层面另用 GPT Image 2.5 出图、腾讯 Hunyuan3D-2 生成 3D 模型（Credits 页有完整清单）。因作者未公开源码仓库、且不在主榜的 GitHub 索引口径内，仍列附录，不计入主榜；但模型归属按作者原话记为 Fable 5.2，而非先前据 Credits 误判的「素材生成特例」。试玩链接返回 HTTP 200。
> **2026-11-23** 新增 14 款、9 个新仓库（另在既有《回声游戏厅》仓库补录第 14 期）：Claude Fable 5.2 作品 3 款、GPT-6.2 Astra 1 款、Gemini 4 Carbon 1 款、Gemini 4 Neon 8 款，以及同提示词的 Claude Opus 5.5 对照版 1 款。Neon 的 100 个 HTML studies 中只选入 4 款有明确胜负或解题目标的游戏；纯视觉研究未计入。13 个浏览器试玩网址返回 HTTP 200，仅核验可访问性，未逐款实际通关；《霜谷铲雪社》无托管试玩页，README 提供本地启动方法。模型归属按作者 README、仓库 About 或模型日志标注，Astra、Carbon、Neon 与 Fable 分组记录。
> **2026-11-24** 新增 3 款、3 个新仓库：GPT-6.2 Astra 新作《Solar Drift》1 款；Gemini 4 Neon 新作《Token 花园》《PrimeWordle》2 款。Solar Drift 的浏览器试玩页返回 HTTP 200，仅核验可访问性；《Token 花园》需 Godot 4.7.2 本地启动，《PrimeWordle》可运行 `python run_web.py` 启动本地网页。Fable 5.2 与 Gemini 4 Carbon 本轮未发现符合收录条件的新仓库。另发现两组共 12 款 Astra 小游戏展示页带 `noindex,nofollow`，本轮未纳入公开目录；Neon 的 Heartwood Hollow 仓库说明尚无实际玩法，也未收录。
> **2026-11-25** 新增 39 款、15 个新仓库：Claude Fable 5.2 独立作品 18 款、GPT-6.2 Astra 18 款、Gemini 4 Neon/Fable/Opus 协作 1 款、GLM-5.4 2 款；Gemini 4 Carbon 本轮无新增。Fable Flight 仓库今日有更新，但作品已在清单中，没有重复添加。18 个试玩页均返回 HTTP 200，仅核验可访问性，未逐款完整游玩；其余作品按作者文档提供本地浏览器、CLI、Unity 或桌面运行方式。另见 Astra 展示集声明 `noindex,nofollow`，未纳入。Atlantis 与 Last Light Arcade 四款为前次 48 小时重叠窗口内发现的补录。
> **2026-11-16 试玩链接迁移**：站内托管试玩由 fable52.games 统一换成 **aiarcade.games**（同站新域名，页面 slug 不变），覆盖站上全部 **42 款**，逐一实测返回 HTTP 200；Riftline 此前标注「无在线版本」，已在站上找到试玩页并补上；《潮汐战线》《The County》《MAKINAMON》改为站点试玩优先、作者站备份。
> **2026-11-16 夜间补链**：aiarcade.games 试玩页由 42 个增至 **61 个**，清单里此前只有作者站或本地运行的 **18 款**作品找到站内页面（含 ONE PROMPT WORLDS 全 8 作、Last Return、Duel Knights、SHUTTERPINE、Mini RPG、Escape the Fable 等），已统一改为站点试玩优先、作者站备份；附录新增 1 款站点独占作品《太阳系三维沙盘》。61 个页面逐一实测返回 HTTP 200。
> 作品包含开发中游戏、交互体验与多人原型；没有浏览器试玩链接的 61 款，需按条目说明本地运行、构建或下载作者发布包。
> **2026-11-18 试玩页巡检**：站点试玩页由 61 个增至 **87 个**，新增 26 个页面。其中 23 个是清单内作品在 aiarcade 的镜像（这些作品此前已列作者站试玩，本次不改动链接），另 3 款《Ripcore》《三借芭蕉扇》《Starship Dogfight》不在清单内，已按附录处理并入。清单里仍缺试玩链接的 18 款没有新增页面。3 个新链接逐一实测返回 HTTP 200。
> **2026-11-20 试玩页巡检**：站点试玩页由 88 个增至 **91 个**，新增 3 个页面。其中《LAST LIGHT — Rooftop Run》《Papertrails》是清单内作品（#96、#97）的流式镜像，页面仍从作者站加载，这两款已有作者站试玩链接，本次不改动；另 1 款《Fault Line Echoes · 断层回声》不在清单内，已按附录处理并入。新增的 1 个链接实测返回 HTTP 200。
> **2026-11-20 同款对照补录**：新增 5 款，均出自已收录的仓库分支或基准项目——Claude Fable 5.2 版 2 款（Lantern Drift、Mall Action），Claude Opus 5.5 版 3 款（HIGHLINE、The Tallow Deep、Mall Action）；后 3 款与清单内的 Fable 5.2 / GPT-6.2 Astra 版本使用同一提示词，单列成「附」便于对照。5 个试玩链接均返回 HTTP 200，并已在浏览器中实际进入游戏。Model Arena 第三回合 breath 是互动解剖展览而非游戏，未收录。

## 图例

- 🎮 `[Play Online Live Demo]` —— aiarcade.games 托管镜像，点开即玩，无需安装；作者自建站作为备份一并给出（[技术栈速查表](#十一技术栈速查表)里的「🎮 试玩」同样可直接点）
- 🖥 作者自建站 / GitHub Pages —— 作者本人托管的版本，通常与源码同步更新
- ⌨️ 暂无浏览器试玩链接 —— 按条目说明起静态服务、构建程序，或使用作者提供的桌面版本
- ⭐ —— Star 数（日期见条目）

## 目录

- [一、开放世界与动作（9 款）](#一开放世界与动作9-款)
- [二、第一人称射击（8 款）](#二第一人称射击8-款)
- [三、视觉效果与探索（14 款）](#三视觉效果与探索14-款)
- [四、体育、竞速与其他（56 款）](#四体育竞速与其他56-款)
- [五、Claude Fable 5.2 新作（39 款）](#五claude-fable-52-新作39-款)
- [六、GPT-6.2 Astra 作品（41 款）](#六gpt62-astra-作品41-款)
- [七、Gemini 4 Carbon 作品（3 款）](#七gemini-4-carbon-作品3-款)
- [八、Gemini 4 Neon 作品（13 款）](#八gemini-4-neon-作品13-款)
- [九、GLM-5.4 作品（2 款）](#九glm-54-作品2-款)
- [十、值得收藏的社区合集](#十值得收藏的社区合集)
- [十一、技术栈速查表](#十一技术栈速查表)
- [十二、这些游戏是怎么被写出来的](#十二这些游戏是怎么被写出来的)
- [附录：站上还有这 23 款](#附录站上还有这-23-款)

---

## 一、开放世界与动作（9 款）

**01 · FOG CITY** — GTA 风格开放世界 · [源码](https://github.com/Rikinshah787/Game-Fable-5.2) ⭐ 0
旧金山风格小城，7×7 街区带坡道和跨海大桥；有红绿灯车流、会躲子弹逃跑的行人、可劫持的车辆，五星通缉时警车追上来、警察下车开火，甩掉视线通缉才会清零。
`three.js` · 无构建 · 12 个 ES module 分工（城市 / 车辆 / 警察 AI / 后处理） · ⌨️ 暂无在线版本，`npm start` 后开 <http://localhost:8765>

**02 · Dustfall** — 西部开放世界 · [源码](https://github.com/webKing021/dustfall) ⭐ 2
驯服野马、骑马打猎钓鱼、在酒馆打黑杰克，六个章节的主线加赏金追捕；犯罪需要目击者，赏金会招来追兵团，荣誉值影响物价和结局。
`three.js 0.187 + Vite 8` · 昼夜与暴雨沙尘 · [Play Online Live Demo](https://aiarcade.games/play/dustfall) · [作者站](https://dustfalls.netlify.app/)

**03 · Bayhaven** — 犯罪题材开放世界，AI 逐次提交 · [源码](https://github.com/fablestar/bayhaven) ⭐ 0
不是「AI 辅助」，而是每行代码、每个 commit 都由 Fable 5.2 在公开直播里写完；仓库里除了 `src/`，还有它自己维护的 `ROADMAP.md`、`BUGS.md` 和每个模块的接口契约。
`three.js` · 模块注册表 · 每次提交都跑 headless Chromium 检查 · [Play Online Live Demo](https://aiarcade.games/play/bayhaven)

**04 · Aquila** — 古罗马开放世界 · [源码](https://github.com/GavinLOrio/Fable-5.2-random-game) ⭐ 0
扮演凯撒第十三军团的信使，从卢比孔河走到三月十五日；地图用真实海岸线生成，103 个地点按真实坐标摆放，八章主线、十个支线、28 个据点、18 处沉船可潜水。
`three.js + esbuild` · 单文件 `rome/index.html` · 潜行 / 爬墙 / 方阵战斗 / 划桨船 · ⌨️ 暂无在线版本，`node tools/build.mjs rome` 后打开

**05 · Dawnward** — 3D 奇幻开放世界 · [源码](https://github.com/GavinLOrio/Fable-5.2-random-game) ⭐ 0
永夜之岛，穿越六大区域点亮六座古灯塔，升级拿祝福，最后在「王冠」迎战 Umbra Titan。提灯自动攻击，玩的是走位与冲刺的取舍。
`three.js + esbuild` · 单文件 `index.html`，离线可玩、自动存档 · 支持手机触屏 · ⌨️ 暂无在线版本

**06 · Ironvale** — 《帝国时代》风格 RTS · [源码](https://github.com/SharpWizard/ironvale) ⭐ 0
采集、建城、三个时代升级、科技树、编队热键、战争迷雾、AI 对手会投降；五个原创国度各有独特兵种与建筑，还有三部原创战役。
`three.js r128`（内置 `lib/` 并带 CDN 兜底）· 21 句大白话写成 · 另附 5.8 MB 单文件 `Ironvale.exe` · [Play Online Live Demo](https://aiarcade.games/play/ironvale) · [作者站](https://sharpwizard.github.io/ironvale/) · [完整提示词](https://github.com/SharpWizard/ironvale/blob/main/PROMPTS.md)

**07 · The Long Climb** — 开放世界叙事 · [源码](https://github.com/HILAYTRIVEDI/thirty-days) ⭐ 1（2026-11-16）
围绕 NVIDIA 创业历程展开的三时期 3D 叙事游戏，包含经营抉择、对话和芯片布线小游戏；剧情为游戏演绎。
`three.js` · 无构建 · [Play Online Live Demo](https://aiarcade.games/play/the-long-climb) · 本地运行 `python3 -m http.server 8137` 后打开 <http://localhost:8137> · 作者说明使用 Fable 5.2

**08 · The Boondocks: The Woodcrest Files** — 2D 动作 · [源码](https://github.com/Achraf921/boondocks) ⭐ 0（2026-11-16）
非官方同人清版动作游戏，以街区为据点推进五个任务；支持连招、格挡、弹反与手柄。
`原生 JavaScript` · 无构建 · ⌨️ 暂无浏览器试玩链接，打开 `index.html`；或运行 `python3 -m http.server 8765` · 作者说明使用 Fable 5.2

**09 · Duel Knights** — 3D 动作 · [源码](https://github.com/bitofastickler/duel-knights) ⭐ 0（2026-11-16）
在庭院或山顶回廊里进行三局制骑士决斗，选择角色、武器和对手，通过闪避、佯攻与弹反获胜。
`three.js` · 无构建 · [Play Online Live Demo](https://aiarcade.games/play/duel-knights) · [作者站](https://bitofastickler.github.io/duel-knights/) · 源自 Fable 5.2 的 Ashen Crown，后续扩展见作者 Origin 说明

## 二、第一人称射击（8 款）

**10 · Saltline** — 3D 港口 FPS · [源码](https://github.com/realcodebear/saltline-fable-5.2) ⭐ 230
整条链路的起点：Anthropic 的 Felix Rieseberg 一句提示词、无人干预 8 小时跑出来的雨夜集装箱码头，切断三个中继站，躲开机群「Gulls」和机械狗「Hounds」。
`three.js` 内联 · **单文件 1.4 MB** · 模型、音效、贴图全部代码生成 · [Play Online Live Demo](https://aiarcade.games/play/saltline-fable-5-2-fps) · [作者站](https://realcodebear.github.io/saltline-fable-5.2/)

**11 · 盐线行动 Online** — 港口 FPS 联机版 · [源码](https://github.com/wenzhengshi/fable5-2-salt-online) ⭐ 16
在 Saltline 基础上扩出多人对战：5 秒复活、房间大厅、本地排行榜落盘，无数据库，单机 `node server.js` 就能开局。
`Node.js + Express + WebSocket + three.js` · 前后端同一仓库 · [Play Online Live Demo](https://aiarcade.games/play/saltline-online)

**12 · SUBLEVEL 07** — 科幻地下变电站 FPS · [源码](https://github.com/wquguru/fable52-fps-repro) ⭐ 78
中文社区里最能「抄作业」的一份：一句提示词、73 轮无人干预、41 分钟，产出 **131 KB 单文件**，潮湿地面实时反射、红点卡宾枪、三波悬浮无人机、18 个合成音效，AI 自己写脚本打通关验证零报错。仓库同时公开提示词原文与逐轮 token 账单。
`单文件 HTML` · 体积极小但含后处理 · [Play Online Live Demo](https://aiarcade.games/play/sublevel-07-fps-repro) · [作者站](https://wquguru.github.io/fable52-fps-repro/)

**13 · BLAMELESS** — 程序员主题 FPS · [源码](https://github.com/Petyok/blameless) ⭐ 0
凌晨 3:07 告警响了：你 `kubectl exec` 进生产环境，用 `kill -9`、`grep -r`、`rm -rf` 当武器，清掉十个故障、四台主机、一个根因。没有弹药，只有限流（打太久返回 429），血量就是错误预算，死后写复盘。
`three.js` + npm 构建 · Python 标准库排行榜服务 · 确定性模拟可在 Node 里跑端测 · [Play Online Live Demo](https://aiarcade.games/play/blameless) · [作者站](https://blameless.petruha.ge/)

**14 · Dustline Outpost** — 时间循环 FPS · [源码](https://github.com/systemsluke/fable5.2game) ⭐ 1
每道闪电把世界倒回 70 秒，你上一轮的自己被留下成一个半透明「回声」，按原样重放每一枪。三个中继站相距太远，只能靠不同轮次的自己配合占领——一共六次机会。
`three.js r128` · 无构建 · 回声按 20 Hz 记录并从**当前**世界重发射线 · Poly Haven CC0 扫描素材 · ⌨️ 暂无在线版本，需静态服务且首屏拉 41 MB 资源

**15 · Last Return（原 No Return）** — LiDAR 点云恐怖游戏 · [源码](https://github.com/StefanKnol/Last-Return) ⭐ 1（2026-11-16）
在全黑的地下泵房里寻找三卷测绘资料；手持扫描仪照出的点云会留在原地，停下扫描就看不见周围的东西。
`WebGL 2 + JavaScript` · [Play Online Live Demo](https://aiarcade.games/play/last-return) · [作者站](https://last-return.sknol.com/) · 源码已拆分，`npm run build` 生成单文件 `index.html`；原仓库地址已重定向至此

**16 · Riftline** — 3D 第一人称英雄射击 · [源码](https://github.com/wongh26/claude_fps) ⭐ 0
用 Vesper 的双枪、瞬移和回溯技能打机器人或与朋友联机对决；支持 PeerJS 点对点联机。
`three.js r160 + PeerJS` · 无构建 · [Play Online Live Demo](https://aiarcade.games/play/riftline) · ⌨️ 本地跑：`python3 -m http.server 8000`

**17 · Graveyard Shift** — FPS · [源码](https://github.com/ethanplusai/zombies) ⭐ 9（2026-11-16）
在路边餐馆与加油站抵御逐轮增强的僵尸，修窗、搜刮、购买武器并恢复供电；支持桌面与触屏。
`three.js / WebGL 2` · esbuild · [Play Online Live Demo](https://aiarcade.games/play/graveyard-shift) · [作者站](https://zombies.ethanplus.ai) · 作者说明使用 Fable 5.2

## 三、视觉效果与探索（14 款）

**18 · Tidebell 潮钟** — 3D 水下探索 · [源码](https://github.com/hahaliu1029/fable5.2demo) ⭐ 0
驾驶小潜水器从阳光照透的珊瑚礁一路下潜到深渊，唤醒七口沉睡的潮钟。48 个模型全部由 Blender 里的 Python 脚本生成，手写水下光照：红色最先随深度消失，开灯才把颜色找回来。
`three.js r170` · 单文件 `index.html` · 18,000 个海底实例，鱼群动画跑在顶点着色器里 · [Play Online Live Demo](https://aiarcade.games/play/tidebell)

**19 · MOTHLIGHT // Vesper-9** — 赛博朋克城市驾驶 · [源码](https://github.com/hahaliu1029/fable5.2demo) ⭐ 0
雨夜霓虹城里穿 12 道光门，手刹漂移、加速带、单轨列车与全息飞蛾；9×9 街区 694 栋楼一次实例化绘制，窗户画出带纵深的房间。
`three.js r170` · 单文件 · 湿街道镜面反射与实时环境贴图 · [Play Online Live Demo](https://aiarcade.games/play/mothlight)

**20 · 青云宗 · 御剑采灵** — 3D 仙侠 · [源码](https://github.com/hahaliu1029/fable5.2demo) ⭐ 0
第三人称御剑飞行，在体积云海、浮岩和真实反射的湖面之间收集 20 颗灵气，点亮山门牌匾后穿门通关；水墨标题、飞剑光带、解锁金光柱。
`three.js r170` · 单文件 · 支持触屏；自驾驶脚本可完整通关并录回放 · [Play Online Live Demo](https://aiarcade.games/play/qingyun-sword-flight)

**21 · MISREMEMBER** — 第一人称心理恐怖 · [源码](https://github.com/hahaliu1029/fable5.2demo) ⭐ 0
有什么东西按你的记忆重建了童年的家，而记忆并不可靠：你盯着的东西永远不变，变化只发生在你身后。房间靠门洞模板遮罩拼接，同一扇门下次打开可能通向别处。
`three.js` · 单文件 · 变化排队等离开视野才落地；贴图由 Codex 生成（仓库只放 WebP）· [Play Online Live Demo](https://aiarcade.games/play/misremember)

**22 · Hanford Reach** — 小镇探索与定居点建设 · [源码](https://github.com/chzbloom123/settlement-bluff-fable5.2) ⭐ 0
哥伦比亚河畔小镇废墟上的慢节奏建造游戏，第一人称与第三人称随时切换，带质量档位、性能报表和一键渲染 14 个固定机位的对比截图脚本。
`three.js + Vite` · Vercel 自动部署，每个 PR 有独立预览 · [Play Online Live Demo](https://aiarcade.games/play/hanford-reach) · [作者站](https://settlement-bluff-fable52.vercel.app)

**23 · Boring Game** — 湾区体素世界 · [源码](https://github.com/jakozaur/sf_bay_area_transit_fable_5_2_game) ⭐ 0
用真实地图数据重建旧金山湾区体素地形，规划线路、挖隧道、建车站，把列车开到作者公司楼下。15 条提示词、15 小时、66,000 行、约 $700。
`TypeScript + Vite` · typecheck + Biome + Vitest + 基准测试 · [Play Online Live Demo](https://aiarcade.games/play/boring-game-sf-bay-transit) · [作者站](https://jakozaur.github.io/sf_bay_area_transit_fable_5_2_game/)

**24 · SHUTTERPINE** — 叙事恐怖 · [源码](https://github.com/DQuanBui/shutterpine) ⭐ 0（2026-11-16）
沿失踪摄影师的山林足迹寻找线索，复拍旧照片；相机能看见并阻止追踪者，山顶选择通向两个结局。
`three.js` · Vite · [Play Online Live Demo](https://aiarcade.games/play/shutterpine) · [作者站](https://dquanbui.github.io/shutterpine/) · 作者说明使用 Fable 5.2

**25 · Power the Spire** — 3D 收集探索 · [源码](https://github.com/cdurgun/claude-fable-3d-world) ⭐ 0（2026-11-16）
在程序化漂浮岛城市里驾车收集八颗能量球，点亮中央尖塔；与同仓库的自动镜头场景共享世界。
`three.js 0.187` · 无构建 · ⌨️ 暂无浏览器试玩链接，运行 `npm install && npm start` 后打开 <http://127.0.0.1:4173/game/index.html> · 作者说明使用 Fable 5.2

**26 · Tropical Island** — 海岛探索 · [源码](https://github.com/Tarzno/tropical_island) ⭐ 0（2026-11-16）
在塞舌尔风格海岛步行、游泳、潜水和拍照，观察植物、动物、日月与潮汐；没有战斗目标。
`Godot 4.7.2` · Godot · ⌨️ 暂无浏览器试玩链接，用 Godot 4.7.2 打开项目后运行；[macOS 构建](https://github.com/Tarzno/tropical_island/releases) · Opus 5.5 初始实现，Fable 5.2 进行后续实质扩展

**27 · CASCADE** — 自然灾害体验 · [源码](https://github.com/Cryptopiy/Claude-Fable-5.2-Natural-Disasters) ⭐ 0（2026-11-19）
第一人称观测火山喷发、山体坍塌与海啸的自然灾害体验。作者提供约 11 分钟的流程与可切换的自动镜头模式。
`Unity HDRP` · Unity 6000.6.0f1 · ⌨️ 无浏览器试玩 · [Windows 下载](https://github.com/Cryptopiy/Claude-Fable-5.2-Natural-Disasters/releases/download/v1.0/CASCADE-Windows-x64.zip) · [源码目录](https://github.com/Cryptopiy/Claude-Fable-5.2-Natural-Disasters/tree/main/games/1-cascade) · Claude Fable 5.2（Ultracode）

**28 · MESOCYCLONE** — 自然灾害体验 · [源码](https://github.com/Cryptopiy/Claude-Fable-5.2-Natural-Disasters) ⭐ 0（2026-11-19）
第一人称观测超级单体雷暴、冰雹与龙卷风的自然灾害体验。作者提供约 11 分钟的流程与可切换的自动镜头模式。
`Unity HDRP` · Unity 6000.6.0f1 · ⌨️ 无浏览器试玩 · [Windows 下载](https://github.com/Cryptopiy/Claude-Fable-5.2-Natural-Disasters/releases/download/v1.0/MESOCYCLONE-Windows-x64.zip) · [源码目录](https://github.com/Cryptopiy/Claude-Fable-5.2-Natural-Disasters/tree/main/games/2-mesocyclone) · Claude Fable 5.2（Ultracode）

**29 · ZERO** — 自然灾害体验 · [源码](https://github.com/Cryptopiy/Claude-Fable-5.2-Natural-Disasters) ⭐ 0（2026-11-19）
第一人称观测小行星撞击与冲击波的自然灾害体验。作者提供约 11 分钟的流程与可切换的自动镜头模式。
`Unity URP` · Unity 6000.6.0f1 · ⌨️ 无浏览器试玩 · [Windows 下载](https://github.com/Cryptopiy/Claude-Fable-5.2-Natural-Disasters/releases/download/v1.0/ZERO-Windows-x64.zip) · [源码目录](https://github.com/Cryptopiy/Claude-Fable-5.2-Natural-Disasters/tree/main/games/3-zero) · Claude Fable 5.2（Ultracode）

**30 · OUT OF REACH** — 太空生存 · [源码](https://github.com/alex-slovakia/out-of-reach) ⭐ 1（2026-11-16）
为 NASA Space Apps 制作的第一人称太空生存游戏，先设计任务，再管理飞船资源并应对零重力环境。
`Unity URP` · Unity 6000.3.28f1 · ⌨️ 暂无浏览器试玩链接，拉取 Git LFS 文件后用 Unity 6000.3.28f1 打开 `Assets/_OutOfReach/Scenes/Bootstrap.unity`；[Windows 成品](https://github.com/alex-slovakia/out-of-reach/releases/tag/spaceapps-2026-final) · 作者披露 Fable 5.2、Opus / Sonnet 5.5 与 Codex 协作

**31 · うしろのハニワ** — 第一人称解谜 · [源码](https://github.com/shioa2006-game/ONE_PROMPT_WORLDS) ⭐ 0（2026-11-16）
在古坟石室逐格移动，用视线控制背后靠近的埴轮，把它们引到对应台座；支持撤销。
`原生 JavaScript` · 无构建 · [Play Online Live Demo](https://aiarcade.games/play/ushiro-no-haniwa) · [作者站](https://shioa2006-game.github.io/ONE_PROMPT_WORLDS/game6/index.html) · ONE PROMPT WORLDS 第 1–8 作，作者标注为 Fable 5.2

## 四、体育、竞速与其他（56 款）

**32 · Soccer 3D** — 7 人制 3D 足球 · [源码](https://github.com/ShaunPrice/soccer-3d) ⭐ 0
有裁判、越位、红黄牌、点球与人墙、伤停补时和平局点球大战；阵型/心态/逼抢三档战术，体力、受伤、三个换人名额，进球慢镜回放，八级难度。
`单文件 HTML` · PWA 可装到手机主屏、离线可玩 · 音效与解说由 ElevenLabs 生成 · [Play Online Live Demo](https://aiarcade.games/play/pocket-soccer-3d) · [作者站](https://shaunprice.github.io/soccer-3d/)

**33 · TukTuk** — 埃及街头驾驶 · [源码](https://github.com/basemazab/tuktuk) ⭐ 0
在挤满小巴、出租和西瓜车的开罗街道里钻缝拉客，收车费、躲路障。所有形状、材质、音效都由代码生成，仓库里没有一张图片、一个音频文件。
`three.js` · `game.js` + `index.html` 两个文件 · [Play Online Live Demo](https://aiarcade.games/play/tuktuk) · [作者站](https://basemazab.github.io/tuktuk/)

**34 · Emberdeep** — 浏览器冒险 · [源码](https://github.com/DNDNoob/EmberDeep) ⭐ 0
火把在烧，往下走。单文件地牢下潜，约 100 KB。
`单文件 HTML` · [Play Online Live Demo](https://aiarcade.games/play/emberdeep) · [作者站](https://dndnoob.github.io/EmberDeep/)

**35 · Daedalus** — 古希腊神话解谜 · [源码](https://github.com/S77FFY/daedalus) ⭐ 1
以代达罗斯迷宫为题的谜题游戏，121 KB 单文件。
`单文件 HTML` · [Play Online Live Demo](https://aiarcade.games/play/daedalus) · [作者站](https://s77ffy.github.io/daedalus/)

**36 · Sternenjäger** — 科幻太空射击 · [源码](https://github.com/oldzitterhand/sternenjaeger) ⭐ 0
12 个星区、3 场 Boss 战，飞船自动开火，玩家只管飞位与 EMP；手机、键盘、手柄三种操作都支持。
`单文件 HTML` · 无构建无服务 · [Play Online Live Demo](https://aiarcade.games/play/sternenjaeger) · [作者站](https://oldzitterhand.github.io/sternenjaeger/)

**37 · Shuttle Strike** — 第一人称羽毛球 · [源码](https://github.com/fedifianto/shuttlestrike) ⭐ 0
用摄像头追踪手部：握拳即握拍，挥快球杀球，拍面高低决定挑高或吊球；张开手掌停住是暂停。没摄像头可切鼠标模式。
`单文件 HTML` + CDN 手部追踪 · 需 HTTPS 或 localhost 才能开摄像头 · [Play Online Live Demo](https://aiarcade.games/play/shuttle-strike) · [作者站](https://fedifianto.github.io/shuttlestrike/)

**38 · NEON RUNNER** — 赛博朋克 2D 跑酷 · [源码](https://github.com/Ilias-AK/NewGameFromFable5.2) ⭐ 0
霓虹城市无尽跑酷，障碍按「与玩家相遇的时间」生成，因此难度提升不会压缩反应窗口；三档难度、护盾与磁铁道具、每 500 米记速、Top-5 本地存档。
`单文件 HTML` · Canvas 2D + Web Audio + LocalStorage，零外部资源 · ⌨️ 暂无在线版本，双击 `index.html` 即可

**39 · Becario del Universo** — 宇宙主题小游戏 · [源码](https://github.com/masugus/fable5.2-5min-game) ⭐ 0
「宇宙最新实习生」的琐碎任务合集，桌面与手机同一份代码，5 分钟能玩完一局，最高分存在浏览器里。
`单文件 HTML` · [Play Online Live Demo](https://aiarcade.games/play/becario-del-universo) · [作者站](https://masugus.github.io/fable5.2-5min-game/)

**40 · Harvest Standoff** — 农场 5v5 团队竞技 · [源码](https://github.com/andreteow/farm-ca) ⭐ 0
动物对农场工人，回合制 5v5，有商店、金币、中场与「臭南瓜」；十名角色全部由 Blender 脚本雕刻生成，语音与配乐由脚本批量产出。
`three.js` + 自写 `build.mjs` · 有 AI 自动对战测试与地图公平性统计 · [Play Online Live Demo](https://aiarcade.games/play/harvest-standoff) · [作者站](https://harvest-standoff.vercel.app)

**41 · 潮汐战线（Tidemark）** — 《高级战争》式回合制战棋 · [源码](https://github.com/CocoSgt/dsh-game-tidemark) ⭐ 12（2026-11-14）
陆海空 33 个兵种、29 位指挥官和 27 关战役；纯前端、多文件 HTML/JavaScript，无需构建，支持本地打开游玩。
`HTML Canvas + JavaScript` · [Play Online Live Demo](https://aiarcade.games/play/tidemark) · [作者站](https://dsh-game-store.com/games/tidemark/) · [游戏手册](https://dsh-game-store.com/games/tidemark/manual/)

**42 · The County** — 土豆农场经营策略 · [源码](https://github.com/TheMizeGuy/fable-5.2-potatobench) ⭐ 1（2026-11-14）
从六块田和一名农夫起步，安排种植、收获、雇工、扩地和订单；作物长在地下，得等收成时才知道结果。
`TypeScript + three.js + Vite` · [Play Online Live Demo](https://aiarcade.games/play/the-county) · [作者站](https://themizeguy.github.io/fable-5.2-potatobench/)

**43 · MAKINAMON · Versión Pulso** — Game Boy Color 风格像素怪物 RPG · [源码](https://github.com/gavilanbe/makinamon-pulso) ⭐ 0（2026-11-14）
在 10 个章节里收集并培养 50 种机器生物，挑战 6 名中央设施首领；50 种攻击各有动画与音效。
`Canvas 2D + JavaScript` · [Play Online Live Demo](https://aiarcade.games/play/makinamon-pulso) · [作者站](https://gavilanbe.github.io/makinamon-pulso/)

**44 · SUPERFORGE GT** — SNES 赛车生涯游戏 · [源码](https://github.com/jreinach-alt/sf-gt) ⭐ 0（2026-11-14）
买车、跑 12 场赛事、用奖金改装；8 台车、6 条 Mode 7 赛道和 9 名对手，最终构建为 4 MB SNES ROM。
`65C816 Assembly + Python` · 按 README 在 Linux 上构建，再用 SNES 模拟器运行

**45 · FableFlight** — 飞行模拟 · [源码](https://github.com/Rolandjg/fableflight) ⭐ 213（2026-11-16）
Rust 编写的开放世界飞行模拟器，提供实时天气、真实空中交通、燃油与配重、无线电导航和可绑定的飞行外设。
`wgpu + egui` · Cargo · ⌨️ 暂无浏览器试玩链接，安装 Rust 后运行 `cargo run --release` · 作者披露由 Fable 5.2 与 Opus 5.5 协作制作

**46 · Liquid Labyrinth** — 物理解谜 · [源码](https://github.com/tuki0918/maze-exit) ⭐ 0（2026-11-16）
旋转 3D 迷宫，让液体在重力作用下流向出口；可通过带种子参数的 URL 分享同一迷宫。
`three.js 0.187` · Vite + TypeScript · [Play Online Live Demo](https://aiarcade.games/play/liquid-labyrinth) · [作者站](https://maze.bbbit.cc) · 仓库 About 标注为 Fable 5.2 sample game

**47 · Mini RPG** — RPG · [源码](https://github.com/ertertwert/Mini-RPG) ⭐ 0（2026-11-16）
浏览器角色扮演游戏，支持为战斗、地牢和高塔等主题替换配乐；音乐来源见作者 README。
`原生 JavaScript` · 无构建 · [Play Online Live Demo](https://aiarcade.games/play/mini-rpg) · [作者站](https://ertertwert.com/MiniRPG.html) · 作者说明使用 Fable 5.2

**48 · Rufus Crush** — 三消 · [源码](https://github.com/bhoult/phone-games) ⭐ 0（2026-11-16）
围绕黑色拉布拉多 Rufus 日常生活的三消游戏，含 36 关、三档难度和特殊棋子；首次加载后可离线。
`macroquad / WebGL` · Rust → WebAssembly · [在线试玩](https://bhoult.github.io/phone-games/rufus-crush/) · 作者说明使用 Fable 5.2

**49 · ぽん、と森は灯る** — 物理探索 · [源码](https://github.com/shioa2006-game/ONE_PROMPT_WORLDS) ⭐ 0（2026-11-16）
弹射孢子长出蘑菇，把新蘑菇作为下一座发射台，逐步照亮森林并抵达深处大树。
`原生 JavaScript` · 无构建 · [Play Online Live Demo](https://aiarcade.games/play/pon-to-mori-wa-tomoru) · [作者站](https://shioa2006-game.github.io/ONE_PROMPT_WORLDS/game/index.html) · ONE PROMPT WORLDS 第 1–8 作，作者标注为 Fable 5.2

**50 · ひとつぶ庭園** — 粒子解谜 · [源码](https://github.com/shioa2006-game/ONE_PROMPT_WORLDS) ⭐ 0（2026-11-16）
把砂、水、种子与火种倒进瓶子，利用粒子相互反应培育小小的夜间花园。
`原生 JavaScript` · 无构建 · [Play Online Live Demo](https://aiarcade.games/play/hitotsubu-teien) · [作者站](https://shioa2006-game.github.io/ONE_PROMPT_WORLDS/game2/index.html) · ONE PROMPT WORLDS 第 1–8 作，作者标注为 Fable 5.2

**51 · EMBERDEEP ― 燈守りの坑道** — 动作 RPG · [源码](https://github.com/shioa2006-game/ONE_PROMPT_WORLDS) ⭐ 0（2026-11-16）
提灯深入矿道，点燃火盆、与暗影战斗，逐区驱散黑暗并抵达最深处炉心。
`原生 JavaScript` · 无构建 · [Play Online Live Demo](https://aiarcade.games/play/emberdeep-tomoshimori) · [作者站](https://shioa2006-game.github.io/ONE_PROMPT_WORLDS/game3/index.html) · ONE PROMPT WORLDS 第 1–8 作，作者标注为 Fable 5.2

**52 · LUMEN REEL ― まわる灯台と三つの海路** — 转轮解谜 · [源码](https://github.com/shioa2006-game/ONE_PROMPT_WORLDS) ⭐ 0（2026-11-16）
转动灯塔卷轴为航路送光，重组卷轴零件，越过五个夜晚把迷航船只送回港口。
`原生 JavaScript` · 无构建 · [Play Online Live Demo](https://aiarcade.games/play/lumen-reel) · [作者站](https://shioa2006-game.github.io/ONE_PROMPT_WORLDS/game4/index.html) · ONE PROMPT WORLDS 第 1–8 作，作者标注为 Fable 5.2

**53 · REEL DELVE ― まわる迷宮と三人の旅** — 地牢解谜 · [源码](https://github.com/shioa2006-game/ONE_PROMPT_WORLDS) ⭐ 0（2026-11-16）
选择时机停下卷轴，三行符号构成三位冒险者的通路，逐步探索十二层地下迷宫。
`原生 JavaScript` · 无构建 · [Play Online Live Demo](https://aiarcade.games/play/reel-delve) · [作者站](https://shioa2006-game.github.io/ONE_PROMPT_WORLDS/game5/index.html) · ONE PROMPT WORLDS 第 1–8 作，作者标注为 Fable 5.2

**54 · 切りもどし ― 鋏と春の小さな鉢** — 盆栽解谜 · [源码](https://github.com/shioa2006-game/ONE_PROMPT_WORLDS) ⭐ 0（2026-11-16）
修剪枝条并让春天催生新芽，以分枝规则控制盆栽形状并使花朵开放。
`原生 JavaScript` · 无构建 · [Play Online Live Demo](https://aiarcade.games/play/kirimodoshi) · [作者站](https://shioa2006-game.github.io/ONE_PROMPT_WORLDS/game7/index.html) · ONE PROMPT WORLDS 第 1–8 作，作者标注为 Fable 5.2

**55 · ひつじが いっぴき ― 牧羊犬コロの一日** — 牧羊动作 · [源码](https://github.com/shioa2006-game/ONE_PROMPT_WORLDS) ⭐ 0（2026-11-16）
操纵牧羊犬把羊群送进小屋，利用步行聚拢、奔跑驱散的差异走过九座牧场。
`原生 JavaScript` · 无构建 · [Play Online Live Demo](https://aiarcade.games/play/hitsuji-ga-ippiki) · [作者站](https://shioa2006-game.github.io/ONE_PROMPT_WORLDS/game8/index.html) · ONE PROMPT WORLDS 第 1–8 作，作者标注为 Fable 5.2

**56 · MAPLE RUN** — 3D 跑酷 · [源码](https://github.com/nanha0130/maple-run-fable) ⭐ 0（2026-11-16）
在红叶季乡间铁路上三轨奔跑，躲避火车与障碍、收集金叶；支持键盘与触屏，需要 WebGPU。
`PlayCanvas + Splat Engine / WebGPU` · Vite · [在线试玩](https://maple-run-fable.vercel.app) · 作者说明使用 Fable 5.2

**57 · Escape the Fable** — 密室解谜 · [源码](https://github.com/ai-gamez-r-funz/escape-the-fable) ⭐ 0（2026-11-16）
生成可解的二十世纪风格密室，使用钥匙、密码盘和家具暗格逃脱；内置关卡工作坊与链接分享。
`three.js` · 无构建 · [Play Online Live Demo](https://aiarcade.games/play/escape-the-fable) · 本地运行 `npm start` 后打开 <http://localhost:8080> · 作者说明使用 Fable 5.2

**58 · Circular Tic Tac Toe** — 棋盘 · [源码](https://github.com/muhammad-sayed-mahdy/circular-tic-tac-toe-web) ⭐ 0（2026-11-16）
在四环八辐的环形棋盘上连成四子，支持双人、不同难度 AI、提示、撤销与主题切换。
`SVG + JavaScript` · 无构建 · [Play Online Live Demo](https://aiarcade.games/play/circular-tic-tac-toe) · [作者站](https://muhammad-sayed-mahdy.github.io/circular-tic-tac-toe-web/) · 作者说明使用 Fable 5.2

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
`three.js` · 无构建 · [Play Online Live Demo](https://aiarcade.games/play/rawza-ring) · [作者站](https://hashmatullahzaher.github.io/mazar-rawza-race/) · 作者说明使用 Fable 5.2

**64 · Gifts for the Tall One** — 猫咪收集探索 · [源码](https://github.com/eyeb0l/catslop) ⭐ 0（2026-11-16）
扮演小岛上的猫，潜行捕猎并带回家换零食，购买装备、毛色和帽子；同仓库其他模型的运行不计入本条。
`three.js` · 无构建 · ⌨️ 暂无浏览器试玩链接，运行 `npm run serve` 后打开 `/runs/claude-fable-5-2/` · README 与 runs/claude-fable-5-2/NOTES.md 标明模型；这是作者的演示运行

**65 · Fight Ring** — 2D 模型对战格斗 · [源码](https://github.com/ganson-labs/fight-ring) ⭐ 0（2026-11-17）
Claude Fable 5.2 创作的 Цугцванг 对战 Gemini 4 Carbon 创作的 КАЙРОС；可观看可复现比赛，也可亲自挑战。`原生 JavaScript 2D 引擎` · 本地运行 `npm start` 后打开 <http://localhost:4848> · 多模型协作，Fable 负责其中一位斗士

**66 · The Blooming Dark** — 叙事解谜 · [源码](https://github.com/Pandaemonium/Psychedelia) ⭐ 0（2026-11-17）
六章夜间旅程，包含五类解谜；完成故事后解锁七个世界的自由万花筒。`HTML/CSS/JavaScript + WebGL` · 无构建，直接打开 `index.html` · 仓库 About 标注由 Fable 5.2 生成

**67 · Лисёнок и огненный жёлудь** — 2D 平台跳跃 · [源码](https://github.com/sashatchersunov6-rgb/lisenok-game) ⭐ 0（2026-11-17）
单文件横版平台游戏，键盘和手机触控均可操作。`Canvas 2D + Web Audio` · 无构建 · [Play Online Live Demo](https://sashatchersunov6-rgb.github.io/lisenok-game/) · 作者说明由 Claude Fable 5.2 编写

**68 · Gabriel's Sweet Town** — 亲子角色扮演沙盒 · [源码](https://github.com/chomachomachoma/candyland_pwa) ⭐ 0（2026-11-17）
在 17 个地点自由扮演、互动和探索，包含 240 多件可移动物品；安装后可离线游玩。`HTML/CSS/SVG + Web Audio` · PWA，无构建 · [Play Online Live Demo](https://chomachomachoma.github.io/candyland_pwa/) · 仓库 About 标注使用 Claude Code Fable 5.2

> 《回声游戏厅》合集的 13 款小游戏均由作者说明为 Claude Fable 5.2 制作；以下链接分别进入各自游戏。

**69 · 广州漂移（第 13 期）** — 3D 竞速 · [源码](https://github.com/zhgarylu/everyday-game) ⭐ 0（2026-11-17）
雨夜骑电动车在广州送外卖，穿光门接单送达并用漂移攒小费。`three.js 0.170 + JavaScript` · 无构建 · [Play Online Live Demo](https://zhgarylu.github.io/everyday-game/gz/)

**70 · 皮衣老黄（第 12 期）** — 回合制策略 · [源码](https://github.com/zhgarylu/everyday-game) ⭐ 0（2026-11-17）
在 12 个季度里经营芯片公司，通过研发、扩产和地盘争夺把市值拉回第一。`three.js 0.170 + JavaScript` · 无构建 · [Play Online Live Demo](https://zhgarylu.github.io/everyday-game/chip/)

**71 · 骑手（第 11 期）** — 3D 驾驶模拟 · [源码](https://github.com/zhgarylu/everyday-game) ⭐ 0（2026-11-17）
在老城骑车送外卖，赶订单时限并应对天气、车流、信号灯和突发路况。`three.js 0.170 + JavaScript` · 无构建 · [Play Online Live Demo](https://zhgarylu.github.io/everyday-game/rider/)

**72 · 怒砸办公室（第 10 期）** — 街机动作 · [源码](https://github.com/zhgarylu/everyday-game) ⭐ 0（2026-11-17）
在保安赶到前连续砸毁办公室物品，连击和怒气会提升破坏速度。`three.js 0.170 + JavaScript` · 无构建 · [Play Online Live Demo](https://zhgarylu.github.io/everyday-game/smash/)

**73 · 相亲角速配（第 9 期）** — 条件判断 · [源码](https://github.com/zhgarylu/everyday-game) ⭐ 0（2026-11-17）
按条件左右滑动判断候选人是否合适，条件会逐轮增加。`three.js 0.170 + JavaScript` · 无构建 · [Play Online Live Demo](https://zhgarylu.github.io/everyday-game/match/)

**74 · 夜市套圈（第 8 期）** — 街机技巧 · [源码](https://github.com/zhgarylu/everyday-game) ⭐ 0（2026-11-17）
用有限的套圈瞄准夜市摊位，争取圈中更值钱的物品。`three.js 0.170 + JavaScript` · 无构建 · [Play Online Live Demo](https://zhgarylu.github.io/everyday-game/ring/)

**75 · 捏泡泡纸（第 7 期）** — 休闲反应 · [源码](https://github.com/zhgarylu/everyday-game) ⭐ 0（2026-11-17）
划破泡泡纸争取连击与加时，避开带惩罚的泡泡。`three.js 0.170 + JavaScript` · 无构建 · [Play Online Live Demo](https://zhgarylu.github.io/everyday-game/pop/)

**76 · 挤地铁（第 6 期）** — 物理益智 · [源码](https://github.com/zhgarylu/everyday-game) ⭐ 0（2026-11-17）
在关门前把乘客推上车，同时先让下车的人通过。`three.js 0.170 + JavaScript` · 无构建 · [Play Online Live Demo](https://zhgarylu.github.io/everyday-game/metro/)

**77 · 摸鱼大师（第 5 期）** — 潜行反应 · [源码](https://github.com/zhgarylu/everyday-game) ⭐ 0（2026-11-17）
观察老板、摄像头和 HR 的动向，在工作场景里抓准摸鱼时机。`three.js 0.170 + JavaScript` · 无构建 · [Play Online Live Demo](https://zhgarylu.github.io/everyday-game/moyu/)

**78 · 搓澡大师（第 4 期）** — 街机技巧 · [源码](https://github.com/zhgarylu/everyday-game) ⭐ 0（2026-11-17）
在限时内搓掉顾客背上的泥，避开痛点并争取小费。`three.js 0.170 + JavaScript` · 无构建 · [Play Online Live Demo](https://zhgarylu.github.io/everyday-game/scrub/)

**79 · 吃啥拉啥（第 3 期）** — 动作街机 · [源码](https://github.com/zhgarylu/everyday-game) ⭐ 0（2026-11-17）
操纵小兽吃下不同食物，利用食物效果打倒身后的怪物。`three.js 0.170 + JavaScript` · 无构建 · [Play Online Live Demo](https://zhgarylu.github.io/everyday-game/eat/)

**80 · 清潮（第 2 期）** — 小队射击 · [源码](https://github.com/zhgarylu/everyday-game) ⭐ 0（2026-11-17）
带领自动开火的小队清除怪潮，并通过拾取强化队伍和武器。`three.js 0.170 + JavaScript` · 无构建 · [Play Online Live Demo](https://zhgarylu.github.io/everyday-game/tide/)

**81 · 晶塔守卫（第 1 期）** — 塔防策略 · [源码](https://github.com/zhgarylu/everyday-game) ⭐ 0（2026-11-17）
沿路线布置九种防御塔、释放大招并逐关解锁四张地图。`three.js 0.170 + JavaScript` · 无构建 · [Play Online Live Demo](https://zhgarylu.github.io/everyday-game/td/)

**134 · 天师摇人（第 14 期）** — 槽式塔防 · [源码](https://github.com/zhgarylu/everyday-game) ⭐ 3（2026-11-23）
在 3×3 功德机上摇出法器，抵御十波妖怪并守住结界；可炼化法器叠层、选择局间法宝。作者说明《回声游戏厅》14 款游戏均由 Claude Fable 5.2 制作。`HTML Canvas + JavaScript` · 无构建 · [在线玩](https://zhgarylu.github.io/everyday-game/merit/)

**82 · Apex Lap** — 3D 计时竞速 · [源码](https://github.com/ololo-dev/apex-lap-fable-5-2) ⭐ 1（2026-11-17）
单车单赛道计时，三轮任务逐步增加对竞速感和对手的要求。`three.js 0.187 + Vite 8` · [Play Online Live Demo](https://ololo-dev.github.io/apex-lap-fable-5-2/) · 作者说明由 Claude Fable 5.2 构建

**83 · Apex Lap: Blender Edition** — 3D 计时竞速 · [源码](https://github.com/ololo-dev/apex-lap-fable-5-2-blender) ⭐ 0（2026-11-17）
同一竞速题目的独立实现，Fable 5.2 通过 Blender MCP 制作赛车、赛道组件和场景并导出 glTF。`three.js 0.187 + Vite 8` · [Play Online Live Demo](https://ololo-dev.github.io/apex-lap-fable-5-2-blender/)

**84 · Raptor Race** — 3D 跑酷 · [源码](https://github.com/drew879/raptor-race-fable) ⭐ 0（2026-11-17）
以不同史前时代为背景，操纵有羽恐龙向前奔跑。`three.js 0.187 + TypeScript + Vite 8` · [Play Online Live Demo](https://drew879.github.io/raptor-race-fable/) · 仓库 About 说明本版本由 Fable 5.2 制作

**85 · Uno com escada（Fable 5.2 版）** — WebGPU 3D 赛车 · [源码](https://github.com/viktorkav/uno-com-escada) ⭐ 4（2026-11-17）
驾驶车顶绑着梯子的 Fiat Uno，在山路赛道竞速；同仓库另有 Opus 5.5 版本，本条只列 Fable 5.2 版。`原生 JavaScript + WebGPU` · 单文件 `fable/index.html` · [Play Online Live Demo](https://viktorkav.com.br/apoio/uno-com-escada/fable/)

**86 · 柑仔的晚霞航空信（Claude Fable 5.2 版）** — 2D 邮航游戏 · [源码](https://github.com/jambocoder159/ai-game-duel) ⭐ 0（2026-11-18）
与同仓库的《夕阳邮航》（GPT-6.2 Astra 版）使用同一组素材，是两个独立的模型版本。`Canvas 2D` · 无构建 · [试玩 Fable 5.2 版](https://jambocoder159.github.io/ai-game-duel/#fable)

---

## 五、Claude Fable 5.2 新作（39 款）

本节收录 39 款涉及 Claude Fable 5.2 的作品；多模型协作按作者公开说明标注。《Papertrails》是自由漫游体验，没有关卡目标。

**87 · Port Fable (Low)** — 低多边形岛屿开放世界，含车辆、船只、飞机、武器与通缉系统 · Claude Fable 5.2（Low） · [Windows 下载](https://github.com/Cryptopiy/Claude-Fable-5.2-Effort-Test-Open-World/releases/download/v1.0/PortFable-Low-Windows-x64.zip) · [源码](https://github.com/Cryptopiy/Claude-Fable-5.2-Effort-Test-Open-World/tree/main/games/1-low-port-fable) ⭐ 0（2026-11-19）
`Godot 4.7.2` · Windows x64 可执行文件与 Godot 源码

**88 · Port Cinder (Medium)** — 海岸岛屿沙盒，15 辆车，含航空、地铁、商店、车库、天气与警察系统 · Claude Fable 5.2（Medium） · [Windows 下载](https://github.com/Cryptopiy/Claude-Fable-5.2-Effort-Test-Open-World/releases/download/v1.0/PortCinder-Medium-Windows-x64.zip) · [源码](https://github.com/Cryptopiy/Claude-Fable-5.2-Effort-Test-Open-World/tree/main/games/2-medium-port-cinder) ⭐ 0（2026-11-19）
`Godot 4.7.2` · Windows x64 可执行文件与 Godot 源码

**89 · Marlow Bay (High)** — 八个街区的明亮城市，含交通、警察、航空、单轨列车与改装车库 · Claude Fable 5.2（High） · [Windows 下载](https://github.com/Cryptopiy/Claude-Fable-5.2-Effort-Test-Open-World/releases/download/v1.0/MarlowBay-High-Windows-x64.zip) · [源码](https://github.com/Cryptopiy/Claude-Fable-5.2-Effort-Test-Open-World/tree/main/games/3-high-marlow-bay) ⭐ 0（2026-11-19）
`Godot 4.7.2` · Windows x64 可执行文件与 Godot 源码

**90 · Neon Tide (Max)** — 霓虹夜景岛屿开放世界，含 19 辆车、17 种武器与电台 · Claude Fable 5.2（Max）；作者说明部分过程由 Claude Opus 5.5 继续 · [Windows 下载](https://github.com/Cryptopiy/Claude-Fable-5.2-Effort-Test-Open-World/releases/download/v1.0/NeonTide-Max-Windows-x64.zip) · [源码](https://github.com/Cryptopiy/Claude-Fable-5.2-Effort-Test-Open-World/tree/main/games/4-max-neon-tide) ⭐ 0（2026-11-19）
`Godot 4.7.2` · Windows x64 可执行文件与 Godot 源码

**91 · Cinder Bay (Extra)** — 含 21 辆车、掩体潜行、警察追捕、特技跳跃与计时赛的开放世界 · Claude Fable 5.2（Extra）；作者说明部分过程由 Claude Opus 5.5 继续 · [Windows 下载](https://github.com/Cryptopiy/Claude-Fable-5.2-Effort-Test-Open-World/releases/download/v1.0/CinderBay-Extra-Windows-x64.zip) · [源码](https://github.com/Cryptopiy/Claude-Fable-5.2-Effort-Test-Open-World/tree/main/games/5-extra-cinder-bay) ⭐ 0（2026-11-19）
`Godot 4.7.2` · Windows x64 可执行文件与 Godot 源码

**92 · Halcyon Bay (Ultracode)** — 八个街区、22 辆车、17 种武器，另有 Rodin 模型素材版 · Claude Fable 5.2（Ultracode）；作者说明部分过程由 Claude Opus 5.5 继续 · [Windows 下载](https://github.com/Cryptopiy/Claude-Fable-5.2-Effort-Test-Open-World/releases/download/v1.0/HalcyonBay-Ultracode-Windows-x64.zip) · [源码](https://github.com/Cryptopiy/Claude-Fable-5.2-Effort-Test-Open-World/tree/main/games/6-ultracode-halcyon-bay) ⭐ 0（2026-11-19）
`Godot 4.7.2` · Windows x64 可执行文件与 Godot 源码

**93 · Помехи / Pomehi (Low)** — 1987 年针叶林无线电中继站的生存恐怖游戏 · Claude Fable 5.2（Low） · [Windows 下载](https://github.com/Cryptopiy/Claude-Fable-5.2-vs-Opus-5.5-Horror-Games/releases/download/v1.0/Pomehi-Windows-x64.zip) · [源码](https://github.com/Cryptopiy/Claude-Fable-5.2-vs-Opus-5.5-Horror-Games/tree/main/games/1-pomehi-fable-low) ⭐ 0（2026-11-19）
`Godot 4.7.2` · Windows x64 可执行文件与 Godot 源码

**94 · ЛЕЕР / Leer (Max + Ultracode)** — 极地气象站的五夜恐怖游戏，含四种结局 · Claude Fable 5.2（Max + Ultracode） · [Windows 下载](https://github.com/Cryptopiy/Claude-Fable-5.2-vs-Opus-5.5-Horror-Games/releases/download/v1.0/Leer-Windows-x64.zip) · [源码](https://github.com/Cryptopiy/Claude-Fable-5.2-vs-Opus-5.5-Horror-Games/tree/main/games/2-leer-fable-max) ⭐ 0（2026-11-19）
`Godot 4.7.2` · Windows x64 可执行文件与 Godot 源码

**95 · Backrooms: The Complex** — 摄像机视角的后室恐怖游戏 · Claude Opus 5.5 与 Claude Fable 5.2（Ultracode）协作 · [Windows 下载](https://github.com/Cryptopiy/Claude-Opus-5.5-Backrooms/releases/download/v1.0/BackroomsComplex-Windows-x64.zip) · [源码](https://github.com/Cryptopiy/Claude-Opus-5.5-Backrooms/tree/main/games/backrooms-the-complex) ⭐ 0（2026-11-19）
`Godot 4.7.2` · Windows x64 可执行文件与 Godot 源码

**96 · LAST LIGHT — Rooftop Run** — 高楼屋顶计时跑酷；Model Arena 的 Fable 5.2 独立版本，与 Astra、Opus、Sol 使用同一提示词 · Claude Fable 5.2（High） · [浏览器试玩](https://clockendbader.github.io/model-arena/) · [源码](https://github.com/clockendbader/model-arena/tree/main/fable-5.2/parkour) ⭐ 0（2026-11-19）
`Canvas 2D` · 无构建 · 单文件 HTML

**97 · Papertrails** — 纸艺立体书风格的自由漫游世界，支持地图、昼夜与视角切换；作者称无胜负目标 · Claude Fable 5.2 与 Claude Opus 5.5 协作 · [浏览器试玩](https://xikhar.github.io/papertrails/) · [作者模型说明](https://x.com/xikhar/status/2122682962647122403) · [源码](https://github.com/xikhar/papertrails) ⭐ 83（2026-11-19）
`Three.js 0.187` · Vite 8.3.8 · 浏览器站点 · 无需下载源码


**98 · Boo-mas** — 在雪花球星球上绕行，用灯串闭合圈点亮地表、躲避 Humbugs，在午夜前救下圣诞 · Claude Fable 5.2（作者称单提示词、Max thinking） · [在线试玩](https://robinduckett.github.io/boo-mas/) · [源码](https://github.com/robinduckett/boo-mas) ⭐ 1（2026-11-20）
`Three.js r187` · 无构建，ES modules · [作者模型说明](https://news.ycombinator.com/item?id=50553152)

**99 · Wildlife Odyssey 3D — The Living World** — 东南亚野生动物探索与科学发现：观察 36 种动物、拍摄、识别物种并建立野外日志 · Claude Fable 5.2（仓库 About 标为模型测试） · [源码](https://github.com/quanap5/wildlife-odyssey-3d) ⭐ 1（2026-11-20）
`React 19 + TypeScript 6 + Three.js r187 + React Three Fiber 9` · Vite 8 · 本地运行：Node.js 20.19+，`npm install && npm run dev`

**100 · 星烬原野 · Demo** — 八位可切换角色的 3D 开放世界动作 demo，包含探索、战斗、采集与区域任务 · Claude Fable 5.2 · [源码](https://github.com/weit0529/gamedemo_by_Fable5.2) ⭐ 1（2026-11-20）
`TypeScript 7 + Three.js 0.187 + WebGL 2` · Vite 8.3.8 · 本地运行：Node.js 20.19+，`npm install && npm run dev`

**101 · Space 2601AE** — 九个星区中的太空贸易、货运任务、飞船战斗与存档战役；作者将它作为多模型长期协作基准 · Claude Fable 5.2、GPT-6.2 Astra 等模型协作（[作者模型日志](https://github.com/AJankovic234/fable-space-engine#change-log)） · [源码](https://github.com/AJankovic234/fable-space-engine) ⭐ 0（2026-11-20）
`F# + Fable 5.2 + WebGL 2` · Vite 8.3.8 · 本地运行需 .NET SDK 10 与 Node.js 22.12+：`npm install`、`npm run restore`、`npm run dev`

**123 · Lantern Drift · 天灯漂流（Claude Fable 5.2 第二回合）** — 与 GPT-6.2 Astra 使用同一任务、同一 GG-skills v4.0 技能包分别生成的独立版本；剪纸画风，美术由 Fable 通过 Codex 调用 GPT 图片生成；作者记录跑到 47 分钟上限被停下，介入 1 次请它收尾 · Claude Fable 5.2 · [在线试玩](https://jambocoder159.github.io/ai-game-duel/#r2-fable) · [Fable 构建目录](https://github.com/jambocoder159/ai-game-duel/tree/main/versions/r2-fable) ⭐ 0（2026-11-20）
`React 19 + TypeScript` · 仓库提供预构建静态包 · 浏览器静态站点与 assets · [作者模型对照说明](https://github.com/jambocoder159/ai-game-duel)

**126 · Mall Action（Claude Fable 5.2 版）** — 商场多层横版谍战 + 俯视角店铺搜索；与 Astra、Opus 等版本分支分开记录。分支说明记录：Claude Code（开启 advisor 工具）约 1 小时 15 分，无人工介入，151 个自动化测试 · Claude Fable 5.2 · [在线试玩](https://rlorca.github.io/mall-action/fable-5.2/) · [Fable 源码分支](https://github.com/rlorca/mall-action/tree/fable-5-2) ⭐ 0（2026-11-20）
`TypeScript + WebGL` · Vite 构建 · 所有像素图、字体、音乐由代码生成

**128 · Crash Quota** — 60 秒内驾驶撞车：跑完 3 圈、撞毁 5 辆失控原型车或撞倒 40 个假人均可通关 · Claude Fable 5.2（Max Ultracode） · [在线试玩](https://smashi.app/arcade/crash-quota-fable/) · [构建页](https://smashi.app/games/carmageddon/crash-quota-fable/) · [源码](https://github.com/Mythfinity/crash-quota-fable) ⭐ 0（2026-11-21）
`原生 JavaScript + WebGL 2` · 无构建 · 多文件 ES modules；README 披露约 3 小时 30 分、222 个自动化测试

**129 · NIGHTSHIFT: Survive the Midnight（Claude Fable 5.2 版）** — 夜雨高速驾驶，穿过车流、用氮气加速并躲避油罐车事故 · Claude Fable 5.2（Extra-high）；Claude Opus 5.5 子 Agent 参与 · [浏览器试玩](https://eddizege.github.io/nightshift-fable/) · [同提示词对照说明](https://lab.edizegemercan.com/posts/nightshift-gemini-4-carbon-vs-claude-fable-5-2/) · [Fable 源码](https://github.com/EddizEge/nightshift-fable) ⭐ 0（2026-11-21）
`TypeScript + Three.js 0.187 + Rapier + WebGL 2` · Vite · 浏览器静态站点；作者称约 16 小时 36 分，由 Fable 主导、Opus 子 Agent 协作

**135 · Loamlands** — 方块建造生存游戏；与 Opus 5.5 版本使用同一提示词和时限 · Claude Fable 5.2 · [浏览器试玩](https://modelbehavioryt.github.io/fable-vs-opus-block-game/fable/) · [Fable 源码](https://github.com/ModelBehaviorYT/fable-vs-opus-block-game/tree/main/fable) ⭐ 0（2026-11-23）
`Three.js 0.160` · 无构建 · 多文件静态站点；作者称代码由模型独立编写

**137 · Saltline Brawl** — 单关卡清版动作游戏；七分钟生成的复古街机打斗 demo · Claude Fable 5.2（Medium） · [浏览器试玩](https://smashi.app/arcade/saltline-brawl-fable/) · [作者构建页](https://smashi.app/games/cadillacs-and-dinosaurs/saltline-brawl-fable/) · [源码](https://github.com/Mythfinity/saltline-brawl-fable) ⭐ 0（2026-11-23）
`HTML Canvas + 原生 JavaScript + Web Audio` · 无构建 · 多文件静态站点；作者说明这是原创作品，未复用原作角色、美术、音乐或关卡

**151 · Cinderwatch** — 五地等距塔防；AI 指挥官自动迎战，也可随时接管 · Claude Fable 5.2 · [浏览器试玩](https://kevintngo.github.io/cinderwatch/) · [模型生成提交](https://github.com/kevintngo/cinderwatch/commit/6640b81286df8b1fd2e5a745b48211c4a9323f83) · [源码与说明](https://github.com/kevintngo/cinderwatch) ⭐ 54（2026-11-25）
`自制等距 3D 渲染 · 无构建 · 单文件 HTML`

**152 · Brushwild** — 手绘风开放世界 RPG：行走、战斗、拾取装备并升级，地形持续生成 · Claude Fable 5.2 · [浏览器试玩](https://kevintngo.github.io/procedural-rpg/) · [模型生成提交](https://github.com/kevintngo/procedural-rpg/commit/8078241d536193a43468b6e56f6fbf91172b86c8) · [源码与说明](https://github.com/kevintngo/procedural-rpg) ⭐ 5（2026-11-25）
`自制 WebGL shader · 无构建 · 浏览器静态站点`

**153 · 雪迹 · Cold Smoke** — 无尽下坡滑雪；画面与音效均由代码生成 · Claude Fable 5.2 · [浏览器试玩](https://huisky.xyz/cold-smoke/play) · [源码与说明](https://github.com/huiskylabs/cold-smoke) ⭐ 59（2026-11-25）
`Canvas 2D + Web Audio · 无构建 · 单文件 HTML`

**154 · Grand Tel Aviv 6** — 以色列特拉维夫开放世界浏览器游戏 · Claude Fable 5.2 · [浏览器试玩](https://grand-tel-aviv-6.web.app) · [源码与说明](https://github.com/LorelDev/grand-tel-aviv-6) ⭐ 0（2026-11-25）
`Three.js · npm run dev · 浏览器站点`

**155 · UNWRITTEN** — ASCII 动作游戏：探索五片大陆的开放世界 · Claude Fable 5.2 · [浏览器试玩](https://tetriss22.github.io/unwritten/) · [源码与说明](https://github.com/Tetriss22/unwritten) ⭐ 0（2026-11-25）
`Canvas 2D · 无构建 · GitHub Pages 静态站点`

**156 · 叠塔（Tower Stack）** — 点击叠放方块，尽量把塔搭高 · Claude Fable 5.2 · [源码与说明](https://github.com/YHY-coding/fable-works/tree/main/tower/) ⭐ 0（2026-11-25）
`HTML Canvas · 无构建 · 单文件 HTML（本地打开）`

**157 · 光的顺序（Simon 记忆游戏）** — 记住灯光与音符的顺序并重复输入 · Claude Fable 5.2 · [源码与说明](https://github.com/YHY-coding/fable-works/tree/main/simon/) ⭐ 0（2026-11-25）
`HTML + Web Audio · 无构建 · 单文件 HTML（本地打开）`

**158 · Palmera Heat** — GTA 风格犯罪题材开放世界；步行、驾驶与射击 · Claude Fable 5.2 · [浏览器试玩](https://modelbehavioryt.github.io/claude-vs-chatgpt-ai-games/browser/claude/) · [源码与说明](https://github.com/ModelBehaviorYT/claude-vs-chatgpt-ai-games) ⭐ 0（2026-11-25）
`WebGL 3D · 无构建 · 浏览器静态站点`

**159 · NeonCoast** — Fable 5.2 制作的 Unreal Engine 5.8 开放世界游戏 · Claude Fable 5.2 · [源码与说明](https://github.com/ModelBehaviorYT/claude-vs-chatgpt-ai-games) ⭐ 0（2026-11-25）
`Unreal Engine 5.8 · Unreal Engine 5.8 · Windows x64 游戏包 + Unreal 源项目 · [Windows 发布包](https://github.com/ModelBehaviorYT/claude-vs-chatgpt-ai-games/releases/latest)`

**160 · Beatbound** — 单键节奏平台跳跃：跟随节拍跳过障碍 · Claude Fable 5.2 · [浏览器试玩](https://modelbehavioryt.github.io/claude-vs-chatgpt-dash-game/claude/) · [源码与说明](https://github.com/ModelBehaviorYT/claude-vs-chatgpt-dash-game) ⭐ 0（2026-11-25）
`HTML Canvas · 无构建 · 浏览器静态站点`

**161 · Turbo Critters** — 一分钟完成的卡丁车竞速 · Claude Fable 5.2 · [浏览器试玩](https://modelbehavioryt.github.io/claude-ai-kart-racer/1-minute/) · [源码与说明](https://github.com/ModelBehaviorYT/claude-ai-kart-racer) ⭐ 0（2026-11-25）
`浏览器 Canvas · 无构建 · 浏览器静态站点`

**162 · Zoomie Dash Grand Prix** — 十分钟时限的卡丁车竞速 · Claude Fable 5.2 · [浏览器试玩](https://modelbehavioryt.github.io/claude-ai-kart-racer/10-minutes/) · [源码与说明](https://github.com/ModelBehaviorYT/claude-ai-kart-racer) ⭐ 0（2026-11-25）
`浏览器 Canvas · 无构建 · 浏览器静态站点`

**163 · Turbo Pals Grand Prix** — 一小时制作的卡丁车竞速版本 · Claude Fable 5.2 · [浏览器试玩](https://modelbehavioryt.github.io/claude-ai-kart-racer/1-hour/) · [源码与说明](https://github.com/ModelBehaviorYT/claude-ai-kart-racer) ⭐ 0（2026-11-25）
`浏览器 Canvas · 无构建 · 浏览器静态站点`

**164 · Atlantis** — 用 WebGPU 在水下遗迹中自由飞行探索 · Claude Fable 5.2 · [浏览器试玩](https://noniv.github.io/atlantis/) · [源码与说明](https://github.com/Noniv/atlantis) ⭐ 133（2026-11-25）
`WebGPU · 无构建 · 浏览器 ES modules 站点`

**165 · Jet Arm** — 驾驶战机发射导弹、翻滚并穿过海面水雾 · Claude Fable 5.2 · [浏览器试玩](https://last-light-arcade.2020124002.workers.dev/jet-arm/) · [源码与说明](https://github.com/LeeHongji/last-light-arcade) ⭐ 0（2026-11-25）
`Canvas 2D · 无构建 · 单文件 HTML / Workers`

**166 · Knee Down** — 摩托竞速：倾身过弯、切换赛道并冲过海岸公路 · Claude Fable 5.2 · [浏览器试玩](https://last-light-arcade.2020124002.workers.dev/#knee-down) · [源码与说明](https://github.com/LeeHongji/last-light-arcade) ⭐ 0（2026-11-25）
`Canvas 2D · 无构建 · 单文件 HTML / Workers`

**167 · Dusk Rotor** — 驾驶武装直升机，在城市峡谷间发射火箭 · Claude Fable 5.2 · [浏览器试玩](https://last-light-arcade.2020124002.workers.dev/dusk-rotor/) · [源码与说明](https://github.com/LeeHongji/last-light-arcade) ⭐ 0（2026-11-25）
`Canvas 2D · 无构建 · 单文件 HTML / Workers`

**168 · Dusk Depths** — 驾驶潜艇锁定航母，在水下调整深度并发射鱼雷 · Claude Fable 5.2 · [浏览器试玩](https://last-light-arcade.2020124002.workers.dev/dusk-depths/) · [源码与说明](https://github.com/LeeHongji/last-light-arcade) ⭐ 0（2026-11-25）
`Canvas 2D · 无构建 · 多文件静态网页 / Workers`

### 附：同款对照中的 Claude Opus 5.5 版本（4 款）

以下作品与本清单已收录的 Claude Fable 5.2 / GPT-6.2 Astra 版本使用同一提示词，单独记录以便对照。

**124 · HIGHLINE — A Rooftop Run at Golden Hour** — 高楼屋顶计时跑酷；Model Arena 的 Opus 5.5 独立版本，与 Fable（#96）、Astra（#109）、Sol 使用同一提示词，Arena 记录用时 55 分钟 · Claude Opus 5.5（High） · [浏览器试玩](https://clockendbader.github.io/model-arena/opus-5.5/parkour/) · [源码](https://github.com/clockendbader/model-arena/tree/main/opus-5.5/parkour) ⭐ 0（2026-11-20）
`Three.js r170 + WebGL` · 无构建 · 多文件静态站点 · 仅桌面键鼠

**125 · The Tallow Deep** — 单文件第一人称恐怖 roguelike，提灯下探十层；与 Saltwake（#112）同一基准提示词，作者个人排名 21 个作品中第一 · Claude Code · Opus 5.5 Max · [在线试玩](https://chojondocho.github.io/single-html-game-bench/claudecode-opus-5-5-max.html) · [源码文件](https://github.com/chojondocho/single-html-game-bench/blob/main/claudecode-opus-5-5-max.html) ⭐ 11（2026-11-20）
`HTML + WebGL 2` · 无构建 · 单文件 HTML · [作者模型与提示词说明](https://github.com/chojondocho/single-html-game-bench#prompt-used)

**127 · Mall Action（Claude Opus 5.5 版）** — 商场多层横版谍战 + 俯视角店铺搜索；与 Fable（#126）、Astra（#113）版本分支分开记录 · Claude Opus 5.5 · [在线试玩](https://rlorca.github.io/mall-action/opus-5.5/) · [Opus 源码分支](https://github.com/rlorca/mall-action/tree/opus-5-5) ⭐ 0（2026-11-20）
`JavaScript + PixiJS 8` · Vite 构建 · 无素材文件，300+ 单元测试

**136 · Blockhaven** — 方块建造生存游戏；与 Fable 5.2 的 Loamlands 使用同一提示词和时限 · Claude Opus 5.5 · [浏览器试玩](https://modelbehavioryt.github.io/fable-vs-opus-block-game/opus/) · [Opus 源码](https://github.com/ModelBehaviorYT/fable-vs-opus-block-game/tree/main/opus) ⭐ 0（2026-11-23）
`Three.js 0.170` · 无构建 · 多文件静态站点

---

## 六、GPT-6.2 Astra 作品（41 款）

**102 · 夕阳邮航（GPT-6.2 Astra 版）** — 2D 邮航游戏 · [源码](https://github.com/jambocoder159/ai-game-duel) ⭐ 0（2026-11-18）
与同仓库的《柑仔的晚霞航空信》（Claude Fable 5.2 版）使用同一组素材，是独立的 Astra 模型版本。`Canvas 2D` · 无构建 · [试玩 GPT-6.2 Astra 版](https://jambocoder159.github.io/ai-game-duel/#astra)

**103 · Santa Express: Chimney Panic!** — 3D 圣诞街机游戏 · [源码](https://github.com/thestringtheories/Santa-Game) ⭐ 0（2026-11-18）
作者说明首个可玩原型由一个提示词交给 GPT-6.2 Astra 生成，后续又完成电影感画面迭代。`three.js 0.186 + TypeScript + WebGL 2` · Vite 构建 · [在线试玩](https://thestringtheories.github.io/Santa-Game/)

**104 · Operation Fracture** — 离线第一人称区域作战游戏；作者标注为模型能力测试产物 · GPT-6.2 Astra · [离线试玩包](https://github.com/Thweki/operation-fracture/releases) · [源码](https://github.com/Thweki/operation-fracture) ⭐ 0（2026-11-19）
`Three.js 0.187 + WebGL 2` · esbuild 0.28.2 · ZIP 中的单文件 HTML（需桌面浏览器）

**105 · Tidepost（潮邮局）** — 中文像素风航邮冒险，包含实时邮航与回合制海图解谜 · GPT-6.2 Astra · [桌面版与 Web 下载包](https://github.com/Thweki/tidepost/releases) · [源码](https://github.com/Thweki/tidepost) ⭐ 0（2026-11-19）
`Godot 4.7.2` · macOS、Windows、Linux 桌面版及 Web ZIP；预发布

**106 · Blackburn Type D** — 驾驶 1912 年 Blackburn Type D 穿越四个圆环 · GPT-6.2 Astra · [浏览器试玩](https://blackburn-flight.pages.dev/) · [离线单文件版](https://github.com/Dun4ev/blackburn-flight/releases/latest/download/Blackburn-Flight.html) · [源码](https://github.com/Dun4ev/blackburn-flight) ⭐ 0（2026-11-19）
`Three.js 0.186.1 + WebGL` · Python 构建脚本 + esbuild · Cloudflare Pages 站点

**107 · Spillway Run** — 可设计球洞的迷你高尔夫，支持真实物理、计杆与标准杆 · GPT-6.2 Astra（X-High，单提示词） · [浏览器试玩](https://kostikoneuro.github.io/astra-6-2-solo/4-minigolf/?lang=ru) · [源码](https://github.com/KostiKoNeuro/astra-6-2-solo/tree/main/4-minigolf) ⭐ 0（2026-11-19）
`HTML + Canvas 2D` · 无构建 · 浏览器小游戏

**108 · Hamster Colony（仓鼠群落）** — 低多边形笼舍里的仓鼠会自行觅食、饮水、奔轮、社交、繁殖和老化；可暂停、调速、查看个体状态 · GPT-6.2 Astra（X-High，单提示词） · [浏览器试玩](https://kostikoneuro.github.io/astra-6-2-solo/5-hamsters/?lang=ru) · [源码](https://github.com/KostiKoNeuro/astra-6-2-solo/tree/main/5-hamsters) ⭐ 0（2026-11-19）
`Three.js`（CDN）· 无构建 · 单文件 HTML

**109 · Dusk Runner — Rooftop Time Trial** — 高楼屋顶计时跑酷；Model Arena 的 GPT-6.2 Astra 独立版本，与 Fable、Opus、Sol 使用同一提示词 · GPT-6.2 Astra（High） · [浏览器试玩](https://clockendbader.github.io/model-arena/) · [源码](https://github.com/clockendbader/model-arena/tree/main/astra-6.2/parkour) ⭐ 0（2026-11-19）
`Three.js + WebGL` · 无构建 · 多文件静态站点

**110 · Uno com escada（GPT-6.2 Astra 版）** — 同仓库 Fable 与 Opus 版本使用相同需求的独立实现 · GPT-6.2 Astra · [浏览器试玩](https://viktorkav.com.br/apoio/uno-com-escada/astra/) · [源码](https://github.com/viktorkav/uno-com-escada) ⭐ 135（2026-11-19）
`原生 JavaScript + WebGPU` · 无构建 · 单文件 HTML

**111 · FAULTLINE — Cold Relay** — 一句话生成的第一人称射击，冷色调无线电站小关卡 · GPT-6.2 Astra（X-High） · ⌨️ 暂无线上试玩；按作者说明下载或 clone 后，用 Chrome / Edge 打开 `index.html` · [源码目录](https://github.com/Yari-tuber/gpt62-vs-opus55-tests/tree/main/05_%E4%B8%80%E5%8F%A5%E8%AF%9D3A%E5%B0%84%E5%87%BB/gpt-6.2-astra) ⭐ 0（2026-11-19）
`WebGL 2 + GLSL` · 无构建 · 单文件 HTML（约 88 KB）


**112 · Saltwake: The Drowned Abbey** — 单文件恐怖 RPG / roguelike，深入沉没修道院；该版本是统一提示词、无迭代修改的 Codex GPT-6.2 Astra Max 基准产物 · [在线试玩](https://chojondocho.github.io/single-html-game-bench/codex-gpt-6-2-astra-max.html) · [源码文件](https://github.com/chojondocho/single-html-game-bench/blob/main/codex-gpt-6-2-astra-max.html) ⭐ 11（2026-11-20）
`HTML` · 无构建 · 单文件游戏 · [作者模型与提示词说明](https://github.com/chojondocho/single-html-game-bench#prompt-used)

**113 · Mall Action（GPT-6.2 Astra xhigh 版）** — 商场多层横版动作游戏：搜寻目标、射击、跳踢间谍并完成逃离任务；与其他模型版本分支分开记录 · GPT-6.2 Astra（xhigh） · [在线试玩](https://rlorca.github.io/mall-action/gpt-6.2-astra-xhigh/) · [Astra 源码分支](https://github.com/rlorca/mall-action/tree/gpt-6-2-astra-xhigh) ⭐ 0（2026-11-20）
`JavaScript + Canvas 2D` · Node 构建脚本生成单 HTML · [作者模型与实测说明](https://github.com/rlorca/mall-action/tree/gpt-6-2-astra-xhigh)

**114 · Lantern Drift · 天灯漂流（GPT-6.2 Astra 第二回合）** — 与 Fable 5.2 使用同一任务、分别生成的独立游戏版本；作者记录 Astra 用时 42 分 11 秒、零人工介入 · [在线试玩](https://jambocoder159.github.io/ai-game-duel/#r2-astra) · [Astra 构建目录](https://github.com/jambocoder159/ai-game-duel/tree/main/versions/r2-astra) ⭐ 0（2026-11-20）
`React 19 + TypeScript` · 仓库提供预构建静态包 · [作者模型对照说明](https://github.com/jambocoder159/ai-game-duel)

**115 · Undertow FM（逆潮电台）** — 中文单人像素横版冒险游戏源码快照；作者明确标为 GPT-6.2 Astra 能力测试产物，并说明它不是成熟成品 · GPT-6.2 Astra · [桌面与 Web 下载包](https://github.com/Thweki/undertow-fm/releases/tag/v1.0.0-preview) · [源码与运行说明](https://github.com/Thweki/undertow-fm) ⭐ 0（2026-11-20）
`Godot 4.7.2` · 暂无托管试玩页；作者提供 macOS、Windows、Linux 和 Web ZIP，也可用 Godot 打开 `project.godot` 并运行 `game/Main.tscn`

**116 · Pocket Roads: Midnight Pass** — 瑞士阿尔卑斯山午夜山道计时赛，左右转向并完成路线挑战 · GPT-6.2 Astra · [在线试玩](https://aartiles.github.io/local-model-benchmarks-site/demos/pocket-roads/) · [源码目录](https://github.com/aartiles/local-model-benchmarks-site/tree/main/demos/pocket-roads) · [作者模型说明](https://x.com/aartiles24/status/2122811749019824368) ⭐ 0（2026-11-20）
`HTML + CSS + JavaScript + SVG` · 多文件静态站点

**117 · Flying Anglia** — 在 ESP32-S3 触摸屏上倾斜操控蓝色 Anglia 飞过山谷，在蒸汽火车进隧道前追上它 · GPT-6.2 Astra · [源码与硬件运行说明](https://github.com/baturyilmaz/flying-anglia) ⭐ 0（2026-11-20）
`TypeScript + Gea3D` · 无浏览器试玩；需 Waveshare ESP32-S3 Touch AMOLED 2.06 硬件、Node.js 24 与 ESP-IDF 6

**118 · Bitcade Pac-Man（GPT-6.2 Astra 版）** — 同一短提示词下的 Pac-Man 迷宫追逐独立模型构建；实验记录注明 Codex API-key fair-cell 与 high effort · [在线试玩](https://jonclegg.github.io/pacman-bakeoff/entries/gpt-6.2-astra.html) · [源码文件](https://github.com/jonclegg/pacman-bakeoff/blob/main/entries/gpt-6.2-astra.html) ⭐ 5（2026-11-20）
`HTML + Canvas 2D` · 无构建 · 单文件 HTML · [模型运行记录](https://github.com/jonclegg/pacman-bakeoff/blob/main/entries/meta.json)

**119 · Fault in the Bath** — 旋转九块瓷砖，让断开的同心圆纹样重新对齐 · GPT-6.2 Astra · [在线试玩](https://miaai-lab.github.io/GPT-6.2-Astra-100-HTML-Files/009-tile-fault.html) · [单文件源码](https://github.com/MiaAI-Lab/GPT-6.2-Astra-100-HTML-Files/blob/main/009-tile-fault.html) ⭐ 0（2026-11-20）
`HTML + CSS + JavaScript` · 无构建 · 单文件 HTML

**120 · The Chalk Yard** — 把移动中的粉笔石板落在堆叠物上，累计七层并避免失衡 · GPT-6.2 Astra · [在线试玩](https://miaai-lab.github.io/GPT-6.2-Astra-100-HTML-Files/042-chalk-quarry.html) · [单文件源码](https://github.com/MiaAI-Lab/GPT-6.2-Astra-100-HTML-Files/blob/main/042-chalk-quarry.html) ⭐ 0（2026-11-20）
`HTML + CSS + JavaScript` · 无构建 · 单文件 HTML

**121 · The Patient Egg** — 调整平衡梁坡度，让滚动的鸡蛋在窝中稳定两秒 · GPT-6.2 Astra · [在线试玩](https://miaai-lab.github.io/GPT-6.2-Astra-100-HTML-Files/074-egg-balance.html) · [单文件源码](https://github.com/MiaAI-Lab/GPT-6.2-Astra-100-HTML-Files/blob/main/074-egg-balance.html) ⭐ 0（2026-11-20）
`HTML + CSS + JavaScript` · 无构建 · 单文件 HTML

**122 · The Keyless Works** — 逐齿转动黄铜齿轮，让两处校准线对齐并锁住定位销 · GPT-6.2 Astra · [在线试玩](https://miaai-lab.github.io/GPT-6.2-Astra-100-HTML-Files/097-lockstep.html) · [单文件源码](https://github.com/MiaAI-Lab/GPT-6.2-Astra-100-HTML-Files/blob/main/097-lockstep.html) ⭐ 0（2026-11-20）
`HTML + CSS + JavaScript` · 无构建 · 单文件 HTML

**138 · 荆棘誓约 · 黑棘森林** — 3D 剑盾战斗 demo：近战积攒怒气，用突进斩、回旋飞盾与旋风斩击败半兽人和首领 · GPT-6.2 Astra（Ultra） · [浏览器试玩](https://chan-yuu.github.io/thornbound-gpt-6.2-astra-ultra/) · [源码与模型说明](https://github.com/chan-yuu/thornbound-gpt-6.2-astra-ultra) ⭐ 0（2026-11-23）
`HTML5 + Three.js（CDN）` · 无构建 · 多文件静态站点

**148 · Solar Drift** — 驾驶悬浮摩托穿越沙漠峡谷计时赛：漂移、加速并通过 12 道路标 · GPT-6.2 Astra（Codex，作者称 6 次提示词、未手写代码） · [浏览器试玩](https://souranyp-stack.github.io/solar-drift/) · [源码、提示词与本地运行说明](https://github.com/souranyp-stack/solar-drift) ⭐ 0（2026-11-23）
`Three.js + WebGL` · Vite · 浏览器静态站点

---

**169 · Sundown Syndicate: Port Azure** — GTA 风格开放世界犯罪游戏；步行、驾驶与射击 · GPT-6.2 Astra · [浏览器试玩](https://modelbehavioryt.github.io/claude-vs-chatgpt-ai-games/browser/chatgpt/) · [源码与说明](https://github.com/ModelBehaviorYT/claude-vs-chatgpt-ai-games) ⭐ 0（2026-11-25）
`WebGL 3D · 无构建 · 浏览器静态站点`

**170 · Sunbreak** — GPT-6.2 Astra 制作的 Unreal Engine 5.8 开放世界游戏 · GPT-6.2 Astra · [源码与说明](https://github.com/ModelBehaviorYT/claude-vs-chatgpt-ai-games) ⭐ 0（2026-11-25）
`Unreal Engine 5.8 · Unreal Engine 5.8 · Windows x64 游戏包 + Unreal 源项目 · [Windows 发布包](https://github.com/ModelBehaviorYT/claude-vs-chatgpt-ai-games/releases/latest)`

**171 · Slipwake · Relay Yard** — 离线 3v3 竞技场格斗：与两名队友对抗对方小队 · GPT-6.2 Astra · [源码与说明](https://github.com/Itckt/token-burn-games/tree/main/games/002) ⭐ 0（2026-11-25）
`Raw WebGL · 无构建 · 多文件网页（本地浏览器） · 本地指令见子目录 README`

**172 · Neon Causeway** — 三分钟双路线卡牌对战，争夺两侧桥面上的控制塔 · GPT-6.2 Astra · [源码与说明](https://github.com/Itckt/token-burn-games/tree/main/games/003) ⭐ 0（2026-11-25）
`HTML + CSS + JavaScript · 无构建 · 多文件网页（本地浏览器） · 本地指令见子目录 README`

**173 · Twistlab** — 可手动转动并观察自动求解的 3×3×3 魔方谜题 · GPT-6.2 Astra · [源码与说明](https://github.com/Itckt/token-burn-games/tree/main/games/007) ⭐ 0（2026-11-25）
`Three.js / WebGL · 无构建 · 多文件网页（本地浏览器） · 本地指令见子目录 README`

**174 · Loop Foundry** — 拼装弹珠轨道并以最快时间冲过终点旗 · GPT-6.2 Astra · [源码与说明](https://github.com/Itckt/token-burn-games/tree/main/games/009) ⭐ 0（2026-11-25）
`Three.js / WebGL · 无构建 · 多文件网页（本地浏览器） · 本地指令见子目录 README`

**175 · Street Cantonese · 街談** — 40 条香港俚语口袋词典，并带俗语小测 · GPT-6.2 Astra · [源码与说明](https://github.com/Itckt/token-burn-games/tree/main/games/080) ⭐ 0（2026-11-25）
`HTML + CSS + JavaScript · 无构建 · 多文件网页（本地浏览器） · 本地指令见子目录 README`

**176 · The Eleventh Morning** — 十天期限内决定如何使用 AI token 资助，并帮助角色解决社区问题的文字冒险 · GPT-6.2 Astra · [源码与说明](https://github.com/Itckt/token-burn-games/tree/main/games/018) ⭐ 0（2026-11-25）
`终端文字游戏 · Python · Python CLI · 本地指令见子目录 README`

**177 · Gutterlight Relay** — 在两条路线部署夜间队伍、管理能量并争夺塔点的卡牌战斗 · GPT-6.2 Astra · [源码与说明](https://github.com/Itckt/token-burn-games/tree/main/games/034) ⭐ 0（2026-11-25）
`终端文字游戏 · Python · Python CLI · 本地指令见子目录 README`

**178 · Pinchline Six** — 选择三名英雄，在收缩的场地上进行 3v3 自动战斗 · GPT-6.2 Astra · [源码与说明](https://github.com/Itckt/token-burn-games/tree/main/games/035) ⭐ 0（2026-11-25）
`终端 ASCII 战场 · Python · Python CLI · 本地指令见子目录 README`

**179 · Kowloon Stack** — 在 10×20 井中拼放方块、消除完整横行 · GPT-6.2 Astra · [源码与说明](https://github.com/Itckt/token-burn-games/tree/main/games/040) ⭐ 0（2026-11-25）
`终端字符界面 · Node.js · Node.js CLI · 本地指令见子目录 README`

**180 · Terminal Snake** — 控制蛇吃点心、增长身体，撞墙或撞到自己即结束 · GPT-6.2 Astra · [源码与说明](https://github.com/Itckt/token-burn-games/tree/main/games/041) ⭐ 0（2026-11-25）
`终端字符界面 · Node.js · Node.js CLI · 本地指令见子目录 README`

**181 · 2048 | Kowloon Tong study break** — 在终端玩 2048，可请求提示或让 expectimax AI 接手 · GPT-6.2 Astra · [源码与说明](https://github.com/Itckt/token-burn-games/tree/main/games/042) ⭐ 0（2026-11-25）
`终端字符界面 · Python · Python CLI · 本地指令见子目录 README`

**182 · Tic-tac-toe and Connect Four** — 井字棋与四子棋，可对战 minimax AI 或双人同机游玩 · GPT-6.2 Astra · [源码与说明](https://github.com/Itckt/token-burn-games/tree/main/games/043) ⭐ 0（2026-11-25）
`终端字符界面 · Python · Python CLI · 本地指令见子目录 README`

**183 · Steamfold Noodle Works** — 经营即食面工厂：升级机器、完成订单并争取 Brass Ladle 特许 · GPT-6.2 Astra · [源码与说明](https://github.com/Itckt/token-burn-games/tree/main/games/058) ⭐ 0（2026-11-25）
`终端字符界面 · Python · Python CLI · 本地指令见子目录 README`

**184 · Friday, Filed** — 终端单人自由职业接单模拟，在一周内完成工作并收款 · GPT-6.2 Astra · [源码与说明](https://github.com/Itckt/token-burn-games/tree/main/games/079) ⭐ 0（2026-11-25）
`终端文字游戏 · Python · Python CLI · 本地指令见子目录 README`

**185 · Study Break Blackjack** — 用基本策略机器人对抗六副牌庄家，模拟下注、分牌与加倍 · GPT-6.2 Astra · [源码与说明](https://github.com/Itckt/token-burn-games/tree/main/games/085) ⭐ 0（2026-11-25）
`终端文字游戏 · Python · Python CLI · 本地指令见子目录 README`

**186 · Weirlight** — 在泄洪道布置防御塔并控制水流，守住 20 波敌人 · GPT-6.2 Astra · [源码与说明](https://github.com/Itckt/token-burn-games/tree/main/games/111) ⭐ 0（2026-11-25）
`终端字符界面 · Python · Python CLI · 本地指令见子目录 README`

## 七、Gemini 4 Carbon 作品（3 款）

作者明确披露 Gemini 4 Carbon 的独立作品与协作作品分别列出；《After the Tide》中的 GPT-6 Astra 未注明 6.2，不归入 Astra 作品统计。

**130 · NIGHTSHIFT: Survive the Midnight（Gemini 4 Carbon 版）** — 夜雨高速驾驶，穿过车流、用氮气加速并躲避油罐车事故；与 Fable 5.2 使用同一长提示词 · Gemini 4 Carbon（High） · [浏览器试玩](https://eddizege.github.io/nightshift/) · [同提示词对照说明](https://lab.edizegemercan.com/posts/nightshift-gemini-4-carbon-vs-claude-fable-5-2/) · [源码](https://github.com/EddizEge/nightshift) ⭐ 0（2026-11-21）
`TypeScript + Three.js 0.187 + Rapier3D WASM + WebGL 2` · Vite · 浏览器静态站点；作者称单提示词、约 2 小时 8 分钟、无人工编写代码

**131 · After the Tide** — 第一人称海岸观测站恐怖游戏：录下环境声音并在异处播放，引开水下存在，再取回最后一张潮汐图 · Gemini 4 Carbon 负责编码与游戏设计；GPT-6 Astra 负责规划（未注明版本） · [源码与本地运行说明](https://github.com/MichaelCao1/after-the-tide) ⭐ 1（2026-11-21）
`Three.js 0.187 + WebGL 2 + Web Audio` · Vite；也可运行 `python3 scripts/build_dist.py` 生成 `dist/`，再按 README 在本机起服务

**139 · 林间血战 · 剑盾怒气** — 3D 森林战斗 demo：近战积攒怒气，使用三种技能击败半兽人和首领 · Gemini 4 Carbon（High） · [浏览器试玩](https://chan-yuu.github.io/forest-warrior-3d-gemini-4-carbon-high/forest_warrior_demo/) · [源码与模型说明](https://github.com/chan-yuu/forest-warrior-3d-gemini-4-carbon-high) ⭐ 0（2026-11-23）
`HTML5 + Three.js（CDN）` · 无构建 · 单文件 HTML

## 八、Gemini 4 Neon 作品（13 款）

**132 · Kurogane III** — 3D 格斗游戏，含锦标赛、双人本地对战与 CPU 对手；源码另含联机房间 · Gemini 4 Neon（仓库定位为模型开发评估；生成日志、原始提示词和模型设置未披露） · [浏览器试玩](https://gemini-4-neon-3d-game-benchmark.vercel.app/) · [源码与说明](https://github.com/HaroonBadshahAI/gemini-4-neon-3d-game-benchmark) ⭐ 0（2026-11-21）
`TypeScript + Next.js + React + Three.js + WebSocket` · `npm run dev`，默认使用 `http://localhost:3000`；README 说明 Vercel 部署的 WebSocket 联机还需单独服务，作者报告的移动端试玩不代表我们已独立验证全部模式

**133 · Street Trash: Dezombifier** — 3D 僵尸生存射击：18 分钟内收集齿轮、穿过街区并守住撤离点 · Gemini 4 Neon（作者称从 GTA 6 游戏画面重新制作） · [下载页：Windows / Linux / Android](https://github.com/Twarga/Street-Trash-III-Dezombifie-Clone-/releases/latest) · [源码](https://github.com/Twarga/Street-Trash-III-Dezombifie-Clone-) ⭐ 0（2026-11-21）
`GDScript + Godot 4.6` · 提供桌面与 Android 发布包；无浏览器试玩页

**140 · 林海斩兽 · 剑盾战魂** — 3D 森林战斗 demo：以近战积攒怒气，并用三种技能击败半兽人与首领 · Gemini 4 Neon（xHigh） · [浏览器试玩](https://chan-yuu.github.io/orc-forest-combat-gemini-4-neon-xhigh/) · [源码与模型说明](https://github.com/chan-yuu/orc-forest-combat-gemini-4-neon-xhigh) ⭐ 0（2026-11-23）
`HTML5 + Three.js（CDN）` · 无构建 · 多文件静态站点

**141 · The Locked Vault** — 迷你高尔夫关卡：调整力度与方向，让球穿过障碍并击入洞中 · Gemini 4 Neon（Extra） · [浏览器试玩](https://kostikoneuro.github.io/gemini-4-neon-solo/4-minigolf/?lang=en) · [源码](https://github.com/KostiKoNeuro/gemini-4-neon-solo/tree/main/4-minigolf/game/index.html) ⭐ 0（2026-11-23）
`HTML Canvas + JavaScript` · 无构建 · 单文件 HTML · [作者模型与运行记录](https://github.com/KostiKoNeuro/gemini-4-neon-solo)

**142 · Gravity Slingshot Puzzle** — 在八个星系中发射探测器，借行星引力绕行并命中远方信标 · Gemini 4 Neon · [浏览器试玩](https://miaai-lab.github.io/Gemini-4-Neon-100-HTML-Files/031-gravity-slingshot-puzzle.html) · [单文件源码](https://github.com/MiaAI-Lab/Gemini-4-Neon-100-HTML-Files/blob/main/031-gravity-slingshot-puzzle.html) ⭐ 0（2026-11-23）
`HTML Canvas + JavaScript` · 无构建 · 单文件 HTML

**143 · Nonogram Woodcut Atelier** — 解开六道 10×10 图画逻辑谜题，完成后揭出木刻风格图案 · Gemini 4 Neon · [浏览器试玩](https://miaai-lab.github.io/Gemini-4-Neon-100-HTML-Files/048-nonogram-woodcut-atelier.html) · [单文件源码](https://github.com/MiaAI-Lab/Gemini-4-Neon-100-HTML-Files/blob/main/048-nonogram-woodcut-atelier.html) ⭐ 0（2026-11-23）
`HTML + CSS + JavaScript` · 无构建 · 单文件 HTML

**144 · Hex Connection** — 9×9 六角棋盘连通策略游戏，对战内置 AI · Gemini 4 Neon · [浏览器试玩](https://miaai-lab.github.io/Gemini-4-Neon-100-HTML-Files/066-hex-connection-strategy.html) · [单文件源码](https://github.com/MiaAI-Lab/Gemini-4-Neon-100-HTML-Files/blob/main/066-hex-connection-strategy.html) ⭐ 0（2026-11-23）
`SVG + JavaScript` · 无构建 · 单文件 HTML

**145 · Modernist Mosaic** — 拼合 4×4 十五块滑块，让三幅几何艺术画恢复完整 · Gemini 4 Neon · [浏览器试玩](https://miaai-lab.github.io/Gemini-4-Neon-100-HTML-Files/094-modernist-sliding-tile-puzzle.html) · [单文件源码](https://github.com/MiaAI-Lab/Gemini-4-Neon-100-HTML-Files/blob/main/094-modernist-sliding-tile-puzzle.html) ⭐ 0（2026-11-23）
`SVG + JavaScript` · 无构建 · 单文件 HTML · [模型说明（仓库 About）](https://github.com/MiaAI-Lab/Gemini-4-Neon-100-HTML-Files)

**146 · Chamonix // Mont Blanc Freeride** — 第一人称滑雪模拟：刻弯、加速、跳跃并可触发雪崩 · Gemini 4 Neon（High） · [浏览器试玩](https://techkwon.github.io/neon-webgl-rematch/runs/ski/neon/) · [模型运行记录](https://github.com/techkwon/neon-webgl-rematch/blob/main/data.json) · [单文件源码](https://github.com/techkwon/neon-webgl-rematch/blob/main/runs/ski/neon/index.html) ⭐ 0（2026-11-23）
`Raw WebGL 2 + Web Audio` · 无构建 · 单文件 HTML；作者提示与用时见运行记录

**147 · 霜谷铲雪社（Frosthollow Plow）** — 驾驶铲雪车清理三段雪村道路、救出埋在雪下的信箱并升级车辆 · Gemini 4 Neon（仓库 About 标注） · [源码与本地运行方法](https://github.com/enhen-x/Frosthollow_PLOW_CO.) ⭐ 0（2026-11-23）
`React 19 + TypeScript + Three.js` · Vite 8；在仓库目录执行 `npm install && npm run dev`

**149 · Token 花园（Token Garden）** — 4 人泡泡堂式竞技：放置 Token 炸弹、抢道具并利用机关淘汰对手 · Gemini 4 Neon（仓库 About 标注） · [源码与本地运行说明](https://github.com/XYUUrbuu/Bubble-Fighter) ⭐ 1（2026-11-23）
`Godot 4.7.2` · 在 Godot 打开 `project.godot` 并按 F5；可导出 Windows 版本

**150 · PrimeWordle** — 将 Wordle / Mastermind 扩展为多符号逻辑解谜；仓库还包含规则求解器与 25M 参数 Transformer 实验 · Gemini 4 Neon（仓库 About 标注） · [源码与本地网页启动说明](https://github.com/P1ayerWp/PrimeWordle) · ⌨️ `python run_web.py` ⭐ 0（2026-11-24）
`Python + HTML/CSS/JavaScript` · 无构建 · 本地 HTTP 服务启动网页小游戏

---

**187 · Cretacea: Blackout（Unity）** — 第一人称恐龙园区生存恐怖游戏；Gemini 4 Neon 移植到 Unity，Claude Fable 5.2 与 Claude Opus 5.5 参与后续画面调整 · Gemini 4 Neon、Claude Fable 5.2、Claude Opus 5.5 协作 · [源码与阶段记录](https://github.com/jc-able/Cretacea-Blackout-Unity) ⭐ 0（2026-11-25）
`C# + Unity 6 HDRP 17.6 · Unity 6000.6.9f1 · 需本地打开 Unity 项目`

## 九、GLM-5.4 作品（2 款）

**188 · NEON PINBALL // CYBER ARCADE** — 霓虹弹珠台，键盘控制挡板并挑战高分 · GLM-5.4 · [浏览器试玩](https://neon-pinball-263.netlify.app/) · [源码与模型说明](https://github.com/iceplantengineering/neon-pinball) ⭐ 0（2026-11-25）
`单文件 HTML · Canvas 2D + Web Audio · 无构建`

**189 · Pelican on a Bicycle · 3D** — 操控骑自行车的鹈鹕在乡间道路无尽骑行，躲避路障并切换场景风格 · GLM-5.4 · [浏览器试玩](https://unlinearity.github.io/pelican-bike-3d/) · [源码与模型说明](https://github.com/UNLINEARITY/pelican-bike-3d) ⭐ 0（2026-11-25）
`Three.js + WebGL · Node.js build.mjs · 单 HTML 构建产物 + 多文件源码`

## 十、值得收藏的社区合集

**GPT-6.2 Astra 与 Sol 游戏、3D 世界及创意作品合集** — [AI-Terrarium/awesome-gpt-6.2](https://github.com/AI-Terrarium/awesome-gpt-6.2)
截至 2026-11-19 收录 55 个 GPT-6.2 项目，标注 29 个 Astra、24 个 Sol 与 2 个混合项目；部分条目提供源码和作者归属。

**Fable 5.2 视频与游戏案例合集** — [sandbase-lab/awesome-fable-5-2](https://github.com/sandbase-lab/awesome-fable-5-2) ⭐ 0
Three.js 场景、Canvas 动画、动效片段 + 提示词指南与模型对比，每天从 SandBase Lab 同步。

**22 款 Fable 游戏精选** — [ummydev/awesome-claude-fable-games](https://github.com/ummydev/awesome-claude-fable-games) ⭐ 3
带试玩链接、游戏截图、提示词和作者署名，每款在 vibegamer.io 上也有镜像。

**76 个 HTML 作品与完整提示词** — [MiaAI-Lab/Claude-Fable-5.2-HTML-Files](https://github.com/MiaAI-Lab/Claude-Fable-5.2-HTML-Files) ⭐ 109
76 个视觉小作品，每个都附截图和原始提示词，适合当「提示词语料库」翻。

## 十一、技术栈速查表

表中的 🎮 可以直接点开玩；⌨️ 表示无在线版本，需按上方条目的说明在本地运行。

| 游戏 | 渲染 / 引擎 | 构建方式 | 交付形态 | 在线试玩 |
| --- | --- | --- | --- | :---: |
| FOG CITY | three.js | 无构建 | 多文件 ES module | ⌨️ |
| Dustfall | three.js 0.187 | Vite 8 | 站点 | [🎮 试玩](https://aiarcade.games/play/dustfall) |
| Bayhaven | three.js | Vite | 模块化站点 | [🎮 试玩](https://aiarcade.games/play/bayhaven) |
| Aquila | three.js | esbuild | 单文件 877 KB | ⌨️ |
| Dawnward | three.js | esbuild | 单文件 678 KB | ⌨️ |
| Ironvale | three.js r128 | 手写 HTML + 本地 lib | 单 HTML + 模型目录 + exe | [🎮 试玩](https://aiarcade.games/play/ironvale) |
| The Long Climb | three.js | 无构建 | 多文件静态站点 | [🎮 试玩](https://aiarcade.games/play/the-long-climb) |
| The Boondocks: The Woodcrest Files | 原生 JavaScript | 无构建 | 多文件静态站点 | ⌨️ |
| Duel Knights | three.js | 无构建 | 多文件静态站点 | [🎮 试玩](https://aiarcade.games/play/duel-knights) |
| Saltline | three.js | 无 | 单文件 1.4 MB | [🎮 试玩](https://aiarcade.games/play/saltline-fable-5-2-fps) |
| 盐线行动 Online | three.js + WS | npm 打包 | Node 服务 | [🎮 试玩](https://aiarcade.games/play/saltline-online) |
| SUBLEVEL 07 | three.js | 无 | 单文件 131 KB | [🎮 试玩](https://aiarcade.games/play/sublevel-07-fps-repro) |
| BLAMELESS | three.js | npm 构建 | 站点 + Python 榜单 | [🎮 试玩](https://aiarcade.games/play/blameless) |
| Dustline Outpost | three.js r128 | 无 | HTML + game.js + assets | ⌨️ |
| Last Return（原 No Return） | WebGL 2 | Node.js 自写构建 | 单文件 index.html | [🎮 试玩](https://aiarcade.games/play/last-return) |
| Riftline | three.js r160 + PeerJS | 无构建 | 多文件静态站点 | [🎮 试玩](https://aiarcade.games/play/riftline) |
| Graveyard Shift | three.js / WebGL 2 | esbuild | 单文件 dist/index.html；可选 Worker + D1 | [🎮 试玩](https://aiarcade.games/play/graveyard-shift) |
| Tidebell 潮钟 | three.js r170 | 无 | 单文件 | [🎮 试玩](https://aiarcade.games/play/tidebell) |
| MOTHLIGHT | three.js r170 | 无 | 单文件 | [🎮 试玩](https://aiarcade.games/play/mothlight) |
| 青云宗 · 御剑采灵 | three.js r170 | 无 | 单文件 | [🎮 试玩](https://aiarcade.games/play/qingyun-sword-flight) |
| MISREMEMBER | three.js r170 | 无 | 单文件 | [🎮 试玩](https://aiarcade.games/play/misremember) |
| Hanford Reach | three.js | Vite | 站点（Vercel） | [🎮 试玩](https://aiarcade.games/play/hanford-reach) |
| Boring Game | three.js | Vite + tsc | TypeScript 站点 | [🎮 试玩](https://aiarcade.games/play/boring-game-sf-bay-transit) |
| SHUTTERPINE | three.js | Vite | 浏览器站点 dist/ | [🎮 试玩](https://aiarcade.games/play/shutterpine) |
| Power the Spire | three.js 0.187 | 无构建 | 多文件静态站点 | ⌨️ |
| Tropical Island | Godot 4.7.2 | Godot | macOS 应用 / Godot 源码项目 | ⌨️ |
| CASCADE | Unity HDRP | Unity 6000.6.0f1 | Windows 构建 + Unity 源码（Git LFS） | ⌨️ |
| MESOCYCLONE | Unity HDRP | Unity 6000.6.0f1 | Windows 构建 + Unity 源码（Git LFS） | ⌨️ |
| ZERO | Unity URP | Unity 6000.6.0f1 | Windows 构建 + Unity 源码（Git LFS） | ⌨️ |
| OUT OF REACH | Unity URP | Unity 6000.3.28f1 | Windows 程序 / Unity 源码项目 | ⌨️ |
| うしろのハニワ | 原生 JavaScript | 无构建 | 多文件静态站点 | [🎮 试玩](https://aiarcade.games/play/ushiro-no-haniwa) |
| Soccer 3D | 自绘 + three.js | 无 | 单文件 + PWA | [🎮 试玩](https://aiarcade.games/play/pocket-soccer-3d) |
| TukTuk | three.js | 无 | 单文件 | [🎮 试玩](https://aiarcade.games/play/tuktuk) |
| Emberdeep | 原生 | 无 | 单文件 | [🎮 试玩](https://aiarcade.games/play/emberdeep) |
| Daedalus | 原生 | 无 | 单文件 121 KB | [🎮 试玩](https://aiarcade.games/play/daedalus) |
| Sternenjäger | 原生 | 无 | 单文件 | [🎮 试玩](https://aiarcade.games/play/sternenjaeger) |
| Shuttle Strike | three.js + 手部追踪 | 无 | 单文件 + CDN | [🎮 试玩](https://aiarcade.games/play/shuttle-strike) |
| NEON RUNNER | Canvas 2D | 无 | 单文件 | ⌨️ |
| Becario del Universo | 原生 | 无 | 单文件 | [🎮 试玩](https://aiarcade.games/play/becario-del-universo) |
| Harvest Standoff | three.js | 自写 build.mjs | dist 目录 | [🎮 试玩](https://aiarcade.games/play/harvest-standoff) |
| 潮汐战线（Tidemark） | HTML Canvas | 无构建 | 多文件 HTML + JavaScript | [🎮 试玩](https://aiarcade.games/play/tidemark) |
| The County | three.js + Vite | Vite + TypeScript | 浏览器站点 | [🎮 试玩](https://aiarcade.games/play/the-county) |
| MAKINAMON | Canvas 2D | 无构建 | 多文件 HTML + JavaScript | [🎮 试玩](https://aiarcade.games/play/makinamon-pulso) |
| SUPERFORGE GT | SNES Mode 7 | Make + ca65/ld65 | 4 MB `.sfc` ROM | ⌨️ |
| FableFlight | wgpu + egui | Cargo | Rust 原生桌面程序 | ⌨️ |
| Liquid Labyrinth | three.js 0.187 | Vite + TypeScript | 浏览器站点 dist/ | [🎮 试玩](https://aiarcade.games/play/liquid-labyrinth) |
| Mini RPG | 原生 JavaScript | 无构建 | 多文件静态站点 | [🎮 试玩](https://aiarcade.games/play/mini-rpg) |
| Rufus Crush | macroquad / WebGL | Rust → WebAssembly | 静态 WASM 站点；另有 Android WebView 构建 | [🎮 试玩](https://bhoult.github.io/phone-games/rufus-crush/) |
| ぽん、と森は灯る | 原生 JavaScript | 无构建 | 多文件静态站点 | [🎮 试玩](https://aiarcade.games/play/pon-to-mori-wa-tomoru) |
| ひとつぶ庭園 | 原生 JavaScript | 无构建 | 多文件静态站点 | [🎮 试玩](https://aiarcade.games/play/hitotsubu-teien) |
| EMBERDEEP ― 燈守りの坑道 | 原生 JavaScript | 无构建 | 多文件静态站点 | [🎮 试玩](https://aiarcade.games/play/emberdeep-tomoshimori) |
| LUMEN REEL ― まわる灯台と三つの海路 | 原生 JavaScript | 无构建 | 多文件静态站点 | [🎮 试玩](https://aiarcade.games/play/lumen-reel) |
| REEL DELVE ― まわる迷宮と三人の旅 | 原生 JavaScript | 无构建 | 多文件静态站点 | [🎮 试玩](https://aiarcade.games/play/reel-delve) |
| 切りもどし ― 鋏と春の小さな鉢 | 原生 JavaScript | 无构建 | 多文件静态站点 | [🎮 试玩](https://aiarcade.games/play/kirimodoshi) |
| ひつじが いっぴき ― 牧羊犬コロの一日 | 原生 JavaScript | 无构建 | 多文件静态站点 | [🎮 试玩](https://aiarcade.games/play/hitsuji-ga-ippiki) |
| MAPLE RUN | PlayCanvas + Splat Engine / WebGPU | Vite | 浏览器站点 dist/ | [🎮 试玩](https://maple-run-fable.vercel.app) |
| Escape the Fable | three.js | 无构建 | 多文件静态站点 | [🎮 试玩](https://aiarcade.games/play/escape-the-fable) |
| Circular Tic Tac Toe | SVG + JavaScript | 无构建 | 多文件静态站点 | [🎮 试玩](https://aiarcade.games/play/circular-tic-tac-toe) |
| EarthFM · Listening Game | Next.js + React + Tone.js | Next.js | Web 应用 | [🎮 试玩](https://earthfm.vercel.app/play) |
| T-Minus | Preact + PeerJS / WebRTC | Vite + TypeScript | 浏览器站点 game/ | [🎮 试玩](https://missioncontrol.dractec.com/) |
| Jester | MediaPipe + three.js | Vite + TypeScript（Make） | 浏览器站点 app/dist | [🎮 试玩](https://jester-pi.vercel.app) |
| Retro Sisters | Canvas + SID 音频 | 无构建 | 多文件静态站点 | ⌨️ |
| Rawza Ring | three.js | 无构建 | 多文件静态站点 | [🎮 试玩](https://aiarcade.games/play/rawza-ring) |
| Gifts for the Tall One | three.js | 无构建 | 多文件静态站点 | ⌨️ |

| Boo-mas | Three.js r187 | 无构建 | 多文件 ES modules | [🎮 试玩](https://robinduckett.github.io/boo-mas/) |
| Wildlife Odyssey 3D | React Three Fiber + Three.js r187 | Vite 8 | 浏览器站点（本地启动） | ⌨️ |
| 星烬原野 · Demo | Three.js 0.187 + WebGL 2 | Vite 8.3.8 | 浏览器站点（本地启动） | ⌨️ |
| Space 2601AE | Fable + 原生 WebGL 2 | Vite 8.3.8 | 浏览器 ES modules / Docker | ⌨️ |
| Saltwake: The Drowned Abbey | 单文件 HTML | 无构建 | 单文件 HTML | [🎮 试玩](https://chojondocho.github.io/single-html-game-bench/codex-gpt-6-2-astra-max.html) |
| Mall Action（Astra xhigh） | Canvas 2D | Node 构建脚本 | 单 HTML 构建产物 + 源码 | [🎮 试玩](https://rlorca.github.io/mall-action/gpt-6.2-astra-xhigh/) |
| Lantern Drift · 天灯漂流（Astra） | React 19 | 预构建 | 静态站点与 assets | [🎮 试玩](https://jambocoder159.github.io/ai-game-duel/#r2-astra) |
| Undertow FM · 逆潮电台 | Godot 4.7.2 | Godot | Godot 项目 / 桌面发行说明 | ⌨️ |
| Pocket Roads: Midnight Pass | HTML + CSS + SVG | 无构建 | 多文件静态站点 | [🎮 试玩](https://aartiles.github.io/local-model-benchmarks-site/demos/pocket-roads/) |
| Flying Anglia | Gea3D + 原生渲染器 | GeaStack + ESP-IDF 6 | ESP32-S3 固件 / 硬件游戏 | ⌨️ |
| Bitcade Pac-Man（Astra） | Canvas 2D | 无构建 | 单文件 HTML | [🎮 试玩](https://jonclegg.github.io/pacman-bakeoff/entries/gpt-6.2-astra.html) |
| Fault in the Bath | CSS / DOM | 无构建 | 单文件 HTML | [🎮 试玩](https://miaai-lab.github.io/GPT-6.2-Astra-100-HTML-Files/009-tile-fault.html) |
| The Chalk Yard | DOM geometry | 无构建 | 单文件 HTML | [🎮 试玩](https://miaai-lab.github.io/GPT-6.2-Astra-100-HTML-Files/042-chalk-quarry.html) |
| The Patient Egg | CSS / DOM | 无构建 | 单文件 HTML | [🎮 试玩](https://miaai-lab.github.io/GPT-6.2-Astra-100-HTML-Files/074-egg-balance.html) |
| The Keyless Works | SVG / DOM | 无构建 | 单文件 HTML | [🎮 试玩](https://miaai-lab.github.io/GPT-6.2-Astra-100-HTML-Files/097-lockstep.html) |
| Lantern Drift · 天灯漂流（Fable） | React 19 | 预构建 | 静态站点与 assets | [🎮 试玩](https://jambocoder159.github.io/ai-game-duel/#r2-fable) |
| HIGHLINE | Three.js r170 | 无构建 | 多文件静态站点 | [🎮 试玩](https://clockendbader.github.io/model-arena/opus-5.5/parkour/) |
| The Tallow Deep | WebGL 2 | 无构建 | 单文件 HTML | [🎮 试玩](https://chojondocho.github.io/single-html-game-bench/claudecode-opus-5-5-max.html) |
| Mall Action（Fable 5.2） | WebGL | Vite | 浏览器静态站点 | [🎮 试玩](https://rlorca.github.io/mall-action/fable-5.2/) |
| Mall Action（Opus 5.5） | PixiJS 8 | Vite | 浏览器静态站点 | [🎮 试玩](https://rlorca.github.io/mall-action/opus-5.5/) |
| Crash Quota | 自制 WebGL 2 引擎 | 无构建 | 多文件 ES modules | [🎮 试玩](https://smashi.app/arcade/crash-quota-fable/) |
| NIGHTSHIFT（Fable 5.2） | Three.js + Rapier | Vite + TypeScript | 浏览器静态站点 | [🎮 试玩](https://eddizege.github.io/nightshift-fable/) |
| NIGHTSHIFT（Gemini 4 Carbon） | Three.js + Rapier3D WASM | Vite + TypeScript | 浏览器静态站点 | [🎮 试玩](https://eddizege.github.io/nightshift/) |
| After the Tide | Three.js + WebGL 2 | Vite / 离线构建脚本 | 本地服务或单文件 HTML | ⌨️ |
| Kurogane III | Three.js | Next.js + WebSocket 服务 | 浏览器站点 | [🎮 试玩](https://gemini-4-neon-3d-game-benchmark.vercel.app/) |
| Street Trash: Dezombifier | Godot 4.6 | Godot | Windows / Linux / Android 发布包 | ⌨️ |

完整的体积、依赖、素材来源、生成成本对照见 **[TECH_STACK.md](TECH_STACK.md)**。

## 十二、这些游戏是怎么被写出来的

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

发现漏掉的 Claude Fable 5.2、GPT-6.2 Astra、Gemini 4 Carbon 或 Gemini 4 Neon 作品？欢迎提 PR，只需按现有格式补充一行，或直接改 [`data/games.csv`](data/games.csv)：

- 必须是**能跑起来**的作品（在线可玩，或仓库里有明确启动方式）
- 必须给出**源码仓库**，不接受只有视频的条目
- 必须有作者 README 或项目说明作为**模型归属依据**；同仓库的不同模型版本分开列，多模型协作按作者披露记录；Gemini 4 Carbon 与 Neon 分开，未注明 6.2 的 GPT-6 Astra 不计入 GPT-6.2 Astra
- 试玩链接请实测可访问，并在 PR 里说明抓取日期

## 说明

- 本仓库只做索引，不托管任何游戏代码，版权归各作者所有，请遵守各仓库的 LICENSE。
- 部分作品借鉴既有游戏玩法，也有明确标注的同人作品；素材、角色与第三方资源的使用范围以作者 README 和许可证为准。
- 部分作品仍在开发中，完成度差异很大；「在线可玩」只代表能打开，不代表完成度。
- 原有条目快照为 2026-11-12、2026-11-14；新增 32 款与 Last Return 更新记录于 2026-11-16，新增 21 款记录于 2026-11-17，新增三款作品及模型归属字段记录于 2026-11-18，后续核验记录见上方；Star 数与在线状态会随时间变化。
- 只有作者明确标注 GPT-6.2 Astra 的作品才计入该模型；未注明 6.2 的 GPT-6 Astra 和 GPT-6.2 Sol 均单独区分。Gemini 4 Carbon 与 Gemini 4 Neon 也分别统计；只写 Gemini 或 Antigravity 时不推断具体版本。

## 附录：站上还有这 23 款

以下作品不在上面的 189 款里（多数没有公开仓库，或不在最初流传的清单中），一并列出；除特别注明外均在 aiarcade.games 上可以直接玩。🆕 为 2026-11-16 新增，✨ 为 2026-11-18 新增，✦ 为 2026-11-20 新增，★ 为 2026-11-21 新增。

| 作品 | 一句话 | 试玩 |
| --- | --- | --- |
| Black Tide 🆕 | Saltline 引擎上的海盗劫案改版：敲中继站读货单、撬开钻井平台 | [Play](https://aiarcade.games/play/black-tide-hdab0j) |
| Undertow 🆕 | 夜暴雨里的港湾拖船：钩住漂移的集装箱，在 Saltline 引擎上重做 | [Play](https://aiarcade.games/play/undertow-y8xvs5) |
| Duskline 🆕 | 3D 无尽跑酷：维修机器人沿高架地铁逃离清扫无人机 | [Play](https://aiarcade.games/play/duskline-vxn7rh) |
| 烬堡 EMBERHOLD 🆕 | 单个 HTML 文件里的几何风魂类，闯废堡、打对决 | [Play](https://aiarcade.games/play/emberhold-xwn1lu) |
| Arcfall Artillery 🆕 | 崩裂天空岛上的回合制炮战 | [Play](https://aiarcade.games/play/arcfall-artillery-ho7odp) |
| Open Skies 🆕 | 飞遍地球：真实机场、真实地形、实时天气 | [Play](https://aiarcade.games/play/flight-simulator-nfljgw) |
| Evensong | 沉没大教堂里的一场决斗，浏览器里的魂类 demo | [Play](https://aiarcade.games/play/evensong) |
| What the Water Keeps | 提灯小船穿过一串截然不同的水域 | [Play](https://aiarcade.games/play/what-the-water-keeps) |
| 黑神话：悟空 · 虎先锋 | 同人 Boss 战，复刻虎先锋 | [Play](https://aiarcade.games/play/wukong-tiger-vanguard) |
| 雾锁山门 | 云海山门 3D 动作 demo | [Play](https://aiarcade.games/play/wusuo-shanmen) |
| 海克斯大乱斗 | 冰封大桥上的同人 ARAM 竞技场 | [Play](https://aiarcade.games/play/hextech-aram) |
| 运输船 3D | 经典地图团队死斗的浏览器复刻 | [Play](https://aiarcade.games/play/transport-ship-3d) |
| BREACH · 运输船联机大厅 | 运输船地图的多人联机大厅 | [Play](https://aiarcade.games/play/breach-transport-ship-online) |
| 几猫 CS | Saltline 的中文本地化改版 | [Play](https://aiarcade.games/play/jimao-cs) |
| 飞车 3D | 带漂移蓄力、氮气与道具赛的卡丁车 | [Play](https://aiarcade.games/play/feiche-3d) |
| 鹈鹕骑单车 | 戴头盔的鹈鹕沿海岸骑复古单车 | [Play](https://aiarcade.games/play/pelican-on-a-bike) |
| 暖光玩具房 · V25 | 温馨玩具房里的跑跳搬运平台 demo | [Play](https://aiarcade.games/play/warm-toy-room-v25) |
| 太阳系三维沙盘 Solar System 3D 🆕 | 按真实轨道与距离摆放 36 个天体，从水星到奥尔特云，可加速到每秒 10 年 | [Play](https://aiarcade.games/play/solar-system-3d) |
| Ripcore ✨ | 钢碗里两个陀螺对撞：后拉定角度与力度，松手开转，先到四分者胜 | [Play](https://aiarcade.games/play/ripcore) |
| 三借芭蕉扇 ✨ | 西游回合制 RPG：三借芭蕉扇灭火焰山，五行相克、七十二变，约一小时流程 | [Play](https://aiarcade.games/play/sanjie-bajiaoshan) |
| Starship Dogfight ✨ | 小行星带上的第三人称太空缠斗：无尽波次、六发导弹，每五波一艘无畏舰 | [Play](https://aiarcade.games/play/starship-dogfight) |
| Fault Line Echoes · 断层回声 ✦ | 白石都城与四片荒野的第一人称冒险 RPG：四种行者流派，接委托、签那份没盖章的汛报 | [Play](https://aiarcade.games/play/fault-line-echoes-hkbbj1) |
| 重庆（试玩版）★ | 浏览器里观光重庆：李子坝轻轨穿楼、洪崖洞夜景，可飞行、坐轻轨、驾车与计时赛；作者称由 Claude Fable 5.2 用 25 亿 token、187 轮、5 天生成，AI 自己写 Python 指挥 Blender 建模，零人工代码（素材另用 GPT Image 2.5 / Hunyuan3D-2；无公开仓库） | [Play](https://lab.ytdeepsea.com/games/chongqing/) |

---

MIT License · 索引内容可自由转载，请保留各作品作者署名。
