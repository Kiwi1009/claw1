---
name: defect-detector
description: 病害检测识别技能，支持从图片中自动检测病害区域，识别病害类型、严重程度，输出检测结果和结构化信息。
---
# 病害检测识别技能
## 核心功能
1. 支持农作物、工业设备、建筑等多场景病害/缺陷检测
2. 自动定位病害区域，返回精确bounding box坐标和分割掩码
3. 识别病害类型，内置支持120+常见病害分类，可自定义扩展
4. 智能评估病害严重程度（轻微/中等/严重/极重）
5. 输出结构化检测结果，自动对接病害知识库获取解决方案
## 依赖安装
```bash
pip install ultralytics>=8.0 opencv-python>=4.8 numpy>=1.24
```
## 使用方式
```python
from scripts.detector import DefectDetector
detector = DefectDetector(model_path="./models/yolov8_disease_v2.pt")
detection_result = detector.detect("./defect_sample.jpg")
```
## 返回格式
```json
{
  "has_defect": true,
  "defect_count": 2,
  "defects": [
    {
      "type": "玉米叶斑病",
      "confidence": 0.96,
      "severity": "中等",
      "bbox": [120, 85, 260, 190],
      "area_ratio": 0.12
    },
    {
      "type": "玉米锈病",
      "confidence": 0.89,
      "severity": "轻微",
      "bbox": [310, 120, 390, 210],
      "area_ratio": 0.05
    }
  ]
}
```
