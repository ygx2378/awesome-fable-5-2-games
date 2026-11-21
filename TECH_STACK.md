# Claude Fable 5.2、GPT-6.2 Astra 与 Gemini 4 游戏技术栈对比

89 个游戏仓库的横向拆解。原有条目数据抓取于 **2026-11-12**；《潮汐战线》和 5 款游戏于 **2026-11-14** 核验；**2026-11-16** 新增 32 款、23 个仓库，并更新 Last Return；**2026-11-17** 新增 21 款、9 个仓库（含《回声游戏厅》13 款）；**2026-11-18** 新增 3 款、2 个仓库，并为 88 款作品补充模型归属；**2026-11-19** 新增 19 款、10 个仓库，并替换 3 款自然灾害体验的失效源码地址；**2026-11-20** 新增 15 款、11 个仓库（3 款 Fable 单模型、11 款 GPT-6.2 Astra、1 款多模型协作），并增加 10 条在线试玩；**2026-11-21** 新增 6 款、6 个仓库（Fable 独立作品 1 款、Fable/Opus 协作 1 款、Gemini 4 Carbon 1 款及 Carbon/GPT-6 Astra 未注明版本协作 1 款、Gemini 4 Neon 2 款），新增 4 个浏览器试玩地址。多模型协作的范围按作者披露注明。语言参考 GitHub API 与游戏子目录，Star 来自 GitHub API，构建方式、交付形态、素材来源、生成成本来自各仓库 README 原文或项目说明，未做推测填充，未知项标 `—`。

## 一览

