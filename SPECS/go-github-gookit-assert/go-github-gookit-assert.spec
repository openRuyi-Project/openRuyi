# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           assert
%define go_import_path  github.com/gookit/assert

Name:           go-github-gookit-assert
Version:        0.1.1
Release:        %autorelease
Summary:        Provides some tool functions for use with the Go testing
License:        MIT
URL:            https://github.com/gookit/assert
#!RemoteAsset:  sha256:0645ceca7b5531e979d7063ebeac5df020a2bc82e077de1b3ccae4366ed33697
Source0:        https://github.com/gookit/assert/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/gookit/assert) = %{version}

%description
Package gookit/assert provides some of the commonly
used tool functions for assertions in Go unit tests.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
