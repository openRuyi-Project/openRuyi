# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           grep
Version:        3.12
Release:        %autorelease
Summary:        Print lines matching a pattern
License:        GPL-3.0-or-later
URL:            https://www.gnu.org/software/grep/
VCS:            git:https://https.git.savannah.gnu.org/git/grep.git
#!RemoteAsset
Source0:        https://ftpmirror.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz
#!RemoteAsset
Source2:        https://ftpmirror.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz.sig
Buildsystem:    autotools

BuildOption(conf):  --disable-silent-rules
BuildOption(conf):  CONFIG_SHELL=/bin/sh

BuildRequires:  glibc-locale
BuildRequires:  texinfo
BuildRequires:  pkgconfig(libpcre2-8)

Provides:       base:%{_bindir}/grep

%install -a
%find_lang %{name} --generate-subpackages

%description
The grep command searches one or more input files for lines containing a
match to a specified pattern.  By default, grep prints the matching lines.

%files
%license COPYING
%doc README AUTHORS NEWS THANKS TODO ChangeLog*
%{_bindir}/egrep
%{_bindir}/fgrep
%{_bindir}/grep
%{_mandir}/man1/grep.1%{?ext_man}
%{_infodir}/grep.info%{?ext_info}

%changelog
%autochangelog