| 作品 | 仓库 | 主语言 | 渲染 / 框架 | 构建 | 交付形态 | 素材来源 | 生成规模与成本 | 模型归属 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FOG CITY | Rikinshah787/Game-Fable-5.2 | JavaScript | three.js | 无构建 | 多文件 ES module，12 个 src 模块 | 建筑立面 / 广告牌由 Higgsfield 生成，模型与 HDRI 来自 three.js examples 与 Poly Haven | — | Claude Fable 5.2 |
| Dustfall | webKing021/dustfall | JavaScript | three.js 0.187 + Vite 8 | Vite | 站点 | CC0 素材 | — | Claude Fable 5.2 |
| Bayhaven | fablestar/bayhaven | JavaScript | three.js | Vite | 模块化站点，模块间有接口契约 | 工作室提供的美术 | 每次会话全自动提交，公开直播 | Claude Fable 5.2 |
| Aquila | GavinLOrio/Fable-5.2-random-game | HTML | three.js | esbuild | 单文件 `rome/index.html`，877 KB | 海岸线由 Natural Earth 数据生成 | — | Claude Fable 5.2 |
| Dawnward | GavinLOrio/Fable-5.2-random-game | HTML | three.js | esbuild | 单文件 `index.html`，678 KB | 同上 | — | Claude Fable 5.2 |
| Ironvale | SharpWizard/ironvale | HTML | three.js r128（本地 `lib/` + CDN 兜底） | 手写 HTML | 单个 `ironvale.html` + `models/` + `lib/`，另出 5.8 MB 单文件 exe | 用户提供的免费 CC0 模型站链接 | 21 句请求迭代 | Claude Fable 5.2 |
| Saltline | realcodebear/saltline-fable-5.2 | HTML | three.js（内联） | 无 | **单文件 1.4 MB** | 全部代码生成 | 1 句提示词，约 8 小时，445M 输入 / 2.7M 输出 token，约 $550 | Claude Fable 5.2 |
| 盐线行动 Online | wenzhengshi/fable5-2-salt-online | JavaScript | three.js + WebSocket | npm 打包 | Node 服务（Express） | 客户端内置 three.js | — | Claude Fable 5.2 |
| SUBLEVEL 07 | wquguru/fable52-fps-repro | HTML | three.js（CDN） | 无 | **单文件 131 KB** | 纯代码：Web Audio 合成 18 个音效，着色器画材质 | 1 句提示词，73 轮，41 分钟，$15.96 | Claude Fable 5.2 |
| BLAMELESS | Petyok/blameless | JavaScript | three.js | npm 构建 | dist 站点 + Python 标准库 + SQLite 榜单 | 场景全程序化，音乐 MiniMax Music 3 本地跑，旁白 Piper | 1 句「surprise me」提示词 + 第 2 条部署指令 | Claude Fable 5.2 |
| Dustline Outpost | systemsluke/fable5.2game | JavaScript | three.js r128 | 无 | `index.html` + `game.js`（约 640 行）+ assets | Poly Haven CC0 扫描模型与 HDRI | 多轮对话，README 里有压缩成单份的完整 brief | Claude Fable 5.2 |
| Last Return（原 No Return） | StefanKnol/Last-Return | JavaScript | WebGL 2 | Node.js 自写构建 | 单文件 `index.html`（构建产物） | — | 同一仓库更名；Fable 5.2 最小提示词测试 | Claude Fable 5.2 |
| Riftline | wongh26/claude_fps | HTML | three.js r160 + PeerJS | 无构建 | 多文件静态站点 | 角色、模型、音效由代码生成 | README 标注为 Fable 5.2 游戏开发测试 | Claude Fable 5.2 |
| Tidebell / MOTHLIGHT / 青云宗 / MISREMEMBER | hahaliu1029/fable5.2demo | HTML | three.js r170 | 无 | 各自单文件 `index.html`，离线可玩 | 48 个模型由 Blender Python 脚本生成；MISREMEMBER 贴图用 Codex 生图 | 3 句需求出 3 款游戏，另附 10 秒渲染短片 | Claude Fable 5.2 |
| Hanford Reach | chzbloom123/settlement-bluff-fable5.2 | JavaScript | three.js + Vite | Vite | Vercel 站点，PR 预览 | — | 按 `BUILDLOG.md` 逐会话推进 | Claude Fable 5.2 |
| Boring Game | jakozaur/sf_bay_area_transit_fable_5_2_game | TypeScript | three.js + Vite | Vite + tsc + Biome + Vitest | 站点，带基准测试 | 真实地图数据 | 15 条提示词，15 小时，66,000 行，约 $700 | Claude Fable 5.2 |
| The County | TheMizeGuy/fable-5.2-potatobench | TypeScript | three.js + Vite | Vite + TypeScript | GitHub Pages 站点 | 程序化模拟、Web Audio 合成 | 1 句提示词；作者称游戏由 Fable 5.2 完成 | Claude Fable 5.2 |
| Harvest Standoff | andreteow/farm-ca | JavaScript | three.js | 自写 `build.mjs` | dist 目录 | Blender 脚本生成角色；脚本批量生成语音与配乐 | — | Claude Fable 5.2 |
| MAKINAMON · Versión Pulso | gavilanbe/makinamon-pulso | JavaScript | Canvas 2D | 无构建 | 多文件 HTML + JavaScript | 像素素材由工具烘焙；音效与音乐浏览器合成 | README 标注由 Claude Fable 5.2 制作 | Claude Fable 5.2 |
| SUPERFORGE GT | jreinach-alt/sf-gt | Python / 65C816 ASM | SNES Mode 7 | Make + ca65/ld65 | 4 MB `.sfc` ROM | Blender 制作自有场景素材，代码绘制界面 | SuperForge 工具链 + Claude Fable 5.2 | Claude Fable 5.2 |
| Soccer 3D | ShaunPrice/soccer-3d | HTML | 自绘 3D | 无 | 单文件 + PWA（manifest / service worker） | 音效、解说、封面由 ElevenLabs 生成 | 一次对话写完 | Claude Fable 5.2 |
| TukTuk | basemazab/tuktuk | JavaScript | three.js | 无 | `game.js` + `index.html` | **零素材**：形状、材质、声音全部代码生成 | — | Claude Fable 5.2 |
| Emberdeep | DNDNoob/EmberDeep | HTML | — | 无 | 单文件 | — | — | Claude Fable 5.2 |
| Daedalus | S77FFY/daedalus | HTML | — | 无 | 单文件 121 KB | — | — | Claude Fable 5.2 |
| Sternenjäger | oldzitterhand/sternenjaeger | HTML | — | 无 | 单文件 | — | 「zero effort prompt」 | Claude Fable 5.2 |
| Shuttle Strike | fedifianto/shuttlestrike | HTML | three.js + 手部追踪（CDN） | 无 | 单文件 | — | — | Claude Fable 5.2 |
| NEON RUNNER | Ilias-AK/NewGameFromFable5.2 | HTML | Canvas 2D + Web Audio | 无 | 单文件，零外部资源 | 图形、音乐全部代码生成 | — | Claude Fable 5.2 |
| Becario del Universo | masugus/fable5.2-5min-game | HTML | — | 无 | 单文件 | — | 5 分钟出活 | Claude Fable 5.2 |
| 潮汐战线（Tidemark） | CocoSgt/dsh-game-tidemark | HTML / JavaScript | HTML Canvas | 无 | 多文件 HTML + JavaScript | 仓库内资源 | — | Claude Fable 5.2 |
| The Long Climb | HILAYTRIVEDI/thirty-days | JavaScript | three.js | 无构建 | 多文件静态站点 | three.js 来自 CDN；其余见源码 | 作者说明使用 Fable 5.2 | Claude Fable 5.2 |
| The Boondocks: The Woodcrest Files | Achraf921/boondocks | JavaScript | 原生 JavaScript | 无构建 | 多文件静态站点 | 角色、背景与声音由代码生成；对白用浏览器语音 | 作者说明使用 Fable 5.2 | Claude Fable 5.2 |
| Duel Knights | bitofastickler/duel-knights | JavaScript | three.js | 无构建 | 多文件静态站点 | 模型、场景与声音由代码生成 | 源自 Fable 5.2 的 Ashen Crown，后续扩展见作者 Origin 说明 | Claude Fable 5.2 |
| Graveyard Shift | ethanplusai/zombies | JavaScript | three.js / WebGL 2 | esbuild | 单文件 dist/index.html；可选 Worker + D1 | 运行时生成模型、贴图与声音；封面图另附 | 作者说明使用 Fable 5.2 | Claude Fable 5.2 |
| SHUTTERPINE | DQuanBui/shutterpine | JavaScript | three.js | Vite | 浏览器站点 dist/ | — | 作者说明使用 Fable 5.2 | Claude Fable 5.2 |
| Power the Spire | cdurgun/claude-fable-3d-world | JavaScript | three.js 0.187 | 无构建 | 多文件静态站点 | 地形、建筑与粒子由代码生成 | 作者说明使用 Fable 5.2 | Claude Fable 5.2 |
| Tropical Island | Tarzno/tropical_island | GDScript | Godot 4.7.2 | Godot | macOS 应用 / Godot 源码项目 | Blender 脚本与程序化模型；Z Image Turbo / Stable Audio 3 | Opus 5.5 初始实现，Fable 5.2 进行后续实质扩展 | Claude Opus 5.5; Claude Fable 5.2 |
| CASCADE / MESOCYCLONE / ZERO | Cryptopiy/Claude-Fable-5.2-Natural-Disasters | C# | Unity HDRP / URP | Unity 6000.6.0f1 | Windows x64 构建 + Unity 源码项目 | 第三方贴图出处见各项目文档 | 作者说明使用 Fable 5.2（Ultracode） | Claude Fable 5.2 |
| OUT OF REACH | alex-slovakia/out-of-reach | C# | Unity URP | Unity 6000.3.28f1 | Windows 程序 / Unity 源码项目 | 脚本制作模型贴图；合成语音与另列许可的音乐 | 作者披露 Fable 5.2、Opus / Sonnet 5.5 与 Codex 协作 | Claude Fable 5.2; Claude Opus 5.5; Claude Sonnet 5.5 |
| ONE PROMPT WORLDS（Fable 5.2 的 8 作） | shioa2006-game/ONE_PROMPT_WORLDS | JavaScript | 原生 JavaScript | 无构建 | 多文件静态站点 | 原生脚本绘制与浏览器合成声音 | 每款由单个初始提示词启动自主制作；同仓库第 1–8 作标注为 Fable 5.2；第 9 作起的 Opus 5.5 作品未收录 | Claude Fable 5.2 |
| FableFlight | Rolandjg/fableflight | Rust | wgpu + egui | Cargo | Rust 原生桌面程序 | OurAirports / ADS-B / METAR 等外部数据 | 作者披露由 Fable 5.2 与 Opus 5.5 协作制作 | Claude Fable 5.2; Claude Opus 5.5 |
| Liquid Labyrinth | tuki0918/maze-exit | TypeScript | three.js 0.187 | Vite + TypeScript | 浏览器站点 dist/ | — | 仓库 About 标注为 Fable 5.2 sample game | Claude Fable 5.2 |
| Mini RPG | ertertwert/Mini-RPG | JavaScript | 原生 JavaScript | 无构建 | 多文件静态站点 | 作者配乐及第三方音乐，署名见 README | 作者说明使用 Fable 5.2 | Claude Fable 5.2 |
| Rufus Crush | bhoult/phone-games | Rust | macroquad / WebGL | Rust → WebAssembly | 静态 WASM 站点；另有 Android WebView 构建 | SVG 绘图在构建时烘焙；声音启动时合成 | 作者说明使用 Fable 5.2 | Claude Fable 5.2 |
| MAPLE RUN | nanha0130/maple-run-fable | JavaScript | PlayCanvas + Splat Engine / WebGPU | Vite | 浏览器站点 dist/ | PINOC 高斯泼溅角色与动作；环境和音乐由代码生成 | 作者说明使用 Fable 5.2 | Claude Fable 5.2 |
| Escape the Fable | ai-gamez-r-funz/escape-the-fable | JavaScript | three.js | 无构建 | 多文件静态站点 | — | 作者说明使用 Fable 5.2 | Claude Fable 5.2 |
| Circular Tic Tac Toe | muhammad-sayed-mahdy/circular-tic-tac-toe-web | JavaScript | SVG + JavaScript | 无构建 | 多文件静态站点 | — | 作者说明使用 Fable 5.2 | Claude Fable 5.2 |
| EarthFM · Listening Game | Aarosunn/SpaceApps | TypeScript | Next.js + React + Tone.js | Next.js | Web 应用 | NASA 发布的图像数据；Tone.js 合成音乐 | 作者 AI use 披露 Fable 5.2 与其他 Claude 模型协作 | Claude Fable 5.2; other Claude model(s), not specified |
| T-Minus | XDracam/spaceappschallenge2026 | TypeScript | Preact + PeerJS / WebRTC | Vite + TypeScript | 浏览器站点 game/ | — | 作者披露 Fable 5.2、Opus 5.5 与 Sonnet 5.5 协作 | Claude Fable 5.2; Claude Opus 5.5; Claude Sonnet 5.5 |
| Jester | aaron-sulbaran/jester | TypeScript | MediaPipe + three.js | Vite + TypeScript（Make） | 浏览器站点 app/dist | 动作数据与浏览器视觉模型；视频不随源码分发 | 作者披露 Fable 5.2、Opus 5.5 与 Sonnet 5.5 协作 | Claude Fable 5.2; Claude Opus 5.5; Claude Sonnet 5.5 |
| Retro Sisters | rob0511-777/Retro-Sisters | JavaScript | Canvas + SID 音频 | 无构建 | 多文件静态站点 | 原创程序化像素美术与合成音乐 | 多模型协作；Fable 5.2 负责像素美术、动画与视差背景 | Claude Fable 5.2; other model(s), not specified |
| Rawza Ring | Hashmatullahzaher/mazar-rawza-race | JavaScript | three.js | 无构建 | 多文件静态站点 | OpenStreetMap 地图数据；作者后加宣传素材 | 作者称单提示词、约 40 分钟；作者说明使用 Fable 5.2 | Claude Fable 5.2 |
| Gifts for the Tall One | eyeb0l/catslop | JavaScript | three.js | 无构建 | 多文件静态站点 | 模型、贴图与声音由代码生成 | README 与 `runs/claude-fable-5-2/NOTES.md` 标明模型；这是作者的演示运行 | Claude Fable 5.2 |
| 柑仔的晚霞航空信 | jambocoder159/ai-game-duel | JavaScript | Canvas 2D | 无构建 | 多文件静态站点 | 作者提供共用美术 | — | Claude Fable 5.2 |
| 夕阳邮航 | jambocoder159/ai-game-duel | JavaScript | Canvas 2D | 无构建 | 多文件静态站点 | 作者提供共用美术；Astra 版另由模型生成图片 | — | GPT-6.2 Astra |
| Santa Express: Chimney Panic! | thestringtheories/Santa-Game | TypeScript | three.js 0.186 + WebGL 2 | Vite + TypeScript | GitHub Pages 站点 | 程序化场景与 Web Audio；模型资产随项目许可分发 | — | GPT-6.2 Astra |
| Fight Ring | ganson-labs/fight-ring | JavaScript | 原生 JavaScript 2D 格斗引擎 | Node.js `npm start` | 多文件网页 + 本地服务 | 模型生成两名斗士的造型、招式、语音与 AI | 多模型协作，各创建一名参赛斗士 | Claude Fable 5.2; Gemini 4 Carbon |
| The Blooming Dark | Pandaemonium/Psychedelia | JavaScript | WebGL shader + Canvas | 无构建 | 多文件静态站点 | 程序化光效与合成音乐 | — | Claude Fable 5.2 |
| Лисёнок и огненный жёлудь | sashatchersunov6-rgb/lisenok-game | HTML | Canvas 2D + Web Audio | 无构建 | 单文件 HTML | 图形与声音由代码生成 | — | Claude Fable 5.2 |
| Gabriel's Sweet Town | chomachomachoma/candyland_pwa | JavaScript | HTML/CSS/SVG + Web Audio | 无构建 | 离线 PWA，多文件静态站点 | SVG 与声音由代码生成 | — | Claude Fable 5.2 |
| 回声游戏厅（13 款） | zhgarylu/everyday-game | JavaScript | three.js 0.170 | 无构建 | 13 款多文件静态网页游戏 | 主要由代码生成；《清潮》使用角色图素材 | — | Claude Fable 5.2 |
| Apex Lap | ololo-dev/apex-lap-fable-5-2 | JavaScript | three.js 0.187 | Vite 8 | 浏览器站点 | — | — | Claude Fable 5.2 |
| Apex Lap: Blender Edition | ololo-dev/apex-lap-fable-5-2-blender | JavaScript | three.js 0.187 + Blender glTF | Vite 8 | 浏览器站点 | Fable 通过 Blender MCP 制作模型 | — | Claude Fable 5.2 |
| Raptor Race | drew879/raptor-race-fable | TypeScript | three.js 0.187 | Vite 8 + TypeScript | 浏览器站点 | Blender 脚本生成 3D 模型 | — | Claude Fable 5.2 |
| Uno com escada（Fable 5.2 版） | viktorkav/uno-com-escada | HTML | 原生 JavaScript + WebGPU | 无构建 | 单文件 `fable/index.html` | 场景、汽车与音效由代码生成 | — | Claude Fable 5.2 |

