# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           kingpin
%define go_import_path  github.com/alecthomas/kingpin/v2

Name:           go-github-alecthomas-kingpin-v2
Version:        2.4.0
Release:        %autorelease
Summary:        A Go (golang) command line and flag parser
License:        MIT
URL:            https://github.com/alecthomas/kingpin
#!RemoteAsset
Source0:        https://github.com/alecthomas/kingpin/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/alecthomas/units)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/xhit/go-str2duration/v2)

Provides:       go(github.com/alecthomas/kingpin/v2) = %{version}

Requires:       go(github.com/alecthomas/units)
Requires:       go(github.com/stretchr/testify)
Requires:       go(github.com/xhit/go-str2duration/v2)

%description
Kingpin is a fluent-style
(http://en.wikipedia.org/wiki/Fluent_interface), type-safe command-line
parser. It supports flags, nested commands, and positional arguments.

%files
%license COPYING
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
