# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           tools
%define go_import_path  honnef.co/go/tools
# This noarch package contains Go source only. The riscv64 OBS worker's
# brp-remove-la-files crashes while scanning this tree, which cannot contain
# libtool archives.
%global __brp_remove_la_files %{nil}

Name:           go-honnef-go-tools
Version:        0.8.1
Release:        %autorelease
Summary:        Staticcheck tools for Go
License:        MIT
URL:            https://github.com/dominikh/go-tools
#!RemoteAsset:  sha256:7f16b3c7450f7ab62791dfb2e6d40d57d3b74dd01eef30f24a71822db8d45848
Source0:        https://github.com/dominikh/go-tools/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Adapt copied x/tools code to x/tools >= 0.49, which removed private
# typeutil symbols previously accessed through go:linkname.
# Related x/tools commit: 6cbeeacfcd0b3bed4bb186e13df86bb3fbc720c0
# Remove after upstream is fixed.
Patch2000:      2000-typeutil-symbols-avoid-x-tools-private-linkname-symb.patch
# Tests create temporary Go modules and must not inherit GO111MODULE=off.
# Remove after upstream is fixed.
Patch2001:      2001-tests-enable-module-mode-for-temporary-modules.patch

# Go 1.26 vet reports fmt.Sprintf %q with an int64 argument in
# staticcheck/sa1030; keep tests enabled but disable vet. - HNO3Miracle
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go(github.com/BurntSushi/toml)
BuildRequires:  go(golang.org/x/exp)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go-golang-x-tools-go-expect
BuildRequires:  go-rpm-macros

Provides:       go(honnef.co/go/tools) = %{version}
Provides:       go(honnef.co/go/tools/analysis/facts/directives) = %{version}
Provides:       go(honnef.co/go/tools/analysis/facts/generated) = %{version}
Provides:       go(honnef.co/go/tools/analysis/lint) = %{version}
Provides:       go(honnef.co/go/tools/config) = %{version}
Provides:       go(honnef.co/go/tools/quickfix) = %{version}
Provides:       go(honnef.co/go/tools/simple) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck) = %{version}
Provides:       go(honnef.co/go/tools/stylecheck) = %{version}
Provides:       go(honnef.co/go/tools/unused) = %{version}

Requires:       go(github.com/BurntSushi/toml)
Requires:       go(golang.org/x/exp)
Requires:       go(golang.org/x/mod)
Requires:       go(golang.org/x/sync)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/tools)
Requires:       go(golang.org/x/tools/go/expect)

%description
This package provides Staticcheck tools and supporting libraries for Go.

%files
%doc README.md
%license LICENSE
%license LICENSE-THIRD-PARTY
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
