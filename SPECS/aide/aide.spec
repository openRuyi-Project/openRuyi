# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
# SPDX-FileContributor: BH1SCW <kongfanjun@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond selinux 1

Name:           aide
Version:        0.19.3
Release:        %autorelease
Summary:        Intrusion detection environment
License:        GPL-2.0-or-later
URL:            https://github.com/aide/aide
#!RemoteAsset:  sha256:6513170bb5b8c22802dd1b72f02d8aa9f432aef2b4470522db03e755212a3f47
Source0:        https://github.com/aide/aide/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        aide.conf
Source2:        README.quickstart
Source3:        aide.logrotate

BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  --with-config_file=%{_sysconfdir}/aide.conf
BuildOption(conf):  --without-gcrypt
BuildOption(conf):  --with-nettle
BuildOption(conf):  --with-zlib
BuildOption(conf):  --with-curl
BuildOption(conf):  --with-posix-acl
%if %{with selinux}
BuildOption(conf):  --with-selinux
%else
BuildOption(conf):  --without-selinux
%endif
BuildOption(conf):  --with-xattr
BuildOption(conf):  --with-e2fsattrs
BuildOption(conf):  --with-audit
BuildOption(install):  bindir=%{_sbindir}

BuildRequires:  make
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  pkgconfig(libpcre2-posix)
BuildRequires:  pkgconfig(gpg-error)
BuildRequires:  pkgconfig(nettle)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libacl)
%if %{with selinux}
BuildRequires:  pkgconfig(libselinux)
%endif
BuildRequires:  pkgconfig(libattr)
BuildRequires:  pkgconfig(e2p)
BuildRequires:  pkgconfig(audit)
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig(check)

Recommends:     logrotate

%description
AIDE (Advanced Intrusion Detection Environment) is a file integrity
checker and intrusion detection program.

%prep
%autosetup -p1
cp -a %{SOURCE2} .

%install -a
install -Dpm0644 -t %{buildroot}%{_sysconfdir} %{SOURCE1}
install -Dpm0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/logrotate.d/aide
mkdir -p %{buildroot}%{_localstatedir}/log/aide
mkdir -p -m0700 %{buildroot}%{_localstatedir}/lib/aide

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%doc README.quickstart
%{_sbindir}/aide
%{_mandir}/man1/*.1*
%{_mandir}/man5/*.5*
%config(noreplace) %attr(0600,root,root) %{_sysconfdir}/aide.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/aide
%dir %attr(0700,root,root) %{_localstatedir}/lib/aide
%dir %attr(0700,root,root) %{_localstatedir}/log/aide

%changelog
%autochangelog
