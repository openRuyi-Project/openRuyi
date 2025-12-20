# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           symlinks
Version:        1.4
Release:        %autorelease
Summary:        Scan or change symbolic links
License:        Copyright-Only
URL:            http://ibiblio.org/pub/Linux/utils/file/
#!RemoteAsset
Source0:        http://ibiblio.org/pub/Linux/utils/file/%{name}-%{version}.tar.gz
BuildSystem:    autotools
Patch0:         0001-fix-makefile.patch

BuildOption(build):  CFLAGS="%{optflags} %{build_ldflags}"
BuildOption(install):  PREFIX=%{_prefix}
BuildOption(install):  BINDIR=%{_bindir}
BuildOption(install):  MANDIR=%{_mandir}

BuildRequires:  gcc

%description
Scans directories for symbolic links, and identifies dangling,
relative, absolute, messy, and other_fs links.  Can optionally
change absolute links to relative within a given filesystem.

# No configure
%conf

%check
# No tests here.

%files
%{_bindir}/symlinks
%{_mandir}/man8/symlinks.8*

%changelog
%{?autochangelog}
