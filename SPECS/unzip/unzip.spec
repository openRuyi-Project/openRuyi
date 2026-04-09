# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           unzip
Version:        6.0
Release:        %autorelease
Summary:        A utility for unpacking zip files
License:        Info-ZIP
URL:            https://infozip.sourceforge.net/UnZip.html
# VCS: No VCS link available
#!RemoteAsset
Source0:        https://downloads.sourceforge.net/infozip/unzip60.tar.gz
BuildSystem:    autotools

BuildOption(build):  -f unix/Makefile unzips CF_NOOPT="$RPM_OPT_FLAGS -std=gnu17"
BuildOption(install):  -f unix/Makefile prefix=$RPM_BUILD_ROOT%{_prefix} MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1
BuildOption(check):  -f unix/Makefile CF_NOOPT="$RPM_OPT_FLAGS -std=gnu17"

BuildRequires:  make

%patchlist
# Fix executable space protection patch, upstream plans to do this
0001-unzip-6.0-exec-shield.patch
# Fix close_outfile() no return value, upstream plans to do this
0002-unzip-6.0-close.patch
# http://www.info-zip.org/board/board.pl?m-1259575993/
0003-unzip-6.0-attribs-overflow.patch
# Initialize G.pInfo->symlink to 0
0004-unzip-6.0-symlink.patch
# downstream fix for "-Werror=format-security", upstream won't fix
0005-unzip-6.0-format-secure.patch
# Fix valgrind warning by zeroing extra_field if readbuf returns less than requested
0006-unzip-6.0-valgrind.patch
# Fix read_ux3_value call to pass pointers to z_uidgid elements instead of values
0007-unzip-6.0-x-option.patch
# Add check to prevent overflow when using STORED compression method
0008-unzip-6.0-overflow.patch
# Add length check for PKVMS extra field to prevent read overflow
0009-unzip-6.0-cve-2014-8139.patch
# Add check for eb_ucsize being zero to prevent a crash
0010-unzip-6.0-cve-2014-8140.patch
# Add bounds checks in getZip64Data to prevent buffer over-read
0011-unzip-6.0-cve-2014-8141.patch
# Increase cfactorstr buffer size to prevent overflow when formatting large compression method numbers
0012-unzip-6.0-overflow-long-fsize.patch
# Fix heap overflow and infinite loop when invalid input is given
0013-unzip-6.0-heap-overflow-infloop.patch
# support non-{latin,unicode} encoding
0014-unzip-6.0-alt-iconv-utf8.patch
0015-unzip-6.0-alt-iconv-utf8-print.patch
0016-Fix-CVE-2016-9844-rhbz-1404283.patch
# restore unix timestamp accurately
0017-unzip-6.0-timestamp.patch
# fix possible heap based stack overflow in passwd protected files
0018-unzip-6.0-cve-2018-1000035-heap-based-overflow.patch
# Use snprintf to prevent buffer overflow in list.c
0019-unzip-6.0-cve-2018-18384.patch
# covscan issues
0020-unzip-6.0-COVSCAN-fix-unterminated-string.patch
# Add zip bomb detection feature and related bug fixes
0021-unzip-zipbomb-part1.patch
0022-unzip-zipbomb-part2.patch
0023-unzip-zipbomb-part3.patch
0024-unzip-zipbomb-manpage.patch
0025-unzip-zipbomb-part4.patch
0026-unzip-zipbomb-part5.patch
0027-unzip-zipbomb-part6.patch
0028-unzip-zipbomb-part7.patch
0029-unzip-zipbomb-switch.patch

%description
The unzip utility is used to list, test, or extract files from a zip
archive.  Zip archives are commonly found on MS-DOS systems.  The zip
utility, included in the zip package, creates zip archives.  Zip and
unzip are both compatible with archives created by PKWARE(R)'s PKZIP
for MS-DOS, but the programs' options and default behaviors do differ
in some respects.

Install the unzip package if you need to list, test or extract files from
a zip archive.

# no configure
%conf

%build -p
export RPM_OPT_FLAGS="%{optflags} \
-D_GNU_SOURCE -DRCC_LAZY -DWILD_STOP_AT_DIR \
-DLARGE_FILE_SUPPORT -DUNICODE_SUPPORT \
-DUNICODE_WCHAR -DUTF8_MAYBE_NATIVE -DNO_LCHMOD \
-DNOMEMCPY -DDATE_FORMAT=DF_YMD \
-I. -fstack-protector -fno-strict-aliasing -fPIE"

%files
%license LICENSE COPYING.OLD
%doc README BUGS
%{_bindir}/*
%{_mandir}/*/*

%changelog
%autochangelog
