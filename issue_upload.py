# issueクラスをインポート
from pybacklogpy.Issue import Issue


#issueをjson形式で取ってくる
issue_api_2 = Issue()  # Configure クラスを渡さなかった場合は、設定ファイルの情報を読みに行く
response_2 = issue_api_2.get_issue_list()
print(response_2.text)


#csvに記入したファイルを読み取って、json形式にし？upload

#issueの登録


#not項目
#入力:int
#出力:int
#jsonで取得して、最後のproject_id+1する
project_id = 118199

#equal項目
#入力:str
#出力:str
summary = "テストで作成"

#equal項目
#入力:str
#出力:int
#intに変換する
issue_type_id = 547921

#equal項目
#入力:str
#出力:int
#intに変換する
priority_id = 3

#考慮しない
# parent_issue_id = 課題の親課題のID
parent_issue_id = None


#equal項目
#入力:str
#出力:str
description = "pythonからuploadしました"

#equal項目
#入力:(yyyy/MM/dd)
#出力:(yyyy-MM-dd)
start_date = "2020-08-30"

#equal項目
#入力:(yyyy/MM/dd)
#出力:(yyyy-MM-dd)
due_date = "2020-09-01"

#equal項目
#入力:int
#出力:int
estimated_hours = 3

#考慮しない
# actual_hours = 課題の実績時間
actual_hours = None

#equal項目?
#入力:?
#出力:?
category_id = None

#equal項目?
#入力:?
#出力:?
version_id = None

#equal項目?
#入力:?
#出力:?
milestone_id = None

#equal項目
#入力:str
#出力:int
# assignee_id = 課題の担当者のID
assignee_id = 295872

#equal項目
#入力:str
#出力:int
# notified_user_id = 課題の登録の通知を受け取るユーザーのID
notified_user_id = None

#equal項目?
#入力:?
#出力:?
# attachment_id = 添付ファイルの送信APIが返すID
attachment_id = None

#equal項目?
#入力:?
#出力:?
# kwargs = カスタム属性を渡す customField_{id}=[value] または customField_{id}_otherValue=[value] の形式
kwargs = None


# issue_api_2.add_issue(project_id, summary, issue_type_id, priority_id, parent_issue_id, description, start_date, due_date, estimated_hours, actual_hours, category_id, version_id, milestone_id, assignee_id, notified_user_id, attachment_id)
issue_api_2.add_issue(project_id, summary, issue_type_id, priority_id, parent_issue_id)

