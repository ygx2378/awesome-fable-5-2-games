# Fable 5.2 游戏技术栈对比

22 个游戏仓库的横向拆解。数据抓取于 **2026-11-12**：语言与 Star 来自 GitHub API，构建方式、体积、素材来源、生成成本来自各仓库 README 原文，未做推测填充，未知项标 `—`。

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
| Tidebell / MOTHLIGHT / 青云宗 / MISREMEMBER | hahaliu1029/fable5.2demo | HTML | three.js r170 | 无 | 各自单文件 `index.html`，离线可玩 | 48 个模型由 Blender Python 脚本生成；MISREMEMBER 贴图用 Codex 生图 | 3 句需求出 3 款游戏，另附 10 秒渲染短片 |
| Hanford Reach | chzbloom123/settlement-bluff-fable5.2 | JavaScript | three.js + Vite | Vite | Vercel 站点，PR 预览 | — | 按 `BUILDLOG.md` 逐会话推进 |
| Boring Game | jakozaur/sf_bay_area_transit_fable_5_2_game | TypeScript | three.js + Vite | Vite + tsc + Biome + Vitest | 站点，带基准测试 | 真实地图数据 | 15 条提示词，15 小时，66,000 行，约 $700 |
| Soccer 3D | ShaunPrice/soccer-3d | HTML | 自绘 3D | 无 | 单文件 + PWA（manifest / service worker） | 音效、解说、封面由 ElevenLabs 生成 | 一次对话写完 |
| TukTuk | basemazab/tuktuk | JavaScript | three.js | 无 | `game.js` + `index.html` | **零素材**：形状、材质、声音全部代码生成 | — |
| Emberdeep | DNDNoob/EmberDeep | HTML | — | 无 | 单文件 | — | — |
| Daedalus | S77FFY/daedalus | HTML | — | 无 | 单文件 121 KB | — | — |
| Sternenjäger | oldzitterhand/sternenjaeger | HTML | — | 无 | 单文件 | — | 「zero effort prompt」 |
| Shuttle Strike | fedifianto/shuttlestrike | HTML | three.js + 手部追踪（CDN） | 无 | 单文件 | — | — |
| NEON RUNNER | Ilias-AK/NewGameFromFable5.2 | HTML | Canvas 2D + Web Audio | 无 | 单文件，零外部资源 | 图形、音乐全部代码生成 | — |
| Becario del Universo | masugus/fable5.2-5min-game | HTML | — | 无 | 单文件 | — | 5 分钟出活 |

## 交付形态：单文件是主流，但不是全部

- **一个 HTML 文件搞定（16 款）**：Saltline、SUBLEVEL 07、Tidebell、MOTHLIGHT、青云宗、MISREMEMBER、Aquila、Dawnward、Soccer 3D、TukTuk、Emberdeep、Daedalus、Sternenjäger、Shuttle Strike、NEON RUNNER、Becario。双击就能玩，是这波作品最有传播力的形态。
- **无构建但多文件（3 款）**：FOG CITY、Dustline Outpost、Ironvale——源码分层清晰，改起来比单文件舒服，但都需要起静态服务（ES module 与 `fetch` 不走 `file://`）。
- **正经工程化（7 款）**：Dustfall、Bayhaven、Hanford Reach、Boring Game 用 Vite；盐线行动 Online 前后端同仓；BLAMELESS 带 Python 榜单与 headless 端测；Harvest Standoff 自写 `build.mjs` 与 AI 对战测试。
- **超出浏览器（1 款）**：Ironvale 另外产出了 5.8 MB 单文件 Windows exe。

## 素材来源谱系

从「零外部素材」到「大量第三方资产」，这 26 款正好铺成一条光谱：

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
