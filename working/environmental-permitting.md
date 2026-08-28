# Step 5 — environmental permitting

> ## CORRECTION, 2026-08-28
>
> **An earlier version of this file overstated the permitting constraint.** It
> reported that no subzone permits a linear rail corridor and implied the
> alignment therefore runs through the reserve without a permitted pathway. A
> GIS overlay against CONANP's own ANP boundary shapefile shows that
> **the Cañada valley floor — where both MEX-135 and the railway run — is
> largely EXCLUDED from the reserve.** All nine corridor waypoints test outside
> the boundary, and south of ~17.53°N there is no reserve at any longitude.
>
> The subzone analysis below remains factually correct about the reserve's
> internal rules. What changed is whether those rules **bind on this
> alignment** — and on current evidence they may substantially not. The
> constraint is downgraded from "potentially forecloses" to "narrow margin,
> unresolved". See `## GIS overlay` below.

**This revises the risk register.** R-01 was recorded as *fatal / unassessed*
because `whc.unesco.org` returned 403. The CONANP management programme was then
obtained and the risk is now **evidenced**, and its framing has changed.

**Source:** CONANP, *Programa de Manejo Reserva de la Biosfera Tehuacán-Cuicatlán*
(2013), 336 pp. `[conanp-2013-pm-tehuacan-cuicatlan]`

**Access:** `www.conanp.gob.mx` serves a bot-challenge page on its HTML
homepage, but the PDF is served unchallenged from **both**
`simec.conanp.gob.mx/pdf_libro_pm/123_libro_pm.pdf` and
`www.conanp.gob.mx/que_hacemos/pdf/programas_manejo/tehuacan_2013.pdf`. Same
domain, different path — the third instance of this pattern.

---

## Correction: this reserve has no core or buffer zones

The brief asks whether the right-of-way passes through **core zones, buffer
zone, or outside the property**. That framing does not apply here. The
management programme is explicit (p. 140):

> "En la declaratoria de la Reserva de la Biosfera Tehuacán-Cuicatlán se
> estableció un **polígono general**, es decir, **no se estableció una
> zonificación (zona núcleo y zona de amortiguamiento)**…"

Instead the programme establishes **subzonas** under LGEEPA Arts. 47 BIS,
47 BIS 1 and 48. So the operative question is not core-vs-buffer; it is **which
subzona the alignment crosses, and what that subzona permits.**

## What each subzona permits for infrastructure

| Subzona | Hectares | % of reserve | Infrastructure rule |
|---|---:|---:|---|
| Preservación | 141,781.7 | 29.06% | Maintenance of **existing roads** only. "Abrir senderos, brechas o caminos" **prohibited** |
| Uso Tradicional | 133,739.3 | 27.41% | Infrastructure only **in support of** research, environmental education, low-impact tourism |
| Aprov. Sust. de los Recursos Naturales | 33,046.9 | 6.77% | Same — only **in support of** research/education/tourism |
| Aprov. Sust. de los Ecosistemas | 178,168.9 | 36.51% | Same — only **in support of** research/education/tourism |
| Uso Público | 1,000.6 | 0.21% | Tourism-oriented (4 polygons) |
| **Aprovechamiento Especial** | **239.2** | **0.049%** | **The only subzona permitting general "construcción y mantenimiento de infraestructura"** |
| **Total** | **487,976.5** | | |

### The finding

> **The only subzone in which general infrastructure construction is a listed
> permitted activity covers 239.2 hectares — 0.049% of the reserve — across 14
> polygons that are, without exception, quarries, salt works and the Tehuacán
> landfill.**

Named sites: Canteras San Luis Temalacayuca, San Lorenzo, Nutek, El Riego,
Santa María Coapam, Ignacio Mejilla, Nanahuatipam; Salinas Grandes, Chiquitas,
La Barranca, El Castillo, Desconocidas, Rinconada; relleno sanitario de
Tehuacán. **Not one is a transport corridor.**

For scale: a 216.5 km alignment at a 20 m right-of-way `[ASSUMED width]` covers
~433 ha — **1.8× the entire Aprovechamiento Especial subzone**, and only part of
the alignment lies inside the reserve.

In the other ~99.95% of the reserve, the only infrastructure construction listed
as permitted is that **in support of scientific research, environmental
education or low-impact tourism**. Three of the four large subzones additionally
prohibit "Abrir senderos, brechas o caminos" outright.

## Corroboration of the geotechnical risk, from CONANP