| Port Fable (Low) | Cryptopiy/Claude-Fable-5.2-Effort-Test-Open-World | GDScript | Godot 4.7.2 | Godot 导出 | Windows x64 可执行文件 + Godot 源码 | Blender MCP 制作模型；第三方依赖见 NOTICE | 同一提示词，Low | Claude Fable 5.2 |
| Port Cinder (Medium) | Cryptopiy/Claude-Fable-5.2-Effort-Test-Open-World | GDScript | Godot 4.7.2 | Godot 导出 | Windows x64 可执行文件 + Godot 源码 | Blender MCP 制作模型；第三方依赖见 NOTICE | 同一提示词，Medium | Claude Fable 5.2 |
| Marlow Bay (High) | Cryptopiy/Claude-Fable-5.2-Effort-Test-Open-World | GDScript | Godot 4.7.2 | Godot 导出 | Windows x64 可执行文件 + Godot 源码 | Blender MCP 制作模型；第三方依赖见 NOTICE | 同一提示词，High | Claude Fable 5.2 |
| Neon Tide (Max) | Cryptopiy/Claude-Fable-5.2-Effort-Test-Open-World | GDScript | Godot 4.7.2 | Godot 4.7.2 | Windows x64 可执行文件 + Godot 源码 | Blender MCP 制作模型；第三方依赖见 NOTICE | 同一提示词，部分流程由 Opus 5.5 续做 | Claude Fable 5.2; Claude Opus 5.5 |
| Cinder Bay (Extra) | Cryptopiy/Claude-Fable-5.2-Effort-Test-Open-World | GDScript | Godot 4.7.2 | Godot 导出 | Windows x64 可执行文件 + Godot 源码 | Blender MCP 制作模型；第三方依赖见 NOTICE | 同一提示词，部分流程由 Opus 5.5 续做 | Claude Fable 5.2; Claude Opus 5.5 |
| Halcyon Bay (Ultracode) | Cryptopiy/Claude-Fable-5.2-Effort-Test-Open-World | GDScript | Godot 4.7.2 | Godot 导出 | Windows x64 可执行文件 + Godot 源码 | Blender MCP / 可选 Rodin 模型；第三方依赖见 NOTICE | 同一提示词，部分流程由 Opus 5.5 续做 | Claude Fable 5.2; Claude Opus 5.5 |
| Помехи / Pomehi | Cryptopiy/Claude-Fable-5.2-vs-Opus-5.5-Horror-Games | GDScript | Godot 4.7.2 | Godot 导出 | Windows x64 可执行文件 + Godot 源码 | 原始资源与第三方依赖见 LICENSE-ASSETS / NOTICE | 对照测试，Low | Claude Fable 5.2 |
| ЛЕЕР / Leer | Cryptopiy/Claude-Fable-5.2-vs-Opus-5.5-Horror-Games | GDScript | Godot 4.7.2 | Godot 导出 | Windows x64 可执行文件 + Godot 源码 | 原始资源与第三方依赖见 LICENSE-ASSETS / NOTICE | 对照测试，Max + Ultracode | Claude Fable 5.2 |
| Backrooms: The Complex | Cryptopiy/Claude-Opus-5.5-Backrooms | GDScript | Godot 4.7.2 | Godot 导出 | Windows x64 可执行文件 + Godot 源码 | 原始资源与第三方依赖见 LICENSE-ASSETS / NOTICE | 多模型协作；Fable 使用 Ultracode | Claude Opus 5.5; Claude Fable 5.2 |
| LAST LIGHT — Rooftop Run | clockendbader/model-arena | HTML | Canvas 2D | 无构建 | 单文件 HTML | 作品构建随仓库发布；素材授权按目录说明 | 四模型同提示词独立生成，High effort | Claude Fable 5.2 |
| Papertrails | xikhar/papertrails | JavaScript | Three.js 0.187 | Vite 8.3.8 | 浏览器静态站点 | 作者生成的纸艺图集与音频，来源见项目说明 | 单提示词、多子 Agent 与盲评流程 | Claude Fable 5.2; Claude Opus 5.5 |
| Operation Fracture | Thweki/operation-fracture | JavaScript | Three.js 0.187 + WebGL 2 | esbuild 0.28.2 | ZIP 内离线单文件 HTML | 模型能力测试交付；第三方依赖许可见 licenses/ | 原始提示与参数未提供 | GPT-6.2 Astra |
| 潮邮局 / Tidepost | Thweki/tidepost | GDScript | Godot 4.7.2 | Godot 4.7.2 | macOS / Windows / Linux 桌面版 + Web ZIP | 第三方许可见 notices/ | 模型能力测试交付；原始评分未提供 | GPT-6.2 Astra |
| Blackburn Type D | Dun4ev/blackburn-flight | JavaScript | Three.js 0.186.1 + WebGL | Python build.py + esbuild 0.25.12 | Cloudflare Pages + 单文件离线模拟器 | Blender 重建与历史照片，摄影许可见 CREDITS | 简化飞行动力学与环线挑战 | GPT-6.2 Astra |
| Spillway Run | KostiKoNeuro/astra-6-2-solo | HTML | Canvas 2D | 无构建 | 浏览器小游戏 | 自绘球洞与内嵌字体 | X-High，单提示词 | GPT-6.2 Astra |
| Hamster Colony（仓鼠群落） | KostiKoNeuro/astra-6-2-solo | HTML | Three.js（CDN） | 无构建 | 单文件 HTML / GitHub Pages | 笼舍与仓鼠行为由代码生成 | X-High，单提示词 | GPT-6.2 Astra |
| Dusk Runner — Rooftop Time Trial | clockendbader/model-arena | JavaScript | Three.js + WebGL（本地 vendor） | 无构建 | 多文件静态站点 | 仓库包含模型独立生成的完整构建 | 四模型同提示词独立生成，High effort | GPT-6.2 Astra |
| Uno com escada（GPT-6.2 Astra 版） | viktorkav/uno-com-escada | HTML | 原生 JavaScript + WebGPU | 无构建 | 单文件 HTML | 车、赛道、场景与声音由代码生成 | 同一需求，19 轮，作者记录 0 个严重缺陷 | GPT-6.2 Astra |
| FAULTLINE — Cold Relay | Yari-tuber/gpt62-vs-opus55-tests | HTML | WebGL 2 + GLSL | 无构建 | 单文件 HTML（本地浏览器打开） | 场景、材质与声音由代码和着色器生成 | 同提示词三模型对照，X-High | GPT-6.2 Astra |

