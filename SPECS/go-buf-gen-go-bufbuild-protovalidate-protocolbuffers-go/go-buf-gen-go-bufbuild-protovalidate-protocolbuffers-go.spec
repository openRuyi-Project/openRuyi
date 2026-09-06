# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           protovalidate-protocolbuffers-go
%define go_import_path  buf.build/gen/go/bufbuild/protovalidate/protocolbuffers/go
%define source_version  1.36.6-20250425153114-8976f5be98c1.1

Name:           go-buf-gen-go-bufbuild-protovalidate-protocolbuffers-go
Version:        1.36.6+git20250425.8976f5b
Release:        %autorelease
Summary:        Generated Go bindings for Protovalidate
License:        Apache-2.0
URL:            https://buf.build/bufbuild/protovalidate
#!RemoteAsset:  sha256:e2b23e34fb399628419ffee0d2b4ef598fe83a88a3111561a8a275334ecc70da
Source0:        https://proxy.golang.org/%{go_import_path}/@v/v%{source_version}.zip#/%{_name}-%{version}.zip
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  unzip

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(google.golang.org/protobuf)

%description
This package contains generated Go protocol buffer bindings for the
Protovalidate schema published by Buf Schema Registry.

%prep
%setup -q -c -T
unzip -q %{SOURCE0}
cp -a "%{go_import_path}@v%{source_version}/." .
rm -rf buf.build

%files
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
