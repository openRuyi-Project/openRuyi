# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           natural
%define go_import_path  github.com/maruel/natural

Name:           go-github-maruel-natural
Version:        1.3.0
Release:        %autorelease
Summary:        Natural sorting for Go
License:        Apache-2.0
URL:            https://github.com/maruel/natural
#!RemoteAsset:  sha256:b8943846d265b3ab8687bacfbecec29c6357313f57405dac62f7ffb4fb54b6a6
Source0:        https://github.com/maruel/natural/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/maruel/natural) = %{version}

%description
This package provides Natural sorting for Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
