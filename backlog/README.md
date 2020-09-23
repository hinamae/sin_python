# readme
https://github.com/kitadakyou/PyBacklogPy
https://kitadakyou.github.io/PyBacklogPy/pybacklogpy.html#module-pybacklogpy.Issue
https://developer.nulab.com/ja/docs/backlog/api/2/add-issue/#リクエストパラメーター
https://test1996.backlog.com/find/DAN_T?projectId=118199&statusId=1&statusId=2&statusId=3&sort=UPDATED&order=false&simpleSearch=true&allOver=false&offset=0

## 使用方法
secretsにサイト名とAPIキー(backlogの設定で生成)を記載



## 方針

- project_id(jsonでとってこないとわからない)などは、get_issue_list()かなんかのメソッドでとってくる

- とってきたパラメータをadd_issue()にわたす

## 解決

- 課題
【Python】requestsで取得したAPIからのレスポンスが「<Response [200]>」となる
https://qiita.com/r-wakatsuki/items/dd960ba729ee0c3eb0d3
- 解決
rではなくr.textとする。



### 取ってきた課題一個分のjson形式データ

```json

[
    {
        "id": 7204956,
        "projectId": 118199,
        "issueKey": "DAN_T-1",
        "keyId": 1,
        "issueType": {
            "id": 547921,
            "projectId": 118199,
            "name": "タスク",
            "color": "#7ea800",
            "displayOrder": 0
        },
        "summary": "課題",
        "description": "課題の作り方を学ぶ",
        "resolution": null,
        "priority": {
            "id": 3,
            "name": "中"
        },
        "status": {
            "id": 1,
            "projectId": 118199,
            "name": "未対応",
            "color": "#ed8077",
            "displayOrder": 1000
        },
        "assignee": {
            "id": 295872,
            "userId": "KhrT2Cuipo",
            "name": "前山陽南",
            "roleType": 1,
            "lang": "ja",
            "mailAddress": "hinahina117mae@gmail.com",
            "nulabAccount": {
                "nulabId": "7WL9jNVVBhoRwTJMNb40jHZS51T1D8IOzoMMQU3ftjWZJ98Itz",
                "name": "前山陽南",
                "uniqueId": "hinahina117mae"
            },
            "keyword": "前山陽南 MAEYAMAYOUNAN"
        },
        "category": [],
        "versions": [],
        "milestone": [],
        "startDate": "2020-09-07T00:00:00Z",
        "dueDate": "2020-09-10T00:00:00Z",
        "estimatedHours": 3,
        "actualHours": 3,
        "parentIssueId": null,
        "createdUser": {
            "id": 295872,
            "userId": "KhrT2Cuipo",
            "name": "前山陽南",
            "roleType": 1,
            "lang": "ja",
            "mailAddress": "hinahina117mae@gmail.com",
            "nulabAccount": {
                "nulabId": "7WL9jNVVBhoRwTJMNb40jHZS51T1D8IOzoMMQU3ftjWZJ98Itz",
                "name": "前山陽南",
                "uniqueId": "hinahina117mae"
            },
            "keyword": "前山陽南 MAEYAMAYOUNAN"
        },
        "created": "2020-09-07T05:26:08Z",
        "updatedUser": {
            "id": 295872,
            "userId": "KhrT2Cuipo",
            "name": "前山陽南",
            "roleType": 1,
            "lang": "ja",
            "mailAddress": "hinahina117mae@gmail.com",
            "nulabAccount": {
                "nulabId": "7WL9jNVVBhoRwTJMNb40jHZS51T1D8IOzoMMQU3ftjWZJ98Itz",
                "name": "前山陽南",
                "uniqueId": "hinahina117mae"
            },
            "keyword": "前山陽南 MAEYAMAYOUNAN"
        },
        "updated": "2020-09-07T05:26:08Z",
        "customFields": [],
        "attachments": [],
        "sharedFiles": [],
        "stars": []
    }
]

```