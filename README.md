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

## ディレクトリ構成

```
TRFont/
├── .github/workflows/
│   └── build-font.yml   # push/手動実行でTTFを自動ビルドするGitHub Actions
├── config.py       # 設計パラメータ（ここを変えると全文字が再生成される）
├── primitives.py   # 図形プリミティブ（矩形バー・楕円・ブール演算合成）
├── glyphs.py       # A-Z, a-z, 0-9, ギリシャ文字の字形定義
├── symbols.py      # 記号・科学記号の字形定義
├── build.py        # UFOを組み立ててTTFにコンパイル
├── preview.py      # 生成したフォントでpreview.pngを作る
├── output/
│   └── TRSans-Regular.ttf
└── preview/
    └── preview.png
```

## 修正済みの既知バグ（重要・再発防止のため記録）

**症状**: B, D, 8, 9 など「輪(穴)を持つ文字」が、穴の部分まで黒く塗りつぶされてしまう。

**原因**: `build.py` の `ufo2ft.compileTTF()` に `removeOverlaps=True` を指定していたが、
`primitives.py` の `combine()` がその時点で既にskia-pathopsによるブール演算
（重なり除去・穴の生成）を完了させていたため、**二重に重なり除去処理がかかり**、
本来残るべき内部の穴が外形とマージされて消えてしまっていた。

**対処**: `build.py` は `removeOverlaps=False` で呼び出すこと。
`combine()` を使わず単純な輪郭だけを描画する場合は `True` に戻して構わないが、
このプロジェクトの `glyphs.py` / `symbols.py` は全グリフが `combine()` 経由のため、
**`removeOverlaps` は常に `False` のままにする**のが正しい。

## セットアップ

```bash
pip install ufoLib2 ufo2ft fonttools skia-pathops
```

（`skia-pathops` は、複数の図形を重ねて1つのアウトラインに統合するブール演算に使用）

## 実行方法

```bash
# 1. フォントを生成
python build.py
# → output/TRSans-Regular.ttf が生成される

# 2. プレビュー画像を生成（生成したフォントを実際に読み込んで確認）
python preview.py
# → preview/preview.png が生成される
```

## GitHub Actionsでの自動ビルド

`.github/workflows/build-font.yml` をリポジトリに含めてpushすると、
`config.py` / `glyphs.py` / `symbols.py` などを変更してpushするたびに、
GitHub Actions上で自動的に:

1. 依存ライブラリのインストール
2. `python build.py`（TTF生成）
3. `python preview.py`（プレビュー画像生成）
4. 生成物（TTF + プレビュー画像）をArtifactとしてアップロード

まで実行される。GitHubリポジトリの「Actions」タブから手動実行（`workflow_dispatch`）も可能。

## OSへのインストール方法

- **macOS**: `output/TRSans-Regular.ttf` をダブルクリック → 「フォントをインストール」
- **Windows**: `output/TRSans-Regular.ttf` を右クリック → 「インストール」
- **Linux**: `~/.local/share/fonts/` にコピーして `fc-cache -f` を実行

## 設計値を変える（config.py）

例えば線幅を太くしたい場合:

```python
STROKE_WIDTH = 90  # 70 → 90 に変更
```

変更後 `python build.py` を再実行すれば、全62+17文字が新しい線幅で再生成されます。

## 今後の改善案（優先度順）

1. **曲線の質を上げる**: C/S/3/eなどの「開いた円」を、四角で断ち切る現在の方式から、
   角度指定のアーク（部分円弧）で切り出す方式に変えると、開口部が自然な曲線になる。
2. **CORNER_RADIUS の実装**: バーの端・交差部に小さな丸め処理を入れると
   「わずかに角を丸める」というコンセプトに近づく。
3. **カーニングペア**: 特に `AV` `To` `LT` のような組み合わせの詰め。
4. **太さのバリエーション**: `STROKE_WIDTH` を変えた複数ウェイト(Light/Bold)の生成。
5. **Greek/記号の拡充**: 残りのギリシャ文字・数学記号（∞ √ ∑ ≠ など）の追加。
6. **ヒンティング**: 小サイズ表示の品質向上（`fontTools.ttLib.tables._h_i_n_t` 等）。
7. **人間による字形レビュー**: 現状は数値検証（bbox・空グリフチェック）のみ。
   実際にタイプデザイナーや目視での字形調整を挟むと品質が大きく上がる。