| Boo-mas | robinduckett/boo-mas | JavaScript | Three.js r187 | 无构建（可选 esbuild） | 多文件 ES modules 站点 | 几何、贴图、音乐与音效由代码生成 | 作者称单提示词、Fable 5.2 Max | Claude Fable 5.2 |
| Wildlife Odyssey 3D — The Living World | quanap5/wildlife-odyssey-3d | TypeScript | React 19 + React Three Fiber 9 + Three.js r187 / WebGL 2 | Vite 8 | 浏览器游戏，需本地启动 | 地形、动植物、纹理与声音程序化生成 | — | Claude Fable 5.2 |
| 星烬原野 · Demo | weit0529/gamedemo_by_Fable5.2 | TypeScript | Three.js 0.187 + WebGL 2 | Vite 8.3.8 + TypeScript | 浏览器游戏，需本地启动 | 角色模型、动作与音效由代码生成 | — | Claude Fable 5.2 |
| Space 2601AE | AJankovic234/fable-space-engine | F# | Fable 5.2 + 原生 WebGL 2 | Fable + Vite 8.3.8 | 浏览器 ES modules / Docker 静态服务 | 详见作者资源清单 | 多阶段基准，作者逐项记录模型、贡献和 token | Claude Fable 5.2; GPT-6.2 Astra; GPT-6.2 Sol; Claude Opus 5.5; Claude Sonnet 5.5; Claude Haiku 5.5; Gemini 3.8 Flash; Gemini (version unreported); Gemini 4 Neon; Gemini 4 Hydrogen; OpenAI ImageGen (version unreported); Microsoft Neural TTS (version unreported) |
| Saltwake: The Drowned Abbey | chojondocho/single-html-game-bench | HTML | — | 无构建 | 单文件 HTML | — | Codex GPT-6.2 Astra Max；单提示词基准 | GPT-6.2 Astra |
| Mall Action（GPT-6.2 Astra xhigh 版） | rlorca/mall-action | JavaScript | Canvas 2D | Node.js `scripts/build.mjs` | 单 HTML 构建产物 + 多文件源码 | — | 作者记录约半小时构建与键盘实测 | GPT-6.2 Astra |
| Lantern Drift · 天灯漂流（GPT-6.2 Astra 第二回合） | jambocoder159/ai-game-duel | TypeScript | React 19；渲染方式未标注 | — | 预构建静态包 + assets | 作者记录本轮模型生成素材 | 42 分 11 秒，作者记录零人工介入 | GPT-6.2 Astra |
| Undertow FM（逆潮电台） | Thweki/undertow-fm | GDScript | Godot 4.7.2 / Compatibility | Godot 4.7.2 | Godot 源码 + macOS / Windows / Linux / Web ZIP | 项目含图像、音乐与音效资源；来源待逐项查阅 notices | 模型能力测试；原始 prompt 与版本参数未公开 | GPT-6.2 Astra |
| Pocket Roads: Midnight Pass | aartiles/local-model-benchmarks-site | HTML | HTML + CSS + SVG | 无构建 | 多文件静态站点 | 车模与场景素材来源见作者披露 | GPT-6.2 Astra 编码运行；作者另披露图像与车辆模型工具 | GPT-6.2 Astra |
| Flying Anglia | baturyilmaz/flying-anglia | TypeScript | Gea3D + 原生渲染器 | GeaStack + ESP-IDF 6 | ESP32-S3 Touch AMOLED 2.06 硬件游戏 | 按项目资源清单 | — | GPT-6.2 Astra |
| Bitcade Pac-Man（GPT-6.2 Astra 版） | jonclegg/pacman-bakeoff | HTML | Canvas 2D | 无构建 | 单文件 HTML | 程序化 2D 图形与合成音频 | Codex API-key fair cell；high effort | GPT-6.2 Astra |
| Fault in the Bath | MiaAI-Lab/GPT-6.2-Astra-100-HTML-Files | HTML | CSS / DOM | 无构建 | 单文件 HTML / GitHub Pages | CSS 生成瓷砖图案 | 100 个 Astra HTML 作品中的目标型拼图 | GPT-6.2 Astra |
| The Chalk Yard | MiaAI-Lab/GPT-6.2-Astra-100-HTML-Files | HTML | DOM geometry | 无构建 | 单文件 HTML / GitHub Pages | CSS / DOM 几何 | 100 个 Astra HTML 作品中的堆叠游戏 | GPT-6.2 Astra |
| The Patient Egg | MiaAI-Lab/GPT-6.2-Astra-100-HTML-Files | HTML | CSS / DOM | 无构建 | 单文件 HTML / GitHub Pages | CSS 生成蛋、梁与动画 | 100 个 Astra HTML 作品中的平衡游戏 | GPT-6.2 Astra |
| The Keyless Works | MiaAI-Lab/GPT-6.2-Astra-100-HTML-Files | HTML | SVG / DOM | 无构建 | 单文件 HTML / GitHub Pages | 程序化齿轮轮廓与动画 | 100 个 Astra HTML 作品中的齿轮拼图 | GPT-6.2 Astra |
| Lantern Drift · 天灯漂流（Fable 第二回合） | jambocoder159/ai-game-duel | TypeScript | React 19（渲染方式未标注） | 预构建静态包 | 浏览器静态站点与 assets | 美术由 Fable 经 Codex 调 GPT 图片生成 | 与 Astra 版同一任务对照；47 分钟上限被停，人工介入 1 次 | Claude Fable 5.2 |
| HIGHLINE | clockendbader/model-arena | JavaScript | Three.js r170 + WebGL | 无构建 | 多文件静态站点 | 程序化几何与光照 | 同提示词四模型对照；Arena 记录 55 分钟 | Claude Opus 5.5 |
| The Tallow Deep | chojondocho/single-html-game-bench | HTML | WebGL 2 | 无构建 | 单文件 HTML | 程序化场景与音效 | 与 Saltwake 同一基准提示词；作者排名 21 作第一 | Claude Opus 5.5 |
| Mall Action（Fable 5.2 版） | rlorca/mall-action | TypeScript | WebGL 像素帧缓冲 | Vite | 浏览器静态站点 | 像素图、字体、音乐由代码生成 | 约 1 小时 15 分，151 个自动化测试 | Claude Fable 5.2 |
| Mall Action（Opus 5.5 版） | rlorca/mall-action | JavaScript | PixiJS 8 | Vite | 浏览器静态站点 | 无素材文件 | 300+ 单元测试 | Claude Opus 5.5 |

