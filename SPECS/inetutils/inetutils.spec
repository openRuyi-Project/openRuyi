# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           inetutils
Version:        2.7
Release:        %autorelease
Summary:        GNU network utilities
License:        GPL-3.0-or-later
URL:            https://www.gnu.org/software/inetutils
VCS:            git:https://codeberg.org/inetutils/inetutils.git
#!RemoteAsset
Source0:        https://ftpmirror.gnu.org/gnu/inetutils/inetutils-v%{version}-src.tar.gz
BuildSystem:    autotools

# CVE-2026-24061: https://codeberg.org/inetutils/inetutils/commit/fd702c02497b2f398e739e3119bed0b23dd7aa7b
Patch0:         0001-fix-injection-bug-with-bogus-user-names.patch
# CVE-2026-24061: https://codeberg.org/inetutils/inetutils/commit/ccba9f748aa8d50a38d7748e2e60362edd6a32cc
Patch1:         0002-sanitize-all-variable-expansions.patch
# CVE-2026-28372: https://codeberg.org/inetutils/inetutils/commit/4db2f19f4caac03c7f4da6363c140bd70df31386
Patch2:         0003-telnetd-don-t-allow-systemd-service-credentials.patch
# CVE-2026-24061: https://codeberg.org/inetutils/inetutils/commit/81d436d26d5497423e28841af91756e373446cf4
Patch3:         0004-telnetd-add-the-new-accept-env-option.patch
# CVE-2026-32746: https://codeberg.org/inetutils/inetutils/commit/6864598a29b652a6b69a958f5cd1318aa2b258af
Patch4:         0005-telnetd-fix-stack-buffer-overflow-processing-SLC-sub.patch
# https://codeberg.org/inetutils/inetutils/pulls/9
Patch5:         0006-tests-Remove-bogus-test-for-unsorted-file-listing.patch

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
