# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           asmfmt
%define go_import_path  github.com/klauspost/asmfmt

Name:           go-github-klauspost-asmfmt
Version:        1.3.2
Release:        %autorelease
Summary:        Go Assembler Formatter
License:        MIT
URL:            https://github.com/klauspost/asmfmt
#!RemoteAsset
Source0:        https://github.com/klauspost/asmfmt/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/klauspost/asmfmt) = %{version}

%description
This will format your assembler code in a similar way that gofmt formats
your Go code.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