| Crash Quota | Mythfinity/crash-quota-fable | JavaScript | 自制 WebGL 2 引擎 | 无构建 | 浏览器 ES modules 站点 | 程序化模型与 Web Audio 合成 | 作者记录 Fable Max Ultracode，约 3 小时 30 分、222 项自动化测试 | Claude Fable 5.2 |
| NIGHTSHIFT（Fable 5.2） | EddizEge/nightshift-fable | TypeScript | Three.js 0.187 + Rapier + WebGL 2 | Vite + TypeScript | 浏览器静态站点 | Blender 自制车辆；纹理与字体见 ASSETS.md | 作者记录约 16 小时 36 分；Opus 子 Agent 协作 | Claude Fable 5.2; Claude Opus 5.5 |
| NIGHTSHIFT（Gemini 4 Carbon） | EddizEge/nightshift | TypeScript | Three.js 0.187 + Rapier3D WASM + WebGL 2 | Vite + TypeScript | 浏览器静态站点 | Blender 脚本自制车辆；授权素材见 ASSETS.md | 作者记录单提示词、约 2 小时 8 分、无人工编写代码 | Gemini 4 Carbon |
| After the Tide | MichaelCao1/after-the-tide | HTML | Three.js 0.187 + WebGL 2 + Web Audio | Vite / scripts/build_dist.py | 本地服务 / 单文件 HTML | 场景几何、纹理、标识和音效由项目生成 | GPT-6 Astra 负责规划，Gemini 4 Carbon 负责编码与游戏设计 | Gemini 4 Carbon; GPT-6 Astra (version unreported) |
| Kurogane III | HaroonBadshahAI/gemini-4-neon-3d-game-benchmark | TypeScript | Next.js + React + Three.js | Next.js + tsx server | 浏览器站点 | — | README 称为 Gemini 4 Neon 游戏开发评估；提示词、模型设置和生成日志未提供 | Gemini 4 Neon |
| Street Trash: Dezombifier | Twarga/Street-Trash-III-Dezombifie-Clone- | GDScript | Godot 4.6 | Godot 4.6 | Windows / Linux / Android 发布包 | 基于游戏画面复刻；素材出处按仓库文档 | 作者称由 Antigravity (Gemini 4 Neon) 从画面重新制作 | Gemini 4 Neon |

