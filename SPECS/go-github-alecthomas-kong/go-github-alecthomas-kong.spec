# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           kong
%define go_import_path  github.com/alecthomas/kong

Name:           go-github-alecthomas-kong
Version:        1.13.0
Release:        %autorelease
Summary:        Kong is a command-line parser for Go
License:        MIT
URL:            https://github.com/alecthomas/kong
#!RemoteAsset
Source0:        https://github.com/alecthomas/kong/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/alecthomas/assert)
BuildRequires:  go(github.com/alecthomas/repr)

Provides:       go(github.com/alecthomas/kong) = %{version}

Requires:       go(github.com/alecthomas/assert)
Requires:       go(github.com/alecthomas/repr)

%description
Kong aims to support arbitrarily complex command-line structures with as
little developer effort as possible.

To achieve that, command-lines are expressed as Go types, with the
structure and tags directing how the command line is mapped onto the
struct.

%files
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
