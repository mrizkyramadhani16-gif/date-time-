"""Jalankan delapan praktikum dan simpan bukti stdout/stderr."""
from pathlib import Path
from datetime import datetime, timezone
import json
import platform
import subprocess
import sys

ROOT = Path(__file__).resolve().parent


def main():
    hasil = []
    header = [
        "HASIL RUN PRAKTIKUM PYTHON DATETIME DAN TIME",
        "Waktu eksekusi UTC: " + datetime.now(timezone.utc).isoformat(),
        "Python: " + platform.python_version(),
        "Sistem: " + platform.system() + " " + platform.machine(),
        "Perintah: python run_all.py",
        "Waktu dinamis mengikuti jam lingkungan eksekusi.",
    ]
    for script in sorted((ROOT / "praktikum").glob("[0-9][0-9]_*.py")):
        proses = subprocess.run(
            [sys.executable, str(script)], capture_output=True,
            text=True, encoding="utf-8", timeout=15,
        )
        hasil.append({
            "file": script.name, "exit_code": proses.returncode,
            "stdout": proses.stdout, "stderr": proses.stderr,
        })
        header += ["", "=" * 64, script.name,
                   "Exit code: " + str(proses.returncode), proses.stdout]
        if proses.stderr:
            header += ["STDERR:", proses.stderr]
    sukses = sum(item["exit_code"] == 0 for item in hasil)
    header += [f"RINGKASAN: {sukses}/{len(hasil)} program berhasil."]
    output = ROOT / "hasil"
    output.mkdir(exist_ok=True)
    teks = "\n".join(header) + "\n"
    (output / "hasil_run.txt").write_text(teks, encoding="utf-8")
    (output / "hasil_run.json").write_text(
        json.dumps(hasil, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print(teks)
    return 0 if sukses == 8 and len(hasil) == 8 else 1


if __name__ == "__main__":
    raise SystemExit(main())
