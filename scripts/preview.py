#!/usr/bin/env python3
"""Quick check sheet: python preview.py in.mp4 out.jpg [effect ...]  (3 moments of each of the 20 newer effects, one row each)."""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fx
import numpy as np, cv2

TESTS = [('live-cursor', {}, 1.6), ('clone-row', {}, 1.4), ('day-dial', {}, 1.6), ('predict-keys', {}, 2.0), ('orbit-ring', {}, 1.6),
         ('code-body', {}, 1.6), ('post-wall', {}, 1.6), ('letter-dive', {}, 1.8), ('comment-drop', {}, 3.2), ('layer-explode', {}, 2.2),
         ('sketch-words', {}, 1.8), ('blade-slice', {}, 0.8), ('head-stack', {}, 2.2), ('rack-focus', {}, 1.6), ('banknote', {}, 1.8),
         ('voice-note', {}, 2.2), ('impact-frame', {}, 0.9), ('dolly-zoom', {}, 1.8), ('press-front', {}, 1.6), ('paper-tear', {}, 1.0),
         ('blow-away', {}, 2.2)]


def main():
    src, dst = sys.argv[1], sys.argv[2]; only = sys.argv[3:]
    extra = json.loads(os.environ.get('FX_OPTS', '{}'))
    fr, fps, dur, sw, sh = fx.probe(src); W = 1080; H = int(round(W * sh / sw / 2)) * 2; aw = 540; ah = int(round(aw * sh / sw / 2)) * 2
    tests = [t for t in TESTS if not only or t[0] in only]; base = 1.0
    want = {}
    for name, o, d in tests:
        for k, f_ in enumerate((0.22, 0.55, 0.9)): want.setdefault(int(round((base + d * f_) * fps)), []).append((name, k))
    frames = {}
    for i, frame in enumerate(fx.read_frames(src, W, H, fr)):
        if i in want: frames[i] = frame.copy()
        if i > max(want): break
    trk = fx.Tracker(aw, ah); info = {}
    for i in sorted(frames):
        trk.prev = None; m, f = trk(cv2.resize(frames[i], (aw, ah), interpolation=cv2.INTER_AREA), int(i / fps * 1000)); info[i] = (m, f)
    rows = []
    for name, o, d in tests:
        e = fx.Fx({'fx': name, 'start': base, 'end': base + d, **o, **extra.get(name, {}), **extra.get('*', {})}, fps); cells = []
        for f_ in (0.22, 0.55, 0.9):
            i = int(round((base + d * f_) * fps)); m, f = info[i]; c = fx.Ctx(); c.W, c.H, c.t, c.fps = W, H, i / fps, fps
            c.img = frames[i].astype(np.float32) / 255; c.m = cv2.resize(m, (W, H)).astype(np.float32) / 255
            sc = W / aw; f = f or (aw / 2, ah * 0.33, aw * 0.15); c.fx, c.fy, c.fw = f[0] * sc, f[1] * sc, max(f[2] * sc, W * 0.05); c.lt = c.t - e.start
            fx.EFFECTS[name][0](c, e)
            if os.environ.get('FX_LIST'):
                tl = fx.Fx({'fx': 'tracklist', 'start': 0, 'end': 99, 'ticks': '0|0.3|0.6'}, fps); c.lt = c.t; fx.EFFECTS['tracklist'][0](c, tl)
            im = cv2.resize((np.clip(c.img, 0, 1) * 255).astype(np.uint8), (360, int(360 * H / W)), interpolation=cv2.INTER_AREA)
            cv2.putText(im, name, (8, 22), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2); cells.append(im)
        rows.append(np.hstack(cells)); print('ok', name, flush=True)
    per = int(os.environ.get('FX_PER', 3)); sheets = [np.hstack(rows[k:k + per]) for k in range(0, len(rows), per)]
    w = max(s.shape[1] for s in sheets); sheets = [np.pad(s, ((0, 0), (0, w - s.shape[1]), (0, 0))) for s in sheets]
    base_, ext = os.path.splitext(dst)
    for k in range(0, len(sheets), 2):
        out = f'{base_}-{k // 2 + 1}{ext}'; cv2.imwrite(out, cv2.cvtColor(np.vstack(sheets[k:k + 2]), cv2.COLOR_RGB2BGR)); print('saved', out)


if __name__ == '__main__':
    main()
