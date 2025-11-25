import argparse
import json
import os
import sys
import cv2

def parse_args():
    p = argparse.ArgumentParser(description="Minimal CV inference stub")
    p.add_argument("--input", required=True, help="input image path")
    p.add_argument("--output", required=True, help="output JSON path")
    return p.parse_args()

def main():
    args = parse_args()

    if not os.path.isfile(args.input):
        raise SystemExit(f"Input file not found: {args.input}")

    img = cv2.imread(args.input)
    if img is None:
        raise SystemExit(f"cv2 failed to read: {args.input}")

    h, w = img.shape[:2]

    result = {
        "input": args.input,
        "shape": {"height": h, "width": w},
        "msg": "Inference pipeline working"
    }

    outdir = os.path.dirname(args.output) or "."
    os.makedirs(outdir, exist_ok=True)

    with open(args.output, "w") as f:
        json.dump(result, f, indent=2)

    print("Wrote result to", args.output)

if __name__ == "__main__":
    main()
