inputs = [1, 2, 3, 4]
targets = [12, 14, 16, 18]

b = 0.3
w = 0.1 
epochs = 400
learning_rate = 0.1

def predict(i):
    return w * i + b # 가중치 * 인풋 + 편향

# train networks
for _ in range(epochs):
    pred = [predict(i) for i in inputs]
    # 예측은 모든 인풋데이터에 대해서 체크된다.
    errors = [t - p for t, p in zip(pred, targets)]
    cost = sum(errors) / len(targets) 
    # 오차를 체크한다.
    print("weight : {}, cost : {}, bias : {}".format(w, cost, b))
    
    errors_d = [2 * (p - t) for p, t in zip(pred, targets)]
    weight_d = [e * i for e, i in zip(errors_d, inputs)]
    bias_d = [e * 1 for e in errors_d]
    
    w -= learning_rate * sum(weight_d) / len(weight_d)
    b -= learning_rate * sum(bias_d) / len(bias_d)
    # 오차의 결과를 다시 학습률과 함께 가중치에 적용해준다.
    # 핵심은 모든 루프마다 가중치는 업데이트 된다. 이 학습의 루프를 에폭이라고 한다.
    # 이를 배치 경사하강법이라고 하며, 모든 트레이닝 샘플은 가중치가 업데이트 되기 전에 처리된다.
    
# cost가 0으로 다가가야 한다. 하지만 현재의 모습에서는 점점 cost가 점차 상승한다.
# 이것을 줄이기 위해 우리는 학습률을 사용한다. 학습률을 지정해주면 점점 비용이 줄어드는 것을 볼 수 있다.
# 딥러닝 훈련을 위해서 feed forward, 순전파로 예측을 확인한다.
# 비용함수를 통해서 오차를 확인한다.
# 이를 바탕으로 역전파 back propagation을 통해서 가중치를 수정한다.
# 1번의 사이클이 마치면 ? 순전파 + 오차측정 + 역전파 

# 순전파 : 모든 훈련 데이터에 대한 예측 값을 계산한다.
# 비용함수 : 모든 훈련 데이터에 대한 오차를 기반으로 비용을 계산한다.
# 역전파 : 오차의 델타 값, 가중치의 델타값을 계산하고, 가중치를 업데이트 한다.

# test the network 
test_inputs = [5, 6]
test_targets = [20, 22]
pred = [predict(i) for i in test_inputs]
for i, t, p in zip(test_inputs, test_targets, pred):
    print("input : {}, target : {}, pred : {}".format(i, t, p))

# 비용함수(cost function) : 오차들의 평균을 찾아서 하나의 숫자로 제시해준다.
# 우리의 목표는 이 비용을 0에 가깝게 맞추어 가는 것이다. 이 과정을 비용 최소화 과정이라고 한다.
# c.funciton = (sum(target - pred)) / len(target)
# pred = w * input 우리가 하는 건 가중치의 조정이 전부다.

# 왜 비용함수의 미분 값을 사용해야 하는가?
# 최소값을 찾기 위해서 비용함수의 미분값을 통해서 경사의 음양을 확인한다. 경사가 0에 가까워져야 한다.

## 현재까지 한 것을 배치 경사하강법이라고 한다.



