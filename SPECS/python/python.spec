# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global flavor @BUILD_FLAVOR@%{nil}

# If we don't have python then we need to bootstrap it
# Set this to 1 in order to enable bootstrap
%if "%{flavor}" == "bootstrap"
%bcond bootstrap 1
%else
%bcond bootstrap 0
%endif

%global _test_target test
%global pybasever 3.13
# pybasever without the dot
%global pyshortver 313

%if %{with bootstrap}
%global pkgname python3-bootstrap
%else
%global pkgname python3
%endif


# Whether to use RPM build wheels from the python-{pip,setuptools,wheel}-wheel packages
# Uses upstream bundled prebuilt wheels otherwise
%bcond rpmwheels %{without bootstrap}

# If the rpmwheels condition is disabled, we use the bundled wheel packages
# from Python with the versions below.
# This needs to be manually updated when we update Python.
# Explore the sources tarball (you need the version before %%prep is executed):
#  $ tar -tf Python-%%{upstream_version}.tar.xz | grep whl
%global pip_version 25.2
%global setuptools_version 79.0.1
# All of those also include a list of indirect bundled libs:
# pip
#  $ %%{_rpmconfigdir}/pythonbundles.py <(unzip -p Lib/ensurepip/_bundled/pip-*.whl pip/_vendor/vendor.txt)
%global pip_bundled_provides %{expand:
Provides: bundled(python3dist(cachecontrol)) = 0.14.3
Provides: bundled(python3dist(certifi)) = 2025.7.14
Provides: bundled(python3dist(dependency-groups)) = 1.3.1
Provides: bundled(python3dist(distlib)) = 0.4
Provides: bundled(python3dist(distro)) = 1.9
Provides: bundled(python3dist(idna)) = 3.10
Provides: bundled(python3dist(msgpack)) = 1.1.1
Provides: bundled(python3dist(packaging)) = 25
Provides: bundled(python3dist(platformdirs)) = 4.3.8
Provides: bundled(python3dist(pygments)) = 2.19.2
Provides: bundled(python3dist(pyproject-hooks)) = 1.2
Provides: bundled(python3dist(requests)) = 2.32.4
Provides: bundled(python3dist(resolvelib)) = 1.2
Provides: bundled(python3dist(rich)) = 14.1
Provides: bundled(python3dist(setuptools)) = 70.3
Provides: bundled(python3dist(tomli)) = 2.2.1
Provides: bundled(python3dist(tomli-w)) = 1.2
Provides: bundled(python3dist(truststore)) = 0.10.1
Provides: bundled(python3dist(urllib3)) = 1.26.20
}
# setuptools
# vendor.txt not in .whl
# %%{_rpmconfigdir}/pythonbundles.py <(unzip -l Lib/test/wheeldata/setuptools-*.whl | grep -E '_vendor/.+dist-info/RECORD' | sed -E 's@^.*/([^-]+)-([^-]+)\.dist-info/.*$@\1==\2@')
%global setuptools_bundled_provides %{expand:
Provides: bundled(python3dist(autocommand)) = 2.2.2
Provides: bundled(python3dist(backports-tarfile)) = 1.2
Provides: bundled(python3dist(importlib-metadata)) = 8
Provides: bundled(python3dist(inflect)) = 7.3.1
Provides: bundled(python3dist(jaraco-collections)) = 5.1
Provides: bundled(python3dist(jaraco-context)) = 5.3
Provides: bundled(python3dist(jaraco-functools)) = 4.0.1
Provides: bundled(python3dist(jaraco-text)) = 3.12.1
Provides: bundled(python3dist(more-itertools)) = 10.3
Provides: bundled(python3dist(packaging)) = 24.2
Provides: bundled(python3dist(platformdirs)) = 4.2.2
Provides: bundled(python3dist(tomli)) = 2.0.1
Provides: bundled(python3dist(typeguard)) = 4.3
Provides: bundled(python3dist(typing-extensions)) = 4.12.2
Provides: bundled(python3dist(wheel)) = 0.45.1
Provides: bundled(python3dist(zipp)) = 3.19.2
}

