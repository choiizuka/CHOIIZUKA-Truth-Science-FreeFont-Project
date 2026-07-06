import sys, os, yaml, fontforge
font_dir = sys.argv[1].rstrip('/')
meta = yaml.safe_load(open(f"{font_dir}/metadata.yml"))
sys.path.insert(0, font_dir)
import config, glyphs

font = fontforge.font()
font.fontname = meta['id']
font.familyname = meta['family']
font.fullname = f"{meta['name']} {meta['weight']}"
font.em = config.UPM
font.ascent = config.ASCENDER
font.descent = abs(config.DESCENDER)

glyphs.build(font, config) # ←ここでstrokeする

os.makedirs('dist', exist_ok=True)
font.generate(f"dist/{meta['output']}")
print(f"✅ {meta['output']}")
