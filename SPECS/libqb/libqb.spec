# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: sunyuechi <sunyuechi@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libqb
Version:        2.0.9
Release:        %autorelease
Summary:        Library providing high performance logging, tracing, ipc, and poll
License:        LGPL-2.1-or-later
URL:            https://github.com/ClusterLabs/libqb
#!RemoteAsset:  sha256:57288f02c64a67b096fc73641f90db5b885dc1edcdb0e66b6d861c600d4e000d
Source:         %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(libxml-2.0)

%description
A "Quite Boring" library that provides high-performance, reusable
features for client-server architecture, such as logging, tracing,
inter-process communication (IPC), and polling.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
This package contains the header files, shared library symlinks and
pkg-config files needed to develop applications that link against
%{name}.

%package        doxygen2man
Summary:        Generate man pages from Doxygen XML files
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    doxygen2man
This package contains a program to create nicely-formatted man pages
from Doxygen XML files.

%conf -p
autoreconf -fiv

%install -a
# remove duped documents
rm -rf %{buildroot}%{_docdir}/%{name}

%check
# Upstream tests rely on IPC sockets and live processes that are not
# reliable inside the build chroot; Fedora gates them behind --with check
# for the same reason.

%files
%license COPYING
%{_sbindir}/qb-blackbox
%{_libdir}/libqb.so.*
%{_mandir}/man8/qb-blackbox.8*

%files devel
%doc README.markdown
%{_includedir}/qb/
%{_libdir}/libqb.so
%{_libdir}/pkgconfig/libqb.pc
%{_mandir}/man3/qb*.3*

%files doxygen2man
%{_bindir}/doxygen2man
%{_mandir}/man1/doxygen2man.1*

%changelog
%autochangelog