## 交付形态与平台

按主要交付形态归类，以下前三项合计 133 款；最后一项是跨平台补充统计。单 HTML 也可能由构建工具产出。

- **单 HTML 交付（35 款）**：含 Saltwake、Mall Action 构建版、Bitcade Pac-Man 和 4 款 GPT-6.2 Astra 单文件拼图，以及原有单文件作品。Last Return 与 Graveyard Shift 由源码构建为自包含 HTML。
- **无构建但多文件（47 款）**：在原有多文件作品基础上增加 Boo-mas 与 Pocket Roads，加上《回声游戏厅》的 13 款、《Gabriel's Sweet Town》、《The Blooming Dark》、Fight Ring、《柑仔的晚霞航空信》和《夕阳邮航》，以及 Model Arena 的 Dusk Runner（Astra 版）、Crash Quota。需要静态服务的作品按条目说明启动。
- **其余工程化构建（51 款）**：在原有工程化作品基础上增加 Wildlife Odyssey 3D、星烬原野、Space 2601AE、Lantern Drift、Undertow FM 与 Flying Anglia，加上 9 款 Godot Windows 构建、Papertrails、Tidepost 桌面版、两版 NIGHTSHIFT、After the Tide、Kurogane III 与 Street Trash: Dezombifier。包含 Vite / Next.js 站点、Rust / WASM 和 Unity / Godot 桌面项目。
- **提供浏览器以外交付（22 款）**：在原有桌面作品基础上增加 Undertow FM 与 Flying Anglia，加上本轮 9 款 Godot Windows 构建、Tidepost 桌面版与 Street Trash: Dezombifier 的原生发布包。

