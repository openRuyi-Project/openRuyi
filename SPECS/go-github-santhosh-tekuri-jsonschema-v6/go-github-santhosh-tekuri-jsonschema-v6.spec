# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           jsonschema
%define go_import_path  github.com/santhosh-tekuri/jsonschema/v6
# Example_fromHTTPS fetches raw.githubusercontent.com; OBS builders do not
# have network access during %check - HNO3Miracle
%define go_test_exclude_glob %{go_import_path}*

Name:           go-github-santhosh-tekuri-jsonschema-v6
Version:        6.0.2
Release:        %autorelease
Summary:        JSON Schema validation library for Go
License:        Apache-2.0
URL:            https://github.com/santhosh-tekuri/jsonschema
#!RemoteAsset:  sha256:06465cc1c647b086f9b8d590c9de1608e5b335b58598d0eb84b9ee63a747e1d7
Source0:        https://github.com/santhosh-tekuri/jsonschema/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/dlclark/regexp2)
BuildRequires:  go(golang.org/x/text)

Provides:       go(github.com/santhosh-tekuri/jsonschema/v6) = %{version}

Requires:       go(golang.org/x/text)

%description
jsonschema provides JSON Schema validation support for Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}
# Nested Go modules are packaged separately; do not let this module own
# their source directories, otherwise RPM can hit file conflicts. - HNO3Miracle
%exclude %{go_sys_gopath}/%{go_import_path}/cmd/jv

%changelog
%autochangelog
