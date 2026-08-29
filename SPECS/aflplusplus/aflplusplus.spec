# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jvle <keke.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global llvm_config /usr/bin/llvm-config
%global gcc /usr/bin/gcc-%{gcc_version}
%global gxx /usr/bin/g++-%{gcc_version}
%global clang /usr/bin/clang
%global lld /usr/bin/ld.lld
%global afl_helper_path %{_libdir}/af
%global _lto_cflags %{nil}
%global srcname Aflplusplus

Name:           %{srcname}
Version:        5.02c
Release:        %autorelease
Summary:        Practical, instrumentation-driven fuzzer for binary formats
License:        Apache-2.0
URL:            https://aflplus.plus/
VCS:            git:https://github.com/AFLplusplus/AFLplusplus
#!RemoteAsset:  sha256:118415843e5d289d63bd6d8f2252c18212978f15ac9e86acbbc75766cd45acde
Source0:        https://github.com/AFLplusplus/AFLplusplus/archive/refs/tags/v%{version}.tar.gz
# For running the tests:
Source1:        hello.c
BuildSystem:    autotools

BuildOption(prep):  -n AFLplusplus-%{version}
%ifnarch x86_64
BuildOption(build):  AFL_NO_X86=1
BuildOption(install):  AFL_NO_X86=1
%endif
BuildOption(build):  LLVM_CONFIG="%{llvm_config}"
BuildOption(build):  CC="%{gcc}"
BuildOption(build):  CXX="%{gxx}"
BuildOption(build):  AFL_REAL_LD="%{lld}"
BuildOption(build):  PREFIX="%{_prefix}"
BuildOption(build):  HELPER_PATH="%{afl_helper_path}"
BuildOption(build):  DOC_PATH="%{_pkgdocdir}"
BuildOption(build):  MAN_PATH="%{_mandir}/man8"
BuildOption(build):  MISC_PATH="%{_pkgdocdir}"
BuildOption(build):  source-only
BuildOption(install):  LLVM_CONFIG="%{llvm_config}"
BuildOption(install):  CC="%{gcc}"
BuildOption(install):  CXX="%{gxx}"
BuildOption(install):  AFL_REAL_LD="%{lld}"
BuildOption(install):  PREFIX="%{_prefix}"
BuildOption(install):  HELPER_PATH="%{afl_helper_path}"
BuildOption(install):  DOC_PATH="%{_pkgdocdir}"
BuildOption(install):  MAN_PATH="%{_mandir}/man8"
BuildOption(install):  MISC_PATH="%{_pkgdocdir}"

BuildRequires:  clang
BuildRequires:  gcc%{gcc_version}-c++
BuildRequires:  gcc%{gcc_version}-devel
BuildRequires:  llvm-devel
%ifarch x86_64
BuildRequires:  lld
%endif
BuildRequires:  make
BuildRequires:  unzip

%description
Aflplusplus uses a novel type of compile-time instrumentation
and genetic algorithms to automatically discover clean, interesting
test cases that trigger new internal states in the targeted
binary. This substantially improves the functional coverage for the
fuzzed code. The compact synthesized corpuses produced by the tool are
also useful for seeding other, more labor- or resource-intensive
testing regimes down the road.

Compared to other instrumented fuzzers, afl-fuzz is designed to be
practical: it has a modest performance overhead, uses a variety of
highly effective fuzzing strategies, requires essentially no
configuration, and seamlessly handles complex, real-world use cases -
say, common image parsing or file compression libraries.

%package        clang
Summary:        Clang and clang++ support for %{srcname}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%if "%{clang_major_version}" != ""
Requires:       clang(major) = %{clang_major_version}
%endif
%ifarch x86_64
Requires:       %{lld}
%endif
# This ensures that AFL_USE_ASAN=1 works out of the box.  However as
# it is not strictly required to use AFL, make it optional.
Recommends:     compiler-rt

%description    clang
This subpackage contains clang and clang++ support for
%{srcname}.

%build -p
# We used to set CFLAGS/CXXFLAGS = %%{optflags} here, but these break
# the Clang instrumentation in some way.
unset CFLAGS
unset CXXFLAGS

%conf
# No configure script

%install -p
# We used to set CFLAGS/CXXFLAGS = %%{optflags} here, but these break
# the Clang instrumentation in some way.
unset CFLAGS
unset CXXFLAGS

%install -a
%ifnarch x86_64
# On non-x86 these files are built and installed but they don't
# function, so delete them.  Only afl-clang-fast* works.
# afl-clang-fast* is a symlink to afl-cc / afl-c++ so we cannot delete
# those binaries.
rm $RPM_BUILD_ROOT%{_bindir}/afl-clang
rm $RPM_BUILD_ROOT%{_bindir}/afl-clang++
rm $RPM_BUILD_ROOT%{_bindir}/afl-gcc
rm $RPM_BUILD_ROOT%{_bindir}/afl-g++
rm $RPM_BUILD_ROOT%{_mandir}/man8/afl-cc.8*
rm $RPM_BUILD_ROOT%{_mandir}/man8/afl-c++.8*
%endif