## 素材来源谱系

从「零外部素材」到「大量第三方资产」，这 133 款覆盖不同的素材路线：

1. **纯代码生成** — SUBLEVEL 07（着色器画积水与锈迹、Web Audio 合成 18 个音效）、TukTuk、NEON RUNNER、MOTHLIGHT。体积最小（131 KB ~ 数百 KB），加载最快。
2. **代码生成 + 脚本建模** — Tidebell 四件套用 Blender Python 脚本生成 48 个模型；Harvest Standoff 用 Blender 脚本雕十名角色。
3. **CC0 扫描素材** — Dustline Outpost 用了 Poly Haven 的枪械、集装箱、HDRI，首屏要拉 41 MB；Dustfall、Ironvale 也走这条路，观感最接近 3A。
4. **生成式图像与语音** — FOG CITY 的建筑立面与广告牌（Higgsfield）、Soccer 3D 的音效与解说（ElevenLabs）、BLAMELESS 的配乐（MiniMax Music 3 本地跑）与旁白（Piper）、MISREMEMBER 的贴图（Codex）。

这条光谱直接决定了三件事：**体积**、**首屏时间**、以及**能不能商用**（第三方模型往往带非商用条款，FOG CITY 的 README 就明确写了发布前要换掉那台车）。

## 成本与规模

