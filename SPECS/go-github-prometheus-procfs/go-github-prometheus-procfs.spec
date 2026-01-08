# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           procfs
%define go_import_path  github.com/prometheus/procfs

Name:           go-github-prometheus-procfs
Version:        0.19.2
Release:        %autorelease
Summary:        procfs provides functions to retrieve system, kernel and process metrics from the pseudo-filesystem proc.
License:        Apache-2.0
URL:            https://github.com/prometheus/procfs
#!RemoteAsset
Source0:        https://github.com/prometheus/procfs/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# https://sources.debian.org/src/golang-github-prometheus-procfs/0.19.2-1/debian/patches/0001-Fix-testdata-paths.patch
Patch0:         2000-Fix-testdata-paths.patch

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sys)

Provides:       go(github.com/prometheus/procfs) = %{version}

Requires:       go(github.com/google/go-cmp)
Requires:       go(golang.org/x/sync)
Requires:       go(golang.org/x/sys)

%description
This package provides functions to retrieve system, kernel, and process
metrics from the pseudo-filesystems /proc and /sys.

# This module have a specific testdata
%check
%{go_common}
%__mkdir -p %{_builddir}/go/src/%{go_import_path}
%__cp -a . %{_builddir}/go/src/%{go_import_path}
# Extract testdata
cd %{_builddir}/go/src/%{go_import_path}
./ttar -C %{_builddir}/go/src/%{go_import_path}/testdata \
    -x -f testdata/fixtures.ttar
%__go test -v ./...

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%{?autochangelog}
