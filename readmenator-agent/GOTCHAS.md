# Gotchas

## God Nodes (high connectivity)

These files have the most connections. Changes here have high blast radius.

- `script_animator.py` (score: 0.30)

## Hotspots (complexity + centrality)

- `script_animator.py` -- complexity: 1.0, centrality: 1.0, combined: 1.0

## Dataflow Issues (INFERRED, review each lead)

- `script_animator.py:29` `generate_frames` [UNCHECKED_ALLOC] `bg_image`: Result of allocator stored in `bg_image` is never checked against NULL.
