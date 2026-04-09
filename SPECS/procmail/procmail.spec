# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: Bo YU <yubo@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           procmail
Summary:        Mail processing program
Version:        3.24
Release:        %autorelease
License:        Artistic-1.0 OR GPL-2.0-or-later
URL:            https://github.com/BuGlessRB/procmail
#!RemoteAsset:  sha256:514ea433339783e95df9321e794771e4887b9823ac55fdb2469702cf69bd3989
Source0:        https://github.com/BuGlessRB/procmail/archive/v%{version}/procmail-%{version}.tar.gz
BuildSystem:    autotools

# Fix issue from coverity scan, the patch from fedora:
# https://src.fedoraproject.org/rpms/procmail/blob/rawhide/f/procmail-3.24-coverity-scan-fixes.patch
Patch0:         1000-procmail-3.24-coverity-scan-fixes.patch
# Fix gcc-14 build issue
Patch1:         1001-procmail-3.24-gcc-14-fix.patch
# Update some API to support ipv6
Patch2:         1002-procmail-3.24-ipv6.patch
# Reset some config for system
Patch3:         1003-procmail-3.24-rhconfig.patch
#
Patch4:         2000-procmail-3.15.1-man.patch
# Fix a race condition issue related to file truncation
Patch5:         2001-procmail-3.22-truncate.patch

BuildOption(build):  RPM_OPT_FLAGS="$RPM_OPT_FLAGS -Wno-comments  -std=gnu89"
BuildOption(install):  BASENAME=${RPM_BUILD_ROOT}%{_prefix}
BuildOption(install):  MANDIR=${RPM_BUILD_ROOT}%{_mandir}

BuildRequires:  make
BuildRequires:  gcc

%description
Procmail can be used to create mail-servers, mailing lists, sort your
incoming mail into separate folders/files (real convenient when subscribing
to one or more mailing lists or for prioritising your mail), preprocess
your mail, start any programs upon mail arrival (e.g. to generate different
chimes on your workstation for different types of mail) or selectively
forward certain incoming mail automatically to someone.

%conf
find examples -type f | xargs chmod 644

# no check
%check

%files
%doc Artistic COPYING FAQ FEATURES HISTORY README KNOWN_BUGS examples

%{_bindir}/formail
%attr(2755,root,mail) %{_bindir}/lockfile
%{_bindir}/mailstat
%attr(0755,root,mail) %{_bindir}/procmail

%{_mandir}/man[15]/*

%changelog
%autochangelog
