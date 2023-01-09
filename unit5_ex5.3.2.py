# exercise 5.3.2 from unit 5
'''
Here is the frequency table for each note, in each octave:

La 55 110 220 440 880
Si 61.74 123.48 246.96 493.92 987.84
Do 65.41 130.82 261.64 523.28 1046.56
Re 73.42 146.84 293.68 587.36 1174.72
Mi 82.41 164.82 329.64 659.28 1318.56
Fa 87.31 174.62 349.24 698.48 1396.96
Sol 98 196 392 784 1568
Write a new MusicNotes class that will implement the iterator protocol, and in each call to next will return the frequency of the next note in the note scale.
Note that in each octave (column), the frequency is multiplied by 2 from the previous column.
Think about the stopping condition of the iterator you are building.

'''

freqs = [
    ['La', 55],
    ['Si', 61.74],
    ['Do', 65.41],
    ['Re', 73.42],
    ['Mi', 82.41],
    ['Fa', 87.31],
    ['Sol', 98],
]

OCT_NUM = 5


class MusicNotes:
    def __init__(self):
        self._freqs = freqs

    def __iter__(self):
        self._index_octabs = 1
        self._index_freq = -1
        return self
      
    def __next__(self):
        if self._index_octabs == OCT_NUM and self._index_freq >= len(self._freqs) - 1:
            raise StopIteration
        elif self._index_freq >= len(self._freqs) - 1:
            self._index_freq = -1
            self._index_octabs += 1
        self._index_freq += 1
        return self._freqs[self._index_freq][1] * (2 ** (self._index_octabs - 1))


def main():
    notes_iter = iter(MusicNotes())
    for freq in notes_iter:
        print(freq)


if __name__ == "__main__":
    main()


