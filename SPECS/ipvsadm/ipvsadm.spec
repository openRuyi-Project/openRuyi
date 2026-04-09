# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           ipvsadm
Summary:        Utility to administer the Linux Virtual Server
Version:        1.31
Release:        %autorelease
License:        GPL-2.0-or-later
URL:            https://kernel.org/pub/linux/utils/kernel/ipvsadm/
VCS:            git:https://git.kernel.org/pub/scm/utils/kernel/ipvsadm/ipvsadm.git
#!RemoteAsset
Source0:        https://kernel.org/pub/linux/utils/kernel/ipvsadm/ipvsadm-%{version}.tar.gz
Source1:        ipvsadm.service
Source2:        ipvsadm.sysconfig
BuildSystem:    autotools

BuildOption(build):  -C libipvs
BuildOption(install):  BUILD_ROOT=%{buildroot}%{_prefix}
BuildOption(install):  SBIN=%{buildroot}%{_sbindir}
BuildOption(install):  MANDIR=%{buildroot}%{_mandir}
BuildOption(install):  MAN=%{buildroot}%{_mandir}/man8
BuildOption(install):  INIT=%{buildroot}%{_initrddir}

BuildRequires:  gcc
BuildRequires:  pkgconfig(libnl-3.0)
BuildRequires:  pkgconfig(popt)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  systemd-rpm-macros
BuildRequires:  make
%{?systemd_requires}

%description
ipvsadm is used to setup, maintain, and inspect the virtual server
table in the Linux kernel. The Linux Virtual Server can be used to
build scalable network services based on a cluster of two or more
nodes.

# No configure.
%conf

%build -a
# relys on the libipvs.
make ipvsadm

%install -a
rm -f %{buildroot}%{_initrddir}/%{name}
install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service
install -p -D -m 0600 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/%{name}-config

%check
# No tests here.

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%doc MAINTAINERS README
%{_unitdir}/ipvsadm.service
%config(noreplace) %{_sysconfdir}/sysconfig/ipvsadm-config
%{_sbindir}/ipvsadm
%{_sbindir}/ipvsadm-restore
%{_sbindir}/ipvsadm-save
%{_mandir}/man8/ipvsadm.8*
%{_mandir}/man8/ipvsadm-restore.8*
%{_mandir}/man8/ipvsadm-save.8*

%changelog
%autochangelog
