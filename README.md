# reinforcement-learning-for-recommendation

```bash
>>> source .venv/bin/activate # activate virtual environment
>>> pip install -r requirements.txt # install required packages
```

## Markov decision process
A Markov decision process is a 4-tuple ${\displaystyle (S,A,P_{a},R_{a})}$, where:

${\displaystyle S}$ is a set of states called the state space,

${\displaystyle A}$ is a set of actions called the action space (alternatively, ${\displaystyle A_{s}}$ is the set of actions available from state ${\displaystyle s}$),

${\displaystyle P_{a}(s,s')=\Pr(s_{t+1}=s'\mid s_{t}=s,a_{t}=a)}$ is the probability that action ${\displaystyle a}$ in state ${\displaystyle s}$ at time ${\displaystyle t}$ will lead to state ${\displaystyle s'}$ at time ${\displaystyle t+1}$,

${\displaystyle R_{a}(s,s')=R(s_{t+1}=s'\mid s_{t}=s,a_{t}=a)}$ is the immediate reward received after transitioning from state ${\displaystyle s}$ to state ${\displaystyle s'}$, due to action ${\displaystyle a}$.


## Multi-armed bandit
A multi-armed bandit is a 2-tuple ${\displaystyle (A,R_{a})}$, where:

${\displaystyle A}$ is a set of actions called the action space (alternatively, ${\displaystyle A_{t}}$ is the set of actions available at time step ${\displaystyle t}$),

${\displaystyle R_{a}=R(a_{t}=a)}$ is the immediate reward received after taking action ${\displaystyle a}$ at time step ${\displaystyle t}$.

## Contextual multi-armed bandit
A contextual multi-armed bandit is a 3-tuple ${\displaystyle (S,A,R_{a})}$, where:

${\displaystyle S}$ is a set of states called the state space (namely, the context for actions),

${\displaystyle A}$ is a set of actions called the action space (alternatively, ${\displaystyle A_{t}}$ is the set of actions available at time step ${\displaystyle t}$),

${\displaystyle R_{a}(s)=R(s_{t}=s,a_{t}=a)}$ is the immediate reward received after taking action ${\displaystyle a}$ at time step ${\displaystyle t}$ when the state is ${\displaystyle s}$.


