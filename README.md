# 采购员操作时序图

```mermaid
sequenceDiagram
    participant 采购员
    participant 需求池(PR)
    participant 询价单
    participant 询价单发布
    participant 通知供应商

    采购员->>需求池(PR): 获取需求
    需求池(PR)-->>采购员: 返回需求信息

    采购员->>询价单: 发起并提交询价单
    询价单-->>采购员: 确认提交

    采购员->>询价单发布: 发布询价单
    询价单发布-->>采购员: 确认发布

    采购员->>通知供应商: 通知供应商
    通知供应商-->>采购员: 确认通知
