"""
This type stub file was generated by pyright.
"""

from collections import UserDict

from celery.utils.serialization import strtobool

"""Worker remote control command implementations."""
__all__ = ("Panel",)
DEFAULT_TASK_INFO_ITEMS = ...
logger = ...
controller_info_t = ...

def ok(value): ...
def nok(value): ...

class Panel(UserDict):
    """Global registry of remote control commands."""

    data = ...
    meta = ...
    @classmethod
    def register(cls, *args, **kwargs): ...

def control_command(**kwargs): ...
def inspect_command(**kwargs): ...
@inspect_command()
def report(state):  # -> dict[str, Unknown]:
    """Information about Celery installation for bug reports."""
    ...

@inspect_command(
    alias="dump_conf",
    signature="[include_defaults=False]",
    args=[("with_defaults", strtobool)],
)
def conf(
    state, with_defaults=..., **kwargs
):  # -> dict[Unknown, Unknown | Any] | list[Unknown] | dict[Unknown, Unknown] | str:
    """List configuration."""
    ...

@inspect_command(variadic="ids", signature="[id1 [id2 [... [idN]]]]")
def query_task(
    state, ids, **kwargs
):  # -> dict[Unknown, tuple[Literal['active', 'reserved', 'ready'], Unknown]]:
    """Query for task information by id."""
    ...

@control_command(variadic="task_id", signature="[id1 [id2 [... [idN]]]]")
def revoke(state, task_id, terminate=..., signal=..., **kwargs):  # -> dict[str, str]:
    """Revoke task by task id (or list of ids).

    Keyword Arguments:
        terminate (bool): Also terminate the process if the task is active.
        signal (str): Name of signal to use for terminate (e.g., ``KILL``).
    """
    ...

@control_command(
    variadic="task_id",
    args=[("signal", str)],
    signature="<signal> [id1 [id2 [... [idN]]]]",
)
def terminate(state, signal, task_id, **kwargs):  # -> dict[str, str]:
    """Terminate task by task id (or list of ids)."""
    ...

@control_command(
    args=[("task_name", str), ("rate_limit", str)],
    signature="<task_name> <rate_limit (e.g., 5/s | 5/m | 5/h)>",
)
def rate_limit(state, task_name, rate_limit, **kwargs):  # -> dict[str, str]:
    """Tell worker(s) to modify the rate limit for a task by type.

    See Also:
        :attr:`celery.app.task.Task.rate_limit`.

    Arguments:
        task_name (str): Type of task to set rate limit for.
        rate_limit (int, str): New rate limit.
    """
    ...

@control_command(
    args=[("task_name", str), ("soft", float), ("hard", float)],
    signature="<task_name> <soft_secs> [hard_secs]",
)
def time_limit(state, task_name=..., hard=..., soft=..., **kwargs):  # -> dict[str, str]:
    """Tell worker(s) to modify the time limit for task by type.

    Arguments:
        task_name (str): Name of task to change.
        hard (float): Hard time limit.
        soft (float): Soft time limit.
    """
    ...

@inspect_command()
def clock(state, **kwargs):  # -> dict[str, Unknown]:
    """Get current logical clock value."""
    ...

@control_command()
def election(state, id, topic, action=..., **kwargs):  # -> None:
    """Hold election.

    Arguments:
        id (str): Unique election id.
        topic (str): Election topic.
        action (str): Action to take for elected actor.
    """
    ...

@control_command()
def enable_events(state):  # -> dict[str, str]:
    """Tell worker(s) to send task-related events."""
    ...

@control_command()
def disable_events(state):  # -> dict[str, str]:
    """Tell worker(s) to stop sending task-related events."""
    ...

@control_command()
def heartbeat(state):  # -> None:
    """Tell worker(s) to send event heartbeat immediately."""
    ...

@inspect_command(visible=False)
def hello(
    state, from_node, revoked=..., **kwargs
):  # -> dict[str, Unknown | dict[Unknown, Unknown]] | None:
    """Request mingle sync-data."""
    ...

