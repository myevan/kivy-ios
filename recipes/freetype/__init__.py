from toolchain import Recipe, shprint
from os.path import join
import sh


class FreetypeRecipe(Recipe):
    version = "2.5.5"
    url = "https://downloads.sf.net/project/freetype/freetype2/{version}/freetype-{version}.tar.gz"
    library = "objs/.libs/libfreetype.a"
    include_dir = ["include", ("builds/unix/ftconfig.h", "config/ftconfig.h")]
    include_per_arch = True

    def build_arch(self, arch):
        build_env = arch.get_env()
        configure = sh.Command(join(self.build_dir, "configure"))
        shprint(configure,
                "CC={}".format(build_env["CC"]),
                "LD={}".format(build_env["LD"]),
                "CFLAGS={}".format(build_env["CFLAGS"]),
                "LDFLAGS={}".format(build_env["LDFLAGS"]),
                "--prefix=/",
                "--host={}".format(arch.triple),
                "--without-png",
                "--without-bzip2",
                "--without-fsspec",
                "--without-harfbuzz",
                "--without-old-mac-fonts",
                "--enable-static=yes",
                "--enable-shared=no")
        shprint(sh.make, "clean")
        shprint(sh.make)


recipe = FreetypeRecipe()

