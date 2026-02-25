# Roman ↔ Decimal CLI Converter

Simple Python CLI tool that converts:

- Roman → Decimal
- Decimal → Roman
- Supports negative numbers
- Accepts full sentences
- Strict Roman validation (no IC, no VX, etc.)

## Run

python roman_cli.py

## Example

> 5 1 10
Result: V I X

> M X I
Result: 1000 10 1

> -25
Result: -XXV

> IC
Result: InvalidRoman

> exit
Program stopped.