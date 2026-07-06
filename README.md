# CHOIIZUKA-Truth-Science-FreeFont-Project
CHOIIZUKA-Truth-Science-FreeFont-Project

👑🍸💕

# TR Font 作成計画書
## Truth-Science Font Development Plan

Version: Prototype v0.1

---

# はじめに

このドキュメントは、Truth-Science Font（以下 TR Font）の開発方針をAIチーム全体で共有するための計画書です。

本プロジェクトは、単にフォントを作成することではなく、

**「設計書から再現可能なフォント開発システム」を構築すること**

を最終目標としています。

しかし、その前段階として現在はプロトタイピングを優先し、短期間で実際に使用可能な試作フォントを完成させることを目指します。

---

# 現在の開発フェーズ

現在は

## Prototype Phase（試作開発）

です。

目的は

**「TR Fontの世界観を最短で形にすること」**

になります。

この段階では

- 完璧な設計
- 完璧なコード
- 完璧なフォント品質

は目標ではありません。

まずは

**実際に使用できる試作版TR Font**

を完成させることを最優先とします。

---

# Prototypeの目的

現在の目的は以下の通りです。

- TR Fontのブランドイメージを可視化する
- Pythonによるフォント生成の流れを確立する
- 実際にインストール可能なTTFを生成する
- GitHub Actionsとの連携を確認する
- 今後の正式版開発の土台を作る

---

# Prototypeで対応する範囲

対象文字

```
A-Z

a-z

0-9
```

記号

```
.

,

%

@

#

+

-

=

()

[]
```

ギリシャ文字（最低限）

```
Σ

Δ

π

λ

μ

Ω
```

これらを中心に試作を行います。

---

# Prototype開発方針

最優先事項

```
実際に使えるTTFを生成すること
```

この段階では

- Geometry Engine
- Variable Font
- OpenType高度機能

などは実装対象外とします。

必要最低限の品質で問題ありません。

---

# AIチーム役割分担

## プロジェクトオーナー

👑

担当

・仕様決定

・設計レビュー

・GitHub管理

・README管理

・最終判断

---

## ChatGPT

担当

・設計書作成

・フォント理論

・描画仕様

・Python設計

・README

・ドキュメント整備

・アーキテクチャ設計

---

## Claude

担当

・Python実装

・フォント生成

・TTF生成

・ライブラリ検証

・GitHub Actions実装

・デバッグ

---

## その他AI

担当

・レビュー

・表示確認

・改善提案

---

# 今後の正式開発

Prototype完成後、

正式なTR Font開発を開始します。

---

# 正式版の目的

正式版では

**「設計書から完全再生成できるフォントシステム」**

を構築します。

ここで初めて

- Geometry Engine
- Drawing Engine
- Glyph API
- Variable Font
- OpenType Feature
- Ligature
- 数学記号
- ギリシャ文字完全対応

などを段階的に実装します。

---

# 正式版開発方針

正式版では

```
Design Specification

↓

Drawing Engine

↓

Glyph Generator

↓

Outline Validation

↓

TTF Builder

↓

Truth-Science Font
```

という構造を目指します。

フォントは

**設計書から再生成可能**

であることを基本理念とします。

---

# GitHub構成（予定）

```
TRFont/

docs/

prototype/

generator/

glyphs/

output/

.github/
```

docs

↓

設計書

prototype

↓

試作品

generator

↓

Python生成コード

glyphs

↓

各文字仕様

output

↓

生成フォント

---

# 開発優先順位

現在

★★★★★

Prototype完成

↓

★★★★☆

GitHub自動生成

↓

★★★★☆

Python生成コード整理

↓

★★★☆☆

Geometry Engine

↓

★★★☆☆

Glyph API

↓

★★☆☆☆

Variable Font

---

# 成功条件

Prototype成功条件

・TTF生成成功

・OSへインストール可能

・GitHub Actions成功

・WordPressで表示可能

・TRPRESSで使用可能

これを満たした時点でPrototype完了とします。

