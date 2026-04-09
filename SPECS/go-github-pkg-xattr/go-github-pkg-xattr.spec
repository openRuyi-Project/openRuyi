# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           xattr
%define go_import_path  github.com/pkg/xattr

Name:           go-github-pkg-xattr
Version:        0.4.12
Release:        %autorelease
Summary:        Extended attribute support for Go (linux + darwin + freebsd)
License:        BSD-2-Clause
URL:            https://github.com/pkg/xattr
#!RemoteAsset
Source0:        https://github.com/pkg/xattr/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/sys)

Provides:       go(github.com/pkg/xattr) = %{version}

Requires:       go(golang.org/x/sys)

%description
Extended attribute support for Go (linux + darwin + freebsd + netbsd + solaris).

"Extended attributes are name:value pairs associated permanently with files and directories, similar to the environment strings associated with a process. An attribute may be defined or undefined. If it is defined, its value may be empty or non-empty."

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