%global pylibdir %{_libdir}/python%{pybasever}
%global dynload_dir %{pylibdir}/lib-dynload

# We use the upstream arch triplets, we convert them from %%{_arch}-linux%%{_gnu}
%global platform_triplet %{expand:%(echo %{_arch}-linux%{_gnu})}

# All bytecode files are in a __pycache__ subdirectory, with a name
# reflecting the version of the bytecode.
# See PEP 3147: http://www.python.org/dev/peps/pep-3147/
# For example,
#   foo/bar.py
# has bytecode at:
#   foo/__pycache__/bar.cpython-%%{pyshortver}.pyc
#   foo/__pycache__/bar.cpython-%%{pyshortver}.opt-1.pyc
#   foo/__pycache__/bar.cpython-%%{pyshortver}.opt-2.pyc
%global bytecode_suffixes .cpython-%{pyshortver}*.pyc

%if "%{flavor}" == "bootstrap"
Name:           python-bootstrap
%else
Name:           python
%endif

Version:        3.13.8
Release:        %autorelease
Summary:        Python 3 Interpreter
License:        Python-2.0.1
URL:            https://www.python.org
#!RemoteAsset:  sha256:b9910730526b298299b46b35595ced9055722df60c06ad6301f6a4e2c728a252
Source0:        %{url}/ftp/python/%{version}/Python-%{version}.tar.xz
#!RemoteAsset:  sha256:741978566e632b39ba64d522f5e2356e0fca96b0517186a7db64658f38634f8e
Source1:        %{url}/ftp/python/%{version}/Python-%{version}.tar.xz.asc
BuildSystem:    autotools

# Set values of base and platbase in sysconfig from /usr to /usr/local
Patch0:        0001-change-user-install-location.patch

BuildOption(conf):  --without-ensurepip
BuildOption(conf):  --with-wheel-pkg-dir=%{python_wheel_dir}
BuildOption(conf):  --with-platlibdir=%{_lib}
BuildOption(conf):  --enable-ipv6
BuildOption(conf):  --enable-shared
BuildOption(conf):  --with-system-expat
BuildOption(conf):  --with-lto
BuildOption(conf):  --with-dbmliborder=gdbm:ndbm

%if %{without bootstrap}
# Regenerate generated files (needs python3)
BuildOption(build):  regen-all PYTHON_FOR_REGEN="python%{pybasever}"
%endif

BuildRequires:  unzip
BuildRequires:  autoconf
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(expat)
BuildRequires:  gdbm-devel
BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  make
BuildRequires:  pkgconfig(libmpdec)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(uuid)

%if %{with rpmwheels}
# Python 3.12 removed the deprecated imp module,
# the first compatible version of pip is 23.1.2.
BuildRequires:  python-pip-wheel >= 23.1.2
%endif

%if %{without bootstrap}
BuildRequires:  python%{pybasever}
# for proper automatic provides
BuildRequires:  python3-rpm-generators
%endif

%description
Python %{pybasever} is an accessible, high-level, dynamically typed, interpreted
programming language, designed with an emphasis on code readability.
It includes an extensive standard library, and has a vast ecosystem of
third-party libraries.

%package        -n %{pkgname}
Summary:        Python %{pybasever} interpreter

# For consistency, we provide python3.X from python3 as well.
Provides:       python%{pybasever} = %{version}-%{release}
Provides:       python%{pybasever}%{?_isa} = %{version}-%{release}
# We recommend /usr/bin/python so users get it by default
Recommends:     %{_bindir}/python
# Packages with Python modules in standard locations automatically
# depend on python(abi). Provide that here.
Provides:       python(abi) = %{pybasever}
Provides:       /bin/python3
Requires:       %{pkgname}-libs%{?_isa} = %{version}-%{release}

# This prevents ALL subpackages built from this spec to require
# /usr/bin/python3* or python(abi). Granularity per subpackage is impossible.
# It's intended for the libs package not to drag in the interpreter
# All other packages require %%{pkgname} explicitly.
%global __requires_exclude ^(/usr/bin/python3|python\\(abi\\))

