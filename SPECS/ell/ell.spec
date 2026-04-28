# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           ell
Version:        0.80
Release:        %autorelease
Summary:        Embedded Linux Library
License:        LGPL-2.1-or-later
URL:            https://git.kernel.org/cgit/libs/ell/ell.git
VCS:            git:https://git.kernel.org/pub/scm/libs/ell/ell.git
#!RemoteAsset
Source:         https://mirrors.kernel.org/pub/linux/libs/ell/ell-%{version}.tar.xz
BuildSystem:    autotools

# the test will fail.
Patch0:         0001-remove-hwdb-test.patch

BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  xz
# for test
BuildRequires:  procps-ng

%description
The "Embedded Linux Library" (ELL) provides a comprehensive set of APIs for
asynchronous programming, event loops, and various utility functions. This package
contains the runtime shared library.

%package        devel
Summary:        Development files for the Embedded Linux Library (ELL)
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the header files, pkg-config files, and other development
files for the Embedded Linux Library (ELL).

%files
%license COPYING
%{_libdir}/libell.so.*

%files devel
%{_libdir}/libell.so
%{_libdir}/pkgconfig/ell.pc
%{_includedir}/ell/

%changelog
%{?autochangelog}
