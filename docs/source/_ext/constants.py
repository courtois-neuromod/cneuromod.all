_CONTRIB_EMOJI = {
    'audio':             '🔊',
    'bug':               '🐛',
    'code':              '💻',
    'data':              '🔣',
    'design':            '🎨',
    'doc':               '📖',
    'financial':         '💰',
    'fundingFinding':    '🔍',
    'ideas':             '🤔',
    'infra':             '🚇',
    'maintenance':       '🚧',
    'mentoring':         '🧑‍🏫',
    'projectManagement': '📆',
    'question':          '💬',
    'research':          '🔬',
    'review':            '👀',
    'security':          '🛡️',
    'talk':              '📢',
    'test':              '⚠️',
    'tool':              '🔧',
    'translation':       '🌍',
    'tutorial':          '✅',
    'userTesting':       '📓',
    'video':             '📹',
}

_CONTRIB_LABEL = {
    'audio':             'audio',
    'bug':               'bug reports',
    'code':              'code',
    'data':              'data',
    'design':            'design',
    'doc':               'documentation',
    'financial':         'funding',
    'fundingFinding':    'funding finding',
    'ideas':             'ideas',
    'infra':             'infrastructure',
    'maintenance':       'maintenance',
    'mentoring':         'mentoring',
    'projectManagement': 'project management',
    'question':          'questions',
    'research':          'research',
    'review':            'review',
    'security':          'security',
    'talk':              'talks',
    'test':              'tests',
    'tool':              'tools',
    'translation':       'translation',
    'tutorial':          'tutorials',
    'userTesting':       'user testing',
    'video':             'video',
}

_STATUS_ICON = {
    'available':     '✅',
    'pending':       '⬜',
    'not_collected': '❌',
}

# Uppercase .md files at the repo root excluded from auto-discovery entirely
_ROOT_MD_EXCLUDE = {'README.md', 'CLAUDE.md'}
# Uppercase .md files that are symlinked but hardcoded in index.rst (kept out of the placeholder)
_ROOT_MD_MANUAL = {'DOWNLOADING.md'}
