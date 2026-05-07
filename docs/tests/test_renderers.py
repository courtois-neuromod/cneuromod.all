import sys
from pathlib import Path

# Allow importing _ext without a Sphinx build
sys.path.insert(0, str(Path(__file__).parent.parent / 'source'))

from _ext.renderers import (
    _extract_component_title,
    _render_citation,
    _render_contributors,
    _render_key_facts,
    _shift_headings,
)


class TestRenderCitation:
    def test_few_authors(self, citation_cff):
        result = _render_citation(citation_cff)
        assert 'Smith, Alice' in result
        assert 'Jones, Bob' in result
        assert 'A great paper' in result
        assert '**NeuroImage**' in result
        assert '10.1234/test' in result
        assert ':::{tip}' in result

    def test_many_authors_et_al(self, citation_cff_many_authors):
        result = _render_citation(citation_cff_many_authors)
        assert 'et al.' in result
        assert 'Author0' in result
        assert 'Author5' not in result  # beyond the 5-author cutoff

    def test_no_preferred_citation(self, citation_cff_no_preferred):
        assert _render_citation(citation_cff_no_preferred) == ''


class TestRenderContributors:
    def test_entries_and_legend(self, contributorsrc):
        result = _render_contributors(contributorsrc)
        assert 'Alice Smith' in result
        assert 'Bob Jones' in result
        assert '## Contributors' in result
        # emojis for data, code, doc should appear
        assert '🔣' in result  # data
        assert '💻' in result  # code
        assert '📖' in result  # doc

    def test_profile_link(self, contributorsrc):
        result = _render_contributors(contributorsrc)
        assert '[Alice Smith](https://github.com/asmith)' in result

    def test_no_profile_plain_name(self, contributorsrc):
        result = _render_contributors(contributorsrc)
        assert 'Bob Jones' in result
        assert '[Bob Jones]' not in result

    def test_empty_contributors(self, contributorsrc_empty):
        assert _render_contributors(contributorsrc_empty) == ''


class TestRenderKeyFacts:
    def test_subjects(self, dataset_info_yaml):
        result = _render_key_facts(dataset_info_yaml)
        assert '`sub-01`' in result
        assert '✅' in result  # available
        assert '⬜' in result  # pending

    def test_tasks(self, dataset_info_yaml):
        result = _render_key_facts(dataset_info_yaml)
        assert 'Movie watching' in result
        assert 'natural stimuli' in result

    def test_modalities_with_components(self, dataset_info_yaml):
        result = _render_key_facts(dataset_info_yaml)
        assert 'fMRI' in result
        assert 'BOLD' in result

    def test_empty_yaml(self, dataset_info_yaml_empty):
        assert _render_key_facts(dataset_info_yaml_empty) == ''

    def test_key_facts_heading(self, dataset_info_yaml):
        result = _render_key_facts(dataset_info_yaml)
        assert '## Key facts' in result

    def test_stats_subjects_count(self, dataset_info_yaml_with_stats):
        result = _render_key_facts(dataset_info_yaml_with_stats)
        assert '6 —' in result
        assert '`sub-01`' in result

    def test_stats_fmri_hours(self, dataset_info_yaml_with_stats):
        result = _render_key_facts(dataset_info_yaml_with_stats)
        assert '8 h/subject' in result
        assert '48 h total' not in result  # totals are dropped; per-subject only

    def test_stats_fmri_no_status_icon(self, dataset_info_yaml_with_stats):
        result = _render_key_facts(dataset_info_yaml_with_stats)
        lines = [l for l in result.splitlines() if 'fMRI' in l]
        assert lines, "No fMRI row found"
        assert '✅' not in lines[0]

    def test_stats_controlled_hours(self, dataset_info_yaml_with_stats):
        result = _render_key_facts(dataset_info_yaml_with_stats)
        lines = [l for l in result.splitlines() if 'Behavior' in l]
        assert lines, "No Behavior row found"
        assert '7.85 h/subject' in lines[0]

    def test_stats_contrasts_count(self, dataset_info_yaml_with_stats):
        result = _render_key_facts(dataset_info_yaml_with_stats)
        lines = [l for l in result.splitlines() if 'Contrasts' in l]
        assert lines, "No Contrasts row found"
        assert '23 contrasts' in lines[0]

    def test_stats_resting_state_unit_h(self, dataset_info_yaml_with_stats):
        result = _render_key_facts(dataset_info_yaml_with_stats)
        lines = [l for l in result.splitlines() if 'Resting state' in l]
        assert lines, "No Resting state row found"
        assert 'h/subject' in lines[0]
        assert 'unique/subject' not in lines[0]


class TestExtractComponentTitle:
    def test_basic_heading(self):
        content = '# My Title\n\nSome content.'
        level, title, rest = _extract_component_title(content)
        assert level == 1
        assert title == 'My Title'
        assert 'Some content.' in rest

    def test_h2_heading(self):
        content = '## Section\n\nBody.'
        level, title, _ = _extract_component_title(content)
        assert level == 2
        assert title == 'Section'

    def test_link_stripped_from_title(self):
        content = '# [My Link Title](http://example.com)\n\nBody.'
        _, title, _ = _extract_component_title(content)
        assert title == 'My Link Title'
        assert 'http' not in title

    def test_no_heading_returns_none(self):
        content = 'Just plain text\nno headings here.'
        level, title, rest = _extract_component_title(content)
        assert level is None
        assert title is None


class TestShiftHeadings:
    def test_shift_by_one(self):
        text = '# Title\n## Sub\n### Deep'
        result = _shift_headings(text, 1)
        assert result == '## Title\n### Sub\n#### Deep'

    def test_shift_by_two(self):
        text = '# H1'
        result = _shift_headings(text, 2)
        assert result.startswith('### ')

    def test_zero_shift_is_noop(self):
        text = '# Title'
        assert _shift_headings(text, 0) == text

    def test_negative_shift_is_noop(self):
        text = '# Title'
        assert _shift_headings(text, -1) == text
