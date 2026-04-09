# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           protoc-gen-star
%define go_import_path  github.com/lyft/protoc-gen-star/v2
# Tests need network access, so ignore test failures - 251
%define go_test_ignore_failure 1

Name:           go-github-lyft-protoc-gen-star-v2
Version:        2.0.4
Release:        %autorelease
Summary:        protoc plugin library for efficient proto-based code generation
License:        Apache-2.0
URL:            https://github.com/lyft/protoc-gen-star
#!RemoteAsset
Source0:        https://github.com/lyft/protoc-gen-star/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/spf13/afero)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(google.golang.org/protobuf)

Provides:       go(github.com/lyft/protoc-gen-star/v2) = %{version}

Requires:       go(github.com/spf13/afero)
Requires:       go(github.com/stretchr/testify)
Requires:       go(golang.org/x/tools)
Requires:       go(google.golang.org/protobuf)

%description
protoc-gen-star (PG*) is a protoc plugin library for efficient
proto-based code generation

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
