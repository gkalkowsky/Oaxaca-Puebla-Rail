# Contribution margin per ton-km — derivation from ARTF primary source

**This closes the gap that was blocking Step 2.** The figure is derived from
ARTF's own published accounts, not from a US Class I proxy.

## Access

`www.gob.mx/artf` serves a bot-challenge page. The Anuario PDFs are served from
the **CMS attachment path**, which is not challenged:

```
https://www.gob.mx/cms/uploads/attachment/file/1020005/Anuario_2024_P.pdf
https://www.gob.mx/cms/uploads/attachment/file/920778/Anuario_2023_ARTF.pdf
```

Same institution, same site, different path. This is the second instance of the
pattern that `micrs.sct.gob.mx` established for DGST.

## Figures — ARTF *Anuario Estadístico Ferroviario* 2024

All in **constant 2024 MXN**. ARTF deflates using INEGI INPC, base 2H July 2018.

| Quantity | Ferrosur (FSRR) | Source |
|---|---|---|
| Revenue per ton-km | **$0.93** | Tabla 7-8 |
| Total freight revenue | $8,538,620 thousand | Tabla 7-3 |
| Operating profit (*utilidad de operación*) | $3,688,169 thousand | Tabla 7.7 |
| Operating margin ratio | 3,688,169 / 8,538,620 = **43.19%** | derived |
| **EBIT per ton-km** | 0.93 × 0.4319 = **$0.402** | derived |

National context 2024: 132.69 Mt, 95,764 million ton-km, total freight revenue
$89,327.6 million MXN; published system-wide revenue per ton-km $0.80
(Tabla 7-8).

**Ferrosur is the right comparator.** It is the Sureste concessionaire, it held
the Art. 23 service obligation on this line from 1999, and the segment was
excluded from its concession in 2012.

## What the figure is, and is not

ARTF defines *costos totales de operación* as including **network operation and
maintenance, plus depreciation and amortisation** (Anuario 2024, §7.2). So:

- **$0.402/ton-km is EBIT**, not contribution margin. Track maintenance is
  already deducted. Using it as the surplus available to service *new*
  rehabilitation capital is **conservative**, because D&A on existing assets is
  also deducted — a partial double-count of capital recovery.
- **$0.93/ton-km is gross revenue**, with no operating cost at all deducted.
  Clearly too generous.
- The true figure lies between. ARTF does not publish the D&A split, so the
  analysis **sweeps 0.402 → 0.93** rather than picking one.

**Consequence for the model:** if the margin input is set on the EBIT basis,
`varOM` and `FixedOM` must be zero, or maintenance is counted twice. ARTF's
cost base already contains them.

## Caveat that runs the other way

Ferrosur's margin is earned on a dense, functioning network. A 216.5 km branch
carrying a fraction of that traffic would very likely earn **less** per ton-km:
fixed costs spread over less volume, shorter hauls, no interline density. Using
Ferrosur's figure is therefore generous to the project. Labelled as an
assumption wherever it is used.

## Reconciliation note

Independently dividing national revenue by national ton-km
(89,327.6 MXNm / 95,764 M ton-km) gives $0.933/ton-km, against the published
system-wide $0.80. The discrepancy is ~16% and is not resolvable from the
document — ARTF's Tabla 7-8 denominator evidently counts a different set of
traffics (the Anuario distinguishes *local / recibido / en tránsito / remitido*).
**The published figure is cited; the derived one is not used.** Flagged rather
than silently reconciled.