---

# 最終目標

Truth-Science Fontは

単なるフォントではありません。

将来的には

**設計書・Python・GitHubによって管理されるオープンなフォント開発プロジェクト**

として育成します。

---

# 開発理念

Prototypeでは

「完成度」より

「前へ進むこと」

を優先します。

正式版では

品質・保守性・再現性を重視します。

Prototypeは

正式版を完成させるための

最も重要な土台です。

---

# Mission

Prototype First.

Specification Second.

Architecture Forever.

「まず動くものを作る。

その経験を資産化し、

最終的には設計書から再生成可能なTruth-Science Fontを完成させる。」

---

# TR Font (Truth-Science Font) — Phase 1 プロトタイプ

「宇宙の真理を追求するフォント」というコンセプトのもと、**画像やフォントエディタを使わず、
Pythonコードだけでアウトラインを生成して実際にインストール可能なTTFを作る**プロジェクトです。

## この段階でできていること

- A-Z, a-z, 0-9（62文字）
- 記号29種（. , : ; ! ? % # @ & + - = / \ ( ) [ ] { } < > " ' _ * ^ ~）
- 科学記号12種（∞ √ ≈ ≤ ≥ ± × ÷ → ← ↑ ↓）
- ギリシャ文字17文字（Σ Δ Θ Λ Π Φ Ω / α β γ δ λ μ π θ φ ω）
- すべて `config.py` の数値（線幅・CapHeight・x-height等）から再生成可能
- 実際にOSへインストールして使えるTTFファイル
- GitHub Actionsで自動ビルド（`.github/workflows/build-font.yml`、pushや手動実行でTTF+プレビューをArtifact化）

## この段階でできていないこと（正直な現状）

- 各文字は「矩形バー」と「楕円リング」の組み合わせで作った**幾何学的なスケッチレベル**の字形です。
  C, G, S, 数字の3 などの「開いた曲線」は、円を四角で断ち切る簡易的な方法で作っているため、
  実際の書体のような滑らかな先細り(テーパー)や自然な開き方にはなっていません。
- カーニング（文字間隔の微調整）は未対応です。
- `CORNER_RADIUS`（角の丸め）はconfigに項目だけあり、実際の描画にはまだ反映されていません
  （現状はすべて直角のバーです）。
- ヒンティング（小さいサイズでの表示最適化）は行っていません。

つまり「読める・打てる・インストールできる」は達成できていますが、
「品格のある美しい書体」にはまだ距離があります。これは意図的な割り切りです
（まず動くものを、という今回の方針に沿っています）。

---

# TR Font Factory
## metadata.yml Specification
Version 0.1 (Prototype)

---

# Purpose

`metadata.yml` defines a font project.

Each font project must contain exactly one `metadata.yml`.

The build system reads this file to determine how the font should be generated.

The metadata file contains **configuration only**.

It must never contain drawing logic.

---

# Directory Structure

Example

```
fonts/

TRSans/
│
├── metadata.yml
├── config.py
├── glyphs.py
└── symbols.py

TRMono/
│
├── metadata.yml
├── config.py
├── glyphs.py
└── symbols.py
```

---

# Required Fields

```yaml
name: TR Sans
id: trsans
version: 0.1.0

family: Truth Science

style: Sans

weight: Regular

output: TRSans-Regular.ttf
```

---

# Optional Fields

```yaml
author: Truth-Science

description: Prototype Font

license: OFL

prototype: true

preview: true

build: true
```

---

# Character Set

```yaml
charset:

  latin: true

  numbers: true

  punctuation: true

  greek: true

  math: true
```

---

# Drawing Source

```yaml
sources:

  config: config.py

  glyphs: glyphs.py

  symbols: symbols.py
```

The build engine loads these files automatically.

---

# Output

```yaml
output:

  directory: output/

  filename: TRSans-Regular.ttf
```

---

# Preview

