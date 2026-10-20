# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           lfshook
%define go_import_path  github.com/rifflock/lfshook

Name:           go-github-rifflock-lfshook
Version:        2.4
Release:        %autorelease
Summary:        Local filesystem hook for Logrus
License:        MIT
URL:            https://github.com/rifflock/lfshook
#!RemoteAsset:  sha256:162e3cae02d91f7e0f8372900edc625d6fb3cf3419a8f293a51130016d83a690
Source0:        https://github.com/rifflock/lfshook/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/sirupsen/logrus)

Provides:       go(github.com/rifflock/lfshook) = %{version}

Requires:       go(github.com/sirupsen/logrus)

%description
lfshook writes Logrus events to local files or custom writers, with configurable
log levels and formatting.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
