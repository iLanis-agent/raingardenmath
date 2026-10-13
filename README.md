# Rain garden math

Rain garden and runoff arithmetic: the roof names the liters, the liters name the bed, and the bed names the mulch.

Live at https://ilanis-agent.github.io/raingardenmath/

## The three tools

- **Catch plan** - liters = roof area x rain x 10 x labeled 0.9 runoff coefficient, with barrel-scale, garden-scale and swale-territory bands.
- **Bed plan** - bed m2 = roof area x labeled 15 percent sizing rule, with planter-box, weekend-dig and landscaper's-job bands.
- **Mulch plan** - liters = bed x labeled 8 cm of mulch; bags = ceil(liters / labeled 50 L), with car-trunk, few-trips and delivery-load bands.

## Formulas and limits

- Liters and bed areas are rounded to one decimal (round half up), mirroring the oracle float-for-float.
- Every number the app borrows is labeled in the interface: runoff coefficient, sizing percent, mulch depth, bag size.
- Illustrative planning arithmetic only. Real sizing depends on your soil's infiltration rate - run a labeled bucket perk test before you dig - and give the water a safe overflow path that never points at a foundation, a neighbor or a septic field. This is not a drainage design.

## Development

- `engine.js` - calculation and render engine (browser global `RainGardenMath`, CommonJS for tests).
- `oracle.py` - Python mirror of the engine; regenerates `expected.json`.
- `test.js` - runs every case through the engine and compares fields and render strings: `node test.js`.
