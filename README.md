
将这段代码粘贴到支持mermaid的Markdown编辑器中，就可以生成一个时序图。如果您想要将这个时序图与您提供的示例代码结合，您可以按照以下方式修改：

```markdown
```mermaid
sequenceDiagram
    participant P as 采购员
    participant PR as 需求池
    participant Q as 询价单
    participant R as 询价单发布
    participant N as 通知供应商
    participant S as 供应商

    P->>PR: 获取需求
    PR-->>P: 返回需求信息

    P->>Q: 发起并提交询价单
    Q-->>P: 确认提交

    P->>R: 发布询价单
    R-->>P: 确认发布

    P->>N: 通知供应商
    N-->>P: 确认通知

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
