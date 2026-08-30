from pathlib import Path
root=Path(__file__).resolve().parents[2]
p=(root/'claude/PROJECT_INSTRUCTIONS.md').read_text(encoding='utf-8')
checks={
 'version':'Project Instructions v1.3.0' in p,
 'binding':'Project Knowledgeの参照方法' in p,
 'no_path_open':'ローカルファイルシステム上のパスとして開こうとしない' in p,
 'safety':'Safety Core（常設フォールバック）' in p,
 'robots':'Web Evidence Fallback' in p,
 'opinion':'Editorial Opinion規則' in p,
}
for k,v in checks.items(): print(f'{k}: {"PASS" if v else "FAIL"}')
raise SystemExit(0 if all(checks.values()) else 1)
