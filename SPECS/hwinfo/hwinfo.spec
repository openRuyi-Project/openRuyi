# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           hwinfo
Version:        25.0
Release:        %autorelease
Summary:        Hardware information tool
License:        GPL-1.0-or-later
URL:            https://github.com/openSUSE/hwinfo
#!RemoteAsset
Source0:        https://github.com/openSUSE/hwinfo/archive/refs/tags/%{version}.tar.gz
BuildSystem:    autotools

# it needs lex,but flex no lex.
Patch0:         0001-use-flex.patch

BuildOption(build):  LDFLAGS="%{build_ldflags} -Lsrc"
BuildOption(build):  LIBDIR=%{_libdir}
BuildOption(build):  HWINFO_VERSION=%{version}
BuildOption(build):  -j1
BuildOption(build):  GIT2LOG=:
BuildOption(install):  LIBDIR=%{_libdir}
BuildOption(install):  DESTDIR=%{buildroot}
BuildOption(install):  GIT2LOG=:

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  pkgconfig(uuid)
BuildRequires:  flex
BuildRequires:  libx86emu-devel

%description
hwinfo is used to probe for the hardware present in the system. It can be used to
generate a system overview log which can be later used for support.

%package        devel
Summary:        Development files for hwinfo
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Header files and libraries for developing with libhd library.

# No configure.
%conf

%install -a
%if "%{_sbindir}" == "%{_bindir}"
# Makefile hardcodes sbin paths. Fix the install locations here.
mv %{buildroot}/usr/sbin  %{buildroot}%{_sbindir}
%endif

# No tests
%check

%files
%doc *.md MAINTAINER
%license COPYING
%{_sbindir}/check_hd
%{_sbindir}/convert_hd
%{_sbindir}/getsysinfo
%{_sbindir}/hwinfo
%{_sbindir}/mk_isdnhwdb
%{_datadir}/hwinfo
%{_libdir}/libhd.so.*

%files devel
%{_includedir}/hd.h
%{_libdir}/pkgconfig/hwinfo.pc
%{_libdir}/libhd.so

%changelog
%autochangelog
