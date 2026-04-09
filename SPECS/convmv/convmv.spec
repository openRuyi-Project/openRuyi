# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global _test_target test

Name:           convmv
Version:        2.06
Release:        %autorelease
Summary:        Convert filename encodings
License:        GPL-2.0-only OR GPL-3.0-only
URL:            http://j3e.de/linux/convmv
VCS:            git:https://git.altlinux.org/gears/c/convmv.git
#!RemoteAsset
Source0:        https://j3e.de/linux/convmv/convmv-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(install):  PREFIX=%{_prefix}
BuildOption(install):  DESTDIR=%{buildroot}

BuildRequires:  make

%description
convmv converts filenames from one encoding to another, such as
from Latin1 to UTF-8.

# No configure.
%conf

%files
%doc CREDITS Changes TODO
%license GPL2
%{_bindir}/convmv
%{_mandir}/man1/*

%changelog
%autochangelog