@inspect_command(default_timeout=0.2)
def ping(state, **kwargs):  # -> dict[str, str]:
    """Ping worker(s)."""
    ...

@inspect_command()
def stats(state, **kwargs):
    """Request worker statistics/information."""
    ...

@inspect_command(alias="dump_schedule")
def scheduled(
    state, **kwargs
):  # -> list[dict[str, Unknown | str | dict[str, Unknown | bool | dict[str, Unknown | Any | None] | None] | None]]:
    """List of currently scheduled ETA/countdown tasks."""
    ...

@inspect_command(alias="dump_reserved")
def reserved(state, **kwargs):  # -> list[Unknown]:
    """List of currently reserved tasks, not including scheduled/active."""
    ...

@inspect_command(alias="dump_active")
def active(state, safe=..., **kwargs):  # -> list[Unknown]:
    """List of tasks currently being executed."""
    ...

@inspect_command(alias="dump_revoked")
def revoked(state, **kwargs):  # -> list[Unknown]:
    """List of revoked task-ids."""
    ...

@inspect_command(
    alias="dump_tasks",
    variadic="taskinfoitems",
    signature="[attr1 [attr2 [... [attrN]]]]",
)
def registered(
    state, taskinfoitems=..., builtins=..., **kwargs
):  # -> list[str | Unknown]:
    """List of registered tasks.

    Arguments:
        taskinfoitems (Sequence[str]): List of task attributes to include.
            Defaults to ``exchange,routing_key,rate_limit``.
        builtins (bool): Also include built-in tasks.
    """
    ...

@inspect_command(
    default_timeout=60,
    args=[("type", str), ("num", int), ("max_depth", int)],
    signature="[object_type=Request] [num=200 [max_depth=10]]",
)
def objgraph(state, num=..., max_depth=..., type=...):  # -> dict[str, str]:
    """Create graph of uncollected objects (memory-leak debugging).

    Arguments:
        num (int): Max number of objects to graph.
        max_depth (int): Traverse at most n levels deep.
        type (str): Name of object to graph.  Default is ``"Request"``.
    """
    ...

@inspect_command()
def memsample(state, **kwargs):  # -> str | None:
    """Sample current RSS memory usage."""
    ...

@inspect_command(args=[("samples", int)], signature="[n_samples=10]")
def memdump(state, samples=..., **kwargs):  # -> str:
    """Dump statistics of previous memsample requests."""
    ...

@control_command(args=[("n", int)], signature="[N=1]")
def pool_grow(state, n=..., **kwargs):  # -> dict[str, str]:
    """Grow pool by n processes/threads."""
    ...

@control_command(args=[("n", int)], signature="[N=1]")
def pool_shrink(state, n=..., **kwargs):  # -> dict[str, str]:
    """Shrink pool by n processes/threads."""
    ...

@control_command()
def pool_restart(
    state, modules=..., reload=..., reloader=..., **kwargs
):  # -> dict[str, str]:
    """Restart execution pool."""
    ...

@control_command(args=[("max", int), ("min", int)], signature="[max [min]]")
def autoscale(state, max=..., min=...):  # -> dict[str, str]:
    """Modify autoscale settings."""
    ...

@control_command()
def shutdown(state, msg=..., **kwargs):
    """Shutdown worker(s)."""
    ...

@control_command(
    args=[
        ("queue", str),
        ("exchange", str),
        ("exchange_type", str),
        ("routing_key", str),
    ],
    signature="<queue> [exchange [type [routing_key]]]",
)
def add_consumer(
    state, queue, exchange=..., exchange_type=..., routing_key=..., **options
):  # -> dict[str, str]:
    """Tell worker(s) to consume from task queue by name."""
    ...

@control_command(args=[("queue", str)], signature="<queue>")
def cancel_consumer(state, queue, **_):  # -> dict[str, str]:
    """Tell worker(s) to stop consuming from task queue by name."""
    ...

@inspect_command()
def active_queues(state):  # -> list[dict[Unknown, Unknown]]:
    """List the task queues a worker is currently consuming from."""
    ...