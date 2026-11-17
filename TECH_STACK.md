# Fable 5.2 游戏技术栈对比

60 个游戏仓库的横向拆解。原有条目数据抓取于 **2026-11-12**；《潮汐战线》和 5 款游戏于 **2026-11-14** 核验；**2026-11-16** 新增 32 款、23 个仓库，并更新 Last Return；**2026-11-17** 新增 21 款、9 个仓库（含《回声游戏厅》13 款）。多模型协作的范围按作者披露注明。语言参考 GitHub API 与游戏子目录，Star 来自 GitHub API，构建方式、交付形态、素材来源、生成成本来自各仓库 README 原文或项目说明，未做推测填充，未知项标 `—`。

## 一览

| 作品 | 仓库 | 主语言 | 渲染 / 框架 | 构建 | 交付形态 | 素材来源 | 生成规模与成本 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| FOG CITY | Rikinshah787/Game-Fable-5.2 | JavaScript | three.js | 无构建 | 多文件 ES module，12 个 src 模块 | 建筑立面 / 广告牌由 Higgsfield 生成，模型与 HDRI 来自 three.js examples 与 Poly Haven | — |
| Dustfall | webKing021/dustfall | JavaScript | three.js 0.187 + Vite 8 | Vite | 站点 | CC0 素材 | — |
| Bayhaven | fablestar/bayhaven | JavaScript | three.js | Vite | 模块化站点，模块间有接口契约 | 工作室提供的美术 | 每次会话全自动提交，公开直播 |
| Aquila | GavinLOrio/Fable-5.2-random-game | HTML | three.js | esbuild | 单文件 `rome/index.html`，877 KB | 海岸线由 Natural Earth 数据生成 | — |
| Dawnward | GavinLOrio/Fable-5.2-random-game | HTML | three.js | esbuild | 单文件 `index.html`，678 KB | 同上 | — |
| Ironvale | SharpWizard/ironvale | HTML | three.js r128（本地 `lib/` + CDN 兜底） | 手写 HTML | 单个 `ironvale.html` + `models/` + `lib/`，另出 5.8 MB 单文件 exe | 用户提供的免费 CC0 模型站链接 | 21 句请求迭代 |
| Saltline | realcodebear/saltline-fable-5.2 | HTML | three.js（内联） | 无 | **单文件 1.4 MB** | 全部代码生成 | 1 句提示词，约 8 小时，445M 输入 / 2.7M 输出 token，约 $550 |
| 盐线行动 Online | wenzhengshi/fable5-2-salt-online | JavaScript | three.js + WebSocket | npm 打包 | Node 服务（Express） | 客户端内置 three.js | — |
| SUBLEVEL 07 | wquguru/fable52-fps-repro | HTML | three.js（CDN） | 无 | **单文件 131 KB** | 纯代码：Web Audio 合成 18 个音效，着色器画材质 | 1 句提示词，73 轮，41 分钟，$15.96 |
| BLAMELESS | Petyok/blameless | JavaScript | three.js | npm 构建 | dist 站点 + Python 标准库 + SQLite 榜单 | 场景全程序化，音乐 MiniMax Music 3 本地跑，旁白 Piper | 1 句「surprise me」提示词 + 第 2 条部署指令 |
| Dustline Outpost | systemsluke/fable5.2game | JavaScript | three.js r128 | 无 | `index.html` + `game.js`（约 640 行）+ assets | Poly Haven CC0 扫描模型与 HDRI | 多轮对话，README 里有压缩成单份的完整 brief |
| Last Return（原 No Return） | StefanKnol/Last-Return | JavaScript | WebGL 2 | Node.js 自写构建 | 单文件 `index.html`（构建产物） | — | 同一仓库更名；Fable 5.2 最小提示词测试 |
| Riftline | wongh26/claude_fps | HTML | three.js r160 + PeerJS | 无构建 | 多文件静态站点 | 角色、模型、音效由代码生成 | README 标注为 Fable 5.2 游戏开发测试 |
| Tidebell / MOTHLIGHT / 青云宗 / MISREMEMBER | hahaliu1029/fable5.2demo | HTML | three.js r170 | 无 | 各自单文件 `index.html`，离线可玩 | 48 个模型由 Blender Python 脚本生成；MISREMEMBER 贴图用 Codex 生图 | 3 句需求出 3 款游戏，另附 10 秒渲染短片 |
| Hanford Reach | chzbloom123/settlement-bluff-fable5.2 | JavaScript | three.js + Vite | Vite | Vercel 站点，PR 预览 | — | 按 `BUILDLOG.md` 逐会话推进 |
| Boring Game | jakozaur/sf_bay_area_transit_fable_5_2_game | TypeScript | three.js + Vite | Vite + tsc + Biome + Vitest | 站点，带基准测试 | 真实地图数据 | 15 条提示词，15 小时，66,000 行，约 $700 |
| The County | TheMizeGuy/fable-5.2-potatobench | TypeScript | three.js + Vite | Vite + TypeScript | GitHub Pages 站点 | 程序化模拟、Web Audio 合成 | 1 句提示词；作者称游戏由 Fable 5.2 完成 |
| Harvest Standoff | andreteow/farm-ca | JavaScript | three.js | 自写 `build.mjs` | dist 目录 | Blender 脚本生成角色；脚本批量生成语音与配乐 | — |
| MAKINAMON · Versión Pulso | gavilanbe/makinamon-pulso | JavaScript | Canvas 2D | 无构建 | 多文件 HTML + JavaScript | 像素素材由工具烘焙；音效与音乐浏览器合成 | README 标注由 Claude Fable 5.2 制作 |
| SUPERFORGE GT | jreinach-alt/sf-gt | Python / 65C816 ASM | SNES Mode 7 | Make + ca65/ld65 | 4 MB `.sfc` ROM | Blender 制作自有场景素材，代码绘制界面 | SuperForge 工具链 + Claude Fable 5.2 |
| Soccer 3D | ShaunPrice/soccer-3d | HTML | 自绘 3D | 无 | 单文件 + PWA（manifest / service worker） | 音效、解说、封面由 ElevenLabs 生成 | 一次对话写完 |
| TukTuk | basemazab/tuktuk | JavaScript | three.js | 无 | `game.js` + `index.html` | **零素材**：形状、材质、声音全部代码生成 | — |
| Emberdeep | DNDNoob/EmberDeep | HTML | — | 无 | 单文件 | — | — |
| Daedalus | S77FFY/daedalus | HTML | — | 无 | 单文件 121 KB | — | — |
| Sternenjäger | oldzitterhand/sternenjaeger | HTML | — | 无 | 单文件 | — | 「zero effort prompt」 |
| Shuttle Strike | fedifianto/shuttlestrike | HTML | three.js + 手部追踪（CDN） | 无 | 单文件 | — | — |
| NEON RUNNER | Ilias-AK/NewGameFromFable5.2 | HTML | Canvas 2D + Web Audio | 无 | 单文件，零外部资源 | 图形、音乐全部代码生成 | — |
| Becario del Universo | masugus/fable5.2-5min-game | HTML | — | 无 | 单文件 | — | 5 分钟出活 |
| 潮汐战线（Tidemark） | CocoSgt/dsh-game-tidemark | HTML / JavaScript | HTML Canvas | 无 | 多文件 HTML + JavaScript | 仓库内资源 | — |
| The Long Climb | HILAYTRIVEDI/thirty-days | JavaScript | three.js | 无构建 | 多文件静态站点 | three.js 来自 CDN；其余见源码 | 作者说明使用 Fable 5.2 |
| The Boondocks: The Woodcrest Files | Achraf921/boondocks | JavaScript | 原生 JavaScript | 无构建 | 多文件静态站点 | 角色、背景与声音由代码生成；对白用浏览器语音 | 作者说明使用 Fable 5.2 |
| Duel Knights | bitofastickler/duel-knights | JavaScript | three.js | 无构建 | 多文件静态站点 | 模型、场景与声音由代码生成 | 源自 Fable 5.2 的 Ashen Crown，后续扩展见作者 Origin 说明 |
| Graveyard Shift | ethanplusai/zombies | JavaScript | three.js / WebGL 2 | esbuild | 单文件 dist/index.html；可选 Worker + D1 | 运行时生成模型、贴图与声音；封面图另附 | 作者说明使用 Fable 5.2 |
| SHUTTERPINE | DQuanBui/shutterpine | JavaScript | three.js | Vite | 浏览器站点 dist/ | — | 作者说明使用 Fable 5.2 |
| Power the Spire | cdurgun/claude-fable-3d-world | JavaScript | three.js 0.187 | 无构建 | 多文件静态站点 | 地形、建筑与粒子由代码生成 | 作者说明使用 Fable 5.2 |
| Tropical Island | Tarzno/tropical_island | GDScript | Godot 4.7.2 | Godot | macOS 应用 / Godot 源码项目 | Blender 脚本与程序化模型；Z Image Turbo / Stable Audio 3 | Opus 5.5 初始实现，Fable 5.2 进行后续实质扩展 |
| CASCADE / MESOCYCLONE / ZERO | Prokopiy8247/Fable5-2-Natural-Disasters | C# | Unity HDRP / URP | Unity 6000.6.0f1 | Windows 构建 + Unity 源码（Git LFS） | 第三方贴图出处见各项目文档 | 作者说明使用 Fable 5.2 |
| OUT OF REACH | alex-slovakia/out-of-reach | C# | Unity URP | Unity 6000.3.28f1 | Windows 程序 / Unity 源码项目 | 脚本制作模型贴图；合成语音与另列许可的音乐 | 作者披露 Fable 5.2、Opus / Sonnet 5.5 与 Codex 协作 |
| ONE PROMPT WORLDS（Fable 5.2 的 8 作） | shioa2006-game/ONE_PROMPT_WORLDS | JavaScript | 原生 JavaScript | 无构建 | 多文件静态站点 | 原生脚本绘制与浏览器合成声音 | 每款由单个初始提示词启动自主制作；同仓库第 1–8 作标注为 Fable 5.2；第 9 作起的 Opus 5.5 作品未收录 |
| FableFlight | Rolandjg/fableflight | Rust | wgpu + egui | Cargo | Rust 原生桌面程序 | OurAirports / ADS-B / METAR 等外部数据 | 作者披露由 Fable 5.2 与 Opus 5.5 协作制作 |
| Liquid Labyrinth | tuki0918/maze-exit | TypeScript | three.js 0.187 | Vite + TypeScript | 浏览器站点 dist/ | — | 仓库 About 标注为 Fable 5.2 sample game |
| Mini RPG | ertertwert/Mini-RPG | JavaScript | 原生 JavaScript | 无构建 | 多文件静态站点 | 作者配乐及第三方音乐，署名见 README | 作者说明使用 Fable 5.2 |
| Rufus Crush | bhoult/phone-games | Rust | macroquad / WebGL | Rust → WebAssembly | 静态 WASM 站点；另有 Android WebView 构建 | SVG 绘图在构建时烘焙；声音启动时合成 | 作者说明使用 Fable 5.2 |
| MAPLE RUN | nanha0130/maple-run-fable | JavaScript | PlayCanvas + Splat Engine / WebGPU | Vite | 浏览器站点 dist/ | PINOC 高斯泼溅角色与动作；环境和音乐由代码生成 | 作者说明使用 Fable 5.2 |
| Escape the Fable | ai-gamez-r-funz/escape-the-fable | JavaScript | three.js | 无构建 | 多文件静态站点 | — | 作者说明使用 Fable 5.2 |
| Circular Tic Tac Toe | muhammad-sayed-mahdy/circular-tic-tac-toe-web | JavaScript | SVG + JavaScript | 无构建 | 多文件静态站点 | — | 作者说明使用 Fable 5.2 |
| EarthFM · Listening Game | Aarosunn/SpaceApps | TypeScript | Next.js + React + Tone.js | Next.js | Web 应用 | NASA 发布的图像数据；Tone.js 合成音乐 | 作者 AI use 披露 Fable 5.2 与其他 Claude 模型协作 |
| T-Minus | XDracam/spaceappschallenge2026 | TypeScript | Preact + PeerJS / WebRTC | Vite + TypeScript | 浏览器站点 game/ | — | 作者披露 Fable 5.2、Opus 5.5 与 Sonnet 5.5 协作 |
| Jester | aaron-sulbaran/jester | TypeScript | MediaPipe + three.js | Vite + TypeScript（Make） | 浏览器站点 app/dist | 动作数据与浏览器视觉模型；视频不随源码分发 | 作者披露 Fable 5.2、Opus 5.5 与 Sonnet 5.5 协作 |
| Retro Sisters | rob0511-777/Retro-Sisters | JavaScript | Canvas + SID 音频 | 无构建 | 多文件静态站点 | 原创程序化像素美术与合成音乐 | 多模型协作；Fable 5.2 负责像素美术、动画与视差背景 |
| Rawza Ring | Hashmatullahzaher/mazar-rawza-race | JavaScript | three.js | 无构建 | 多文件静态站点 | OpenStreetMap 地图数据；作者后加宣传素材 | 作者称单提示词、约 40 分钟；作者说明使用 Fable 5.2 |
| Gifts for the Tall One | eyeb0l/catslop | JavaScript | three.js | 无构建 | 多文件静态站点 | 模型、贴图与声音由代码生成 | README 与 runs/claude-fable-5-2/NOTES.md 标明模型；这是作者的演示运行 |

