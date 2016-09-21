from conan.packager import ConanMultiPackager


if __name__ == "__main__":
    builder = ConanMultiPackager(username="sunside", channel="testing")
    builder.add_common_builds(shared_option_name="lmdb:shared", pure_c=False)

    patched_builds = []
    for settings, options in builder.builds:

        # Selecting the debug runtimes (MTd, MDd) on Windows for Debug builds
        if settings["compiler"] == "Visual Studio":
            if settings["compiler.runtime"].startswith("MT"):
                continue
            if settings["build_type"] == "Debug" and not settings["compiler.runtime"].endswith("d"):
                settings["compiler.runtime"] += "d"

        # Build both libstdc++ and libstdc++11
        elif settings["compiler"] == "gcc":
            settings["compiler.libcxx"] = "libstdc++11"
            patched_builds.append([settings, options])

            settings["compiler.libcxx"] = "libstdc++"
            patched_builds.append([settings, options])

        else:
            patched_builds.append([settings, options])

    builder.builds = patched_builds

    builder.run()