%description    -n %{pkgname}
Python %{pybasever} is an accessible, high-level, dynamically typed, interpreted
programming language, designed with an emphasis on code readability.
It includes an extensive standard library, and has a vast ecosystem of
third-party libraries.

The %{pkgname} package provides the "%{pkgname}" executable: the reference
interpreter for the Python language, version 3.
The majority of its standard library is provided in the %{pkgname}-libs package,
which should be installed automatically along with %{pkgname}.
The remaining parts of the Python standard library are broken out into the
%{pkgname}-tkinter and %{pkgname}-test packages, which may need to be installed
separately.

Documentation for Python is provided in the %{pkgname}-docs package.

Packages containing additional libraries for Python are generally named with
the "%{pkgname}-" prefix.

%if %{without bootstrap}
%package        -n python-unversioned-command
Summary:        The "python" command that runs Python 3
BuildArch:      noarch
Requires:       python3 == %{version}-%{release}
Provides:       python = %{version}-%{release}
# Something like https://launchpad.net/ubuntu/noble/+package/python-is-python3
Provides:       python-is-python3 = %{version}-%{release}

%description    -n python-unversioned-command
This package contains /usr/bin/python - the "python" command that runs Python 3.
%endif

%package        -n %{pkgname}-libs
Summary:        Python runtime libraries
%if %{with rpmwheels}
Requires:       python-pip-wheel >= 23.1.2
License:        Python-2.0.1 AND CC0-1.0 AND MIT
%else
Provides:       bundled(python3dist(pip)) = %{pip_version}
%pip_bundled_provides
License:        Python-2.0.1 AND CC0-1.0 AND MIT AND Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND ISC AND LGPL-2.1-only AND MPL-2.0 AND (Apache-2.0 OR BSD-2-Clause)
%endif
# Bundled internal headers are used even when building with system libb2
# last updated by https://github.com/python/cpython/pull/6286
Provides:       bundled(libb2) = 0.98.1
# Bundled mimalloc version in Include/internal/mimalloc/mimalloc.h
# Python's version is modified, differences are listed in:
# https://github.com/python/cpython/issues/113141
Provides:       bundled(mimalloc) = 2.12
# There are files in the standard library that have python shebang.
# We've filtered the automatic requirement out so libs are installable without
# the main package. This however makes it pulled in by default.
Recommends:     %{pkgname}%{?_isa} = %{version}-%{release}
# tkinter is part of the standard library,
# but it is torn out to save an unwanted dependency on tk and X11.
# we recommend it when tk is already installed (for better UX)
Recommends:     (%{pkgname}-tkinter%{?_isa} = %{version}-%{release} if tk%{?_isa})
# The zoneinfo module needs tzdata
Requires:       tzdata

%description    -n %{pkgname}-libs
This package contains runtime libraries for use by Python:
- the majority of the Python standard library
- a dynamically linked library for use by applications that embed Python as
  a scripting language, and by the main "%{exename}" executable

%package        -n %{pkgname}-devel
Summary:        Libraries and header files needed for Python development
License:        Python-2.0.1 AND MIT
Requires:       %{pkgname} = %{version}-%{release}
Requires:       %{pkgname}-libs%{?_isa} = %{version}-%{release}
# The RPM related dependencies bring nothing to a non-RPM Python developer
# But we want them when packages BuildRequire python3-devel
Requires:       python-rpm-macros
Requires:       python3-rpm-macros
Requires:       pyproject-rpm-macros
Requires:       unzip
Recommends:     %{pkgname}-pip
# tox users are likely to need the devel subpackage
Supplements:    tox

%if %{without bootstrap}
# Generators run on the main Python 3 so we cannot require them when bootstrapping it
Requires:       python3-rpm-generators
%endif

%description    -n %{pkgname}-devel
This package contains the header files and configuration needed to compile
Python extension modules (typically written in C or C++), to embed Python
into other programs, and to make binary distributions for Python libraries.

