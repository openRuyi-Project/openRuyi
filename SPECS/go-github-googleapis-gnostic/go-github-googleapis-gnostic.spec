# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: wangyf0611 <wangyufeng@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gnostic
%define go_import_path  github.com/googleapis/gnostic
%define go_test_include %{shrink:
    %{go_import_path}/compiler
    %{go_import_path}/extensions
    %{go_import_path}/openapiv2
}

Name:           go-github-googleapis-gnostic
Version:        0.4.1
Release:        %autorelease
Summary:        Gnostic is a tool for building better REST APIs through knowledge
License:        Apache-2.0
URL:            https://github.com/googleapis/gnostic
VCS:            git:https://github.com/googleapis/gnostic.git
#!RemoteAsset:  sha256:cc20ab94cf800fdfe377778aa0e2c640045c80193a873253e97605297801733f
Source0:        https://github.com/googleapis/gnostic/archive/v0.4.1.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n gnostic-0.4.1
BuildOption(check):  -vet=off -run '^$'

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/docopt/docopt-go)
BuildRequires:  go(github.com/golang/protobuf)
BuildRequires:  go(gopkg.in/check.v1)
BuildRequires:  go(gopkg.in/yaml.v2)

Provides:       go(github.com/googleapis/gnostic) = %{version}

Requires:       go(github.com/docopt/docopt-go)
Requires:       go(github.com/golang/protobuf)
Requires:       go(gopkg.in/yaml.v2)

%description
This package provides the github.com/googleapis/gnostic Go module source.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
