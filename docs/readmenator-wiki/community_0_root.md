# root

*Community 0 | 1 files | cohesion 1.00*

## Definition

This community groups 1 file(s) rooted at `root` with dominant language py (cohesion 1.00). Central symbols: `add_text_to_image`, `generate_frames`, `main`. Core file: `script_animator.py` (3 symbols).

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `script_animator.py` | py | utility | 3 | no |

## Key Symbols

- `add_text_to_image` (function, `script_animator.py:15`) `def add_text_to_image(draw, text, position, font, color)`
- `generate_frames` (function, `script_animator.py:27`) `def generate_frames(text, bg_image_path, font_path, output_resolution, fps, char`
- `main` (function, `script_animator.py:97`) `def main()`

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 0
- Cross-boundary resolved imports (EXTRACTED): 0

## Connections

- No cross-community bridges recorded. This community is self-contained.

## Risks

- [dataflow UNCHECKED_ALLOC] `script_animator.py:29` `generate_frames` `bg_image`: Result of allocator stored in `bg_image` is never checked against NULL.

## Open Questions

- Why do 1 file(s) lack file-level docs (e.g. `script_animator.py`)? What purpose do they serve?
- What would break if the most connected file in root changed?
- Should root be split, given cohesion 1.00?

## Sources

- `script_animator.py`