| 作品 | 提示词数量 | 时长 / 轮数 | 产物规模 | 折算成本 |
| --- | --- | --- | --- | --- |
| SUBLEVEL 07 | 1 句 + 环境说明 | 73 轮 / 41 分钟 | 131 KB 单文件 | $15.96 |
| Saltline | 1 句 | 约 8 小时 | 1.4 MB 单文件 | 约 $550 |
| Boring Game | 15 条 | 15 小时 | 66,000 行 TypeScript | 约 $700 |
| Ironvale | 21 句 | 逐句迭代 | RTS + exe | — |
| Dustline Outpost | 多轮对话压成 1 份 brief | — | 约 640 行 game.js + assets | — |

同一句话，成本相差 40 倍：$15.96 与 $550 的差距几乎全在**上下文长度与轮数**上——长任务每轮都要重读整个工程，缓存命中价只有基础输入价的 0.025 倍，所以能否把轮间隔压在几秒内，直接决定账单。

## 三条可复用的结论

**单文件是传播格式，不是工程格式。** 想在社交平台被点开，就内联依赖、代码生成素材，把体积压到 1 MB 以内；想长期迭代，就老老实实上 Vite + 模块，像 Bayhaven 那样给每个模块写接口契约。

**给 AI 一个能自检的闭环，比给它更长的提示词有用。** SUBLEVEL 07 的产出质量来自「能开浏览器截图、能写脚本打通三波战斗」；Ironvale 的作者总结得很直接：贴截图说「这里不对」，比描述半天更有效。

**素材策略要在第一次 prompt 里定。** 说「不许加载外部图片、模型、音频」，模型就会去写着色器和合成器；说「可以用这些 CC0 链接」，它就会去下模型、写烘焙工具。中途改主意，返工量最大。

---

数据如有错漏，欢迎提 PR 修正 [data/games.csv](data/games.csv)。
