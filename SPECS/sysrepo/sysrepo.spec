# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           sysrepo
Version:        4.2.10
Release:        %autorelease
Summary:        YANG-based configuration and operational data store
License:        BSD-3-Clause
URL:            https://github.com/sysrepo/sysrepo
#!RemoteAsset
Source0:        https://github.com/sysrepo/sysrepo/archive/v%{version}/%{name}-%{version}.tar.gz
Source2:        sysrepo.sysusers
Source3:        sysrepo-plugind.sysusers
Source4:        sysrepo-plugind.service
BuildSystem:    cmake

BuildOption(conf):  -DCMAKE_BUILD_TYPE=RELWITHDEBINFO
BuildOption(conf):  -DSYSREPO_UMASK=007
BuildOption(conf):  -DSYSREPO_GROUP=sysrepo
BuildOption(conf):  -DNACM_SRMON_DATA_PERM=660

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(libyang) >= 2.2.0
# for tests
BuildRequires:  pkgconfig(cmocka)
# for sysrepo-plugind systemd support
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  systemd-rpm-macros

%description
YANG-based configuration and operational data store - runtime Applications can
use sysrepo to store their configuration modeled by provided YANG model
instead of using e.g. flat configuration files. Sysrepo will ensure data
consistency of the data stored in the data store and enforce data constraints
defined by YANG model.

The library is implemented in C and provides an API for other software
to use for accessing sysrepo datastore.

The package also contains executable tools for sysrepo:

* sysrepoctl - manipulation of YANG modules (schemas)
* sysrepocfg - manipulation of YANG instance data

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
Headers of sysrepo library.

%package        plugind
Summary:        sysrepo plugin daemon
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    plugind
Sysrepo plugin daemon and service.

%install -a
install -D -p -m 0644 %{SOURCE2} %{buildroot}%{_sysusersdir}/sysrepo.conf
install -D -p -m 0644 %{SOURCE3} %{buildroot}%{_sysusersdir}/sysrepo-plugind.conf
install -D -p -m 0644 %{SOURCE4} %{buildroot}%{_unitdir}/sysrepo-plugind.service
mkdir -p -m=770 %{buildroot}%{_sysconfdir}/sysrepo

%pre
%sysusers_create_package %{name} %{SOURCE2}

%postun
# sysrepo apps shared memory
rm -rf /dev/shm/sr_*
rm -rf /dev/shm/srsub_*

%pre plugind
%sysusers_create_package %{name}-plugind %{SOURCE3}

%post plugind
%systemd_post %{name}-plugind.service

%postun plugind
%systemd_postun_with_restart %{name}-plugind.service

%files
%license LICENSE
%doc README.md
%{_sysusersdir}/sysrepo.conf
%{_libdir}/libsysrepo.so.*
%{_datadir}/yang/modules/sysrepo/*.yang
%dir %{_datadir}/yang/modules/sysrepo/
%dir %{_sysconfdir}/sysrepo
%dir %{_libdir}/sysrepo
%dir %{_libdir}/sysrepo/plugins
%attr(0770,root,sysrepo) %{_sysconfdir}/sysrepo
%{_bindir}/sysrepocfg
%{_bindir}/sysrepoctl
%{_datadir}/man/man1/sysrepocfg.1.gz
%{_datadir}/man/man1/sysrepoctl.1.gz

%files devel
%{_libdir}/libsysrepo.so
%{_libdir}/pkgconfig/sysrepo.pc
%{_includedir}/sysrepo*.h
%{_includedir}/sysrepo/*.h
%dir %{_includedir}/sysrepo/

%files plugind
%{_unitdir}/sysrepo-plugind.service
%{_sysusersdir}/sysrepo-plugind.conf
%{_bindir}/sysrepo-plugind
%{_datadir}/man/man8/sysrepo-plugind.8.gz
%dir %{_libdir}/sysrepo-plugind
%dir %{_libdir}/sysrepo-plugind/plugins

%changelog
%autochangelog
