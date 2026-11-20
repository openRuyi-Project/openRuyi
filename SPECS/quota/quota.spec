# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           quota
Version:        4.11
Release:        %autorelease
Summary:        Linux Diskquota system as part of the Linux kernel
License:        GPL-2.0-only AND GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://sourceforge.net/projects/linuxquota/
VCS:            git:https://git.code.sf.net/p/linuxquota/code
#!RemoteAsset:  sha256:0a51b8f920254d8e83c34a4c3082b7d241f5d6fd65188afadf29859d5223ef78
Source0:        https://downloads.sourceforge.net/linuxquota/%{name}-%{version}.tar.gz
Source1:        quota_nld.service
Source2:        quota_nld.sysconfig
Source3:        rpc-rquotad.service
Source4:        rpc-rquotad.sysconfig
#!RemoteAsset:  sha256:20e50fe7aae3e56378ebf0417d9de904f55a0e61e4df315333e632a4d3555d95
Source5:        https://www.gnu.org/licenses/old-licenses/lgpl-2.1.txt
Source6:        warnquota.conf
BuildSystem:    autotools

# Check the RPC port upper bound; https://src.fedoraproject.org/rpms/quota/blob/2e8eac20489e1836c5f43b58d5b909e7d0c70d42/f/quota-4.03-Validate-upper-bound-of-RPC-port.patch
Patch2001:      2001-validate-rpc-port.patch

BuildOption(conf):  --enable-bsd-behaviour
BuildOption(conf):  --enable-ext2direct=yes
BuildOption(conf):  --enable-ldapmail=yes
BuildOption(conf):  --disable-libwrap
BuildOption(conf):  --enable-netlink=yes
BuildOption(conf):  --enable-nls
BuildOption(conf):  --with-pid-dir=/run
BuildOption(conf):  --enable-rpc=yes
BuildOption(conf):  --enable-rpcsetquota=yes
BuildOption(conf):  --disable-xfs-roothack

BuildRequires:  coreutils
BuildRequires:  rpcgen
BuildRequires:  systemd
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  e2fsprogs
BuildRequires:  gettext-devel
BuildRequires:  pkgconfig(ldap)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(libnl-3.0) >= 3.1
BuildRequires:  pkgconfig(libnl-genl-3.0)
BuildRequires:  pkgconfig(libtirpc)
BuildRequires:  pkgconfig(com_err)
BuildRequires:  pkgconfig(ext2fs)
BuildRequires:  systemd-rpm-macros

Requires:       rpcbind

%systemd_requires

%description
The quota package contains system administration tools for monitoring
and limiting user and or group disk usage per file system.

%package        devel
Summary:        Development files for quota RPC
License:        GPL-2.0-only
Requires:       pkgconfig(libtirpc)

%description    devel
This package contains development header files for implementing disk quotas
on remote machines.

%package        help
Summary:        Additional documentation for disk quotas
Requires:       %{name}%{?_isa} = %{version}-%{release}
BuildArch:      noarch

%description    help
This package contains additional documentation for disk quotas concept in
Linux/UNIX environment.

%prep -a
cp -p %{SOURCE5} lgpl-2.1.txt

%install -a
install -D -p -m 644 %{SOURCE6} %{buildroot}%{_sysconfdir}/warnquota.conf
install -D -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_unitdir}/quota_nld.service
install -D -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/quota_nld
install -D -p -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_unitdir}/rpc-rquotad.service
install -D -p -m 644 %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/rpc-rquotad

%find_lang %{name} --generate-subpackages

%post
%systemd_post quota_nld.service rpc-rquotad.service

%preun
%systemd_preun quota_nld.service rpc-rquotad.service

%postun
%systemd_postun_with_restart quota_nld.service rpc-rquotad.service

%files
%doc Changelog
%license COPYING lgpl-2.1.txt
%{_bindir}/*
%{_unitdir}/*.service
%config(noreplace) %{_sysconfdir}/quotatab
%config(noreplace) %{_sysconfdir}/quotagrpadmins
%config(noreplace) %{_sysconfdir}/warnquota.conf
%config(noreplace) %{_sysconfdir}/sysconfig/quota_nld
%config(noreplace) %{_sysconfdir}/sysconfig/rpc-rquotad
%exclude %{_docdir}/%{name}

%files devel
%license COPYING
%dir %{_includedir}/rpcsvc
%{_includedir}/rpcsvc/rquota.*

%files help
%doc doc/* ldap-scripts README.ldap-support README.mailserver
%{_mandir}/man*/*

%changelog
%autochangelog
