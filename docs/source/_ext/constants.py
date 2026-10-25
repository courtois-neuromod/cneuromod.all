# The 14 CRediT (Contributor Roles Taxonomy) roles, in canonical display order.
_CREDIT_ROLES = [
    'Conceptualization',
    'Data curation',
    'Formal analysis',
    'Funding acquisition',
    'Investigation',
    'Methodology',
    'Project administration',
    'Resources',
    'Software',
    'Supervision',
    'Validation',
    'Visualization',
    'Writing – original draft',
    'Writing – review & editing',
]

# Public alias for code outside the Sphinx extension (e.g. the paper build).
CREDIT_ROLES = _CREDIT_ROLES

_STATS_EMOJI = {
    'neuroimaging.fmri':      '🧠',
    'tasks.images':           '🖼️',
    'tasks.video':            '🎬',
    'tasks.audio':            '🔊',
    'tasks.speech_listening': '🗣️',
    'tasks.text_reading':     '📖',
    'tasks.resting_state':    '💤',
    'tasks.game':             '🎮',
    'tasks.controlled':       '📊',
    'tasks.contrasts':        '📐',
    'physiology.ecg':         '🫀',
    'physiology.respiration': '🫁',
    'physiology.plethysmograph': '🫀',
    'physiology.eda':         '😓',
    'physiology.eye_tracking': '👁️',
}

_STATS_LABEL = {
    'neuroimaging.fmri':      'fMRI',
    'tasks.images':           'Images',
    'tasks.video':            'Naturalistic video',
    'tasks.audio':            'Audio',
    'tasks.speech_listening': 'Speech listening',
    'tasks.text_reading':     'Text reading',
    'tasks.resting_state':    'Resting state',
    'tasks.game':             'Gameplay',
    'tasks.controlled':       'Controlled',
    'tasks.contrasts':        'Contrasts',
    'physiology.ecg':         'ECG',
    'physiology.respiration': 'Respiration',
    'physiology.plethysmograph': 'Pulse',
    'physiology.eda':         'Skin conductance (EDA)',
    'physiology.eye_tracking': 'Eye tracking',
}

_STATS_UNIT = {
    'tasks.images':           'unique images/subject',
    'tasks.video':            'h',
    'tasks.audio':            'h',
    'tasks.speech_listening': 'h',
    'tasks.text_reading':     'h',
    'tasks.resting_state':    'h',
    'tasks.game':             'h',
    'tasks.controlled':       'h',
    'tasks.contrasts':        'contrasts',
}

_STATUS_ICON = {
    'available':              '✅',
    'partial':                '🟡',
    'pending':                '⬜',
    'not_collected':          '❌',
    'collected_not_released': '🔒',
}

# Dataset maturity ladder (`maturity.level` in dataset_info.yaml), most to least mature.
# reference: validation paper and substantial reuse; stable: validation paper or substantial
# reuse; beta: complete (all planned participants released, fMRIPrep, README) but neither;
# alpha: anything short of beta.
_MATURITY = {
    'reference': {
        'emoji': '🏆', 'label': 'Reference',
        'description': 'Formal validation paper and substantial reuse.',
    },
    'stable': {
        'emoji': '🟢', 'label': 'Stable',
        'description': 'Formal validation paper or substantial reuse.',
    },
    'beta': {
        'emoji': '🟡', 'label': 'Beta',
        'description': 'Complete (all planned participants released, fMRIPrep derivatives, README) '
                       'but neither validated nor substantially reused yet.',
    },
    'alpha': {
        'emoji': '🟠', 'label': 'Alpha',
        'description': 'Not fully acquired or released, or missing a README.',
    },
}

_COMPONENT_ICON = {
    'bids':        '📁',
    'fmriprep':    '🧠',
    'mriqc':       '📊',
    'smriprep':    '🏗️',
    'physprep':    '🫀',
    'freesurfer':  '🗺️',
    'atlases':     '📍🗺️',
    'pycortex':    '🖥️',
    'rois':        '📍',
    'prf':         '👁️',
    'behaviour':   '🎮',
    'glm':         '📉',
    'glmsingle':   '📉',
    'training':    '🕹️',
    'scenes':      '🗺️',
}

_DATASET_EMOJI = {
    'anat':           '💀',
    'emotion-videos': '😮',
    'floc':           '🎯',
    'friends':        '📺',
    'gamepad':        '🎮',
    'harrypotter':    '📚',
    'hcptrt':         '🎭',
    'hearing':        '👂',
    'langlocalizer':  '🗣️',
    'mario':          '🕹️',
    'mario3':         '🍄',
    'mario_eeg':      '🧠',
    'mariostars':     '⭐',
    'movie10':        '🎬',
    'multfs':         '🧩',
    'mutemusic':      '🎶',
    'narratives':     '📖',
    'ood':            '🔍',
    'petit-prince':   '👑',
    'retinotopy':     '👁️',
    'shinobi':        '🥷',
    'things':         '🖼️',
    'triplets':       '🔺',
}

# Uppercase .md files at the repo root excluded from auto-discovery entirely
_ROOT_MD_EXCLUDE = {'README.md', 'CLAUDE.md'}
# Uppercase .md files that are symlinked but hardcoded in index.rst (kept out of the placeholder)
_ROOT_MD_MANUAL = {'DOWNLOADING.md'}
