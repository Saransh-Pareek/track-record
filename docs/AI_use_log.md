# AI Use Log — Track Record (DATA7901/7902)

Keep this file in the repo under `docs/`. Add a row every time you use an AI tool, and fill in the "What I checked" column honestly. If you can't fill it in, you haven't verified it yet.

## Log

| Date | Task | What the AI did | What I did / checked | Verified? |
|---|---|---|---|---|
| Aug 2026 | Understanding the project | Wrote a plain-English orientation to the project and CETS Modules 1 and 9 | | ☐ |
| Aug 2026 | Literature review | Searched for and summarised ~10 papers on TQIs, deterioration modelling, defect combinations | Chose which papers to cite | ☐ |
| Aug 2026 | Paper explainer | Explained each paper from basics upward | | ☐ |
| Aug 2026 | Dev environment | Generated repo scaffold (folders, venv, requirements, .gitignore, README, setup guide) | Ran it locally | ☐ |
| Aug 2026 | Draft proposal v1–v5 | Drafted and edited text against Lisa's rubric and feedback, and Archie's feedback | Submitted v5 on 29 Aug | ☐ |
| 19 Sep 2026 | Feedback diagnosis | Explained why draft lost marks on C3–C7 using my own sentences | | ☐ |
| 19 Sep 2026 | Full proposal | Researched CQCN figures and QCA budget; read CETS Modules via OCR; drafted all sections; made Figures 1–2 | | ☐ |
| 19 Sep 2026 | Revision | Added stretch goal (Archie), fixed rubric issues, simplified wording; removed AWS cost estimates and claims of existing code | Rewrote sections in my own words: ______ | ☐ |
| 19 Sep 2026 | Reviewer feedback fixes | Applied 10-point reviewer feedback; rebuilt references; made repo scaffold | | ☐ |

## Facts to verify before submitting

Tick each one only after you've opened the source yourself.

| Claim in proposal | Source | Where to look | ☐ |
|---|---|---|---|
| CQCN 2,670 km, >40 mines, 5 export terminals; 208.0 Mt in FY2025 | [1] Aurizon Annual Report 2024–25 | Network segment review | ☐ |
| A$208.6M maintenance (excl. ballast plant depreciation), A$363.2M renewals | [2] QCA MRSB | Sections 1.2 and 1.3 | ☐ |
| Preventive resurfacing planned from ATIS geometry data | [2] | Table 13, Resurfacing row | ☐ |
| Geometry/turnout defects drove speed restrictions on NCL Aldoga–Midgee; ballast renewals planned there | [2] | Blackwater Permanent Way key trends | ☐ |
| "Development of predictive capability" as a mitigation | [2] | Table 8, Rail Maintenance row | ☐ |
| Coal producers vote on MRSB through the RIG | [2] | Table 11 | ☐ |
| TGMS max interval 6 months on mainline | [3] Module 1 | Appendix CETS 1.A, 1.7.5 row | ☐ |
| Priority A = before next train; d1/d7/d14 = 1/7/14 days; m1–m3 months | [3] Module 1 | Table 1.1 | ☐ |
| Workers may raise any priority, or lower d7/d14; d1 cannot be lowered | [4] Module 9 | Section 9.3.4, clauses 3–4 | ☐ |
| Combined defects: strictest response is the minimum, rest is judgement | [3] Module 1 | Section 1.2.9 | ☐ |
| oTCI must not exceed limits | [4] Module 9 | Section 9.2.3, clause 3 | ☐ |
| PCI via ECDF (MMY004/MMY038) vs mean + 3SD against m3 limits incl. gauge (tight) (ATIS) | [4] Module 9 | Section 9.3.4, clause 6 | ☐ |
| Good track can mask poor track | [4] Module 9 | Section 9.3.4, clause 5 | ☐ |
| ATIS: median = limit ÷ 1.25, lower = median × 0.75; MMY038 levels from ECDF | [4] Module 9 | Table 9.12 notes i and ii | ☐ |
| oTCI algorithm to be replaced by ATIS-based index | [4] Module 9 | Note above Table 9.3 | ☐ |
| oTCI was a KPI under UT4 (2016 undertaking) | [5] QCA | Condition-based assessment page | ☐ |
| NCL sections Parana–Rocklands and Kaili–Durroburra are CQCN; NCL carries passenger/Tilt Train | [6] Queensland Rail | Main text | ☐ |
| ml.t3.medium US$0.05/h; ml.m5.xlarge US$0.23/h | [14] AWS SageMaker AI pricing | Pricing examples #8 and #18 | ☐ |
| Paper findings in refs [7]–[13] | Each paper | Abstract + results | ☐ |

**Still open:** is the oTCI still a KPI under UT5? Not confirmed in public sources. Ask ARCS.

**Assumptions, not facts.** These are labelled as assumptions in the text; don't present them as fact:
- the 0.5 m sampling interval
- the ±2% and 10 m tolerances
- the AWS cost estimate (redo it in the AWS Pricing Calculator)

## Can I explain it in my own words?

Archie may ask any of these. Practise answering each one out loud in two or three sentences without notes.

1. What is the oTCI, and why does Aurizon report it to the QCA?
2. What are top, twist, gauge, versine and cant?
3. What does a d1 exceedance mean?
4. How can a section have an acceptable oTCI but still contain an urgent defect?
5. Why do combined defects matter, and what does Module 1 say about them?
6. What's the difference between the ECDF and ATIS ways of computing the oTCI?
7. What is ELT, and why store raw data unchanged?
8. What is a data contract, and what happens when a batch breaks one?
9. How does the synthetic data generator give us "ground truth"?
10. Why does the pipeline matter for the predictive maintenance stretch goal?
11. What did Offenbacher et al. [10] and Scanlan et al. [11] do, and how are we copying their design?
12. How did you use AI on this proposal, and how did you check its output?
