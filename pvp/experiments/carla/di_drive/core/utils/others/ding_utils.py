from ding.utils import deep_merge_dicts


def compile_config(
    cfg,
    env_manager=None,
    policy=None,
    learner=None,
    collector=None,
    evaluator=None,
    buffer=None,
):
    if env_manager is not None:
        if cfg.env.manager.get('collect') is not None:
            cfg.env.manager.collect = deep_merge_dicts(env_manager.default_config(), cfg.env.manager.collect)
            cfg.env.manager.eval = deep_merge_dicts(env_manager.default_config(), cfg.env.manager.eval)
        else:
            cfg.env.manager = deep_merge_dicts(env_manager.default_config(), cfg.env.manager)
    if policy is not None:
        cfg.policy = deep_merge_dicts(policy.default_config(), cfg.policy)
    if learner is not None:
        cfg.policy.learn.learner = deep_merge_dicts(learner.default_config(), cfg.policy.learn.learner)
    if collector is not None:
        cfg.policy.collect.collector = deep_merge_dicts(collector.default_config(), cfg.policy.collect.collector)
    if evaluator is not None:
        cfg.policy.eval.evaluator = deep_merge_dicts(evaluator.default_config(), cfg.policy.eval.evaluator)
    if buffer is not None:
        cfg.policy.other.replay_buffer = deep_merge_dicts(buffer.default_config(), cfg.policy.other.replay_buffer)
    return cfg
