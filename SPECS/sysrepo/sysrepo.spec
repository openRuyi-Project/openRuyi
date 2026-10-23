# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           sysrepo
Version:        5.2.27
Release:        %autorelease
Summary:        YANG-based configuration and operational data store
License:        BSD-3-Clause
URL:            https://github.com/sysrepo/sysrepo
#!RemoteAsset:  sha256:f08ac11f5b3782ca1305974c4883b67f084f1acf73eadd346d94d2c428871bf1
Source0:        https://github.com/sysrepo/sysrepo/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        sysrepo.sysusers
Source2:        sysrepo-plugind.sysusers
Source3:        sysrepo-plugind.service
Source4:        sysrepo-notifd.sysusers
Source5:        sysrepo-notifd.service
BuildSystem:    cmake

BuildOption(conf):  -DCMAKE_BUILD_TYPE=RELWITHDEBINFO
BuildOption(conf):  -DENABLE_TESTS:BOOL=ON
BuildOption(conf):  -DREPO_SHM_SETUP:BOOL=OFF
BuildOption(conf):  -DNOTIFD_SETUP:BOOL=OFF
BuildOption(conf):  -DSYSREPO_UMASK=007
BuildOption(conf):  -DSYSREPO_GROUP=sysrepo
BuildOption(conf):  -DNACM_SRMON_DATA_PERM=660

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(libyang) >= 6.4.9
# for tests
BuildRequires:  pkgconfig(cmocka)
# for sysrepo-plugind systemd support
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  systemd-rpm-macros

Requires(pre):  systemd-sysusers

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
Requires(pre):  systemd-sysusers

%description    plugind
Sysrepo plugin daemon and service.

%package        notifd
Summary:        Sysrepo notification daemon
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires(pre):  systemd-sysusers

%description    notifd
Sysrepo notification daemon, service, and notification module setup scripts.

%install -a
install -D -p -m 0644 %{SOURCE1} %{buildroot}%{_sysusersdir}/sysrepo.conf
install -D -p -m 0644 %{SOURCE2} %{buildroot}%{_sysusersdir}/sysrepo-plugind.conf
install -D -p -m 0644 %{SOURCE3} %{buildroot}%{_unitdir}/sysrepo-plugind.service
install -D -p -m 0644 %{SOURCE4} %{buildroot}%{_sysusersdir}/sysrepo-notifd.conf
install -D -p -m 0644 %{SOURCE5} %{buildroot}%{_unitdir}/sysrepo-notifd.service
mkdir -p -m=770 %{buildroot}%{_sysconfdir}/sysrepo

%pre
%sysusers_create_package %{name} %{SOURCE1}

%postun
# sysrepo apps shared memory
rm -rf /dev/shm/sr_*
rm -rf /dev/shm/srsub_*

%pre plugind
%sysusers_create_package %{name}-plugind %{SOURCE2}

%post plugind
%systemd_post %{name}-plugind.service

%postun plugind
%systemd_postun_with_restart %{name}-plugind.service

%pre notifd
%sysusers_create_package %{name}-notifd %{SOURCE4}

%post notifd
export SR_NOTIFD_MODULE_DIR=%{_datadir}/yang/modules/sysrepo
export SR_NOTIFD_MODULE_PERMS=660
export SR_NOTIFD_MODULE_OWNER=root
export SR_NOTIFD_MODULE_GROUP=sysrepo
bash %{_datadir}/sysrepo/scripts/setup_notifd.sh
%systemd_post %{name}-notifd.service

%preun notifd
%systemd_preun %{name}-notifd.service

%postun notifd
%systemd_postun_with_restart %{name}-notifd.service

%files
%doc README.md
%license LICENSE
%{_sysusersdir}/sysrepo.conf
%{_libdir}/libsysrepo.so.*
%{_datadir}/yang/modules/sysrepo/*.yang
%dir %{_datadir}/yang/modules/sysrepo/
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

%files notifd
%{_unitdir}/sysrepo-notifd.service
%{_sysusersdir}/sysrepo-notifd.conf
%{_bindir}/sysrepo-notifd
%{_mandir}/man8/sysrepo-notifd.8*
%{_datadir}/sysrepo/scripts

%changelog
%autochangelog
