# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gnostic-models
%define go_import_path  github.com/google/gnostic-models

Name:           go-github-google-gnostic-models
Version:        0.7.1
Release:        %autorelease
Summary:        Protocol Buffer models for API description formats
License:        Apache-2.0
URL:            https://github.com/google/gnostic-models
#!RemoteAsset:  sha256:3d54e4b46c649df8d93dff8106bc8de245d97ecce528d8ffa26d4e543a9191f3
Source0:        https://github.com/google/gnostic-models/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(go.yaml.in/yaml/v3)
BuildRequires:  go(google.golang.org/protobuf)

Provides:       go(github.com/google/gnostic-models) = %{version}

Requires:       go(go.yaml.in/yaml/v3)
Requires:       go(google.golang.org/protobuf)

%description
This package provides Protocol Buffer models for API description formats.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
