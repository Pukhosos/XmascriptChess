# XmascriptChess

A simple chess engine implemented in Xmascript.

## Upstream

Here is the [upstream Xmascript implementation](
    https://github.com/BesserwisserErsterKlasse/Xmascript
)

## How to Run it

In your existing Xmascript notebook, in a new cell run:

```python
interpreter.run('/absolute/path/to/xmas_chess/main.xmascript')
```

For a conventional **terminal/GUI UCI process** run:

```bash
python3.14 run_uci.py /path/to/Xmascript/xmascript.ipynb
```

Your GUI may need to be configured to launch `python3.14` with those two script
arguments, rather than pointing to an executable. The original Xmascript
notebook is required as the chess engine does not implement a replacement
interpreter.

### UI

Create `/bin/xmascript-chess` file

```bash
#!/bin/bash
cd /home/yaz008/Desktop/Code/Vibecode/XmascriptChess
exec python3.14 run_uci.py \
  /home/yaz008/Desktop/Code/GitHub/Xmascript/xmascript.ipynb
```

Make it executable

```bash
chmod +x ~/bin/xmascript-chess
```

Launch the UI

```bash
chess-tui -e ~/bin/xmascript-chess --depth 2
```

**Note:** depths higher than 3 take a very long time to run.

### Tests

For an automated syntax/chess-rule smoke test in the notebook run:

```python
interpreter.run('/absolute/path/to/xmas_chess/smoke_test.xmascript')
```

Or from a terminal:

```bash
python3.14 \
    run_uci.py \
    /path/to/Xmascript/xmascript.ipynb \
    --program smoke_test.xmascript
```

## Example UCI session

```text
uci
isready
ucinewgame
position startpos moves e2e4 e7e5 g1f3
# the next command is a real UCI command; this line is not
# meant to be typed into the engine
go depth 2
position fen r3k2r/8/8/8/8/8/8/R3K2R w KQkq - 0 1
go depth 2
quit
```

The replies to `uci`, `isready`, and `go` include `uciok`, `readyok`, iterative
`info depth ... score cp ... pv ...`, and `bestmove ...` respectively.
`position ...` is accepted for either side to move, as indicated by FEN or the
parity of the applied moves.

**Note:** Remove comment lines when entering UCI commands.

## License

`XmascriptChess` is a free, open-source software distributed under the
[GPLv3 License](LICENSE.txt).
