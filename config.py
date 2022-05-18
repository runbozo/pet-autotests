from dynaconf import Dynaconf

DEFAULT_ENV = "dev"  # [dev|prod]

settings = Dynaconf(
    env=DEFAULT_ENV,
    settings_files=[
        "./dev_settings.toml",
        "./prod_settings.toml",
    ],
    environments=True,
    merge_enabled=True,
)
