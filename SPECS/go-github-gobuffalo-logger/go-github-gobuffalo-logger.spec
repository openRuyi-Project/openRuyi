# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           logger
%define go_import_path  github.com/gobuffalo/logger

Name:           go-github-gobuffalo-logger
Version:        1.0.1
Release:        %autorelease
Summary:        Logging helpers for Go applications
License:        MIT
URL:            https://github.com/gobuffalo/logger
#!RemoteAsset:  sha256:3d4c15d73f9cb709a33afaf2b38d212125188768ac8178f34bb8ff295abc4086
Source0:        https://github.com/gobuffalo/logger/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/gobuffalo/envy)
BuildRequires:  go(github.com/sirupsen/logrus)
BuildRequires:  go(golang.org/x/crypto)

Provides:       go(github.com/gobuffalo/logger) = %{version}

Requires:       go(github.com/gobuffalo/envy)
Requires:       go(github.com/sirupsen/logrus)
Requires:       go(golang.org/x/crypto)

%description
Logging helpers for Go applications.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
