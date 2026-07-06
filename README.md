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

(C) 2026 CHOIIZUKA.COM.
https://CHOIIZUKA.COM
