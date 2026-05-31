# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           prrte
Version:        3.0.13
Release:        %autorelease
Summary:        PMIx Reference RunTime Environment
License:        BSD-3-Clause
URL:            https://docs.prrte.org/
VCS:            git:https://github.com/openpmix/prrte.git
#!RemoteAsset:  sha256:81c27025182a26e90b0bb6aa67929a9313186fbd43964fc6d8734ce5cecd00ae
Source0:        https://github.com/openpmix/prrte/releases/download/v%{version}/prrte-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  --disable-silent-rules
BuildOption(conf):  --sysconfdir=%{_sysconfdir}/%{name}
BuildOption(conf):  --with-pmix
BuildOption(conf):  --with-hwloc
BuildOption(conf):  --with-libevent

BuildRequires:  flex
BuildRequires:  make
BuildRequires:  perl
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(hwloc) >= 1.11.0
BuildRequires:  pkgconfig(libevent) >= 2.0.21
BuildRequires:  pkgconfig(libevent_pthreads) >= 2.0.21
BuildRequires:  pkgconfig(pmix) >= 4.2.4

%description
PRRTE is the PMIx Reference RunTime Environment, a runtime system for
launching, monitoring, and managing parallel applications.

%package        devel
Summary:        Development files for PRRTE
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(hwloc) >= 1.11.0
Requires:       pkgconfig(hwloc) < 3.0.0
Requires:       pkgconfig(libevent) >= 2.0.21
Requires:       pkgconfig(libevent_pthreads) >= 2.0.21
Requires:       pkgconfig(pmix) >= 4.2.4
Requires:       pkgconfig(pmix) < 6.0.0

%description    devel
This package contains PRRTE headers and the shared library symlink for
developing PRRTE plugins and related software.

%install -a
rm -rf %{buildroot}%{_docdir}/%{name}
find %{buildroot} -name '*.la' -delete

%files
%doc README.md
%license LICENSE
%config(noreplace) %{_sysconfdir}/%{name}/prte-default-hostfile
%config(noreplace) %{_sysconfdir}/%{name}/prte-mca-params.conf
%config(noreplace) %{_sysconfdir}/%{name}/prte.conf
%{_bindir}/prte
%{_bindir}/prte_info
%{_bindir}/prted
%{_bindir}/prterun
%{_bindir}/prun
%{_bindir}/pterm
%{_libdir}/libprrte.so.*
%{_mandir}/man1/prte.1*
%{_mandir}/man1/prte_info.1*
%{_mandir}/man1/prted.1*
%{_mandir}/man1/prterun.1*
%{_mandir}/man1/prun.1*
%{_mandir}/man1/pterm.1*
%{_mandir}/man5/prte.5*
%{_datadir}/prte/

%files devel
%{_includedir}/prte.h
%{_includedir}/prte_version.h
%{_includedir}/prte/
%{_libdir}/libprrte.so

%changelog
%autochangelog
