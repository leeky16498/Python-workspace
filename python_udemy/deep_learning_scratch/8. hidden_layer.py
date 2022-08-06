import math

inputs = [(0.0000, 0.3929), (0.5484, 0.7500), (0.0645, 0.5714), (0.5806, 0.5714),
    (0.2258, 0.8929), (0.4839, 0.2500), (0.3226, 0.2143), (0.7742, 0.8214),
    (0.4516, 0.5000), (0.4194, 0.0357), (0.4839, 0.2500), (0.3226, 0.7143),
    (0.5806, 0.5000), (0.5484, 0.1071), (0.6129, 0.6429), (0.6774, 0.1786),
    (0.2258, 0.8214), (0.7419, 0.1429), (0.6452, 1.0000), (0.8387, 0.2500),
    (0.9677, 0.3214), (0.3226, 0.4643), (0.3871, 0.5357), (0.3548, 0.1429),
    (0.3548, 0.6429), (0.1935, 0.4643), (0.4516, 0.3929), (0.4839, 0.6071),
    (0.6129, 0.6786), (0.2258, 0.6071), (0.5161, 0.3214), (0.5484, 0.6786),
    (0.3871, 0.8571), (0.6452, 0.6071), (0.1935, 0.3929), (0.6452, 0.3929),
    (0.6774, 0.4643), (0.3226, 0.2857), (0.7419, 0.7143), (0.7419, 0.3214),
    (1.0000, 0.3929), (0.8065, 0.3929), (0.1935, 0.5000), (0.1613, 0.8214),
    (0.2903, 0.9286), (0.3548, 0.0000), (0.2903, 0.6786), (0.5484, 0.9643),
    (0.4194, 0.1786), (0.2581, 0.2500), (0.3226, 0.7143), (0.5161, 0.3929),
    (0.2903, 0.6429), (0.5484, 0.9286), (0.2581, 0.3214), (0.0968, 0.5000),
    (0.6129, 0.7857), (0.0968, 0.3214), (0.6452, 0.9286), (0.8065, 0.7500)]

purple = (1, 0, 0)
orange = (0, 1, 0)
green = (0, 0, 1)

targets = [purple, orange, purple, orange, green, purple, purple, green, orange,
    purple, purple, green, orange, purple, orange, purple, green, purple, green,
    purple, purple, orange, orange, purple, orange, purple, orange, orange, orange,
    green, orange, orange, green, orange, purple, orange, orange, purple, orange,
    orange, purple, orange, green, green, green, purple, green, green, purple, purple,
    green, orange, green, green, purple, purple, green, purple, green, green]

def softmax(predictions):
    m = max(predictions)
    temp = [math.exp(p-m) for p in predictions]
    total = sum(temp)
    return [t / total for t in temp]

def log_loss(activations, targets):
    losses = [-t * math.log(a) - (1 - t) * math.log(1 - a) for a, t in zip(activations, targets)]
    return sum(losses)

epochs = 3000
learning_rate = .05

# weight matrices

w_i_h = [[0.1, -0.2], [-0.3, 0.25], [0.12, 0.23], [-0.11, -0.22]] # 4 hidden layers
w_h_o = [[0.2, 0.17, 0.3, -0.11], [0.3, -0.4, 0.5, -0.22], [0.12, 0.23, 0.15, 0.33]] # 3 output layers
b_i_h = [-0.02, 0.34, 0.21, 0.44] # 4 hidden layers
b_h_o = [0.3, 0.29, 0.37] # output layers

