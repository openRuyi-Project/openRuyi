# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           zeroconfig
%define go_import_path  go.mau.fi/zeroconfig

Name:           go-go-mau-zeroconfig
Version:        0.2.0
Release:        %autorelease
Summary:        Declarative configuration for zerolog
License:        MPL-2.0
URL:            https://github.com/tulir/zeroconfig
#!RemoteAsset:  sha256:98b24521525572ee1236c59575de8c5c315b7cc8bd72df14b391dc0ffbd2ea85
Source0:        https://github.com/tulir/zeroconfig/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/rs/zerolog)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(gopkg.in/natefinch/lumberjack.v2)

Provides:       go(go.mau.fi/zeroconfig) = %{version}

Requires:       go(github.com/rs/zerolog)
Requires:       go(gopkg.in/natefinch/lumberjack.v2)

%description
Declarative YAML and JSON configuration for zerolog writers, formatting,
log levels and metadata.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
