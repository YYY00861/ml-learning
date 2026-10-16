"""Day 01 — 环境自检 + 第一段代码

运行方式（在本文件夹打开终端）：
    python hello.py

能正常输出结果，就说明你的环境没问题了。
"""

import datetime
import platform
import sys


def main() -> None:
    print("=" * 44)
    print(" Environment check")
    print("=" * 44)
    print(f"Python     : {sys.version.split()[0]}")
    print(f"Executable : {sys.executable}")
    print(f"OS         : {platform.system()} {platform.release()}")
    print(f"Now        : {datetime.datetime.now():%Y-%m-%d %H:%M:%S}")

    # 手写矩阵乘法 —— 这是你后面学「线性代数 + numpy」的起点
    # 先用手算的笨办法写一遍，等你学了 numpy 再回来对比，感受会完全不一样
    a = [[1, 2], [3, 4]]
    b = [[5, 6], [7, 8]]
    c = [[sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]

    print(f"\nA @ B = {c}")
    print("\nOK - your environment works.")


if __name__ == "__main__":
    main()
