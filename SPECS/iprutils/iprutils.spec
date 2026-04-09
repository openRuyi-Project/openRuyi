# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# default without systemd
%bcond systemd 0

Name:           iprutils
Version:        2.4.19
Release:        %autorelease
Summary:        Utilities for the ipr
License:        CPL-1.0
URL:            https://github.com/bjking1/iprutils
#!RemoteAsset
Source0:        https://github.com/bjking1/iprutils/archive/rel-2-4-19/%{name}-%{version}.tar.gz
BuildSystem:    autotools

%if %{with systemd}
BuildOption(conf):  --with-systemd
BuildOption(conf):  --without-initscripts
%else
BuildOption(conf):  --without-systemd
BuildOption(conf):  --with-initscripts
%endif
BuildOption(conf):  --disable-static
BuildOption(conf):  --disable-sosreport

BuildRequires:  libtool
BuildRequires:  pkgconfig(libcap)
BuildRequires:  linux-headers
BuildRequires:  pkgconfig(zlib)
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  pkgconfig(ncurses)
%if %{with systemd}
BuildRequires:  systemd-rpm-macros
%endif

%description
Provides a suite of utilities to manage and configure SCSI devices.

%conf -p
export LDFLAGS="$LDFLAGS -lncursesw -ltinfo"
autoreconf -ivf

%if %{with systemd}
%post
%systemd_post iprinit.service
%systemd_post iprdump.service
%systemd_post iprupdate.service
%systemd_post iprutils.target

%preun
%systemd_preun iprinit.service
%systemd_preun iprdump.service
%systemd_preun iprupdate.service
%systemd_preun iprutils.target
%endif

%files
%doc README
%license LICENSE
%{_sbindir}/*
%if %{with systemd}
%{_unitdir}/*
%{_udevrulesdir}/90-iprutils.rules
%else
/usr/etc/init.d/*
%endif
%dir %{_sysconfdir}/ha.d
%dir %{_sysconfdir}/ha.d/resource.d
%{_sysconfdir}/ha.d/resource.d/iprha
%dir %{_sysconfdir}/bash_completion.d/
%{_sysconfdir}/bash_completion.d/*
%{_mandir}/man8/*
%changelog
%autochangelog