%package        -n %{pkgname}-idle
Summary:        A basic graphical development environment for Python
Requires:       %{pkgname} = %{version}-%{release}
Requires:       %{pkgname}-tkinter = %{version}-%{release}
Provides:       idle3 = %{version}-%{release}
Provides:       idle = %{version}-%{release}
Provides:       %{pkgname}-tools = %{version}-%{release}
Provides:       %{pkgname}-tools%{?_isa} = %{version}-%{release}

%description    -n %{pkgname}-idle
IDLE is Python’s Integrated Development and Learning Environment.

IDLE has the following features: Python shell window (interactive
interpreter) with colorizing of code input, output, and error messages;
multi-window text editor with multiple undo, Python colorizing,
smart indent, call tips, auto completion, and other features;
search within any window, replace within editor windows, and
search through multiple files (grep); debugger with persistent
breakpoints, stepping, and viewing of global and local namespaces;
configuration, browsers, and other dialogs.

%package        -n %{pkgname}-tkinter
Summary:        A GUI toolkit for Python
Requires:       %{pkgname} = %{version}-%{release}

# The importable module "turtle" is here, so provide python3-turtle.
# (We don't provide python3-turtledemo, that's not too useful when imported.)
%py_provides    %{pkgname}-turtle

%description    -n %{pkgname}-tkinter
The Tkinter (Tk interface) library is a graphical user interface toolkit for
the Python programming language.

%package        -n %{pkgname}-test
Summary:        The self-test suite for the main python3 package
Requires:       %{pkgname} = %{version}-%{release}
Requires:       %{pkgname}-libs%{?_isa} = %{version}-%{release}
%if %{with rpmwheels}
Requires:       python-setuptools-wheel
%else
Provides:       bundled(python3dist(setuptools)) = %{setuptools_version}
%setuptools_bundled_provides
License:        Python-2.0.1 AND MIT AND Apache-2.0 AND (Apache-2.0 OR BSD-2-Clause)
%endif

%description -n %{pkgname}-test
The self-test suite for the Python interpreter.

This is only useful to test Python itself. For testing general Python code,
you should use the unittest module from %{pkgname}-libs, or a library such as
%{pkgname}-pytest.

%prep -a
# Verify the second level of bundled provides is up to date
# Arguably this should be done in %%check, but %%prep has a faster feedback loop
# setuptools.whl does not contain the vendored.txt files
if [ -f %{_rpmconfigdir}/pythonbundles.py ]; then
  %{_rpmconfigdir}/pythonbundles.py <(unzip -p Lib/ensurepip/_bundled/pip-*.whl pip/_vendor/vendor.txt) --compare-with '%pip_bundled_provides'
  %{_rpmconfigdir}/pythonbundles.py <(unzip -l Lib/test/wheeldata/setuptools-*.whl | grep -E '_vendor/.+dist-info/RECORD' | sed -E 's@^.*/([^-]+)-([^-]+)\.dist-info/.*$@\1==\2@') --compare-with '%setuptools_bundled_provides'
fi

%if %{with rpmwheels}
rm Lib/ensurepip/_bundled/pip-%{pip_version}-py3-none-any.whl
rm Lib/test/wheeldata/setuptools-%{setuptools_version}-py3-none-any.whl
%endif

# Remove all exe files to ensure we are not shipping prebuilt binaries
# note that those are only used to create Microsoft Windows installers
# and that functionality is broken on Linux anyway
find -name '*.exe' -print -delete

# Remove bundled libraries to ensure that we're using the system copy.
rm -r Modules/expat
rm -r Modules/_decimal/libmpdec

# Remove files that should be generated by the build
# (This is after patching, so that we can use patches directly from upstream)
rm configure pyconfig.h.in

%conf -p
# Tell configure to not use git.
export HAS_GIT=not-found

# Regenerate the configure script and pyconfig.h.in
autoconf
autoheader

%build -p
# Set common compiler/linker flags
export CFLAGS="%{build_cflags} -D_GNU_SOURCE -fPIC -fwrapv"
export CXXFLAGS="%{build_cxxflags}"
export OPT="%{build_cflags}"
export LINKCC="gcc"

