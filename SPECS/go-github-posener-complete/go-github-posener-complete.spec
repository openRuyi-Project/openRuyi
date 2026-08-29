# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: tangyihong <yihong.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           complete
%define go_import_path  github.com/posener/complete

# Some tests exercise shell completion against the real environment, which the
# isolated build sandbox restricts; run them but tolerate the failures.
%define go_test_ignore_failure 1

Name:           go-github-posener-complete
Version:        1.2.3
Release:        %autorelease
Summary:        Bash completion written in and for Go programs
License:        MIT
URL:            https://github.com/posener/complete
#!RemoteAsset:  sha256:2ea9ccea70aae01118c8ffeb608aa57a894c2917cbdd3332a89edeba47241018
Source0:        https://github.com/posener/complete/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/hashicorp/go-multierror)
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/posener/complete) = %{version}

Requires:       go(github.com/hashicorp/go-multierror)

%description
complete provides shell command-line completion for Go programs, allowing a
program to act as its own bash/zsh completion handler. It is used by
mitchellh/cli (and thus the hashicorp/serf agent CLI).

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
