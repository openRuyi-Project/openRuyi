# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           indent
Version:        2.2.13
Release:        %autorelease
Summary:        A GNU program for formatting C code
License:        GPL-3.0-or-later AND BSD-3-Clause AND BSD-4.3TAHOE AND Latex2e-translated-notice
URL:            https://www.gnu.org/software/indent/
VCS:            git:https://git.savannah.gnu.org/git/indent.git/
#!RemoteAsset:  sha256:1b81ba4e9a006ca8e6eb5cbbe4cf4f75dfc1fc9301b459aa0d40393e85590a0b
Source0:        https://ftpmirror.gnu.org/indent/indent-%{version}.tar.xz
BuildSystem:    autotools

# Check for setlocale() at configure time, proposed to an upstream,
# <https://lists.gnu.org/archive/html/bug-indent/2023-04/msg00001.html>.
Patch0:         0001-indent-2.2.13-Check-for-setlocale-function.patch
# Fix a heap overread in search_brace/lexi, in upstream after 2.2.13,
# <https://savannah.gnu.org/bugs/index.php?64503>
Patch1:         0002-indent-2.2.13-Fix-an-out-of-buffer-read-in-search_brace-lexi-on-an.patch
# Fix CVE-2023-40305 (a heap buffer overwrite in search_brace), bug #2231919,
# in upstream after 2.2.13, <https://savannah.gnu.org/bugs/index.php?64503>
Patch2:         0003-indent-2.2.13-Fix-a-heap-buffer-overwrite-in-search_brace-CVE-2023.patch
# Fix CVE-2024-0911 (a heap buffer underread in set_buf_break()),
# bug #2259883, in upstream after 2.2.13,
# <https://lists.gnu.org/archive/html/bug-indent/2024-01/msg00000.html>
Patch3:         0004-indent-2.2.13-Fix-a-heap-buffer-underread-in-set_buf_break.patch

BuildOption(conf):  --enable-largefile
BuildOption(conf):  --enable-nls
BuildOption(conf):  --disable-rpath
BuildOption(build):  CC_FOR_BUILD=gcc

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  gperf
BuildRequires:  make
BuildRequires:  texinfo

%description
Indent is a GNU program for beautifying C code, so that it is easier to
read. Indent can also convert from one C writing style to a different
one.

%conf -p
autoreconf -fiv

%install -a
# remove the html doc as we keep man.
rm -f %{buildroot}%{_infodir}/dir \
      %{buildroot}%{_bindir}/texinfo2man \
      %{buildroot}%{_datadir}/doc/indent/indent.html

# TODO: fix the name error.
# Avoid illegal package names
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*@*
%find_lang %{name} --generate-subpackages

%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS README.md ChangeLog*
%{_bindir}/indent
%{_mandir}/man1/indent.*
%{_infodir}/indent.info*

%changelog
%autochangelog
