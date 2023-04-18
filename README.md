# 供应商报名、报价

```mermaid
sequenceDiagram
    participant 供应商
    participant 采购员
    participant 询价信息
    participant 报名
    participant 报价
    participant 报价截止
    participant 开标
    participant 查看报价

    供应商->>询价信息: 收到询价信息
    询价信息-->>供应商: 确认收到

    供应商->>报名: 报名参与或放弃
    报名-->>供应商: 确认报名状态

    Note over 供应商,报价: 根据配置次数规则多次报价

    供应商->>报价: 提交报价
    报价-->>供应商: 确认报价提交

    供应商->>报价截止: 等待报价截止
    报价截止-->>供应商: 报价截止通知

    采购员->>开标: 开标操作
    开标-->>采购员: 开标结果通知

    采购员->>查看报价: 查看报价情况
    查看报价-->>采购员: 报价查看结果
