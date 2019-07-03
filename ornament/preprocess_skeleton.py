from ornament.skeletons import skeletons
import abjad

def preprocess_skeletons(skeletons):
    '''

    '''
    preprocessed_skeletons = []
    for s in skeletons:
        preprocessed_skeleton = abjad.Score()
        for x in range(len(s)):
            preprocessed_skeleton.append(abjad.Staff())
        first_leaf = abjad.inspect(s[0]).leaf(0)
        resolution = first_leaf.written_duration
        for i, staff in enumerate(s):
            for note in staff:
                notes = [abjad.Note(note.written_pitch, resolution / 2),\
                abjad.Note(note.written_pitch, resolution / 2)]
                preprocessed_skeleton[i].extend(notes)
        preprocessed_skeletons.append(preprocessed_skeleton)
    return preprocessed_skeletons

preprocessed_skeletons = preprocess_skeletons(skeletons)
