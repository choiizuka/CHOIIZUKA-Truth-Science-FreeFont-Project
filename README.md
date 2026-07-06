# CHOIIZUKA-Truth-Science-FreeFont-Project
CHOIIZUKA-Truth-Science-FreeFont-Project

👑🍸💕

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
