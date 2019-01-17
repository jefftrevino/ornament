from ornament.skeletons import skeleton
import abjad

def preprocess_skeleton(skeleton):
    preprocessed_skeleton = abjad.Score()
    for x in range(len(skeleton)):
        preprocessed_skeleton.append(abjad.Staff())
    first_leaf = abjad.inspect(skeleton[0]).leaf(0)
    resolution = first_leaf.written_duration
    for i, staff in enumerate(skeleton):
        for note in staff:
            notes = [abjad.Note(note.written_pitch, resolution / 2),\
            abjad.Note(note.written_pitch, resolution / 2)]
            preprocessed_skeleton[i].extend(notes)
    return preprocessed_skeleton

preprocessed_skeleton = preprocess_skeleton(skeleton)
