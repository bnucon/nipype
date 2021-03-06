# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ....testing import assert_equal
from ..preprocess import SegmentCC


def test_SegmentCC_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    copy_inputs=dict(),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_file=dict(argstr='-aseg %s',
    mandatory=True,
    ),
    in_norm=dict(mandatory=True,
    ),
    out_file=dict(argstr='-o %s',
    hash_files=False,
    keep_extension=False,
    name_source=[u'in_file'],
    name_template='%s.auto.mgz',
    ),
    out_rotation=dict(argstr='-lta %s',
    mandatory=True,
    ),
    subject_id=dict(argstr='%s',
    mandatory=True,
    position=-1,
    usedefault=True,
    ),
    subjects_dir=dict(),
    terminal_output=dict(nohash=True,
    ),
    )
    inputs = SegmentCC.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value


def test_SegmentCC_outputs():
    output_map = dict(out_file=dict(),
    out_rotation=dict(),
    )
    outputs = SegmentCC.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value
