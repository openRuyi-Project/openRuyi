# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           argo-go
%define go_import_path  github.com/beeper/argo-go
# varint tests use values outside the implementation's int64 range. The
# fulltest package has a Go 1.26 vet failure, and test contains failing
# upstream gold-fixture equivalence tests.
%define go_test_exclude_glob %{shrink:
    %{go_import_path}/pkg/varint
    %{go_import_path}/fulltest
    %{go_import_path}/test
}

Name:           go-github-beeper-argo-go
Version:        1.1.2
Release:        %autorelease
Summary:        Argo-go is a Go implementation of Argo,
License:        MIT
URL:            https://github.com/beeper/argo-go
#!RemoteAsset:  sha256:b96c6cf36cec93692bcbe198283111c5ffd45d46a9b5885bc2a434d317ac3496
Source0:        https://github.com/beeper/argo-go/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/elliotchance/orderedmap/v3)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/vektah/gqlparser/v2)

Provides:       go(github.com/beeper/argo-go) = %{version}

Requires:       go(github.com/elliotchance/orderedmap/v3)
Requires:       go(github.com/vektah/gqlparser/v2)

%description
argo-go is a Go implementation of Argo, a compact and compressible binary serialization format for GraphQL. It is written in Go and distributed as a Go module.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
