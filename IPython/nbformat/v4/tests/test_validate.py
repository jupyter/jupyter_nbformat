"""Tests for nbformat validation"""

# Copyright (c) IPython Development Team.
# Distributed under the terms of the Modified BSD License.

import io
import os

import nose.tools as nt

from ..validator import isvalid, validate, ValidationError
from ..nbjson import reads
from ..compose import (
    new_code_cell, new_heading_cell, new_markdown_cell, new_notebook,
    new_output, new_raw_cell,
)

def test_valid_code_cell():
    cell = new_code_cell()
    validate(cell, 'code_cell')

def test_invalid_code_cell():
    cell = new_code_cell()

    cell['source'] = 5
    with nt.assert_raises(ValidationError):
        validate(cell, 'code_cell')

    cell = new_code_cell()
    del cell['metadata']

    with nt.assert_raises(ValidationError):
        validate(cell, 'code_cell')

    cell = new_code_cell()
    del cell['source']

    with nt.assert_raises(ValidationError):
        validate(cell, 'code_cell')

    cell = new_code_cell()
    del cell['cell_type']

    with nt.assert_raises(ValidationError):
        validate(cell, 'code_cell')

def test_invalid_markdown_cell():
    cell = new_markdown_cell()

    cell['source'] = 5
    with nt.assert_raises(ValidationError):
        validate(cell, 'markdown_cell')

    cell = new_markdown_cell()
    del cell['metadata']

    with nt.assert_raises(ValidationError):
        validate(cell, 'markdown_cell')

    cell = new_markdown_cell()
    del cell['source']

    with nt.assert_raises(ValidationError):
        validate(cell, 'markdown_cell')

    cell = new_markdown_cell()
    del cell['cell_type']

    with nt.assert_raises(ValidationError):
        validate(cell, 'markdown_cell')

def test_invalid_heading_cell():
    cell = new_heading_cell()

    cell['source'] = 5
    with nt.assert_raises(ValidationError):
        validate(cell, 'heading_cell')

    cell = new_heading_cell()
    del cell['metadata']

    with nt.assert_raises(ValidationError):
        validate(cell, 'heading_cell')

    cell = new_heading_cell()
    del cell['source']

    with nt.assert_raises(ValidationError):
        validate(cell, 'heading_cell')

    cell = new_heading_cell()
    del cell['cell_type']

    with nt.assert_raises(ValidationError):
        validate(cell, 'heading_cell')

def test_invalid_raw_cell():
    cell = new_raw_cell()

    cell['source'] = 5
    with nt.assert_raises(ValidationError):
        validate(cell, 'raw_cell')

    cell = new_raw_cell()
    del cell['metadata']

    with nt.assert_raises(ValidationError):
        validate(cell, 'raw_cell')

    cell = new_raw_cell()
    del cell['source']

    with nt.assert_raises(ValidationError):
        validate(cell, 'raw_cell')

    cell = new_raw_cell()
    del cell['cell_type']

    with nt.assert_raises(ValidationError):
        validate(cell, 'raw_cell')

def test_sample_notebook():
    here = os.path.dirname(__file__)
    with io.open(os.path.join(here, "v4-test.ipynb"), encoding='utf-8') as f:
        nb = reads(f.read())
    validate(nb)
