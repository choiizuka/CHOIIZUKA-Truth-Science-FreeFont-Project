import sys, os, yaml, fontforge
font_dir = sys.argv[1]
meta = yaml.safe_load(open(f"{font_dir}/metadata.yml"))
sys.path.insert(0, font_dir)
import config, glyphs

font = fontforge.font()
font.fontname = meta['name'].replace(' ', '') + '-' + meta['weight']
font.familyname = meta['name']
font.fullname = f"{meta['name']} {meta['weight']}"
font.version = str(meta['version'])

font.em = config.UPM
font.ascent = config.ASCENDER
font.descent = -config.DESCENDER

glyphs.build(font, config)

os.makedirs('dist', exist_ok=True)
font.generate(f"dist/{meta['output']}")
print(f"✅ {meta['output']} generated")
