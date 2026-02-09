import plistlib
from pathlib import Path

# ==== 設定ここから ====
INPUT_FILE = "Text Substitutions_XXXXXX.plist"  # ← 入力ファイル名をここで指定
# ==== 設定ここまで ====

in_path = Path(INPUT_FILE)
out_path = in_path.with_suffix(".txt")

with open(in_path, "rb") as f:
    plist_data = plistlib.load(f)

output_lines = []

for entry in plist_data:
    reading = entry.get("shortcut") or entry.get("Shortcut") or entry.get("key")
    word = entry.get("phrase") or entry.get("Phrase") or entry.get("replacement")
    if not word or not reading:
        continue
    # Google日本語入力は「読み」「単語」「品詞」の順
    output_lines.append(f"{reading}\t{word}\t名詞")

with open(out_path, "w", encoding="utf-8-sig") as f:
    f.write("\n".join(output_lines))

print(f"変換完了: {out_path} （{len(output_lines)} 件）")