## 既知の技術的な仕組み（参考）

各文字は「足す図形（positives）」と「引く図形（negatives）」のリストとして定義し、
[skia-pathops](https://github.com/fonttools/skia-pathops) でブール演算（合体→差分）した上で、
[ufo2ft](https://github.com/googlefonts/ufo2ft) が3次ベジェをTrueType用の2次ベジェへ自動変換して
TTFにコンパイルしています。図形の重なりや向き(時計回り/反時計回り)を手動で気にする必要がないため、
「円から四角を引いてリングを作る」「バーを重ねて合体させる」といった直感的な組み方が可能です。


---

# TR Font Prototype Drawing Specification
## Truth-Science Font Prototype v0.1

---

# Purpose

This document defines the drawing specifications for the prototype version of Truth-Science Font.

This is **NOT** the final font architecture.

The purpose of this prototype is to create a visually usable font as quickly as possible.

The prototype exists to validate the design direction and development workflow.

Perfect implementation is not required.

---

# Development Goal

The highest priority is:

> Generate an installable TrueType Font (TTF) using Python.

The generated font should be suitable for testing inside

- GitHub
- WordPress
- VSCode
- OBS
- Office
- TRPRESS articles

---

# Development Policy

Prototype First.

Code quality is secondary.

Architecture is secondary.

Visual appearance is more important than implementation elegance.

If multiple implementations are possible, always choose the simplest working solution.

---

# Character Set

Prototype supports only the following characters.

## Latin

ABCDEFGHIJKLMNOPQRSTUVWXYZ

abcdefghijklmnopqrstuvwxyz

---

## Numbers

0123456789

---

## Symbols

.

,

:

;

!

?

%

#

@

&

+

-

=

/

\

()

[]

{}

<>

"

'

_

*

^

~

---

## Scientific Symbols

∞

√

≈

≤

≥

±

×

÷

→

←

↑

↓

---

## Greek Letters

Σ

Δ

π

λ

μ

Ω

α

β

γ

---

# Font Style

Category

Sans Serif

---

Theme

Scientific

Mathematical

Modern

Elegant

Readable

---

Avoid

Overly futuristic

Cyberpunk

Decorative

Calligraphy

Comic style

---

# Design Rules

Stroke width should remain visually consistent.

Corners should be slightly rounded.

Characters should have balanced proportions.

Spacing should prioritize readability.

The font should feel calm and precise.

---

# Geometry

Use a simple coordinate system.

Units Per Em

1000

Baseline

0

Cap Height

700

xHeight

500

Ascender

800

Descender

-200

These values may be adjusted during implementation.

---

# Drawing Method

Glyphs may be created using

- Lines
- Bezier Curves
- Circular Arcs
- Rectangles
- Polygons

The implementation method is flexible.

Visual quality is preferred over mathematical perfection.

---

# Prototype Philosophy

Do not spend time optimizing every glyph.

Instead,

create all glyphs with consistent style.

---

# Code Structure

A simple implementation is preferred.

Example

```
build.py

glyphs.py

config.py

preview.py
```

No complex architecture is required.

---

# Preview

Generate

preview.png

containing

ABCDEFGHIJKLMNOPQRSTUVWXYZ

abcdefghijklmnopqrstuvwxyz

0123456789

Truth-Science

TR Font

GitHub

Version 0.1

Σ Δ π λ μ Ω

---

# Font Output

Generate

TRSans-Regular.ttf

This font must be installable on

Windows

macOS

Linux

---

# Build

The project should be executable using

```
python build.py
```

The output font should be written into

```
output/

TRSans-Regular.ttf
```

---

# Validation

The prototype is considered successful if

✓ TTF generation succeeds

✓ Font installs successfully

✓ Characters display correctly

✓ GitHub Actions can build it

✓ WordPress can use it

Perfect kerning and hinting are NOT required.

---

# AI Development Policy

This prototype prioritizes speed over perfection.

Future versions may completely replace the implementation.

Please avoid unnecessary abstractions.

The objective is to create a working prototype that demonstrates the Truth-Science Font concept.

---

# Future

After the prototype is completed,

the project will move toward a specification-driven font generation system.

That future architecture is intentionally outside the scope of this document.

Focus only on producing the best possible prototype.

---

# Mission

Build something real.

See it.

Use it.

Improve it.

Prototype first.

Architecture later.

---

This document intentionally prioritizes implementation speed over software architecture.

The purpose of this prototype is to discover the optimal design through practical experimentation.

Refactoring is expected after successful validation.

（このドキュメントは意図的にソフトウェアアーキテクチャより実装速度を優先しています。本プロトタイプの目的は、実際に動くフォントを作りながら最適な設計を見つけることです。検証後のリファクタリングを前提としています。）

===

# Truth-Science Font Builder

> **Python × FontForge × GitHub Actions**
>
> Build the Truth-Science Font automatically by merging multiple font sources into a single distributable font.

---

# Concept

Truth-Science Font is designed around a simple philosophy:

> **Readable Japanese × Original Latin Design**

Instead of creating tens of thousands of Japanese glyphs from scratch, the project combines existing high-quality Japanese fonts with an original Truth-Science Latin font.

This dramatically reduces development cost while allowing the project's unique identity to remain in the Latin alphabet, numbers, symbols, and scientific glyphs.

---

# Build Flow

```text
TRSans (Original Latin)
           │
           ▼
      Merge M PLUS
           │
           ▼
     Merge Noto Sans JP
           │
           ▼
 Truth-Science-MPlus.ttf
```

GitHub Actions performs the entire process automatically.

---

# Repository Structure

The workflow expects the following directory layout.

```
Repository/

├── .github/
│   └── workflows/
│       └── build.yml
│
├── M_PLUS_1p/
│   └── mplus-1p-regular.ttf
│
├── Noto_Sans_JP/
│   ├── NotoSansJP-Regular.otf
│   └── (or .ttf)
│
├── output/
│   └── TRSans-Regular.ttf
│
└── dist/
    └── Truth-Science-MPlus.ttf
```

---

# Required Files

## 1. Original Truth-Science Font

```
output/TRSans-Regular.ttf
```

This font contains the original Latin alphabet, numbers, symbols and future Truth-Science glyphs.

---

## 2. M PLUS

```
M_PLUS_1p/mplus-1p-regular.ttf
```

Used as the Japanese fallback font.

---

## 3. Noto Sans JP

```
Noto_Sans_JP/NotoSansJP-Regular.otf
```

or

```
NotoSansJP-Regular.ttf
```

Provides high-quality Japanese glyph coverage.

---

# Naming Rules

GitHub Actions runs on Linux.

Linux treats uppercase and lowercase filenames as different files.

For maximum compatibility, use the exact filenames below.

| Folder | File |
|---------|------|
| M_PLUS_1p | mplus-1p-regular.ttf |
| Noto_Sans_JP | NotoSansJP-Regular.otf |
| output | TRSans-Regular.ttf |

Changing these names may cause the workflow to fail.

---

# Automatic Build

The GitHub Action performs the following steps.

1. Checkout repository
2. Install FontForge
3. Load the original TRSans font
4. Merge M PLUS
5. Merge Noto Sans JP
6. Rename the resulting font
7. Export the final TTF
8. Upload the build artifact

No manual FontForge operations are required.

---

# Output

The generated font is exported as

```
dist/

Truth-Science-MPlus.ttf
```

and uploaded automatically as a GitHub Actions artifact.

---

# Design Philosophy

Truth-Science Font follows a layered architecture.

```
Original Design

↓

TRSans

↓

M PLUS

↓

Noto Sans JP

↓

Truth-Science Font
```

The original Truth-Science glyphs always remain the highest priority.

Japanese glyphs are supplied by mature open-source fonts.

This approach combines

- maximum readability
- minimum maintenance
- original branding

into a single font family.

---

# Future Roadmap

Current

- Latin
- Numbers
- Symbols

Next

- Greek Alphabet
- Mathematical Symbols
- Scientific Operators

Future

- Variable Font
- OpenType Features
- Ligatures
- Truth-Science Icons

---

# Mission

The goal of this project is not simply to create another font.

It is to build a reproducible, open-source typography platform for science, mathematics, AI and philosophy.

Everything should be generated from specifications and code whenever possible.

> **Readable by everyone.
> Recognizable as Truth-Science.**
````
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
