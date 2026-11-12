# Fable 5.2 游戏 Prompt 汇总

这份文档只收录**可复现的原始提示词**：能从作者仓库里原样抄走的，就抄原文；只能看到转述的，就注明来源和链接，不做补写。想自己跑一遍，从这里挑一段复制即可。

---

## 一、一句话做出 3D FPS（SUBLEVEL 07）

作者 [@wquguru](https://github.com/wquguru/fable52-fps-repro) 复刻 Felix Rieseberg 那句提示词，产出 131 KB 单文件、73 轮无人干预。原文如下（第二条是作者加的环境说明）：

```text
Build me a FPS. Insanely detailed quality pls, something that looks visually like it can keep up with AAA. Make it small in scope (like a tiny level) but otherwise impressive photorealistic graphics

（环境说明：做成浏览器里能玩的单文件 HTML，只能从 CDN 引入库，不能加载外部模型、图片、音频文件。输出到 ./demos/04-fps/index.html）
```

配套的 `builder_system.md`（附加系统提示词，允许 agent 自己开浏览器截图自检）与另外三个实验（音效台 / 材质 / 建模）的提示词都在仓库 [`prompts/`](https://github.com/wquguru/fable52-fps-repro/tree/main/prompts) 目录里。

> Saltline 那句被反复引用的原帖提示词，作者只在仓库里说明「去掉了开头的 `You know, you should also`，并补了一句单文件、只用 CDN 的说明」。原帖见 [Felix Rieseberg 的推文](https://x.com/felixrieseberg/status/2119925633564463609)，可直接运行的产物在 [claude.ai artifact](https://claude.ai/artifact/BGY1SztrAYcJQHSsnHHGmp)。

---

## 二、三句需求做出三个 3D 游戏（Tidebell / 青云宗 / MOTHLIGHT）

[hahaliu1029/fable5.2demo](https://github.com/hahaliu1029/fable5.2demo) 的整个仓库就建立在三句话上，原文照抄：

| 顺序 | 需求原文 | 结果 |
| --- | --- | --- |
| 第一句 | 「我想做一款水下探索游戏，而且要尽可能惊艳。」 | Tidebell 潮钟 |
| 第二句 | 「完成之后，用同样的方法，把原来文件夹里的仙侠游戏也打磨一遍。」 | 青云宗 · 御剑采灵 |
| 第三句 | 「把赛博朋克那个也打磨一下，我想把它做成一款赛博城市里的驾驶游戏。」 | MOTHLIGHT // Vesper-9 |

值得注意的是第二、三句的写法：**不重新描述需求，而是指着已有的东西说「打磨」**。作者在 README 里点明，「原来的游戏」是同一个模型更早做出的初版，也留在仓库里——这是把 AI 当长期项目的协作者，而不是一次性生成器。

---

## 三、"Surprise me" 型提示词（BLAMELESS）

[Petyok/blameless](https://github.com/Petyok/blameless) 的作者只给了一个开放命题，游戏题材、武器、剧情、配乐全部由模型自己决定：

```text
Hello fable 5.2! You are 1 day old. I am curious what can you do, so let's do a simple test:
using gpu-serv for builds/test -> build a three.js shooter game. You have only 1 try. This laptop
should handle your game at least 30 fps, 60 fps ideally. What to include to your game decide only
you (story, style, weapons, feel, music, etc.). There is no time limit. You can use other models
only if you RUN THEM LOCALLY on gpu-serv - for instance minimax h3, or etc. Suprise me!
```

结果是一个「值班工程师」FPS：武器是 `kill -9`、`grep -r`、`rm -rf`，血量叫错误预算，没有弹药只有限流（打太久返回 429），通关后生成一份基于你实际操作的事故复盘。

第二条消息同样值得抄：

```text
deploy this, give it a domain, make stats and a leaderboard, make a public repo
```

---

## 四、把玩法规则写进提示词（Dustline Outpost）

[systemsluke/fable5.2game](https://github.com/systemsluke/fable5.2game) 的做法相反：几百字的 brief 里把帧率无关的**具体数值**全部钉死——中继站锁定需要 32 秒、需要在 5 米内、敌方单位 6.5 米内会打断、回声按 20 Hz 采样位置与朝向、每个循环敌人按固定时刻刷新。节选：

```text
CONCEPT
A storm has a container yard stuck on repeat. Every lightning strike rewinds the last 70 seconds.
Every run the player makes stays behind as an "echo": a translucent blue copy of the player that
replays exactly what they did, shot for shot, in the new loop. The player must lock three relays
(A, B, C) inside a single loop. ... The player gets six strikes; fewer is a better result.

RULES
- A relay locks after 32 seconds of at least one friendly body (the player or a living echo)
  standing within 5 m of it while no living hostile is within 6.5 m. Progress pauses when contested,
  never decays, and resets to zero at every strike.
- Record each run as position and facing sampled at 20 Hz, plus every shot ...
- Hostiles spawn on a fixed schedule at fixed places every loop so runs can be planned ...
```

它还示范了怎么给「验收标准」：

```text
QUALITY BAR
- Verify in a real browser before calling it done: take screenshots of the menu, the yard looking
  toward and away from the sun, the scope view, a hostile up close, and an echo replaying a run;
  then simulate three loops and confirm recording, replay, relay capture and the win screen all
  work with no console errors.
- State plainly what was and was not tested.
```

完整 brief（CONCEPT / RULES / PLAYER / HOSTILE BEHAVIOUR / WORLD / ASSETS / RENDERING / AUDIO / HUD AND MENUS / QUALITY BAR 十节）在仓库 README 的「The prompt」一节。

---

## 五、21 句大白话做出一个 RTS（Ironvale）

[Ironvale](https://github.com/SharpWizard/ironvale) 的作者把 21 条请求按顺序公开了，第一条定框架、后面每条都只有一两句话。摘几条最有代表性的：

| # | 说的是什么 |
| --- | --- |
| 1 | 用一份书面规格描述「一个 HTML 文件里的原创 3D 即时战略」：采集、建造、三个时代、军队、AI 对手、战争迷雾、菜单、音效，名字与阵营必须原创 |
| 3 | 「角色要更好看。砍树和采食物要看得见工人真的在做，加个自动收集。整张地图也要好看。」 |
| 4 | （贴一张动物尸体截图）「食物应该自动收集。」 |
| 8 | 十一个模型包链接 +「删掉这个动画，不好看。用这些模型写个故事，加建筑升级、攻击敌人、全图查看、更好的视角控制，多做几种大地图」 |
| 11 | 「还需要哪些更新？」→「全都做。」 |
| 17 | 「给每个国度加独特兵种和建筑」+（截图）「UI 修一下」 |
| 20 | 「做个离线 exe，绿色版，带图标。」 |

作者自己总结的方法论里，两条最有用：

- **先给一整页规格，之后每条只说一两句。**
- **展示，别描述。** 好几个最有效的修复，都是贴一张截图加一句「修这个」。
- **直接问模型「下一步该做什么」，然后回一句「全都做」**，这是产出密度最高的方式。

完整 21 条 + 踩坑经验见 [`PROMPTS.md`](https://github.com/SharpWizard/ironvale/blob/main/PROMPTS.md)。

---

## 六、更多提示词语料

- **[MiaAI-Lab/Claude-Fable-5.2-HTML-Files](https://github.com/MiaAI-Lab/Claude-Fable-5.2-HTML-Files)** —— 76 个视觉小作品，每个都附截图与原始提示词，最适合当语料库翻。
- **[sandbase-lab/awesome-fable-5-2](https://github.com/sandbase-lab/awesome-fable-5-2)** —— 视频与场景案例 + 提示词指南 + 模型对比。
- **[ummydev/awesome-claude-fable-games](https://github.com/ummydev/awesome-claude-fable-games)** —— 22 款精选，带试玩、截图与提示词。
- **[Bayhaven 的 CONTRIBUTING.md](https://github.com/fablestar/bayhaven/blob/main/CONTRIBUTING.md)** —— 一份可以贴给你自己的 coding agent 的贡献提示词。

## 七、从这些提示词里能抄走什么

1. **环境约束要写在第一句。** 「单文件 HTML、只能从 CDN 引库、不许加载外部素材」——这一句决定了后面所有技术选型，写晚了就要返工。
2. **给闭环，不要给更长的描述。** 允许 agent 自己开浏览器截图、写脚本打通关，比多写 500 字需求有效得多（SUBLEVEL 07 与 Ironvale 都验证了这一点）。
3. **玩法数值直接钉死。** 帧率无关的规则、采样率、刷新时刻，写清楚模型才不会自行发挥；写模糊了，你会在调试阶段把时间还回去。
4. **指明验收动作。** 「截图这几个视角、模拟三个循环、确认零控制台报错」这类话，会直接变成它的自测脚本。
5. **迭代时指着已有成果说话。** 「把原来那个打磨一遍」比重新描述一遍需求更省 token，也更不容易跑偏。

---

提示词版权归各作者所有，此处仅作技术复现引用。