| Fight Ring | ganson-labs/fight-ring | JavaScript | 原生 JavaScript 2D 格斗引擎 | Node.js `npm start` | 多文件网页 + 本地服务 | 模型生成两名斗士的造型、招式、语音与 AI | Claude Fable 5.2 与 Gemini 4 Carbon 各自创建一名参赛斗士 |
| The Blooming Dark | Pandaemonium/Psychedelia | JavaScript | WebGL shader + Canvas | 无构建 | 多文件静态站点 | 程序化光效与合成音乐 | 仓库 About 标注由 Fable 5.2 生成 |
| Лисёнок и огненный жёлудь | sashatchersunov6-rgb/lisenok-game | HTML | Canvas 2D + Web Audio | 无构建 | 单文件 HTML | 图形与声音由代码生成 | 作者称 Claude Fable 5.2 编写 |
| Gabriel's Sweet Town | chomachomachoma/candyland_pwa | JavaScript | HTML/CSS/SVG + Web Audio | 无构建 | 离线 PWA，多文件静态站点 | SVG 与声音由代码生成 | 仓库 About 标注使用 Claude Code Fable 5.2 |
| 回声游戏厅（13 款） | zhgarylu/everyday-game | JavaScript | three.js 0.170 | 无构建 | 13 款多文件静态网页游戏 | 主要由代码生成；《清潮》使用角色图素材 | 作者说明 13 款均由 Claude Fable 5.2 制作 |
| Apex Lap | ololo-dev/apex-lap-fable-5-2 | JavaScript | three.js 0.187 | Vite 8 | 浏览器站点 | — | 作者说明由 Claude Fable 5.2 构建 |
| Apex Lap: Blender Edition | ololo-dev/apex-lap-fable-5-2-blender | JavaScript | three.js 0.187 + Blender glTF | Vite 8 | 浏览器站点 | Fable 通过 Blender MCP 制作模型 | 作者说明由 Claude Fable 5.2 构建 |
| Raptor Race | drew879/raptor-race-fable | TypeScript | three.js 0.187 | Vite 8 + TypeScript | 浏览器站点 | Blender 脚本生成 3D 模型 | 仓库 About 将本版本标为 Fable 5.2 remake |
| Uno com escada（Fable 5.2 版） | viktorkav/uno-com-escada | HTML | 原生 JavaScript + WebGPU | 无构建 | 单文件 `fable/index.html` | 场景、汽车与音效由代码生成 | 作者同仓库对比 Fable 5.2 与 Opus 5.5 |

## 交付形态与平台

按主要交付形态归类，以下前三项合计 85 款；最后一项是跨平台补充统计。单 HTML 也可能由构建工具产出。

- **单 HTML 交付（20 款）**：原有 18 款，加上《Лисёнок и огненный жёлудь》和《Uno com escada（Fable 5.2 版）》。Last Return 与 Graveyard Shift 由源码构建为自包含 HTML。
- **无构建但多文件（40 款）**：原有 24 款，加上《回声游戏厅》的 13 款、《Gabriel's Sweet Town》、《The Blooming Dark》和 Fight Ring。需要静态服务的作品按条目说明启动。
- **其余工程化构建（25 款）**：原有 22 款，加上 Apex Lap 两个独立版本和 Raptor Race。包含 Vite / Next.js 站点、Rust / WASM 和 Unity / Godot 桌面项目。
- **提供浏览器以外交付（9 款）**：原有 Ironvale、SUPERFORGE GT，加上 FableFlight、Tropical Island、CASCADE、MESOCYCLONE、ZERO、OUT OF REACH 和另可构建 Android 包的 Rufus Crush。Unity 三款成品使用 Git LFS。

## 素材来源谱系

从「零外部素材」到「大量第三方资产」，这 85 款覆盖不同的素材路线：

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
