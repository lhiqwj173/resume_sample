import random


class ResumeSample():
    """
    支持恢复的采样器
    随机/顺序采样
    """

    def __init__(self, length=0, shuffle=True):
        # 随机产生种子
        self.shuffle = shuffle
        self.step = random.randint(0, 100)
        self.seed = random.randint(0, 100)
        self.size = length
        self.idx = 0
        self.data = []
        self._loop = False

    def state_dict(self):
        return {'step': self.step, 'seed': self.seed, 'shuffle': self.shuffle, 'size': self.size, 'idx': self.idx, 'loop': self._loop}

    def load_state_dict(self, state_dict):
        self.step = state_dict['step']
        self.seed = state_dict['seed']
        self.shuffle = state_dict['shuffle']
        self.size = state_dict['size']
        self.idx = state_dict['idx']
        self._loop = state_dict['loop']

        # 使用原种子
        random.seed(self.seed)
        self._init_data()

        return self

    def _init_data(self):
        if self.shuffle:

            self.data = random.sample(range(self.size), self.size)
        else:
            self.data = list(range(self.size))

    def __iter__(self):
        if not self._loop:
            # 更新种子
            self.seed += self.step

            random.seed(self.seed)
            self._init_data()

            self.idx = 0
            self._loop = True

        return self

    def __next__(self):
        if self.idx >= self.size:
            self._loop = False
            raise StopIteration

        v = self.data[self.idx]
        self.idx += 1
        return v

    def __len__(self):
        return self.size
