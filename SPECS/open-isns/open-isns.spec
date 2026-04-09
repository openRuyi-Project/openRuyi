# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond slp 0

Name:           open-isns
Version:        0.103
Release:        %autorelease
Summary:        An Implementation of the iSNS Protocol
License:        LGPL-2.1-or-later
URL:            https://github.com/open-iscsi/open-isns
#!RemoteAsset
Source:         https://github.com/open-iscsi/open-isns/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    meson

%if %{with slp}
BuildOption(conf):  -Dslp=enabled
%else
BuildOption(conf):  -Dslp=disabled
%endif

BuildRequires:  meson >= 0.55.0
BuildRequires:  pkgconfig(openssl)
BuildRequires:  systemd-rpm-macros
%if %{with slp}
BuildRequires:  openslp-devel
%endif
%{?systemd_requires}
Requires:       coreutils
Recommends:     open-iscsi

%description
This is a partial implementation of the iSNS protocol (RFC 4171),
which supplies directory services for iSCSI initiators and targets.

%package        devel
Summary:        Development files for open-isns
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the header files and libraries needed to develop
applications that use the open-isns library.

# TODO: Fix tests.
# internal error: no pid file: /tmp/isns-test/Test01/server0/pid
%check

%post
%systemd_post isnsd.socket isnsd.service

%preun
%systemd_preun isnsd.socket isnsd.service

%postun
%systemd_postun_with_restart isnsd.socket isnsd.service

%files
%license COPYING
%doc HACKING README.md TODO
%{_sbindir}/isnsd
%{_sbindir}/isnsadm
%{_sbindir}/isnsdd
%dir %{_sysconfdir}/isns
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/isns/isnsd.conf
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/isns/isnsadm.conf
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/isns/isnsdd.conf
%ghost %dir %{_localstatedir}/run/pcscd/
%ghost %dir %{_localstatedir}/run/isnsd/
%{_mandir}/man8/isnsd.8*
%{_mandir}/man8/isnsadm.8*
%{_mandir}/man8/isnsdd.8*
%{_mandir}/man5/isns_config.5*
%{_unitdir}/isnsd.service
%{_unitdir}/isnsd.socket
%{_libdir}/libisns.so.0*

%files devel
%dir %{_includedir}/libisns
%{_includedir}/libisns/*.h
%{_libdir}/libisns.so
%{_libdir}/pkgconfig/libisns.pc

%changelog
%autochangelog
