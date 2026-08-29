# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           inetutils
Version:        2.8
Release:        %autorelease
Summary:        GNU network utilities
License:        GPL-3.0-or-later
URL:            https://www.gnu.org/software/inetutils
VCS:            git:https://codeberg.org/inetutils/inetutils.git
#!RemoteAsset:  sha256:a76bb668060c5d28266a4dcd533cbf48e9a2d2542d1be3e5372e4307d534cd5b
Source0:        https://ftpmirror.gnu.org/gnu/inetutils/inetutils-v%{version}-src.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-syslogd
BuildOption(conf):  --disable-dnsdomainname
BuildOption(conf):  --disable-ping
BuildOption(conf):  --disable-ftp
BuildOption(conf):  --disable-hostname
BuildOption(conf):  --disable-ping6
BuildOption(conf):  --disable-tftp
BuildOption(conf):  --disable-traceroute
BuildOption(conf):  --disable-whois
BuildOption(conf):  --disable-servers

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  make
BuildRequires:  m4
BuildRequires:  gettext
BuildRequires:  gnulib
BuildRequires:  help2man
BuildRequires:  bison

%description
Inetutils is a collection of common network programs.

%package        doc
Summary:        Documentation for GNU inetutils

%description    doc
Documentation (man pages and info) for GNU inetutils.

%prep -a
export GNULIB_SRCDIR=%{_datadir}/gnulib
./bootstrap --gen --no-git

%conf -p
autoreconf -fiv

%files
%license COPYING
%{_bindir}/ifconfig
%{_bindir}/logger
%{_bindir}/rcp
%{_bindir}/rexec
%{_bindir}/rlogin
%{_bindir}/rsh
%{_bindir}/telnet

%files doc
%{_mandir}/man1/*
%{_datadir}/info/inetutils.info.gz

%changelog
%autochangelog
