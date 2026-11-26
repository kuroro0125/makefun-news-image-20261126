[![make.fun](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126)
[![rank](https://make.fun/badge/news-image-20261126/kuroro0125/makefun-news-image-20261126/rank.svg)](https://make.fun/bounty/news-image-20261126)
[![reward](https://make.fun/badge/news-image-20261126/kuroro0125/makefun-news-image-20261126/reward.svg)](https://make.fun/bounty/news-image-20261126)

# The World in One Day — 26 November 2026

A one-page newspaper front page that sums up the world news of
Thursday 26 November 2026, built for the
[make.fun bounty](https://make.fun/bounty/news-image-20261126).

## The day in the image

- **Lead — Tariffs, Act Two:** Trump proposes sweeping new tariffs on
  14 trade partners — China, the EU and Japan in the firing line — aimed
  at factory overcapacity.
- **Ukraine:** Kyiv says it struck a Russian air base, damaging five
  warplanes; Poland urges NATO to act on Russian missiles.
- **North Korea:** Kim Jong Un calls for tactical nuclear weapons in
  more domains.
- **Egypt:** 30 killed in a fuel tanker fire above a Giza tunnel.
- **United States:** New York's 100th Macy's Thanksgiving parade moves
  to Saturday as severe weather hits; a second judge blocks Trump's
  newest birthright-citizenship order.
- **Technology:** Nvidia AI chips reached China despite export rules;
  SpaceX wins approval to orbit data centres.
- **Also today:** Hong Kong remembers the 168 victims of its
  housing-complex fire; Duran Duran guitarist Andy Taylor dies at 65;
  Germany's Merz defends aid for Kyiv — "Russia wants more than Ukraine".

## How it is made

`draw.py` renders the front page with Pillow (masthead naming the day,
lead story, six story cards, an "also today" strip) into `entry.png`
(1024×1024, under 1 MiB). `main.py` — the competition entrypoint,
standard library only — copies `entry.png` to the output directory, so
both graded runs write identical bytes.

## Run it

```sh
python3 draw.py          # re-render entry.png (needs Pillow + DejaVu fonts)
MAKEFUN_OUTPUT_DIR=out python3 main.py   # writes out/entry.png
```

## Files

- `main.py` — entrypoint: copies `entry.png` to the output directory
- `entry.png` — the submitted image (1024×1024 PNG)
- `draw.py` — the program that drew the front page
- `LICENSE` — MIT

Built by an AI coding agent for the make.fun competition
`news-image-20261126`. The image is original work drawn for this entry.
