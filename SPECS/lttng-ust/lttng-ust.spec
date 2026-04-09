# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: gns <wangbingzhen.riscv@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           lttng-ust
Version:        2.14.0
Release:        %autorelease
Summary:        Userspace Tracing (profiling) library
License:        LGPL-2.1-only AND MIT AND GPL-2.0-only AND BSD-3-Clause AND BSD-2-Clause
URL:            https://lttng.org/
VCS:            git:https://github.com/lttng/lttng-ust.git
#!RemoteAsset
Source:         https://lttng.org/files/lttng-ust/%{name}-%{version}.tar.bz2
BuildSystem:    autotools

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(liburcu)
BuildRequires:  pkgconfig(numa)
BuildRequires:  libtool

%description
lttng-ust is the userspace tracing library of LTTng.
It may be used by user-space applications to enable efficient tracing and profiling.

%package        devel
Summary:        Development files for the lttng-ust library
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       userspace-rcu-devel%{?_isa}

%description    devel
This package contains the header files, libraries, and documentation
needed to develop applications that use the lttng-ust library.

%conf -p
autoreconf -vif

%files
%{_libdir}/lib*.so.*
%{_mandir}/man3/*

%dir %{_docdir}/lttng-ust
%{_docdir}/lttng-ust/ChangeLog
%{_docdir}/lttng-ust/java-agent.md
%{_docdir}/lttng-ust/python-agent.md
%{_docdir}/lttng-ust/LICENSE
%{_docdir}/lttng-ust/README.md


%files devel
%{_bindir}/lttng-gen-tp
%{_mandir}/man1/*
%dir %{_includedir}/lttng
%{_includedir}/lttng/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/lttng-ust*.pc

%dir %{_docdir}/lttng-ust/examples
%{_docdir}/lttng-ust/examples/*

%changelog
%autochangelog
