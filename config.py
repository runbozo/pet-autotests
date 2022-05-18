from dynaconf import Dynaconf

DEFAULT_ENV = "dev"  # dev only

settings = Dynaconf(
    env=DEFAULT_ENV,
    settings_files=[
        "./dev_settings.toml",
    ],
    environments=True,
    merge_enabled=True,
)