The programme already identifies the existing roads in this corridor —
Cuacnopalan-Oaxaca, federal 125, and **federal 135 Tehuacán-Cuicatlán** — as
generating a "fuerte efecto de borde… ocasionando **inestabilidad de taludes,
erosión, incendios**" (p. 83). It also lists **"la limpia de derecho de vía"**
(right-of-way clearing) as a source of fire pressure (pp. 81, 83).

So the environmental authority already treats linear infrastructure in the
Cañada as a high-pressure driver, and ROW clearing specifically as a hazard.
This independently corroborates risk R-02 (slope stability and scour).

## Consent surface, for R-05

The reserve covers ~10,000 km² and contains **51 municipios, 130 comunidades y
ejidos, 250 localidades**, ~36,000 inhabitants inside and ~600,000 in the zone
of influence (p. 137). Any alignment consent process runs across that surface.

## Caveats — stated because they genuinely cut the other way

1. **The railway predates the reserve.** The line opened in 1892; the reserve
   was declared in 1998. The management programme's own cartography maps
   **"Vía Férrea"** as an existing feature (pp. 2–3). Pre-existing lawful
   federal infrastructure does not have the same standing as new construction,
   and this analysis does not resolve that question.
2. **Rehabilitation may not be "construction."** Every large subzona permits
   *mantenimiento de caminos existentes*. If rehabilitating an existing rail
   right-of-way were characterised as maintenance of existing infrastructure,
   a pathway might exist — but the programme says *caminos* (roads) and lists
   **no rail maintenance activity anywhere**.
3. **No GIS overlay was performed.** The subzone polygon geometry was not
   obtained, so which subzones the alignment actually crosses is **not
   established** — only that the Cañada is the reserve's central geography and
   the alignment runs through it.
4. This is a determination for SEMARNAT and CONANP. It is **not** a desk
   conclusion, and is not presented as one.

## GIS overlay — what actually changed the conclusion

Source: CONANP's own boundary shapefile, `232-ANP_ITRF08_19162026.shp`, from
`sig.conanp.gob.mx/container/descargas/files/shape/`. (The site root returns
503; the `/Shape` path serves.) Script: `analysis/scripts/anp_overlay.py`.
Full output: `working/anp-overlay.txt`.

Two things came out of it.

**1. Independent confirmation that no zona núcleo exists.** CONANP's
zonas-núcleo layer (`ZP_ANPS_22042024.shp`, 253 polygons nationally) contains
**zero polygons for Tehuacán-Cuicatlán**. That corroborates the management
programme's text (p.140) from a completely different source type.

**2. The valley floor is outside the reserve.** Every corridor waypoint tests
outside the ANP polygon. The reserve occupies the slopes on either side of the
Cañada; the floor sits in a gap:

| Waypoint | Distance from reserve edge to the valley-floor station |
|---|---|
| Tehuacán (corridor entry) | **0.6 km** |
| Santa María Tecomavaca | **0.8 – 1.2 km** |
| San Juan Bautista Cuicatlán | 3.3 km |
| Teotitlán del Camino | 4.6 – 6.5 km |
| Nacaltepec, Etla, Oaxaca City | no reserve at these latitudes |

**A straight-line traverse between waypoints reports 32% "inside". That figure
is an artefact and must not be used.** Chords between excluded valley points cut
across the included slopes; a railway following the valley does not.

### What this means, stated plainly

- The alignment may run **substantially, perhaps wholly, outside** the ANP.
- **South of ~17.53°N — roughly Nacaltepec to Oaxaca City — there is no reserve
  at all.**
- But the excluded corridor is **narrow, under 1 km at Tehuacán and
  Tecomavaca**. Cuttings, borrow pits, spoil, structures and any realignment
  could enter reserve land even where the centreline does not.
- The reserve's **zone of influence** is larger than the ANP polygon and may
  still trigger review.

### What would retire it

The **rail centreline** — never obtained; road stations are the proxy
throughout. Then a SEMARNAT determination on whether rehabilitating a
pre-existing federal ROW is *construction* or *maintenance* under LGEEPA, and
the MIA modality that follows.

## Effect on the screen

**The freight revenue verdict is unaffected** — it never depended on this.

What changes is the standing of the environmental constraint. It was presented
as a second, independent basis for the negative. **On this evidence it is not
strong enough to carry that weight.** It is better described as a live but
unresolved risk with thin margin, not a probable foreclosure. The screen has
been amended accordingly.
