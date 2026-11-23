# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           osc-sdk-go
%define go_import_path  github.com/outscale/osc-sdk-go/v2

Name:           go-github-outscale-osc-sdk-go
Version:        2.34.0
Release:        %autorelease
Summary:        OUTSCALE API SDK for Go
License:        BSD-3-Clause AND CC-BY-4.0
URL:            https://github.com/outscale/osc-sdk-go
#!RemoteAsset:  sha256:a65948ecbb14c4828ab142d9e36361b0d2184113b9be09ef1f9e966335d623bf
Source0:        https://github.com/outscale/osc-sdk-go/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Keep live API tests behind an explicit integration opt-in while retaining all
# offline unit tests.
Patch2000:      2000-require-opt-in-for-live-api-tests.patch
# Use the standard env path in executable repository scripts.
Patch2001:      2001-ci-use-usr-bin-env-for-scripts.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/aws/aws-sdk-go)
BuildRequires:  go(golang.org/x/oauth2)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/aws/aws-sdk-go)
Requires:       go(golang.org/x/oauth2)

%description
This package provides the version 2 OUTSCALE API SDK for Go.

%prep -a
# Resolve links to ../examples before copying the v2 module outside the repository.
cp -aL v2 v2-resolved
rm -r v2
mv v2-resolved v2

%install
# The v2 module lives below the repository root; install it at its import path.
pushd v2
%buildsystem_golangmodules_install
popd

%check
# Run the packaged module's tests from its own source directory.
pushd v2
%buildsystem_golangmodules_check
popd

%files
%doc README.md
%license LICENSES/BSD-3-Clause.txt LICENSES/CC-BY-4.0.txt
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
