# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           logger
%define go_import_path  github.com/google/logger

Name:           go-github-google-logger
Version:        1.1.2
Release:        %autorelease
Summary:        Offers simple cross platform logging for Windows and Linux
License:        Apache-2.0
URL:            https://github.com/google/logger
#!RemoteAsset:  sha256:f2dd33d817147ef93b77d285d40335e99e623152972cefef617906d8a5744a45
Source0:        https://github.com/google/logger/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/sys)

Provides:       go(github.com/google/logger) = %{version}

Requires:       go(golang.org/x/sys)

%description
Logger provides cross-platform logging to system logs and io.Writer targets.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
