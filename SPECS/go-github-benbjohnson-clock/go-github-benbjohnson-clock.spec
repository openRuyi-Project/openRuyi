# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           clock
%define go_import_path  github.com/benbjohnson/clock

Name:           go-github-benbjohnson-clock
Version:        1.3.5
Release:        %autorelease
Summary:        Mockable clock library for Go
License:        MIT
URL:            https://github.com/benbjohnson/clock
#!RemoteAsset:  sha256:d26928c5301d8f7feedebeda0506599fa8c9aeb0b724de619b9d468df441a33c
Source0:        https://github.com/benbjohnson/clock/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
Clock wraps Go's time package with interchangeable real and mock clock
implementations for deterministic testing.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
