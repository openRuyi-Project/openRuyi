# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           speed
%define go_import_path  github.com/performancecopilot/speed/v4

Name:           go-github-performancecopilot-speed-v4
Version:        4.0.0
Release:        %autorelease
Summary:        Performance Co-Pilot instrumentation API for Go
License:        MIT
URL:            https://github.com/performancecopilot/speed
#!RemoteAsset:  sha256:85efceddf3203d910403c91a807d3609accc98f952d5a87843709c6b63ae2c8f
Source0:        https://github.com/performancecopilot/speed/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/HdrHistogram/hdrhistogram-go)
BuildRequires:  go(github.com/edsrzf/mmap-go)
BuildRequires:  go(github.com/pkg/errors)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/HdrHistogram/hdrhistogram-go)
Requires:       go(github.com/edsrzf/mmap-go)
Requires:       go(github.com/pkg/errors)

%description
Speed provides Go bindings for the Performance Co-Pilot instrumentation API.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
