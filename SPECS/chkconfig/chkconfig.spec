# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           chkconfig
Summary:        A system tool for maintaining the /etc/rc*.d hierarchy
Version:        1.33
Release:        %autorelease
License:        GPL-2.0-only
URL:            https://github.com/fedora-sysv/chkconfig
#!RemoteAsset:  sha256:c973a38d46d75ab2b411ab141e4c320a66dc4cc98832c3f2f6c5999531057861
Source:         https://github.com/fedora-sysv/chkconfig/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(build):  RPM_OPT_FLAGS="%{build_cflags}"
BuildOption(build):  LDFLAGS="%{build_ldflags}"
BuildOption(install):  MANDIR=%{_mandir}
BuildOption(install):  SBINDIR=%{_sbindir}

BuildRequires:  pkgconfig(libnewt)
BuildRequires:  pkgconfig(popt)
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  make
BuildRequires:  pkgconfig(systemd)
BuildRequires:  beakerlib

Provides:       update-alternatives
Provides:       alternatives

%description
Chkconfig is a basic system utility.  It updates and queries runlevel
information for system services.  Chkconfig manipulates the numerous
symbolic links in /etc/rc.d, to relieve system administrators of some
of the drudgery of manually editing the symbolic links.

# No configure
%conf

%install -a
# Avoid illegal package names
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*@*
%find_lang %{name} --generate-subpackages

%files -f %{name}.lang
%license COPYING
%dir %{_sysconfdir}/alternatives
%ghost %dir %attr(755, root, root) /etc/alternatives.admindir
%ghost %dir %attr(755, root, root) /var/lib/alternatives
%{_sbindir}/ntsysv
%{_sbindir}/update-alternatives
%{_sbindir}/alternatives
%{_sbindir}/chkconfig
%{_prefix}/lib/systemd/systemd-sysv-install
%{_mandir}/man8/*

%changelog
%autochangelog
