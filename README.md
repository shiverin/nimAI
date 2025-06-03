# 🤖 Q-Learning AI for Nim Game

This project implements an intelligent AI agent that learns to play the classic game of Nim using **Q-learning**, a reinforcement learning algorithm.

---

## Project Overview

The Nim game consists of several piles of objects, where two players alternate turns removing objects from a single pile. The player forced to take the last object loses. This project trains an AI agent to optimally play Nim through self-play and iterative learning.

---

## Technical Highlights

### Q-Learning Fundamentals

- **Q-Values**: The AI learns the expected utility (Q-value) of taking a given action from a given state. A *state* is the current configuration of piles, and an *action* is removing a number of objects from a pile.

- **Q-Table Initialization**: An initially empty dictionary stores Q-values as keys of `(state, action)` pairs. States are represented as tuples of pile sizes for hashing.

- **Training Loop**: The AI trains by playing many games against itself (`n` iterations). During each game, it records states, actions, and resulting states to update Q-values.

- **Q-Value Update Rule**: Q-values are updated iteratively using the formula:

  \[
  Q(s, a) \leftarrow Q(s, a) + \alpha \times \big(\text{reward} + \gamma \times \max_{a'} Q(s', a') - Q(s, a)\big)
  \]

  where:
  - \(\alpha\) is the learning rate,
  - \(\gamma\) is the discount factor for future rewards (implicitly 1 here),
  - \(s\) and \(a\) are the old state and action,
  - \(s'\) is the new state,
  - reward is the immediate reward received,
  - and \(\max_{a'} Q(s', a')\) is the best future expected reward from the new state.

- **Action Selection (Exploration vs Exploitation)**: The AI balances exploration and exploitation using an epsilon-greedy policy—randomly choosing actions with probability \(\epsilon\), or the best-known action otherwise.

### Software Design

- **Modular Classes**:
  - `Nim`: Defines the game mechanics, state representation, available actions, and player switching logic.
  - `NimAI`: Encapsulates the Q-learning logic, including Q-value storage, updating, and action choice.
  
- **Self-Play Training**: The AI plays games against itself, updating Q-values after every move and at game termination, which accelerates convergence to optimal play.

- **Human Interaction Mode**: Allows a human player to challenge the trained AI, showcasing the AI’s learned strategy and decision-making.

---

## Key Learnings & Skills Demonstrated

- Mastery of **reinforcement learning concepts**, especially Q-learning for discrete state-action spaces.
- Practical implementation of **state-action value functions** and efficient Q-table updates.
- Application of **epsilon-greedy policies** for balancing exploration and exploitation.
- Strong understanding of **game theory** and dynamic programming techniques.
- Proficiency in Python with object-oriented programming and algorithmic design.

---

This project showcases my ability to design and implement core AI algorithms with clear understanding of their mathematical foundations, preparing me to contribute effectively to roles involving machine learning, AI development, or intelligent system design.

