# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           check
%define go_import_path  launchpad.net/gocheck
%define commit_id       eb6ee6f84d0a848c7f11b46cd11f28875ba56b1c

Name:           go-launchpad-gocheck
Version:        0+git20261023.eb6ee6f
Release:        %autorelease
Summary:        Historical GoCheck testing framework for Go
License:        BSD-2-Clause
URL:            https://github.com/go-check/check
#!RemoteAsset:  sha256:9ea90eb40a28790562d8461819579cf2ea469994b3e1dbd2ee34ac39904adb8c
Source0:        https://github.com/go-check/check/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Accept Go's gopanic name while retaining the fixture stack assertions.
# https://github.com/go-check/check/commit/119e1995736229ab5aac58c264de9d173b384792
Patch1000:      1000-accept-modern-panic-function-name.patch
# Check benchmark output without assuming scheduler timing or iteration counts.
# https://github.com/go-check/check/commit/822ff90e51871de6e9ffe102e1be8627b597fca8
Patch1001:      1001-fix-erratic-benchmark-tests.patch
# Accept valid throughput below 1 MB/s on slower build workers.
# https://github.com/go-check/check/commit/3e22adfe2c10bbb92cf3b317e92ee2d7f52c5305
Patch1002:      1002-allow-sub-megabyte-benchmark-throughput.patch

BuildOption(prep):  -n %{_name}-%{commit_id}
# The historical error logger uses a dynamic printf format rejected by current vet.
# Keep every upstream test enabled while checking this legacy import path.
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
The historical GoCheck API provides rich assertions, suites, fixtures, and
benchmarks at its original launchpad.net/gocheck import path. This package
retains the complete source and tests of the legacy snapshot.

%files
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
