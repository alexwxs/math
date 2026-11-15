# Math

Node.js site for maths questions and solutions.

## Setup

Python 3 is used only to convert the Word doc into HTML (no `npm install` required).

```bash
npm start
```

Open [http://localhost:2026/year11](http://localhost:2026/year11).

## Routes

| Path | Content |
|------|---------|
| `/` | Home |
| `/year11/` | Year 11 (from docx) |
| `/year12/` | Year 12 — Vector Geometry (1), … |

## Content source

- Year 11: `content/Questions_and_Solutions.docx`
- Year 12: `scripts/build-year12.py` (chapter content) + `content/year12/media/`

Rebuild HTML:

```bash
npm run build:content
```

## Port

Default port is **2026**. Override with:

```bash
set PORT=3000
npm start
```
