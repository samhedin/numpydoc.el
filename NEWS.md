# numpydoc.el NEWS -- history of user visible changes

## Unreleased

..

## 0.6 (Jan 19, 2022)

### Changes

- Added the ability to include a `Returns` block when a return
  typehint is not present
  ([#11](https://github.com/douglasdavis/numpydoc.el/pull/11)).

## 0.5 (Aug 11, 2021)

### Fixed bugs

- Parsing default arguments containing punctuation Arguments with
  commas surrounded by either quotes (strings), braces (dict or set),
  or parentheses (tuples) were causing bad docstrings. Default
  dictionaries with colons were also causing bad docstrings. (Issue
  raised at
  [#7](https://github.com/douglasdavis/numpydoc.el/issues/7), fixed at
  [#8](https://github.com/douglasdavis/numpydoc.el/pull/8)).

## 0.4 (May 23, 2021)

### Changes

- Renamed `numpydoc-template-desc` to `numpydoc-template-arg-desc`
  Marked the previous custom variable as obsolete. This change makes
  the variable name consistent with the closely related variable
  `numpydoc-template-type-desc`.

## 0.3.0 (May 10, 2021)

### Changes

- Added new `defcustom`: `numpydoc-insert-parameter-types` New
  variable controls whether the type hint is added to each argument in
  the parameters block (default is `t`).

## 0.2.0 (Mar 5, 2021)

### Changes

- Added support for yasnippet If yasnippet is installed we
  `yas-expand-snippet` to on-the-fly add the docstring components in
  buffer.

- Added customization `numpydoc-insertion-style`. Use this single
  customization to direct the insertion style instead of multiple
  boolean customization. Can take on:
  - `'prompt` (prompt in minibuffer)
  - `'yas` (use yasnippet)
  - `nil` (no insertion helper, just use templates)

- Added interactive convenience functions for toggling insertion
  style. `numpydoc-use-yasnippet`, `numpydoc-use-prompt`, and
  `numpydoc-use-templates` are new interactive convenience functions
  to adjust `numpydoc-insertion-style` without having to use
  `eval-expression` and `setq`.

### Removed

- Removed variable `numpydoc-prompt-for-input`. Not needed anymore
  (use `numpydoc-insertion-style`).

- Removed function `numpydoc-toggle-prompt`. Not needed anymore (use
  `numpydoc-use-{yasnippet,prompt,templates}`).

## 0.1.0

Initial release
