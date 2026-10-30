# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           wsl
%define wsl_v4_version   4.7.0
%define go_import_path  github.com/bombsimon/wsl/v5

Name:           go-github-bombsimon-wsl
Version:        5.9.0
Release:        %autorelease
Summary:        Whitespace and statement grouping analyzer for Go
License:        MIT
URL:            https://github.com/bombsimon/wsl
#!RemoteAsset:  sha256:39b97d874441ce419211924fb06c6ecada8699cff2d9b27838dadfff25a5752e
Source0:        https://github.com/bombsimon/wsl/archive/v%{version}.tar.gz
# v4 and v5 have different import paths and require different snapshots.
#!RemoteAsset:  sha256:3925dda778284722840d4f2cd658bfc3b7feee7d783065fb0999a567b9159223
Source1:        https://github.com/bombsimon/wsl/archive/v%{wsl_v4_version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go >= 1.26.0
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/stretchr/testify/assert)
BuildRequires:  go(github.com/stretchr/testify/require)
BuildRequires:  go(go.yaml.in/yaml/v3)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(golang.org/x/tools/go/analysis)
BuildRequires:  go(golang.org/x/tools/go/analysis/analysistest)
BuildRequires:  go(golang.org/x/tools/go/analysis/singlechecker)

# Export the source module roots and every installed Go package.
Provides:       go(github.com/bombsimon/wsl/v5) = %{version}
Provides:       go(github.com/bombsimon/wsl/v5/cmd/golangci-lint-migrate) = %{version}
Provides:       go(github.com/bombsimon/wsl/v5/cmd/wsl) = %{version}

Provides:       go(github.com/bombsimon/wsl/v4) = %{wsl_v4_version}
Provides:       go(github.com/bombsimon/wsl/v4/cmd/wsl) = %{wsl_v4_version}

Requires:       go(go.yaml.in/yaml/v3)
Requires:       go(golang.org/x/tools/go/analysis)
Requires:       go(golang.org/x/tools/go/analysis/singlechecker)

%description
Whitespace and statement grouping analyzer for Go. This package contains the
complete upstream repository sources and tests.

# Keep the complete v4 archive separate from the v5 source tree.
%prep
%autosetup -n wsl-%{version}
tar -xf %{SOURCE1} -C ..

# Stage v4 beside v5 so each API resolves at its declared import path.
%check -p
%go_common
mkdir -p %{_builddir}/go/src/github.com/bombsimon/wsl/v4
cp -a ../wsl-%{wsl_v4_version}/. %{_builddir}/go/src/github.com/bombsimon/wsl/v4/

%install -a
mkdir -p %{buildroot}%{go_sys_gopath}/github.com/bombsimon/wsl/v4
cp -a ../wsl-%{wsl_v4_version}/. %{buildroot}%{go_sys_gopath}/github.com/bombsimon/wsl/v4/

# Test both generations without replacing either module path.
%check -a
%go_common
pushd %{_builddir}/go/src/github.com/bombsimon/wsl/v4
%{__go} test %{go_test_flags_default} ./...
popd

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}
%{go_sys_gopath}/github.com/bombsimon/wsl/v4

%changelog
%autochangelog
