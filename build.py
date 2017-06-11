from conan.packager import ConanMultiPackager


if __name__ == "__main__":
    builder = ConanMultiPackager(username="memsharded", channel="stable", visual_versions=["12", "14", "15"])
    builder.add_common_builds(shared_option_name="HelloCi:shared")
    builder.use_default_named_pages()
    builder.run()