# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# ##############################################################################
# WARNING: DO NOT UPGRADE THIS PACKAGE BEYOND VERSION 7.92
# ##############################################################################
# 1. LICENSE CHANGE: Nmap ≥7.93 is licensed ONLY under the NPSL (Nmap Public
#    Source License), which is considered "Non-Free" by Fedora, openSUSE, and
#    some other FOSS distributions due to its custom terms and restrictive
#    clauses for commercial/SaaS use.
#
# 2. THE 7.92 EXCEPTION: Version 7.92 is the LAST release offering a dual-license
#    choice:
#      - GPL-2.0-only WITH Nmap-exception (based on v7.80 terms)
#      - NPSL (Nmap Public Source License)
#
# 3. COMPLIANCE REQUIREMENT: To meet open-source distribution policies and
#    legal standards (e.g., openRuyi, OSI/FSF guidelines), this package MUST
#    remain at 7.92. Do not upgrade unless the Nmap Project adopts an
#    OSI/FSF-approved license in the future.
# ##############################################################################

Name:           nmap
Version:        7.92
Release:        %autorelease
Summary:        Network exploration tool and security scanner
# Nmap 7.92 is dual-licensed: users may choose either the traditional
# GPL-2.0-only with Nmap-specific exceptions, or the newer Nmap Public
# Source License (NPSL). See https://nmap.org/npsl/ for details.
License:        LicenseRef-GPL-2.0-with-Nmap-Exception
URL:            https://nmap.org
VCS:            git:https://github.com/nmap/nmap
#!RemoteAsset
Source0:        https://nmap.org/dist/%{name}-%{version}.tar.bz2
#!RemoteAsset
Source1:        https://nmap.org/dist/sigs/%{name}-%{version}.tar.bz2.asc
BuildSystem:    autotools

BuildOption(conf):  --with-libpcap=yes
BuildOption(conf):  --with-liblua=included
BuildOption(conf):  --without-zenmap
BuildOption(conf):  --without-ndiff
BuildOption(conf):  --enable-dbus
BuildOption(conf):  --with-libssh2=yes
BuildOption(install):  DESTDIR=%{buildroot}
BuildOption(install):  STRIP=true

BuildRequires:  automake
BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  pkgconfig(libpcap)
BuildRequires:  pkgconfig(libssh2)
BuildRequires:  libtool
BuildRequires:  pkgconfig(lua)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(libpcre2-posix)

Provides:       nmap-frontend
Provides:       nmap-ndiff
Provides:       nmap-ncat
Provides:       nc
Provides:       nc6

%patchlist
#prevent possible race condition for shtool, rhbz#158996
nmap-4.03-mktemp.patch
#don't suggest to scan microsoft
nmap-4.52-noms.patch
# upstream provided patch for rhbz#845005, not yet in upstream repository
ncat_reg_stdin.diff
# https://github.com/nmap/nmap/pull/2247
nmap_resolve_config.patch
# backport of upstream pcre2 migration, rhbz#2128336
nmap-pcre2.patch
# https://github.com/nmap/nmap/pull/2724
nmap-ems-ssl-enum-ciphers.patch
# Fix build with libpcap 1.10.5
nmap-libpcap.patch

%description
Nmap ("Network Mapper") is a utility for network exploration or security
auditing. It supports ping scanning (determine which hosts are up), many
port scanning techniques (determine what services the hosts are offering),
and TCP/IP fingerprinting (remote host operating system identification).
Nmap also offers flexible target and port specification, decoy scanning,
determination of TCP sequence predictability characteristics, reverse-identd
scanning, and more. In addition to the classic command-line nmap executable,
the Nmap suite includes a flexible data transfer, redirection, and debugging
tool (netcat utility ncat), a utility for comparing scan results (ndiff),
and a packet generation and response analysis tool (nping).

%prep -a
rm -rf libpcap libpcre macosx mswin32 libssh2 libz

#fix pt_PT/pt zh/zh_CN locale
sed -i '/ALL_LINGUAS =/s/zh/zh_CN/' Makefile.in
mv docs/man-xlate/nmap-zh.1 docs/man-xlate/nmap-zh_CN.1

%conf -p
export CFLAGS="%{optflags} -fno-strict-aliasing"
export CXXFLAGS="%{optflags} -fno-strict-aliasing"

%install -a
rm -f %{buildroot}%{_datadir}/ncat/ca-bundle.crt
rmdir %{buildroot}%{_datadir}/ncat

ln -s ncat.1.gz %{buildroot}%{_mandir}/man1/nc.1.gz
ln -s ncat %{buildroot}%{_bindir}/nc

%find_lang %{name} --with-man --generate-subpackages

# No check
%check

%files
%license LICENSE
%doc docs/README docs/nmap.usage.txt
%{_bindir}/*
%{_datadir}/nmap
%{_mandir}/man1/*.1.gz

%changelog
%autochangelog
