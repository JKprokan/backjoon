n = int(input())
for _ in range(n):
    cnt = 0
    N , M = map(int,input().split())
    pr = list(map(int,input().split()))
    m_pr = [0 for i in range(N)]
    m_pr[M] = 1
    while True:
        if pr[0] == max(pr):
            cnt += 1
            if m_pr[0] != 1:
                del pr[0]
                del m_pr[0]
            else:
                print(cnt)
                break
        else:
            pr.append(pr.pop(0))
            m_pr.append(m_pr.pop(0))