%install -p
# For compatibility
%global _pyconfig32_h pyconfig-32.h
%global _pyconfig64_h pyconfig-64.h
%global _pyconfig_h pyconfig-%{__isa_bits}.h

%install -a
# Rename the -devel script that differs on different arches to arch specific name
mv %{buildroot}%{_bindir}/python%{pybasever}-{,`uname -m`-}config
echo -e '#!/bin/sh\nexec %{_bindir}/python'%{pybasever}'-`uname -m`-config "$@"' > \
    %{buildroot}%{_bindir}/python%{pybasever}-config
    chmod +x %{buildroot}%{_bindir}/python%{pybasever}-config

# Make python3-devel multilib-ready
mv %{buildroot}%{_includedir}/python%{pybasever}/pyconfig.h \
    %{buildroot}%{_includedir}/python%{pybasever}/%{_pyconfig_h}
cat > %{buildroot}%{_includedir}/python%{pybasever}/pyconfig.h << EOF
#include <bits/wordsize.h>

#if __WORDSIZE == 32
#include "%{_pyconfig32_h}"
#elif __WORDSIZE == 64
#include "%{_pyconfig64_h}"
#else
#error "Unknown word size"
#endif
EOF

# Install directories for additional packages
install -d -m 0755 %{buildroot}%{pylibdir}/site-packages/__pycache__
%if "%{_lib}" == "lib64"
# The 64-bit version needs to create "site-packages" in /usr/lib/ (for
# pure-Python modules) as well as in /usr/lib64/ (for packages with extension
# modules).
# Note that rpmlint will complain about hardcoded library path;
# this is intentional.
install -d -m 0755 %{buildroot}%{_prefix}/lib/python%{pybasever}/site-packages/__pycache__
%endif

