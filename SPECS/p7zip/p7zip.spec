# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           p7zip
Version:        17.06
Release:        %autorelease
Summary:        7z file archiver for Linux systems
License:        LGPL-2.1-or-later and (LGPL-2.1-or-later or CPL-1.0)
URL:            https://github.com/p7zip-project/p7zip
#!RemoteAsset:  sha256:c35640020e8f044b425d9c18e1808ff9206dc7caf77c9720f57eb0849d714cd1
Source0:        https://github.com/p7zip-project/p7zip/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(build):  OPTFLAGS="%{optflags}" LDFLAGS="%{build_ldflags}"
BuildOption(install):  DEST_DIR="%{buildroot}"
BuildOption(install):  DEST_HOME="%{_prefix}"
BuildOption(install):  DEST_SHARE=%{_libdir}/p7zip
BuildOption(install):  DEST_MAN="%{_mandir}"

BuildRequires:      gcc-c++

%description
7za is a file archiver with a high compression ratio for Linux systems.

# No configure
%conf

%files
%license DOC/License.txt
%doc README
%doc %{_docdir}/%{name}/
%{_bindir}/*
%{_mandir}/man1/*

%changelog
%{?autochangelog}
