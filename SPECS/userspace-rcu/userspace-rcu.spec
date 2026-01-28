# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           userspace-rcu
Version:        0.15.3
Release:        %autorelease
Summary:        Userspace RCU (read-copy-update) library
License:        LGPL-2.1-or-later
URL:            https://liburcu.org/
VCS:            git:https://git.liburcu.org/userspace-rcu.git
#!RemoteAsset
Source:         https://lttng.org/files/urcu/%{name}-%{version}.tar.bz2
BuildSystem:    autotools

BuildRequires:  pkgconfig
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  make
BuildRequires:  libtool

%description
liburcu is a LGPLv2.1 userspace RCU (read-copy-update) library. This data
synchronization library provides read-side access which scales linearly with
the number of cores.

%package        devel
Summary:        Development files for the userspace-rcu library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the header files, libraries, and documentation
needed to develop applications that use the userspace-rcu library.

%conf -p
autoreconf -vif

%files
%doc ChangeLog README.md
%{_libdir}/lib*.so.*

%files devel
%doc %{_docdir}/%{name}/
%{_includedir}/urcu*
%{_libdir}/lib*.so
%{_libdir}/lib*.a
%{_libdir}/pkgconfig/liburcu*.pc

%changelog
%{?autochangelog}
