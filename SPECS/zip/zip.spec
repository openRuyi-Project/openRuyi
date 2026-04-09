# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: ayostl <yao_xp@yeah.net>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           zip
Version:        3.0
Release:        %autorelease
Summary:        A file compression and packaging utility compatible with PKZIP
License:        Info-ZIP
URL:            http://www.info-zip.org/Zip.html
# VCS: No VCS link available
#!RemoteAsset
Source0:        http://downloads.sourceforge.net/infozip/zip30.tar.gz
BuildSystem:    autotools

# all patch get from fedora
# This patch will probably be merged to zip 3.1
# http://www.info-zip.org/board/board.pl?m-1249408491/
Patch0:         0001-zip-3.0-exec-shield.patch
# Not upstreamed.
Patch1:         0002-zip-3.0-currdir.patch
# Not upstreamed.
Patch2:         0003-zip-3.0-time.patch
Patch3:         0004-man.patch
Patch4:         0005-zip-3.0-format-security.patch
Patch5:         0006-zipnote.patch
Patch6:         0007-zip-gnu89-build.patch
Patch7:         0008-buffer_overflow.patch
Patch8:         0009-zip-3.0-man-strip-extra.patch

BuildOption(build):  -f unix/Makefile
BuildOption(build):  prefix=%{_prefix}
BuildOption(build):  "CFLAGS_NOOPT=-I. -DUNIX $RPM_OPT_FLAGS"
BuildOption(build):  generic_gcc
BuildOption(install):  -f unix/Makefile
BuildOption(install):  prefix=$RPM_BUILD_ROOT%{_prefix}
BuildOption(install):  MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1

BuildRequires:  make
BuildRequires:  bzip2-devel
BuildRequires:  gcc

Requires:       unzip

%description
The zip program is a compression and file packaging utility.  Zip is
analogous to a combination of the UNIX tar and compress commands and
is compatible with PKZIP (a compression and file packaging utility for
MS-DOS systems).

Install the zip package if you need to compress files using the zip
program.

%conf

%install -p
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BULD_ROOT%{_mandir}/man1

# no tests
%check

%files
%license LICENSE
%doc README CHANGES TODO WHATSNEW WHERE README.CR
%doc proginfo/algorith.txt
%{_bindir}/zipnote
%{_bindir}/zipsplit
%{_bindir}/zip
%{_bindir}/zipcloak
%{_mandir}/man1/zip.1*
%{_mandir}/man1/zipcloak.1*
%{_mandir}/man1/zipnote.1*
%{_mandir}/man1/zipsplit.1*

%changelog
%autochangelog