# Make sure sysconfig looks at the right pyconfig-32.h/pyconfig-64.h file instead of pyconfig.h
sed -i -e "s/'pyconfig.h'/'%{_pyconfig_h}'/" \
  %{buildroot}%{pylibdir}/sysconfig/*.py

# Install i18n tools to bindir
for tool in pygettext msgfmt; do
  cp -p Tools/i18n/${tool}.py %{buildroot}%{_bindir}/${tool}%{pybasever}.py
  ln -s ${tool}%{pybasever}.py %{buildroot}%{_bindir}/${tool}3.py
done

# Switch all shebangs to refer to the specific Python version.
# This currently only covers files matching ^[a-zA-Z0-9_]+\.py$,
# so handle files named using other naming scheme separately.
LD_LIBRARY_PATH=. ./python \
  %{_rpmconfigdir}/openruyi/pathfix.py \
  -i "%{_bindir}/python%{pybasever}" -pn \
  %{buildroot} \
  %{buildroot}%{_bindir}/*%{pybasever}.py

# Remove shebang lines from .py files that aren't executable, and
# remove executability from .py files that don't have a shebang line:
find %{buildroot} -name \*.py \
  \( \( \! -perm /u+x,g+x,o+x -exec sed -e '/^#!/Q 0' -e 'Q 1' {} \; \
  -print -exec sed -i '1d' {} \; \) -o \( \
  -perm /u+x,g+x,o+x ! -exec grep -m 1 -q '^#!' {} \; \
  -exec chmod a-x {} \; \) \)

# Get rid of DOS batch files:
find %{buildroot} -name \*.bat -exec rm {} \;

# Get rid of backup files:
find %{buildroot}/ -name "*~" -exec rm -f {} \;
find . -name "*~" -exec rm -f {} \;

# compileall CMD line options:
# -f - force rebuild even if timestamps are up to date
# -o - optimization levels to run compilation with
# -s - part of path to left-strip from path to source file (buildroot)
# -p - path to add as prefix to path to source file (/ to make it absolute)
# --hardlink-dupes - hardlink different optimization level pycs together if identical (saves space)
# --invalidation-mode - we prefer the timestamp invalidation mode for performance reasons
# -x - skip test modules with SyntaxErrors (taken from the Makefile)
LD_LIBRARY_PATH="%{buildroot}%{dynload_dir}/:%{buildroot}%{_libdir}" \
%{buildroot}%{_bindir}/python%{pybasever} -s -B -m compileall \
-f %{_smp_mflags} -o 0 -o 1 -o 2 -s %{buildroot} -p / %{buildroot} --hardlink-dupes --invalidation-mode=timestamp \
-x 'bad_coding|badsyntax|site-packages'

# Turn this BRP off, it is done by compileall2 --hardlink-dupes above
%global __brp_python_hardlink %{nil}

# Since we have *.py files in bindir, this is created, but we don't want it
rm -rf %{buildroot}%{_bindir}/__pycache__

# Fixup permissions for shared libraries from non-standard 555 to standard 755:
find %{buildroot} -perm 555 -exec chmod 755 {} \;

ln -s ./python3 %{buildroot}%{_bindir}/python
ln -s ./pydoc3 %{buildroot}%{_bindir}/pydoc
ln -s ./pygettext3.py %{buildroot}%{_bindir}/pygettext.py
ln -s ./msgfmt3.py %{buildroot}%{_bindir}/msgfmt.py
ln -s ./idle3 %{buildroot}%{_bindir}/idle
ln -s ./python3-config %{buildroot}%{_bindir}/python-config
ln -s ./python3.1 %{buildroot}%{_mandir}/man1/python.1
ln -s ./python3.pc %{buildroot}%{_libdir}/pkgconfig/python.pc

# Remove large, autogenerated sources and keep only the non-optimized pycache
for file in %{buildroot}%{pylibdir}/pydoc_data/topics.py $(grep --include='*.py' -lr %{buildroot}%{pylibdir}/encodings -e 'Python Character Mapping Codec .* from .* with gencodec.py'); do
    directory=$(dirname ${file})
    module=$(basename ${file%%.py})
    mv ${directory}/{__pycache__/${module}.cpython-%{pyshortver}.pyc,${module}.pyc}
    rm ${directory}/{__pycache__/${module}.cpython-%{pyshortver}.opt-?.pyc,${module}.py}
done

%check
%if "%{flavor}" == "bootstrap"
%else
EXCLUDES="-x test_ensurepip -x test_ctypes -x test_tools"
%make_build test TESTOPTS="$EXCLUDES"
%endif

%files -n %{pkgname}
%doc README.rst
%{_bindir}/pydoc*
%{_bindir}/python3
%{_bindir}/python%{pybasever}
%{_mandir}/*/*3*

%if %{without bootstrap}
%files -n python-unversioned-command
%{_bindir}/python
%{_mandir}/*/python.1*
%else
%exclude %{_bindir}/python
%exclude %{_mandir}/*/python.1*
%endif

