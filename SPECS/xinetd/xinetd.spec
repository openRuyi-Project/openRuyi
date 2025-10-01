# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           xinetd
Version:        2.3.15.4
Release:        %autorelease
Summary:        An extended Internet services daemon
License:        xinetd
URL:            https://github.com/openSUSE/xinetd/
#!RemoteAsset
Source0:        https://github.com/openSUSE/xinetd/archive/refs/tags/%{version}.tar.gz
Source1:        sysconfig.xinetd
Patch:          0001-xinetd-service-sysconfig.patch
BuildSystem:    autotools

BuildOption(conf): --disable-silent-rules
BuildOption(conf): --without-libwrap
BuildOption(build): CFLAGS="%{optflags} -std=gnu17"

BuildRequires:  pkgconfig autoconf automake
BuildRequires:  libtool
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  pkgconfig(libtirpc)
BuildRequires:  systemd-rpm-macros
Provides:       inet-daemon

%description
xinetd is a replacement for the inetd daemon. It has more features
like access control, extensive logging, and the ability to make
services available based on time.

%conf -p
autoreconf -fiv

%install -a

install -D -m 0644 contrib/%{name}.service %{buildroot}%{_unitdir}/%{name}.service
install -d -m 755 %{buildroot}%{_sysconfdir}/sysconfig
install -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/sysconfig/xinetd

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun %{name}.service

%files
%doc README.md CHANGELOG COPYRIGHT
%{_mandir}/man5/*
%{_mandir}/man8/*
%dir %{_sysconfdir}/xinetd.d
%config(noreplace) %{_sysconfdir}/xinetd.d/*
%config(noreplace) %{_sysconfdir}/xinetd.conf
%{_sbindir}/xinetd
%{_bindir}/*
%{_unitdir}/xinetd.service
%config(noreplace) %{_sysconfdir}/sysconfig/xinetd

%changelog
%{?autochangelog}
