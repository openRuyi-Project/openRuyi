# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           protoc-gen-jsonschema
%define go_import_path  github.com/chrusty/protoc-gen-jsonschema
%define commit_id       73d5723042b812758310ea5ef661a273f0faa9ed

Name:           go-github-chrusty-protoc-gen-jsonschema
Version:        0+git20260817.73d5723
Release:        %autorelease
Summary:        Protobuf to JSON Schema compiler
License:        Apache-2.0
URL:            https://github.com/chrusty/protoc-gen-jsonschema
#!RemoteAsset:  sha256:cbaba1ed561695a681180771bd40fdcc780bb8efc69215d5ebb7a270e1b9765d
Source0:        https://github.com/chrusty/protoc-gen-jsonschema/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Update golden output for packaged strcase and protobuf versions.
Patch2000:      2000-update-test-output-for-current-dependencies.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  protobuf-compiler
BuildRequires:  go(github.com/alecthomas/jsonschema)
BuildRequires:  go(github.com/envoyproxy/protoc-gen-validate)
BuildRequires:  go(github.com/fatih/camelcase)
BuildRequires:  go(github.com/iancoleman/orderedmap)
BuildRequires:  go(github.com/iancoleman/strcase)
BuildRequires:  go(github.com/konsorten/go-windows-terminal-sequences)
BuildRequires:  go(github.com/kr/pretty)
BuildRequires:  go(github.com/sirupsen/logrus)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/xeipuuv/gojsonpointer)
BuildRequires:  go(github.com/xeipuuv/gojsonschema)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go(gopkg.in/check.v1)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/alecthomas/jsonschema)
Requires:       go(github.com/envoyproxy/protoc-gen-validate)
Requires:       go(github.com/fatih/camelcase)
Requires:       go(github.com/iancoleman/orderedmap)
Requires:       go(github.com/iancoleman/strcase)
Requires:       go(github.com/sirupsen/logrus)
Requires:       go(github.com/xeipuuv/gojsonschema)
Requires:       go(google.golang.org/protobuf)

%description
Protoc-gen-jsonschema converts Protocol Buffer definitions into standalone
JSON schemas for validating messages encoded as JSON.

%check
# The release archive omits this declared git submodule; use the packaged copy.
install -d protoc-gen-validate/validate
cp -a %{go_sys_gopath}/github.com/envoyproxy/protoc-gen-validate/validate/validate.proto \
    protoc-gen-validate/validate/
%buildsystem_golangmodules_check
rm -rf protoc-gen-validate

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
