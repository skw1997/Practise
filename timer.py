import json
import math
from datetime import datetime

import requests
from kubernetes import client, config

class Timer:
    def view_folder_storage_info(self):
        # time1 = datetime(2022,2,21,6,53,35,762789)
        # time2 = datetime(2022, 2, 21, 6, 53, 36, 762789)
        # print(time1.date())
        # print(time1.minute)
        # url = 'https://192.168.100.202:6443'
        config_file = "C:/Users/Administrator/Desktop/kubeconfig.yaml"
        config.kube_config.load_kube_config(config_file=config_file)
        api = client.CustomObjectsApi()
        k8s_nodes = api.list_cluster_custom_object("metrics.k8s.io", "v1beta1", "nodes")
        print(k8s_nodes)
        # v1 = client.CoreV1Api()
        # for ns in v1.list_node().items:
        #     print(ns)
        # node = "amax"
        # url = 'https://192.168.100.103:43373/api/v1/node/k8s-master?filterBy=&itemsPerPage=10&name={}&namespace=&page=1&sortBy=d,creationTimestamp'.format(node)
        # headers = {"Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IiJ9.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJrdWJlLXN5c3RlbSIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VjcmV0Lm5hbWUiOiJhZG1pbi11c2VyLXRva2VuLXdudm5tIiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZXJ2aWNlLWFjY291bnQubmFtZSI6ImFkbWluLXVzZXIiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC51aWQiOiI3YWUyMTUzMi00NjcwLTRhNGUtYWE4ZS1mYjNlNmVjMmM0YzEiLCJzdWIiOiJzeXN0ZW06c2VydmljZWFjY291bnQ6a3ViZS1zeXN0ZW06YWRtaW4tdXNlciJ9.Zy2XYAeyhovGDix2Htw7vUwQdLUlOFBIDE08q5bxmGZGBi5QWxj6QUNiSTquS7c-pPlY7T4kqN0COwPOChay0Kk27PTUZDW11KN4dSColmb3XbGMjrtEl_H2Fjhznrp1evRWR-4wmC_sT-_5EVk4iFfUOjvkVYCKo5XUJC87Oahl8-L-z-0-JJFUudxl0QoXnigHTFXCL1F175Mccx2jibIgpxHuq8aAS-m6ZZyjCBUzuUnmxWHOnGhNRvO5NB-3pr5uHRR6v1Dq_2I3_Yneutep5BLb3b9SsROhLJDlkf8lTHIN-aNKuBKzyNJH4PVo6L6zvBXxcf9kbQAQL1pkDg"}
        # # headers = {'Content-Type':'application/json;charset=UTF-8',"Authorization":"bearer a809655f-e4bf-41b8-9088-85a1d3780d6d"}
        # res = requests.get(url=url, headers=headers, verify=False)
        # ans = json.loads(res.content.decode("utf-8")).get("allocatedResources")
        # url = 'https://192.168.100.103:43373/api/v1/node?filterBy=&itemsPerPage=10&name=&namespace=&page=1&sortBy=d,creationTimestamp'
        # headers = {"Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IiJ9.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJrdWJlLXN5c3RlbSIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VjcmV0Lm5hbWUiOiJhZG1pbi11c2VyLXRva2VuLWd4N2ZuIiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZXJ2aWNlLWFjY291bnQubmFtZSI6ImFkbWluLXVzZXIiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC51aWQiOiI1NWFkOTljNi03NzIzLTRiNDYtYmZlZS01NDY0NTc5NjY1ZWYiLCJzdWIiOiJzeXN0ZW06c2VydmljZWFjY291bnQ6a3ViZS1zeXN0ZW06YWRtaW4tdXNlciJ9.JlQwgIDi7DmLt1SCKB-pEyogQX_91TgXdKAewenJgsPYwMzlMFL_pG-K3vM2E4VB6g4QSbhf5r5SiMuzDu-PMEtcM_KFYYfEtWUN1fQyBhqPH4hRodRyCWmX1TADNi3ToeHTPgItg73o2fWOHUzN1XlV_6Zc5lvuWASatFLvewJAXo_OBLlcayw-LNwfE3U0wAXBb5a0g027l3GsC0MzNaIKvqrmBX41iyJUJ55Ugo03Ibbw5tPa63hWKagXtgh1yErBmDFkdEM56gpq_oV_1c1-nfejjrFg_GU1rwkSzffpJdobN_WH6huQ38zHAxKAvOcLyx0QFRtO9oIeU_Ci6Q"}
        # res = requests.get(url=url, headers=headers, verify=False)
        # ans = json.loads(res.content.decode("utf-8")).get("nodes")
        # for nodes in ans:
        #     node = nodes.get("objectMeta").get("name")
        #     stat = nodes.get("ready")
        #     url = 'https://192.168.100.103:43373/api/v1/node/{}?filterBy=&itemsPerPage=10&name={}&namespace=&page=1&sortBy=d,creationTimestamp'.format(node, node)
        #     headers = {"Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IiJ9.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJrdWJlLXN5c3RlbSIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VjcmV0Lm5hbWUiOiJhZG1pbi11c2VyLXRva2VuLWd4N2ZuIiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZXJ2aWNlLWFjY291bnQubmFtZSI6ImFkbWluLXVzZXIiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC51aWQiOiI1NWFkOTljNi03NzIzLTRiNDYtYmZlZS01NDY0NTc5NjY1ZWYiLCJzdWIiOiJzeXN0ZW06c2VydmljZWFjY291bnQ6a3ViZS1zeXN0ZW06YWRtaW4tdXNlciJ9.JlQwgIDi7DmLt1SCKB-pEyogQX_91TgXdKAewenJgsPYwMzlMFL_pG-K3vM2E4VB6g4QSbhf5r5SiMuzDu-PMEtcM_KFYYfEtWUN1fQyBhqPH4hRodRyCWmX1TADNi3ToeHTPgItg73o2fWOHUzN1XlV_6Zc5lvuWASatFLvewJAXo_OBLlcayw-LNwfE3U0wAXBb5a0g027l3GsC0MzNaIKvqrmBX41iyJUJ55Ugo03Ibbw5tPa63hWKagXtgh1yErBmDFkdEM56gpq_oV_1c1-nfejjrFg_GU1rwkSzffpJdobN_WH6huQ38zHAxKAvOcLyx0QFRtO9oIeU_Ci6Q"}
        #     res = requests.get(url=url, headers=headers, verify=False)
        #     ans = json.loads(res.content.decode("utf-8")).get("allocatedResources")
        #     data = {'name': node,
        #             'ready': stat,
        #             'data': ans}
        #     print(data)
        # print("wjj" + ':' + "9889")
if __name__ == '__main__':
   time = Timer()
   time.view_folder_storage_info()