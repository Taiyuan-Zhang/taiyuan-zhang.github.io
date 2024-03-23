---
collection: publications
permalink: /publication/yxh2022tog
excerpt: 'This paper is about the number 1. The number 2 is left for future work.'
date: 2009-10-01
venue: 'Journal 1'
paperurl: '[paper](/files/yxh2022tog.pdf) [video](/files/yxh2022tog.mp4) [code](https://github.com/lvsichan/jittor-METARL)'
---

We propose a learning-based controller for high-dimensional dynamic systems with coupled fluid and solid objects. The dynamic behaviors of such systems can vary across different simulators and the control tasks subject to changing requirements from users. Our controller features high versatility and can adapt to changing dynamic behaviors and multiple tasks without re-training, which is achieved by combining two training strategies. We use meta-reinforcement learning to inform the controller of changing simulation parameters. We further design a novel task representation, which allows the controller to adapt to continually changing tasks via hindsight experience replay. We highlight the robustness and generality of our controller on a row of dynamic-rich tasks, including scooping up solid balls from a water pool, in-air ball acrobatics using fluid spouts, and zero-shot transferring to unseen simulators and constitutive models. In all the scenarios, our controller consistently outperforms the plain multi-task reinforcement-learning baseline.

Bibtex
-----
```
@article{ren2022versatile,
  title={Versatile Control of Fluid-directed Solid Objects Using Multi-task Reinforcement Learning},
  author={Ren, Bo and Ye, Xiaohan and Pan, Zherong and Zhang, Taiyuan},
  journal={ACM Transactions on Graphics},
  volume={42},
  number={2},
  pages={1--14},
  year={2022},
  publisher={ACM New York, NY}
}
```