# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           fuzzy
%define go_import_path  github.com/sahilm/fuzzy

Name:           go-github-sahilm-fuzzy
Version:        0.1.3
Release:        %autorelease
Summary:        Go library that provides fuzzy string matching optimized for filenames and code symbols in the style of Sublime Text, VSCode, IntelliJ IDEA et al.
License:        MIT
URL:            https://github.com/sahilm/fuzzy
#!RemoteAsset:  sha256:ee951dc268aea78126b04bbb6f283147c191883dc515a65e285d2841b74014ce
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
