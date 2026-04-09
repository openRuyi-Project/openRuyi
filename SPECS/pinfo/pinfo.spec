# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           pinfo
Version:        0.6.13
Release:        %autorelease
Summary:        An info file and man page viewer
License:        GPL-2.0-only
URL:            https://github.com/baszoetekouw/pinfo
#!RemoteAsset
Source:         https://github.com/baszoetekouw/pinfo/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    autotools

Patch0:         0001-pinfo-0.6.9-infopath.patch
Patch1:         0002-pinfo-0.6.9-xdg.patch
Patch2:         0003-pinfo-0.6.10-man.patch
Patch3:         0004-pinfo-0.6.13-fnocommon.patch
Patch4:         0005-pinfo-0.6.13-gccwarn.patch
Patch5:         0006-pinfo-0.6.13-nogroup.patch
Patch6:         0007-pinfo-0.6.13-stringop-overflow.patch
Patch7:         0008-pinfo-configure-c99.patch

BuildOption(conf):  --without-readline

BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  texinfo

Requires:       xdg-utils

%description
Pinfo is an info file (or man page) viewer with a user interface
similar to the Lynx Web browser. It supports searching using regular
expressions and is based on the ncurses library.

%conf -p
./autogen.sh


%install -a
rm -f %{buildroot}%{_infodir}/dir
%find_lang %{name} --generate-subpackages

%files
%license COPYING
%doc AUTHORS NEWS README.md TECHSTUFF
%config(noreplace) %{_sysconfdir}/pinforc
%{_bindir}/pinfo
%{_infodir}/pinfo.info*
%{_mandir}/man1/pinfo.1*

%changelog
%autochangelog
