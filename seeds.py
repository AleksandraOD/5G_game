import numpy as np

puls = np.zeros((17, 17))
puls[2, 4:7] = 1
puls[4:7, 7] = 1

SEED = {"block": np.array(
        [[1, 1],
         [1, 1]]),
    "glider": np.array(
        [[0, 1, 0],
         [0, 0, 1],
         [1, 1, 1]
         ]),
    "blinker": np.array(
        [[0, 1, 0],
         [0, 1, 0],
         [0, 1, 0]
         ]),
    "infinite": np.array(
        [[1, 1, 1, 0, 1],
         [1, 0, 0, 0, 0],
         [0, 0, 0, 1, 1],
         [0, 1, 1, 0, 1],
         [1, 0, 1, 0, 1]
         ]),
    "pulsar": puls,
    "unbounded": np.array(
        [[1, 1, 1, 0, 1],
         [1, 0, 0, 0, 0],
         [0, 0, 0, 1, 1],
         [0, 1, 1, 0, 1],
         [1, 0, 1, 0, 1]
         ]),
    "r_pentomino": np.array(
        [[0, 1, 1],
         [1, 1, 0],
         [0, 1, 0]
         ]),

}