for epoch in range(epochs):
    pred_h = [[sum([w * a for w, a, in zip(weights, inp)]) + bias for weights, bias in zip(w_i_h, b_i_h)] for inp in  inputs]
    print(len(pred_h)) # 총 60개의 sample을 얻게 된다.
    print(len(pred_h[0])) # hidden layer에 대해 4개의 히든레이어를 볼 수 있다.
    
    act_h = [[max(0, p) for p in pred] for pred in pred_h] # ReLU 함수를 적용해서 활성화해준다.
    pred_o = [[sum([w * a for w, a, in zip(weights, inp)]) + bias for weights, bias in zip(w_h_o, b_h_o)] for inp in act_h]
    act_o = [softmax(predictions) for predictions in pred_o]# 아웃풋 레이어의 활성화 함수 : 소프트맥스
    print(act_o)
    
    cost = sum([log_loss(a, t) for a, t in zip(act_o, targets)]) / len(act_o)
    print("epoch : {}, cost : {}\n".format(epoch, cost))
    
    # error derivatives
    errors_d_o = [[a - t for a, t in zip(ac, ta)] for ac, ta in zip(act_o, targets)]
    w_h_o_T = list(zip(*w_h_o))
    errors_d_h = [[sum([d * w for d, w in zip(deltas, weights)]) * (0 if p <= 0 else 1)
                   for weights, p in zip(w_h_o_T, pred)] for deltas, pred in zip(errors_d_o, pred_h)]
    
    # gradient hidden -> output
    act_h_T = list(zip(*act_h))
    errors_d_o_T = list(zip(*errors_d_o))
    w_h_o_d = [[sum([d * a for d, a in zip(deltas, act)]) for deltas in errors_d_o_T] for act in act_h_T]
    b_h_o_d = [sum([d for d in deltas]) for deltas in errors_d_o_T]
    
    # gradient input ->  hidden
    inputs_T = list(zip(*inputs))
    errors_d_h_T = list(zip(*errors_d_h))
    w_i_h_d = [[sum([d * a for d, a, in zip(deltas, act)]) for deltas in errors_d_h_T] for act in inputs_T]
    b_i_h_d = [sum([d for d in deltas]) for deltas in errors_d_h_T]
    
    # update weights and biases for all layers
    w_h_o_d_T = list(zip(*w_h_o_d))
    
    for y in range(len(w_h_o_d_T)):
        for x in range(len(w_h_o_d_T[0])):
            w_h_o[y][x] -= learning_rate * w_h_o_d_T[y][x] / len(inputs)
        b_h_o[y] -= learning_rate * b_h_o_d[y] / len(inputs)
        
    w_i_h_d_T = list(zip(*w_i_h_d))
    
    for y in range(len(w_i_h_d_T)):
        for x in range(len(w_i_h_d_T[0])):
            w_i_h[y][x] -= learning_rate * w_i_h_d_T[y][x] / len(inputs)
        
        b_i_h[y] -= learning_rate * b_i_h_d[y] / len(inputs)
        
# test network

pred_h = [[sum([w * a for w, a, in zip(weights, inp)]) + bias for weights, bias in zip(w_i_h, b_i_h)]
          for inp in pred_h]

act_h = [[max(0, p) for p in pre] for pre in pred_h]
pred_o = [[sum([w * a for w, a, in zip(weights, inp)]) + bias for weights, bias in zip(w_h_o, b_h_o)] for inp in act_h]
act_o = [softmax(predictions) for predictions in pred_o]    
    
test_inputs = [(0.0000, 0.3929), (0.0645, 0.5714), (0.0968, 0.3214),
    (0.0968, 0.5000), (0.2581, 0.3214), (0.1935, 0.4643), (0.2581, 0.2500),
    (0.1935, 0.3929), (0.3226, 0.2143), (0.4839, 0.2500), (0.3226, 0.4643),
    (0.3871, 0.5357), (0.3548, 0.6429), (0.4516, 0.5000), (0.4516, 0.3929),
    (0.5161, 0.3929), (0.5484, 0.7500), (0.6129, 0.6786), (0.5161, 0.3214),
    (0.5484, 0.6786), (0.1935, 0.5000), (0.2258, 0.6071), (0.3226, 0.7143),
    (0.2903, 0.6786), (0.3226, 0.7143), (0.2258, 0.8214), (0.2903, 0.6429),
    (0.6129, 0.7857), (0.7742, 0.8214), (0.8065, 0.7500)]

test_targets = [purple, purple, purple, purple, purple, purple, purple, purple,
                purple, purple, orange, orange, orange, orange, orange, orange, orange, orange,
                orange, orange, green, green, green, green, green, green, green, green, green, green]

correct = 0

for a, t in zip(act_o, test_targets):
    if a.index(max(a)) == t.index(max(t)):
        correct += 1
print("correct :  {} / {} ({}%)".format(correct, len(act_o), (correct / len(act_o)) * 100))

