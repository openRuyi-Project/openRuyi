# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           gzip
Version:        1.14
Release:        %autorelease
Summary:        GNU Zip Compression Utilities
License:        GPL-3.0-or-later
URL:            https://www.gnu.org/software/gzip/
VCS:            git:https://https.git.savannah.gnu.org/git/gzip.git
#!RemoteAsset
Source:         https://ftpmirror.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz
#!RemoteAsset
Source2:        https://ftpmirror.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz.sig
BuildSystem:    autotools

Patch0:         manpage-no-date.patch

# avoid build require "less"
BuildOption(conf):  ac_cv_prog_LESS="less"
BuildOption(check):  XFAIL_TESTS=help-version

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  texinfo

%description
Gzip reduces the size of the named files using Lempel-Ziv coding LZ77.
Whenever possible, each file is replaced by one with the extension .gz,
while keeping the same ownership modes and access and modification
times.

%files
%license COPYING
%doc README AUTHORS ChangeLog TODO NEWS THANKS
%{_bindir}/gunzip
%{_bindir}/gzexe
%{_bindir}/gzip
%{_bindir}/uncompress
%{_bindir}/zcat
%{_bindir}/zcmp
%{_bindir}/zdiff
%{_bindir}/zegrep
%{_bindir}/zfgrep
%{_bindir}/zforce
%{_bindir}/zgrep
%{_bindir}/zless
%{_bindir}/zmore
%{_bindir}/znew
%{_infodir}/gzip.info*
%{_mandir}/man1/gunzip.1*
%{_mandir}/man1/gzexe.1*
%{_mandir}/man1/gzip.1*
%{_mandir}/man1/zcat.1*
%{_mandir}/man1/zcmp.1*
%{_mandir}/man1/zdiff.1*
%{_mandir}/man1/zforce.1*
%{_mandir}/man1/zgrep.1*
%{_mandir}/man1/zless.1*
%{_mandir}/man1/zmore.1*
%{_mandir}/man1/znew.1*

%changelog
%autochangelog
