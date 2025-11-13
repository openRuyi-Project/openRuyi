# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           quota
Version:        4.10
Release:        %autorelease
Summary:        Linux Diskquota system as part of the Linux kernel
License:        GPL-2.0-only AND GPL-2.0-or-later
URL:            https://sourceforge.net/projects/linuxquota/
#!RemoteAsset
Source0:        https://downloads.sourceforge.net/linuxquota/%{name}-%{version}.tar.gz
Source1:    quota_nld.service
Source2:    quota_nld.sysconfig
Source3:    rpc-rquotad.service
Source4:    rpc-rquotad.sysconfig
Patch0:     quota-4.06-warnquota-configuration-tunes.patch
Patch1:     quota-4.03-Validate-upper-bound-of-RPC-port.patch

BuildSystem:    autotools
BuildOption(conf): --enable-bsd-behaviour
BuildOption(conf): --enable-ext2direct=yes
BuildOption(conf): --enable-ldapmail=yes
BuildOption(conf): --disable-libwrap
BuildOption(conf): --enable-netlink=yes
BuildOption(conf): --enable-nls
BuildOption(conf): --disable-rpath
BuildOption(conf): --enable-rpc=yes
BuildOption(conf): --enable-rpcsetquota=yes
BuildOption(conf): --disable-silent-rules
BuildOption(conf): --disable-xfs-roothack

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  coreutils
BuildRequires:  rpcgen
BuildRequires:  systemd
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  e2fsprogs
BuildRequires:  gettext-devel
BuildRequires:  openldap-devel
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(libnl-3.0) >= 3.1
BuildRequires:  pkgconfig(libnl-genl-3.0)
BuildRequires:  pkgconfig(libtirpc)
BuildRequires:  pkgconfig(com_err)
BuildRequires:  pkgconfig(ext2fs)
BuildRequires:  systemd-rpm-macros

Requires:       rpcbind
Requires:       libtirpc-devel

Requires(post):    systemd
Requires(preun):   systemd
Requires(postun):  systemd

%description
The quota package contains system administration tools for monitoring
and limiting user and or group disk usage per file system.

%package        devel
Summary:        Development files for quota RPC
License:        GPL-2.0-only
Requires:       quota%{?_isa}  = %{version}-%{release}

%description    devel
This package contains development header files for implementing disk quotas
on remote machines.

%package        help
Summary:        Additional documentation for disk quotas
Requires:       quota%{?_isa}  = %{version}-%{release}
BuildArch:      noarch

%description    help
This package contains additional documentation for disk quotas concept in
Linux/UNIX environment.

%conf -p
autoreconf -fi

%install -a
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
%license COPYING
%doc Changelog README.ldap-support README.mailserver
%{_bindir}/*
%{_sbindir}/*
%{_unitdir}/*.service
%config(noreplace) %{_sysconfdir}/*
%exclude %{_docdir}/%{name}

%files devel
%dir %{_includedir}/rpcsvc
%{_includedir}/rpcsvc/*

%files help
%doc doc/* ldap-scripts
%{_mandir}/man*/*

%changelog
%{?autochangelog}