%files -n %{pkgname}-libs
%doc README.rst
%dir %{pylibdir}
%dir %{dynload_dir}
%license %{pylibdir}/LICENSE.txt
# Pure Python modules
%{pylibdir}/*.py
%dir %{pylibdir}/__pycache__/
%{pylibdir}/__pycache__/*%{bytecode_suffixes}
%{pylibdir}/_pyrepl/
%{pylibdir}/asyncio/
%{pylibdir}/collections/
%{pylibdir}/concurrent/
%{pylibdir}/ctypes/
%{pylibdir}/curses/
%{pylibdir}/dbm/
%{pylibdir}/encodings/
%{pylibdir}/html/
%{pylibdir}/http/
%{pylibdir}/importlib/
%{pylibdir}/json/
%{pylibdir}/logging/
%{pylibdir}/multiprocessing/
%{pylibdir}/pathlib/
%{pylibdir}/pydoc_data/
%{pylibdir}/re/
%{pylibdir}/sqlite3/
%{pylibdir}/sysconfig/
%{pylibdir}/tomllib/
%{pylibdir}/unittest/
%{pylibdir}/urllib/
%{pylibdir}/venv/
%{pylibdir}/wsgiref/
%{pylibdir}/xml/
%{pylibdir}/xmlrpc/
%{pylibdir}/zipfile/
%{pylibdir}/zoneinfo/
# Handle the email module in detail to mark architecture.rst as %%doc
%dir %{pylibdir}/email/
%dir %{pylibdir}/email/__pycache__/
%{pylibdir}/email/*.py
%{pylibdir}/email/__pycache__/*%{bytecode_suffixes}
%{pylibdir}/email/mime/
%doc %{pylibdir}/email/architecture.rst
# Handle the ensurepip module in detail to not accidentally ship wheels
%dir %{pylibdir}/ensurepip/
%dir %{pylibdir}/ensurepip/__pycache__/
%{pylibdir}/ensurepip/*.py
%{pylibdir}/ensurepip/__pycache__/*%{bytecode_suffixes}
%if %{with rpmwheels}
%exclude %{pylibdir}/ensurepip/_bundled
%else
%dir %{pylibdir}/ensurepip/_bundled
%{pylibdir}/ensurepip/_bundled/pip-%{pip_version}-py3-none-any.whl
%endif
# This will be in the tkinter package
%exclude %{pylibdir}/turtle.py
%exclude %{pylibdir}/__pycache__/turtle*%{bytecode_suffixes}
# Extension modules
%{dynload_dir}/_asyncio.*.so
%{dynload_dir}/_bisect.*.so
%{dynload_dir}/_blake2.*.so
%{dynload_dir}/_bz2.*.so
%{dynload_dir}/_codecs_cn.*.so
%{dynload_dir}/_codecs_hk.*.so
%{dynload_dir}/_codecs_iso2022.*.so
%{dynload_dir}/_codecs_jp.*.so
%{dynload_dir}/_codecs_kr.*.so
%{dynload_dir}/_codecs_tw.*.so
%{dynload_dir}/_contextvars.*.so
%{dynload_dir}/_csv.*.so
%{dynload_dir}/_ctypes.*.so
%{dynload_dir}/_curses.*.so
%{dynload_dir}/_curses_panel.*.so
%{dynload_dir}/_datetime.*.so
%{dynload_dir}/_dbm.*.so
%{dynload_dir}/_gdbm.*.so
%{dynload_dir}/_decimal.*.so
%{dynload_dir}/_elementtree.*.so
%{dynload_dir}/_hashlib.*.so
%{dynload_dir}/_heapq.*.so
%{dynload_dir}/_interpchannels.*.so
%{dynload_dir}/_interpqueues.*.so
%{dynload_dir}/_interpreters.*.so
%{dynload_dir}/_json.*.so
%{dynload_dir}/_lsprof.*.so
%{dynload_dir}/_lzma.*.so
%{dynload_dir}/_md5.*.so
%{dynload_dir}/_multibytecodec.*.so
%{dynload_dir}/_multiprocessing.*.so
%{dynload_dir}/_opcode.*.so
%{dynload_dir}/_pickle.*.so
%{dynload_dir}/_posixshmem.*.so
%{dynload_dir}/_posixsubprocess.*.so
%{dynload_dir}/_queue.*.so
%{dynload_dir}/_random.*.so
%{dynload_dir}/_sha1.*.so
%{dynload_dir}/_sha2.*.so
%{dynload_dir}/_sha3.*.so
%{dynload_dir}/_socket.*.so
%{dynload_dir}/_sqlite3.*.so
%{dynload_dir}/_ssl.*.so
%{dynload_dir}/_statistics.*.so
%{dynload_dir}/_struct.*.so
%{dynload_dir}/_uuid.*.so
%{dynload_dir}/_zoneinfo.*.so
%{dynload_dir}/array.*.so
%{dynload_dir}/binascii.*.so
%{dynload_dir}/cmath.*.so
%{dynload_dir}/fcntl.*.so
%{dynload_dir}/grp.*.so
%{dynload_dir}/math.*.so
%{dynload_dir}/mmap.*.so
%{dynload_dir}/pyexpat.*.so
%{dynload_dir}/readline.*.so
%{dynload_dir}/resource.*.so
%{dynload_dir}/select.*.so
%{dynload_dir}/syslog.*.so
%{dynload_dir}/termios.*.so
%{dynload_dir}/unicodedata.*.so
%{dynload_dir}/zlib.*.so

%dir %{pylibdir}/site-packages/
%dir %{pylibdir}/site-packages/__pycache__/
%{pylibdir}/site-packages/README.txt

%if "%{_lib}" == "lib64"
%attr(0755,root,root) %dir %{_prefix}/lib/python%{pybasever}/
%attr(0755,root,root) %dir %{_prefix}/lib/python%{pybasever}/site-packages/
%attr(0755,root,root) %dir %{_prefix}/lib/python%{pybasever}/site-packages/__pycache__/
%endif

# "Makefile" and the config-32/64.h file are needed by
# sysconfig.get_config_vars(), so we include them in the core
# package, along with their parent directories:
%dir %{pylibdir}/config-%{pybasever}-%{platform_triplet}/
%{pylibdir}/config-%{pybasever}-%{platform_triplet}/Makefile
%dir %{_includedir}/python%{pybasever}/
%{_includedir}/python%{pybasever}/%{_pyconfig_h}

%{_libdir}/*.so
%{_libdir}/*.so.*

%files -n %{pkgname}-devel
%{pylibdir}/config-%{pybasever}-%{platform_triplet}/*
%exclude %{pylibdir}/config-%{pybasever}-%{platform_triplet}/Makefile
%exclude %{_includedir}/python%{pybasever}/%{_pyconfig_h}
%{_includedir}/python%{pybasever}/*.h
%{_includedir}/python%{pybasever}/internal/
%{_includedir}/python%{pybasever}/cpython/

%{_bindir}/pygettext3.py
%{_bindir}/pygettext.py
%{_bindir}/msgfmt3.py
%{_bindir}/msgfmt.py

%{_bindir}/pygettext%{pybasever}.py
%{_bindir}/msgfmt%{pybasever}.py

%{_bindir}/python*-config
%{_libdir}/pkgconfig/python-3.13-embed.pc
%{_libdir}/pkgconfig/python-3.13.pc
%{_libdir}/pkgconfig/python.pc
%{_libdir}/pkgconfig/python3-embed.pc
%{_libdir}/pkgconfig/python3.pc

%files -n %{pkgname}-idle
%{_bindir}/idle*
%{pylibdir}/idlelib

%files -n %{pkgname}-tkinter
%{pylibdir}/tkinter
%{pylibdir}/turtle.py
%{pylibdir}/__pycache__/turtle*%{bytecode_suffixes}
%dir %{pylibdir}/turtledemo
%{pylibdir}/turtledemo/*.py
%{pylibdir}/turtledemo/*.cfg
%dir %{pylibdir}/turtledemo/__pycache__/
%{pylibdir}/turtledemo/__pycache__/*%{bytecode_suffixes}

%files -n %{pkgname}-test
%{pylibdir}/test/
# Pure Python modules
%{pylibdir}/__phello__/
# Extension modules
%{dynload_dir}/_ctypes_test.*.so
%{dynload_dir}/_testbuffer.*.so
%{dynload_dir}/_testcapi.*.so
%{dynload_dir}/_testclinic.*.so
%{dynload_dir}/_testclinic_limited.*.so
%{dynload_dir}/_testexternalinspection.*.so
%{dynload_dir}/_testimportmultiple.*.so
%{dynload_dir}/_testinternalcapi.*.so
%{dynload_dir}/_testlimitedcapi.*.so
%{dynload_dir}/_testmultiphase.*.so
%{dynload_dir}/_testsinglephase.*.so
%{dynload_dir}/_xxtestfuzz.*.so
%{dynload_dir}/xxlimited.*.so
%{dynload_dir}/xxlimited_35.*.so
%{dynload_dir}/xxsubtype.*.so

%undefine _debuginfo_subpackages

%changelog
%autochangelog