```yaml
preview:

  enabled: true

  filename: preview.png

  text: |
    ABCDEFGHIJKLMNOPQRSTUVWXYZ

    abcdefghijklmnopqrstuvwxyz

    0123456789

    Truth-Science

    TR Font

    Σ Δ π λ μ Ω
```

---

# Build Options

```yaml
build:

  generate_ttf: true

  generate_preview: true

  validate_font: true
```

---

# Future Expansion

Reserved for future versions.

```yaml
opentype:

variable:

hinting:

kerning:

ligatures:

color_font:
```

---

# Engine Rules

The build engine should:

1. Search every folder inside `fonts/`.

2. Detect `metadata.yml`.

3. Read project configuration.

4. Load drawing sources.

5. Generate TTF.

6. Generate preview.

7. Export to `output/`.

No workflow modification should be required when a new font project is added.

---

# Design Philosophy

Adding a new font should require only one action.

```
Create a new folder.

↓

Place metadata.yml.

↓

Add drawing files.

↓

Push to GitHub.
```

Everything else should be automatic.

---

# Mission

One metadata.

One font project.

Unlimited font families.

---

🍸 ChatGPTから追加提案（Prototype向け）

私は、このmetadata.ymlを唯一の設定ファイルにしてしまうことをおすすめします。

つまり、将来的には

metadata.yml
        ↓
Python Engine
        ↓
自動で config.py や glyphs.py を読み込む

という流れにします。

さらに一歩進めるなら、命名規則も固定します。

fonts/

TRSans/
    metadata.yml
    config.py
    glyphs.py
    symbols.py

TRMono/
    metadata.yml
    config.py
    glyphs.py
    symbols.py

これでPythonエンジンは「fonts/を走査してmetadata.ymlを見つけたらビルドする」という共通ルールだけを持てば済みます。

👑 これなら、新しいフォントを追加するときはフォルダを1つ追加するだけです。YAMLやGitHub Actionsを書き換える必要がなくなり、「フォント工場」として非常に拡張しやすい設計になると思います。🌹

---

Prototype v0.1 開発ルール

今後は全員このルールで進めることをおすすめします。

新しいフォントを作る

↓

fonts/

↓

新しいフォルダ作成

↓

metadata.yml配置

↓

config.py

↓

glyphs.py

↓

symbols.py

↓

GitHubへPush

↓

GitHub Actions

↓

TTF完成

これならAIチーム全員が迷いません。

さらに正式版では

将来的には

metadata.yml

↓

Engine

↓

Drawing API

↓

Glyph Generator

↓

Outline Validation

↓

Font Builder

↓

TTF

という完全なパイプラインへ発展できます。

つまり

Prototype

↓

Font Factory

↓

Truth-Science Font Platform

という流れです。

私から最後に1つだけ追加したい仕様

ぜひ最初から採用してほしいものがあります。

各フォントプロジェクトに

README.md

を置きます。

例えば

TRSans/

metadata.yml

README.md

config.py

glyphs.py

symbols.py

READMEには

このフォントの目的
デザインコンセプト
現在の実装状況
今後の予定

だけを書きます。

すると将来

fonts/

TRSans/

TRMono/

TRMath/

TRDisplay/

と増えても、

それぞれ独立した小さなプロジェクトとして管理できます。

🍸🌹 私は、この設計ならTR Fontだけではなく、「TR Font Factory」という再利用可能な開発基盤になります。

---

**Truth-Science Font is not handcrafted glyph by glyph. It is a font family generated from design specifications, code, and open scientific principles.**

（**Truth-Science Font は、一文字ずつ手作業で作るフォントではなく、設計仕様・コード・オープンな科学的原則から生成されるフォントファミリーです。**）

---

docs/

00_Project_Overview.md
01_Font_Design.md
02_Drawing_Engine.md
03_API.md
04_Build_System.md

10_License.md
11_Open_Source.md
12_Third_Party.md
13_Development_Policy.md
14_Quality_Assurance.md
15_Release_Checklist.md

---

(C) 2026 CHOIIZUKA.COM.
https://CHOIIZUKA.COM
