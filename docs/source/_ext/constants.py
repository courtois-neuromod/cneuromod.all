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

_STATS_EMOJI = {
    'neuroimaging.fmri':                  '🧠',
    'passive.images':                     '🖼️',
    'passive.video':                      '🎬',
    'passive.resting_state':              '💤',
    'active.controlled':                  '📊',
    'naturalistic_stimuli.images':        '🖼️',
    'naturalistic_stimuli.video':         '🎬',
    'naturalistic_stimuli.resting_state': '💤',
    'responses.controlled_tasks':         '📊',
    'physiology.ecg':                     '📈',
    'physiology.respiration':             '📈',
    'physiology.plethysmograph':          '📈',
    'physiology.eda':                     '📈',
    'physiology.eye_tracking':            '👁️',
}

_STATS_LABEL = {
    'neuroimaging.fmri':                  'Neuroimaging (fMRI)',
    'passive.images':                     'Images',
    'passive.video':                      'Naturalistic video',
    'passive.resting_state':              'Resting state',
    'active.controlled':                  'Behavior (controlled task)',
    'naturalistic_stimuli.images':        'Images',
    'naturalistic_stimuli.video':         'Naturalistic video',
    'naturalistic_stimuli.resting_state': 'Resting state',
    'responses.controlled_tasks':         'Behavior (controlled task)',
    'physiology.ecg':                     'ECG',
    'physiology.respiration':             'Respiration',
    'physiology.plethysmograph':          'Pulse',
    'physiology.eda':                     'Skin conductance (EDA)',
    'physiology.eye_tracking':            'Eye tracking',
}

_STATS_UNIT = {
    'passive.images':                     'unique images/subject',
    'passive.video':                      'h',
    'passive.resting_state':              'h',
    'active.controlled':                  'h',
    'naturalistic_stimuli.images':        'unique images/subject',
    'naturalistic_stimuli.video':         'h',
    'naturalistic_stimuli.resting_state': 'h',
    'responses.controlled_tasks':         'unique conditions / subject',
}

_STATUS_ICON = {
    'available':              '✅',
    'partial':                '🟡',
    'pending':                '⬜',
    'not_collected':          '❌',
    'collected_not_released': '🔒',
}

_COMPONENT_ICON = {
    'bids':        '📁',
    'fmriprep':    '🧠',
    'mriqc':       '📊',
    'smriprep':    '🏗️',
    'physprep':    '📈',
    'freesurfer':  '🗺️',
    'atlases':     '📍',
    'pycortex':    '🖥️',
    'rois':        '🎯',
    'prf':         '👁️',
    'behaviour':   '🎮',
    'glm':         '📉',
    'glmsingle':   '📉',
    'training':    '🕹️',
}

# Uppercase .md files at the repo root excluded from auto-discovery entirely
_ROOT_MD_EXCLUDE = {'README.md', 'CLAUDE.md'}
# Uppercase .md files that are symlinked but hardcoded in index.rst (kept out of the placeholder)
_ROOT_MD_MANUAL = {'DOWNLOADING.md'}
