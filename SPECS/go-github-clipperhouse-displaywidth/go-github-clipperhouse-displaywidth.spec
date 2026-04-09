# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           displaywidth
%define go_import_path  github.com/clipperhouse/displaywidth
%global go_test_exclude_glob %{shrink:
    github.com/clipperhouse/displaywidth/comparison
    github.com/clipperhouse/displaywidth/internal/gen*
}

Name:           go-github-clipperhouse-displaywidth
Version:        0.6.2
Release:        %autorelease
Summary:        Measure the display column width of strings in Go
License:        MIT
URL:            https://github.com/clipperhouse/displaywidth
#!RemoteAsset
Source0:        https://github.com/clipperhouse/displaywidth/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/clipperhouse/stringish)
BuildRequires:  go(github.com/clipperhouse/uax29/v2)

Provides:       go(github.com/clipperhouse/displaywidth) = %{version}

Requires:       go(github.com/clipperhouse/stringish)
Requires:       go(github.com/clipperhouse/uax29/v2)

%description
A high-performance Go package for measuring the monospace display width
of strings, UTF-8 bytes, and runes.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
