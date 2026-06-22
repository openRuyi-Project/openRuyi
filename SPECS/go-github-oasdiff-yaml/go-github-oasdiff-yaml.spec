# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           yaml
%define go_import_path  github.com/oasdiff/yaml

Name:           go-github-oasdiff-yaml
# v0.1.0 changed go.mod to github.com/invopop/yaml; keep the latest tag that
# still provides github.com/oasdiff/yaml for kin-openapi.
Version:        0.1.0
Release:        %autorelease
Summary:        A better way to marshal and unmarshal YAML in Golang
License:        MIT
URL:            https://github.com/oasdiff/yaml
#!RemoteAsset:  sha256:b1438248ce1379452f909068703cf5080ddcfb69de2604f5a5eb6d492b5b5ddd
Source0:        https://github.com/oasdiff/yaml/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# The v0.0.9 source is still built from the old invopop fork and carries an
# import comment for github.com/invopop/yaml, but kin-openapi imports the
# pre-rename github.com/oasdiff/yaml path. - HNO3Miracle
Patch2000:      2000-use-oasdiff-import-path.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/oasdiff/yaml3)

Provides:       go(github.com/oasdiff/yaml) = %{version}

Requires:       go(github.com/oasdiff/yaml3)

%description
YAML marshaling and unmarshaling support for Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
