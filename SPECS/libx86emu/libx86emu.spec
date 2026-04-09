# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libx86emu
Version:        3.7
Release:        %autorelease
Summary:        x86 emulation library
License:        HPND-sell-variant
URL:            https://github.com/wfeldt/libx86emu
#!RemoteAsset
Source0:        https://github.com/wfeldt/libx86emu/archive/refs/tags/%{version}.tar.gz
BuildSystem:    autotools

BuildOption(build):  LIBDIR=%{_libdir}
BuildOption(build):  GIT2LOG=:
BuildOption(build):  VERSION=%{version}
BuildOption(build):  MAJOR_VERSION=3
BuildOption(build):  CFLAGS="-fPIC %{optflags}"
BuildOption(build):  LDFLAGS="-fPIC %{build_ldflags}"
BuildOption(build):  shared
BuildOption(install):  LIBDIR=%{_libdir}
BuildOption(install):  DESTDIR=%{buildroot}
BuildOption(install):  VERSION=%{version}
BuildOption(install):  MAJOR_VERSION=3

BuildRequires:  gcc
BuildRequires:  make

%description
Small x86 emulation library with focus of easy usage and extended execution
logging functions.

%package        devel
Summary:        Development files for libx86emu
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Header files and libraries for developing with libx86emu.

# No configure.
%conf

# No check
%check

%files
%doc README.md
%license LICENSE
%{_libdir}/libx86emu.so.3*

%files devel
%{_includedir}/x86emu.h
%{_libdir}/libx86emu.so

%changelog
%autochangelog
