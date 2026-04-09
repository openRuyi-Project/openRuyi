# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond systemd 1

Name:           conntrack-tools
Version:        1.4.8
Release:        %autorelease
Summary:        Userspace tools for interacting with the Connection Tracking System
License:        GPL-2.0-only
URL:            http://conntrack-tools.netfilter.org/
VCS:            git:https://git.netfilter.org/conntrack-tools
#!RemoteAsset
Source0:        http://netfilter.org/projects/conntrack-tools/files/%{name}-%{version}.tar.xz
Source1:        conntrackd.service
Source2:        conntrackd.conf
BuildSystem:    autotools

BuildOption(conf):  --disable-static
%if %{with systemd}
BuildOption(conf):  --enable-systemd
%else
BuildOption(conf):  --disable-systemd
%endif
BuildOption(build):  CFLAGS='%{optflags} -Wl,-z,lazy -DCONNTRACKD_LIB_DIR=\"%{_libdir}/conntrack-tools\"'

BuildRequires:  pkgconfig(libnfnetlink)
BuildRequires:  pkgconfig(libnetfilter_conntrack)
BuildRequires:  pkgconfig(libtirpc)
BuildRequires:  pkgconfig(libnetfilter_cttimeout)
BuildRequires:  pkgconfig(libnetfilter_cthelper)
BuildRequires:  pkgconfig(libmnl)
BuildRequires:  pkgconfig(libnetfilter_queue)
BuildRequires:  pkgconfig
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  make
%if %{with systemd}
BuildRequires:  pkgconfig(libsystemd)
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
%endif

%description
The conntrack-tools are a set of userspace tools that allow system
administrators to interact with the Connection Tracking System.

%install -a
install -d      %{buildroot}%{_sysconfdir}/conntrackd
install -m644   %{SOURCE2} %{buildroot}%{_sysconfdir}/conntrackd/
%if %{with systemd}
install -d 0755 %{buildroot}%{_unitdir}
install -m644   %{SOURCE1} %{buildroot}%{_unitdir}/
%endif

%if %{with systemd}
%post
%systemd_post conntrackd.service
%preun
%systemd_preun conntrackd.service
%postun
%systemd_postun conntrackd.service
%endif

%files
%doc AUTHORS TODO COPYING
%dir %{_sysconfdir}/conntrackd
%config(noreplace) %{_sysconfdir}/conntrackd/conntrackd.conf
%if %{with systemd}
%{_unitdir}/conntrackd.service
%endif
%{_sbindir}/{conntrack,conntrackd,nfct}
%dir %{_libdir}/conntrack-tools
%{_libdir}/conntrack-tools/*
%doc doc
%{_mandir}/man5/*
%{_mandir}/man8/*

%changelog
%autochangelog
