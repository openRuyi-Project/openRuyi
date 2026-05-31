# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           pmix
Version:        5.0.10
Release:        %autorelease
Summary:        Process Management Interface for Exascale reference implementation
License:        BSD-3-Clause
URL:            https://pmix.org/
VCS:            git:https://github.com/openpmix/openpmix.git
#!RemoteAsset:  sha256:78663f6b932589d68e24feaf7f8a948d60be68d91965f3effbacb4cd88cf9a95
Source:         https://github.com/openpmix/openpmix/releases/download/v%{version}/pmix-%{version}.tar.bz2
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  --disable-wrapper-rpath
BuildOption(conf):  --disable-wrapper-runpath
BuildOption(conf):  --with-hwloc
BuildOption(conf):  --with-libevent
BuildOption(conf):  --with-zlib
BuildOption(conf):  --without-munge

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(hwloc) >= 1.11.0
BuildRequires:  pkgconfig(libevent) >= 2.0.21
BuildRequires:  pkgconfig(zlib)

%description
PMIx provides a standard interface that allows applications, tools,
and runtime systems to exchange process management information. It is
used by MPI implementations and resource managers to coordinate job
startup, namespace data, events, and related runtime services.

%package        devel
Summary:        Development files for PMIx
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
This package contains headers, the PMIx wrapper compiler, pkgconfig
metadata, and shared object symbolic links for developing applications
against PMIx.

%package        doc
Summary:        Documentation for PMIx
BuildArch:      noarch

%description    doc
HTML documentation for PMIx.

%install -a
rm -f %{buildroot}%{_libdir}/libpmix.la
rm -f %{buildroot}%{_libdir}/pmix/*.la

%files
%license LICENSE
%doc AUTHORS README.md VERSION
%config(noreplace) %{_sysconfdir}/pmix-mca-params.conf
%{_bindir}/palloc
%{_bindir}/pattrs
%{_bindir}/pctrl
%{_bindir}/pevent
%{_bindir}/plookup
%{_bindir}/pmix_info
%{_bindir}/pps
%{_bindir}/pquery
%exclude %{_datadir}/pmix/help-pmixcc.txt
%exclude %{_datadir}/pmix/pmixcc-wrapper-data.txt
%{_datadir}/pmix/
%{_libdir}/libpmix.so.*
%dir %{_libdir}/pmix
%{_libdir}/pmix/*.so
%{_mandir}/man1/pmix_info.1*

%files devel
%{_bindir}/pmixcc
%{_includedir}/pmix.h
%{_includedir}/pmix_common.h
%{_includedir}/pmix_deprecated.h
%{_includedir}/pmix_server.h
%{_includedir}/pmix_tool.h
%{_includedir}/pmix_version.h
%{_includedir}/pmix/
%{_libdir}/libpmix.so
%{_libdir}/pkgconfig/pmix.pc
%{_datadir}/pmix/help-pmixcc.txt
%{_datadir}/pmix/pmixcc-wrapper-data.txt
%{_mandir}/man3/PMIx_Abort.3*
%{_mandir}/man3/PMIx_Finalize.3*
%{_mandir}/man3/PMIx_Init.3*
%{_mandir}/man5/openpmix.5*

%files doc
%license LICENSE
%doc %{_docdir}/pmix/html

%changelog
%autochangelog
