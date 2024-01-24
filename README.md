# resume_sample
支持单个epoch内可以保存迭代位置  
数据量大时，可以备份/恢复训练

使用方法（详见test.ipynb）：
```python
import torch
from resume_sample import ResumeSample

sampler = ResumeSample(length=len(data), shuffle=True)
# 自定义sampler不支持参数shuffle
data_loader = torch.utils.data.DataLoader(dataset=data, batch_size=batch_size, sampler=sampler)

# 导出迭代数据
data_loader.sampler.state_dict()

# 恢复迭代数据
sampler2 = ResumeSample()
sampler2.load_state_dict(data_loader.sampler.state_dict())
