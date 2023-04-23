```mermaid
sequenceDiagram
    participant P as 采购员
    participant S as 供应商

    P->>P: 开标
    P->>P: 查看报价
    P->>P: 线下商务谈判
    P->>P: 是否需多轮报价?
    alt 选择否
        P->>P: 评标
    else 选择是
        loop 多轮报价
            P->>S: 发起新一轮报价
            S->>S: 报价
            S->>P: 报价截止
            P->>P: 开标
        end
    end