# Otherwise we see:
# ERROR: No build ID note found in <.o file>
chmod -x $RPM_BUILD_ROOT%{afl_helper_path}/*.o

%if 0%{?__isa_bits} == 64
rm -f $RPM_BUILD_ROOT%{afl_helper_path}/afl-compiler-rt-32.o
rm -f $RPM_BUILD_ROOT%{afl_helper_path}/afl-llvm-rt-32.o
rm -f $RPM_BUILD_ROOT%{afl_helper_path}/afl-llvm-rt-lto-32.o
%endif

# Remove docs since we will package them using %%doc.
mv $RPM_BUILD_ROOT%{_pkgdocdir} pkg-docs

%check
# This just checks that simple programs can be compiled using
# the compiler wrappers.

# Probably users will need to set this manually if they are using
# clang XXX.
export PATH="$(%{llvm_config} --bindir)":$PATH

ln -s %{SOURCE1} hello.cpp
./afl-clang-fast %{SOURCE1} -o hello
./hello
./afl-clang-fast++ hello.cpp -o hello
./hello
export AFL_CC="%{gcc}"
export AFL_CXX="%{gxx}"
./afl-gcc-fast %{SOURCE1} -o hello
./hello
./afl-g++-fast hello.cpp -o hello
./hello

# Also check that we got the %%clang_major_version macro
test -n '%{clang_major_version}'

%files
%doc pkg-docs/*
%license docs/COPYING
%ifarch x86_64
%{_bindir}/afl-g++
%{_bindir}/afl-gcc
%endif
%{_bindir}/afl-analyze
%{_bindir}/afl-addseeds
%{_bindir}/afl-cc
%{_bindir}/afl-c++
%{_bindir}/afl-cmin
%{_bindir}/afl-cmin.awk
%{_bindir}/afl-cmin.bash
%{_bindir}/afl-cmin.py
%{_bindir}/afl-fuzz
%{_bindir}/afl-gcc-fast
%{_bindir}/afl-g++-fast
%{_bindir}/afl-gotcpu
%{_bindir}/afl-health
%{_bindir}/afl-persistent-config
%{_bindir}/afl-plot
%{_bindir}/afl-showmap
%{_bindir}/afl-system-config
%{_bindir}/afl-tmin
%{_bindir}/afl-whatsup
%dir %{afl_helper_path}
%ifarch x86_64
%{afl_helper_path}/afl-compiler-rt-64.o
%endif
%{afl_helper_path}/afl-compiler-rt.o
%{afl_helper_path}/afl-gcc-cmplog-pass.so
%{afl_helper_path}/afl-gcc-cmptrs-pass.so
%{afl_helper_path}/afl-gcc-pass.so
%{afl_helper_path}/afl-gcc-rt.o
%{afl_helper_path}/afl-llvm-ijon-pass.so
%{afl_helper_path}/injection-pass.so
%ifarch x86_64
%{_mandir}/man8/afl-c++.8*
%{_mandir}/man8/afl-cc.8*
%endif
%{_mandir}/man8/afl-addseeds.8*
%{_mandir}/man8/afl-analyze.8*
%{_mandir}/man8/afl-cmin.8*
%{_mandir}/man8/afl-cmin.awk.8*
%{_mandir}/man8/afl-cmin.bash.8*
%{_mandir}/man8/afl-cmin.py.8*
%{_mandir}/man8/afl-fuzz.8*
%{_mandir}/man8/afl-gcc-fast.8*
%{_mandir}/man8/afl-g++-fast.8*
%{_mandir}/man8/afl-gotcpu.8*
%{_mandir}/man8/afl-health.8*
%{_mandir}/man8/afl-plot.8*
%{_mandir}/man8/afl-persistent-config.8*
%{_mandir}/man8/afl-showmap.8*
%{_mandir}/man8/afl-system-config.8*
%{_mandir}/man8/afl-tmin.8*
%{_mandir}/man8/afl-whatsup.8*
%{_includedir}/afl/

%files clang
%license docs/COPYING
%ifarch x86_64
%{_bindir}/afl-clang
%{_bindir}/afl-clang++
%endif
%{_bindir}/afl-clang-fast
%{_bindir}/afl-clang-fast++
%{_bindir}/afl-clang-lto
%{_bindir}/afl-clang-lto++
%{_bindir}/afl-ld-lto
%{_bindir}/afl-lto
%{_bindir}/afl-lto++
%{afl_helper_path}/afl-llvm-dict2file.so
%{afl_helper_path}/afl-c11-pass.so
%{afl_helper_path}/afl-llvm-bug-pass.so
%{afl_helper_path}/afl-llvm-lto-instrumentlist.so
%{afl_helper_path}/afl-llvm-pass.so
%if 0%{?__isa_bits} == 32
%{afl_helper_path}/afl-llvm-rt-lto-32.o
%else
%{afl_helper_path}/afl-llvm-rt-lto-64.o
%endif
%{afl_helper_path}/afl-llvm-rt-lto.o
%{afl_helper_path}/cmplog-instructions-pass.so
%{afl_helper_path}/cmplog-routines-pass.so
%{afl_helper_path}/cmplog-switches-pass.so
%{afl_helper_path}/compare-transform-pass.so
%{afl_helper_path}/dynamic_list.txt
%{afl_helper_path}/libAFLDriver.a*
%{afl_helper_path}/libAFLQemuDriver.a
%{afl_helper_path}/libdislocator.so
%{afl_helper_path}/libtokencap.so
%{afl_helper_path}/SanitizerCoverageLTO.so
%{afl_helper_path}/SanitizerCoveragePCGUARD.so
%{afl_helper_path}/split-compares-pass.so
%{afl_helper_path}/split-switches-pass.so
%{_mandir}/man8/afl-clang-fast.8*
%{_mandir}/man8/afl-clang-fast++.8*
%{_mandir}/man8/afl-clang-lto.8.gz
%{_mandir}/man8/afl-clang-lto++.8.gz
%{_mandir}/man8/afl-lto.8.gz
%{_mandir}/man8/afl-lto++.8.gz

%changelog
%autochangelog
