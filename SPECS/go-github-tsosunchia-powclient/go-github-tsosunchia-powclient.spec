# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           powclient
%define go_import_path  github.com/tsosunchia/powclient

Name:           go-github-tsosunchia-powclient
Version:        0.3.0
Release:        %autorelease
Summary:        Proof-of-work challenge client for Go
License:        GPL-3.0-only
URL:            https://github.com/tsosunchia/powclient
VCS:            git:https://github.com/tsosunchia/powclient
#!RemoteAsset:  sha256:a6145c64373e97a576df9aee4ab2cc399396cd17847f0b3b7dab86a03b393217
Source0:        https://github.com/tsosunchia/powclient/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/tsosunchia/powclient) = %{version}

%description
Powclient is a Go client library for solving proof-of-work challenges.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
