# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           rsync
Version:        3.4.1
Release:        %autorelease
Summary:        Fast and versatile file copying tool for remote and local files
License:        GPL-3.0-or-later
URL:            https://rsync.samba.org/
#!RemoteAsset
Source0:        https://rsync.samba.org/ftp/rsync/src/rsync-%{version}.tar.gz
Source1:        rsyncd.conf
BuildSystem:    autotools

BuildOption(conf):  --enable-ipv6
BuildOption(conf):  --disable-debug
BuildOption(conf):  --with-included-popt=no
BuildOption(conf):  --with-included-zlib=no
BuildOption(conf):  --enable-acl-support
BuildOption(conf):  --enable-xattr-support
BuildOption(conf):  --enable-openssl
BuildOption(conf):  --enable-lz4
BuildOption(conf):  --enable-zstd

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  python3
BuildRequires:  pkgconfig(libacl)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(popt)
BuildRequires:  pkgconfig(libxxhash)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(openssl)

Requires:       acl
Requires:       lz4
Requires:       openssl
Requires:       popt
Requires:       xxhash
Requires:       zlib
Requires:       zstd

%description
Rsync is a fast and extraordinarily versatile file copying tool. It is famous
for its delta-transfer algorithm, which reduces the amount of data sent over
the network. This package provides the `rsync` client utility.

%package        daemon
Summary:        The rsync daemon for serving files
Requires:       %{name}%{?_isa} = %{version}-%{release}
%{?systemd_requires}

%description    daemon
This package contains the `rsyncd` daemon and the necessary systemd units
to run this machine as an rsync server.

%install -a
# Install systemd units directly from the source tree
install -Dm644 packaging/systemd/rsync.service %{buildroot}%{_unitdir}/rsync.service
install -Dm644 packaging/systemd/rsync.socket %{buildroot}%{_unitdir}/rsync.socket
install -Dm644 packaging/systemd/rsync@.service %{buildroot}%{_unitdir}/rsync@.service
# Install the default rsyncd.conf
install -Dm644 %{SOURCE1} %{buildroot}%{_sysconfdir}/rsyncd.conf

# Systemd scriptlets belong to the -daemon package.
%systemd_post daemon rsync.service
%systemd_preun daemon rsync.service
%systemd_postun daemon rsync.service

%files
%license COPYING
%doc README.md NEWS.md tech_report.tex support/
%{_bindir}/rsync
%{_bindir}/rsync-ssl
%{_mandir}/man1/rsync.1.gz
%{_mandir}/man5/rsyncd.conf.5.gz
%{_mandir}/man1/rsync-ssl.1.gz

%files daemon
%config(noreplace) %{_sysconfdir}/rsyncd.conf
%{_unitdir}/rsync.service
%{_unitdir}/rsync.socket
%{_unitdir}/rsync@.service

%changelog
%{?autochangelog}
