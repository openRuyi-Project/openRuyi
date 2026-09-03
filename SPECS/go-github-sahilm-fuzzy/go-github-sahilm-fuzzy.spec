# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           fuzzy
%define go_import_path  github.com/sahilm/fuzzy

Name:           go-github-sahilm-fuzzy
Version:        0.1.2
Release:        %autorelease
Summary:        Go library that provides fuzzy string matching optimized for filenames and code symbols in the style of Sublime Text, VSCode, IntelliJ IDEA et al.
License:        MIT
URL:            https://github.com/sahilm/fuzzy
#!RemoteAsset:  sha256:28f93f07f4f85ee29375623be4d148da2f5a64523b8fb1c01a93943162925e7f
Source0:        https://github.com/sahilm/fuzzy/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/kylelemons/godebug)

Provides:       go(github.com/sahilm/fuzzy) = %{version}

Requires:       go(github.com/kylelemons/godebug)

%description
fuzzy provides fast fuzzy string matching optimized for filenames and code symbols.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
