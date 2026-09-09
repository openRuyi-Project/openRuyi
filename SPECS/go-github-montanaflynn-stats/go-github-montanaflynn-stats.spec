# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           stats
%define go_import_path  github.com/montanaflynn/stats

Name:           go-github-montanaflynn-stats
Version:        0.7.1
Release:        %autorelease
Summary:        Statistical functions for Go
License:        MIT
URL:            https://github.com/montanaflynn/stats
#!RemoteAsset:  sha256:97e9258173992d3caee6f7d7ac175d559dfc086388ad6c65fde439b808e1b725
Source0:        https://github.com/montanaflynn/stats/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Fix format strings rejected by current Go vet.
Patch2000:      2000-fix-non-constant-format-strings.patch
# Preserve intermediate rounding on RISC-V (Go permits fused operations).
Patch2001:      2001-round-scaled-value-before-modf.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/montanaflynn/stats) = %{version}

%description
Statistical functions for Go, including descriptive statistics,
distributions, regression and hypothesis testing.

%prep -a
# Standalone examples each define main and cannot form a single Go package.
rm -rf examples

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
