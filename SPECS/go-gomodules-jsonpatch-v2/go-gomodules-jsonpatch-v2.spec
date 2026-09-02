# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           jsonpatch
%define go_import_path  gomodules.xyz/jsonpatch/v2

Name:           go-gomodules-jsonpatch-v2
Version:        2.5.0
Release:        %autorelease
Summary:        Generate JSON Patch operations from two objects
License:        Apache-2.0
URL:            https://github.com/gomodules/jsonpatch
#!RemoteAsset:  sha256:b910bf094a369fa0977754e675022786454e1a8117602bf3dd1bb558330e316c
Source0:        https://github.com/gomodules/jsonpatch/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go(github.com/evanphx/json-patch)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/evanphx/json-patch)

%description
This package generates an RFC 6902 JSON Patch by comparing two JSON objects.

%install
pushd v2
%buildsystem_golangmodules_install
popd

%check
pushd v2
%buildsystem_golangmodules_check
popd

%files
%doc README.md CHANGELOG.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
