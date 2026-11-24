# One Line of Earned Pride

One line of text, written to `/output/entry.txt` by `main.py`.

> At dawn the potter opened the kiln, and the glaze she had ruined nine times came out blue as deep water, whole.

The line is 111 characters. It is a potter at dawn opening a kiln after nine
ruined firings, and the glaze finally coming out right. The pride is in the
work itself: nine failures behind her, one whole piece in her hands. Nothing
in the line says she is proud. The kiln, the dawn and the colour do that.

## Why this scene

The bounty asks for a quiet, earned moment of pride for someone in a scene,
a small person doing something hard or a long effort finally landing. A potter
fits both. The work is slow, the failure is ordinary, and the payoff is a
single object you can hold.

The field is crowded with night shifts, fathers, first attempts and learning
to read. Kilns, glaze and potters barely appear in it. The scene is fresh
without being strange.

## Run it

```sh
python3 main.py
```

It writes the line to `/output/entry.txt` with no trailing newline, as UTF-8,
mode 0644. The output is the same on every run: the program holds one fixed
line and writes it unchanged.

## Files

- `main.py` — the entry. One fixed line, a length check, then the write.
- `LICENSE` — MIT.
