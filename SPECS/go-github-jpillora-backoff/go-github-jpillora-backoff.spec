# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           backoff
%define go_import_path  github.com/jpillora/backoff

Name:           go-github-jpillora-backoff
Version:        1.0.0
Release:        %autorelease
Summary:        Simple backoff algorithm in Go (golang)
License:        MIT
URL:            https://github.com/jpillora/backoff
#!RemoteAsset
Source0:        https://github.com/jpillora/backoff/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/jpillora/backoff) = %{version}

%description
This package is a simple exponential backoff counter in Go (Golang)

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
