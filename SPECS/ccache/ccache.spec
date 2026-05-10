# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: corestudy <2760018909@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond test 0

Name:           ccache
Version:        4.13.6
Release:        %autorelease
Summary:        A Fast C/C++ Compiler Cache
License:        GPL-3.0-or-later
URL:            https://ccache.dev/
VCS:            git:https://github.com/ccache/ccache
#!RemoteAsset:  sha256:b0688da07593d481ed1901ec39739a770469090c8feff32522256d48077aaf9b
Source:         https://github.com/ccache/ccache/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DFETCHCONTENT_FULLY_DISCONNECTED:BOOL=ON
%if %{without test}
BuildOption(conf):  -DENABLE_TESTING:BOOL=OFF
%endif
BuildOption(conf):  -DREDIS_STORAGE_BACKEND:BOOL=OFF
BuildOption(conf):  -DENABLE_DOCUMENTATION:BOOL=OFF

BuildRequires:  cmake
BuildRequires:  pkgconfig(fmt)
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libxxhash)
%if %{with test}
BuildRequires:  doctest-devel
%endif

Provides:       distcc:%{_bindir}/ccache

%description
ccache is a compiler cache. It speeds up recompilation by caching the
result of previous compilations and detecting when the same compilation is
being done again.

%install -a
# create the ccache directory only
mkdir -p %{buildroot}/%{_libdir}/ccache

# filetrigger to create symlinks when compilers are installed
%filetriggerin -p /bin/sh -- %{_bindir}
# create symlinks for newly installed compilers
mkdir -p %{_libdir}/ccache
while read file; do
    name=$(basename $file)
    # check if it matches compiler patterns we care about
    for base in gcc g++ clang clang++ cc c++ nvcc; do
        # match: base, base-N, target-base, target-base-N
        case $name in
            $base|$base-[0-9]*|*-$base|*-$base-[0-9]*)
                ln -sf ../../bin/ccache %{_libdir}/ccache/$name
                ;;
        esac
    done
done

# filetrigger to remove symlinks when compilers are removed
%filetriggerun -p /bin/sh -- %{_bindir}
# remove symlinks for removed compilers
while read file; do
    name=$(basename $file)
    rm -f %{_libdir}/ccache/$name
done

%files
%license LICENSE.* GPL-3.0.txt
%doc README.*
%{_bindir}/ccache
%{_libdir}/ccache

%changelog
%autochangelog
