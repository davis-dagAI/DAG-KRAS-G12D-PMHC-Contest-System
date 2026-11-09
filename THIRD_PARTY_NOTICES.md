# Third-party materials and attribution

The MIT license covers our original repository code and documentation. We also permit reuse of our campaign-generated data under that permission to the extent of our rights. It does not relicense upstream software, model weights, reference databases, competition-platform material or rights held by others. No upstream engine or model weights are distributed in this repository.

The campaign used the following scientific tools. Consult each upstream project for its software, checkpoint-specific terms and preferred citations:

- [RFD4-Proteina](https://github.com/RosettaCommons/RFD4-Proteina/tree/68058693cb88762a8aaf806571e13b291ce6318a), pinned source revision recorded in METHODS.md.
- [Odin-Multi](https://github.com/DigBioLab/odin_multi/tree/e4567e487d43a4de36524f491e51ad1ea9730d1e) and its ColabDesign dependency, used through the described adaptation.
- [ProteinMPNN](https://github.com/dauparas/ProteinMPNN), including the specified original and soluble checkpoints.
- [Boltz](https://github.com/jwohlwend/boltz), Boltz2 complex prediction.
- [FreeSASA](https://github.com/mittinatten/freesasa), solvent-accessible surface area.
- [SaProt](https://github.com/westlake-repl/SaProt), with the stability-head configuration described in the supplement.
- [OpenMM](https://github.com/openmm/openmm), local minimization with the stated force-field files.

Target coordinates derive from the published [PDB 7OW6](https://www.rcsb.org/structure/7OW6) structural context, with the receptor removed for design, and the target constructs specified by the organizers. Reference coordinates and their modifications must be distinguished from predicted candidate complexes. See [RCSB PDB usage and citation policies](https://www.rcsb.org/pages/policies) and the structure's primary publication. Model-generated structures in this archive are labeled as predictions or preparation/minimization derivatives.

The official [competition page](https://proteinbase.com/competitions/anthropic-adaptyv-2026/challenges/pmhc) and organizer-hosted measurements retain their own publication terms. This repository is a participant's archive, not an organizer endorsement. It contains no copy of a third-party article, model checkpoint or private service implementation.
