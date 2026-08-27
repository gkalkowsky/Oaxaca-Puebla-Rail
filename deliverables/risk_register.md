# Risk Register

Risks to the **screen's conclusion** — the things that would make this
assessment wrong. Not construction or operating risks of the project itself;
those belong to a real study, if one is ever commissioned.

**Status: not started.** Entries below are opened at Phase 0 with the risks
inherent to desk research on this corridor. Likelihood and impact are
unassessed until sources exist.

## Scoring

**Likelihood** — `low` / `medium` / `high`, judged on evidence, not vibes.
**Impact** — effect on the verdict if the risk is real:

| Impact | Meaning |
|---|---|
| `fatal` | Would flip the verdict |
| `major` | Would change a headline figure by more than an order of magnitude |
| `moderate` | Would change a headline figure materially but not the verdict |
| `minor` | Noted for completeness |

## Register

| ID | Risk | Category | Likelihood | Impact | Mitigation | Status |
|----|------|----------|-----------|--------|------------|--------|
| R-01 | Terrain data resolution too coarse to establish a true ruling grade; a corridor screened as viable has an unbuildable segment | Data | _tbd_ | fatal | Cross-check DEM-derived profile against any published survey; state the DEM resolution alongside every grade figure | open |
| R-02 | Capital cost carried from analogue projects in materially different terrain, understating mountain construction | Method | _tbd_ | major | Only use analogues with a stated and comparable grade/tunnel profile; tag every carried figure `[ANALOGUE]` | open |
| R-03 | Demand estimated from population rather than observed O–D travel, overstating a corridor people may simply not travel | Method | _tbd_ | fatal | Anchor to observed bus/air/toll counts; treat population as a ceiling, never a forecast | open |
| R-04 | Mode-capture assumption unsupported; rail assumed to take share from road without journey-time advantage | Method | _tbd_ | fatal | State capture assumption explicitly in §4; test breakeven against a zero-growth, low-capture case | open |
| R-05 | Existing freight concession over part of the corridor forecloses or prices out passenger use | Legal | _tbd_ | fatal | Check ARTF concession registry and DOF grants before any alignment conclusion | open |
| R-06 | Federal sources unretrievable — reorganised sites, dead links across administrations | Data | _tbd_ | major | Wayback recovery, DOF search by date, INAI request; mark `unavailable` rather than substituting press reporting | open |
| R-07 | Reliance on press reporting of announced projects, which routinely misstates cost, scope and status | Source quality | _tbd_ | major | `press` sources may not solely support a conclusion (see data_sources.md §1) | open |
| R-08 | Political announcement mistaken for a funded programme; budget line assumed to exist | Source quality | _tbd_ | major | Require a PEF line item or equivalent before treating funding as real | open |
| R-09 | Protected areas or indigenous community land in the corridor not identified at screen stage | Legal | _tbd_ | major | Overlay protected-area and agrarian tenure data on candidate alignments | open |
| R-10 | Currency, base year and units inconsistently handled across sources (MXN/USD, nominal/real) | Method | _tbd_ | moderate | Fix a base year and currency in the model; record both for every source figure | open |
| R-11 | Screen anchors on the first plausible alignment and never tests alternatives | Method | _tbd_ | moderate | Carry at least two candidate corridors until terrain data eliminates one | open |
| R-12 | Confirmation pressure toward a GO verdict because a GO is a more interesting deliverable | Method | _tbd_ | fatal | Stop rules are evaluated in order and in writing before the verdict is drafted | open |

## Review

The register is reviewed at every phase boundary. New risks are appended, never
renumbered. A risk is closed only with a note stating what evidence closed it.
