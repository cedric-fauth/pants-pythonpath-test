python_sources(name="sources")

pex_binary(
    name="script",
    dependencies=[":sources"],
    entry_point="script.py",
    inherit_path="prefer", # also tried "fallback"
)

# local_environment(
#     name="local-environment",
#     subprocess_environment_env_vars=["PYTHONPATH"],
# )
