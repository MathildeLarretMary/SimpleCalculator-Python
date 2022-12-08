# CHANGELOG

## [Unreleased]

### Added

- run() method to handle the running loop.


### Changed

- methods other than run are marked private
- extracted the loop from __init__
- split responsibilities in small functions
- if invalid output, message does not display ValueError as it would look like an exception
- removed all the nesting (while True + recursion) in the ask_again, now renamed _continue

### Fixed
